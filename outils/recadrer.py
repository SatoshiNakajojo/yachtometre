#!/usr/bin/env python3
"""
Le Yachtomètre — recadrage des illustrations

Le jeu déduit l'échelle d'un dessin de ses dimensions : la largeur de l'image
vaut la longueur du bateau. Une marge transparente laissée autour de l'objet
fausse donc le bonhomme de 1,75 m, qui est le cœur de la blague.

Ce script rogne cette marge sur chaque PNG d'illustrations/. Il tourne tout
seul à chaque publication ; on peut aussi l'appeler à la main :

    python3 outils/recadrer.py

Décodeur et encodeur PNG maison, aucune dépendance. Ne traite que ce que
produisent les générateurs d'images : 8 bits par canal, non entrelacé.
"""
import pathlib, struct, sys, zlib

DOSSIER = pathlib.Path(__file__).parent.parent / 'illustrations'
SEUIL = 8        # en deçà, le pixel est considéré comme vide
CANAUX = {0: 1, 2: 3, 4: 2, 6: 4}


def lire(octets, nom):
    if octets[:8] != b'\x89PNG\r\n\x1a\n':
        sys.exit(f"{nom} n'est pas un PNG")
    i, entete, data = 8, None, bytearray()
    while i + 8 <= len(octets):
        taille = struct.unpack('>I', octets[i:i + 4])[0]
        genre = octets[i + 4:i + 8]
        corps = octets[i + 8:i + 8 + taille]
        if genre == b'IHDR':
            entete = struct.unpack('>IIBBBBB', corps)
        elif genre == b'IDAT':
            data += corps
        elif genre == b'IEND':
            break
        i += 12 + taille
    if entete is None:
        sys.exit(f"{nom} : en-tête IHDR introuvable")
    w, h, profondeur, couleur, _, _, entrelace = entete
    if profondeur != 8 or entrelace or couleur not in CANAUX:
        return None                      # format exotique : on n'y touche pas
    n = CANAUX[couleur]
    plat = zlib.decompress(bytes(data))
    lignes, prec = [], bytearray(w * n)
    pos = 0
    for _ in range(h):
        filtre = plat[pos]; pos += 1
        ligne = bytearray(plat[pos:pos + w * n]); pos += w * n
        for k in range(len(ligne)):
            a = ligne[k - n] if k >= n else 0
            b = prec[k]
            c = prec[k - n] if k >= n else 0
            if filtre == 1:   ligne[k] = (ligne[k] + a) & 255
            elif filtre == 2: ligne[k] = (ligne[k] + b) & 255
            elif filtre == 3: ligne[k] = (ligne[k] + (a + b) // 2) & 255
            elif filtre == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pred = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                ligne[k] = (ligne[k] + pred) & 255
        lignes.append(ligne); prec = ligne
    return w, h, n, couleur, lignes


def ecrire(chemin, w, h, lignes_rgba):
    brut = bytearray()
    for ligne in lignes_rgba:
        brut.append(0); brut += ligne
    def bloc(nom, d):
        x = nom + d
        return struct.pack('>I', len(d)) + x + struct.pack('>I', zlib.crc32(x))
    chemin.write_bytes(b'\x89PNG\r\n\x1a\n'
                       + bloc(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))
                       + bloc(b'IDAT', zlib.compress(bytes(brut), 9))
                       + bloc(b'IEND', b''))


def recadrer(f):
    lu = lire(f.read_bytes(), f.name)
    if lu is None:
        print(f"  {f.name} : format non géré, laissé tel quel")
        return
    w, h, n, couleur, lignes = lu
    if couleur not in (4, 6):
        print(f"  {f.name} : pas de transparence — le fond fera un rectangle "
              f"sur la mer. À regénérer avec un fond transparent.")
        return

    ia = n - 1                       # l'alpha est le dernier canal
    x0, y0, x1, y1 = w, h, -1, -1
    for y, ligne in enumerate(lignes):
        for x in range(w):
            if ligne[x * n + ia] > SEUIL:
                if x < x0: x0 = x
                if x > x1: x1 = x
                if y < y0: y0 = y
                if y > y1: y1 = y
    if x1 < 0:
        print(f"  {f.name} : entièrement transparent, ignoré")
        return
    if (x0, y0, x1, y1) == (0, 0, w - 1, h - 1):
        print(f"  {f.name} : déjà au plus juste ({w}×{h})")
        return

    nw, nh = x1 - x0 + 1, y1 - y0 + 1
    sortie = []
    for y in range(y0, y1 + 1):
        ligne, dest = lignes[y], bytearray()
        for x in range(x0, x1 + 1):
            px = ligne[x * n:(x + 1) * n]
            dest += bytes((px[0], px[0], px[0], px[1])) if n == 2 else px
        sortie.append(dest)
    ecrire(f, nw, nh, sortie)
    print(f"  {f.name} : {w}×{h} → {nw}×{nh}")


def main():
    if not DOSSIER.is_dir():
        print("Aucun dossier illustrations/, rien à faire")
        return
    fichiers = sorted(DOSSIER.glob('*.png'))
    if not fichiers:
        print("Aucun PNG dans illustrations/, rien à faire")
        return
    print(f"Recadrage de {len(fichiers)} image(s) :")
    for f in fichiers:
        recadrer(f)


if __name__ == '__main__':
    main()
