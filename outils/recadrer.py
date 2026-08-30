#!/usr/bin/env python3
"""
Le Yachtomètre — détourage et recadrage des illustrations

Le jeu déduit l'échelle d'un dessin de ses dimensions : la largeur de l'image
vaut la longueur du bateau. Un fond opaque ou une marge transparente faussent
donc le bonhomme de 1,75 m, qui est le cœur de la blague.

Ce script, sur chaque PNG de bateau d'illustrations/ — les portraits de
capitaine sont laissés intacts, leur fond fait partie de l'image :
  1. retire le fond, par remplissage depuis les bords — ce qui laisse intacts
     les noirs intérieurs, hublots et ouvertures ;
  2. rogne ce qui reste de marge transparente.

Il tourne tout seul à chaque publication ; on peut aussi l'appeler à la main :

    python3 outils/recadrer.py

Décodeur et encodeur PNG maison, aucune dépendance. Ne traite que ce que
produisent les générateurs d'images : 8 bits par canal, non entrelacé.
"""
import collections, pathlib, struct, sys, zlib

DOSSIER = pathlib.Path(__file__).parent.parent / 'illustrations'
SEUIL_ALPHA = 8      # en deçà, le pixel est vide
PLAFOND_FOND = 96    # au-dessus, le pixel appartient à l'objet, pas au fond
PAS_MAX = 30         # écart toléré entre deux pixels voisins du fond
CANAUX = {0: 1, 2: 3, 4: 2, 6: 4}


def decoder(octets, nom):
    """Rend (largeur, hauteur, lignes RGBA) ou None si le format est exotique."""
    if octets[:8] != b'\x89PNG\r\n\x1a\n':
        sys.exit(f"{nom} n'est pas un PNG")
    i, entete, data = 8, None, bytearray()
    while i + 8 <= len(octets):
        taille = struct.unpack('>I', octets[i:i + 4])[0]
        genre = octets[i + 4:i + 8]
        if genre == b'IHDR':
            entete = struct.unpack('>IIBBBBB', octets[i + 8:i + 8 + taille])
        elif genre == b'IDAT':
            data += octets[i + 8:i + 8 + taille]
        elif genre == b'IEND':
            break
        i += 12 + taille
    if entete is None:
        sys.exit(f"{nom} : en-tête IHDR introuvable")
    w, h, profondeur, couleur, _, _, entrelace = entete
    if profondeur != 8 or entrelace or couleur not in CANAUX:
        return None
    n = CANAUX[couleur]

    plat = zlib.decompress(bytes(data))
    lignes, prec, pos = [], bytearray(w * n), 0
    for _ in range(h):
        filtre = plat[pos]; pos += 1
        ligne = bytearray(plat[pos:pos + w * n]); pos += w * n
        if filtre:
            for k in range(len(ligne)):
                a = ligne[k - n] if k >= n else 0
                b = prec[k]
                c = prec[k - n] if k >= n else 0
                if filtre == 1:   ligne[k] = (ligne[k] + a) & 255
                elif filtre == 2: ligne[k] = (ligne[k] + b) & 255
                elif filtre == 3: ligne[k] = (ligne[k] + (a + b) // 2) & 255
                else:
                    p = a + b - c
                    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                    pred = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                    ligne[k] = (ligne[k] + pred) & 255
        lignes.append(ligne); prec = ligne

    # tout ramener en RGBA pour n'avoir qu'un cas à traiter ensuite
    rgba = []
    for ligne in lignes:
        d = bytearray(w * 4)
        for x in range(w):
            p = ligne[x * n:(x + 1) * n]
            if n == 1:   r = v = bl = p[0]; al = 255
            elif n == 2: r = v = bl = p[0]; al = p[1]
            elif n == 3: r, v, bl = p; al = 255
            else:        r, v, bl, al = p
            d[x * 4:x * 4 + 4] = bytes((r, v, bl, al))
        rgba.append(d)
    return w, h, rgba


def encoder(chemin, w, h, lignes):
    brut = bytearray()
    for ligne in lignes:
        brut.append(0); brut += ligne
    def bloc(nom, d):
        x = nom + d
        return struct.pack('>I', len(d)) + x + struct.pack('>I', zlib.crc32(x))
    chemin.write_bytes(b'\x89PNG\r\n\x1a\n'
                       + bloc(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))
                       + bloc(b'IDAT', zlib.compress(bytes(brut), 9))
                       + bloc(b'IEND', b''))


def detourer(w, h, lignes):
    """Rend le fond transparent, en partant des bords.

    On avance de proche en proche tant que la couleur ne change presque pas.
    Un vignettage ou un dégradé de studio se laisse donc traverser, alors
    qu'un bord d'objet — une marche brutale du noir vers une coque claire —
    arrête la progression. Et comme on ne part que des bords, un hublot noir
    au milieu de la coque n'est jamais touché.
    """
    def px(x, y):
        return lignes[y][x * 4:x * 4 + 3]

    sombre = lambda p: max(p) <= PLAFOND_FOND
    vu = bytearray(w * h)
    file = collections.deque()

    def semer(x, y):
        if not vu[y * w + x] and sombre(px(x, y)):
            vu[y * w + x] = 1
            file.append((x, y))

    for x in range(w):
        semer(x, 0); semer(x, h - 1)
    for y in range(h):
        semer(0, y); semer(w - 1, y)
    if not file:
        return False, "aucun bord sombre, le fond n'a pas l'air uni"

    efface = 0
    while file:
        x, y = file.popleft()
        p = px(x, y)
        lignes[y][x * 4 + 3] = 0
        efface += 1
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < w and 0 <= ny < h) or vu[ny * w + nx]:
                continue
            q = px(nx, ny)
            if not sombre(q):
                continue
            if abs(q[0] - p[0]) + abs(q[1] - p[1]) + abs(q[2] - p[2]) > PAS_MAX:
                continue
            vu[ny * w + nx] = 1
            file.append((nx, ny))
    return True, f"{efface * 100 // (w * h)} % du fond retiré"


def traiter(f):
    # Les portraits de capitaine gardent leur fond : c'est une pièce sombre,
    # un transat et une photo encadrée, pas un objet à détourer. Les rogner
    # casserait le cadrage, les détourer effacerait le décor.
    if f.stem.startswith('capitaine-'):
        print(f"  {f.name} : portrait, laissé intact")
        return
    lu = decoder(f.read_bytes(), f.name)
    if lu is None:
        print(f"  {f.name} : format non géré, laissé tel quel")
        return
    w, h, lignes = lu

    opaque = all(ligne[x * 4 + 3] > 250 for ligne in lignes for x in (0, w - 1))
    if opaque:
        ok, note = detourer(w, h, lignes)
        print(f"  {f.name} : {note}" if ok
              else f"  {f.name} : fond non détouré — {note}. "
                   f"Regénère avec un fond noir uni #0A0A0B.")
        if not ok:
            return

    x0, y0, x1, y1 = w, h, -1, -1
    for y, ligne in enumerate(lignes):
        for x in range(w):
            if ligne[x * 4 + 3] > SEUIL_ALPHA:
                if x < x0: x0 = x
                if x > x1: x1 = x
                if y < y0: y0 = y
                if y > y1: y1 = y
    if x1 < 0:
        print(f"  {f.name} : entièrement transparent, ignoré")
        return

    nw, nh = x1 - x0 + 1, y1 - y0 + 1
    if (nw, nh) == (w, h) and not opaque:
        print(f"  {f.name} : déjà au plus juste ({w}×{h})")
        return
    encoder(f, nw, nh, [lignes[y][x0 * 4:(x1 + 1) * 4] for y in range(y0, y1 + 1)])
    print(f"  {f.name} : {w}×{h} → {nw}×{nh}")


def main():
    if not DOSSIER.is_dir():
        print("Aucun dossier illustrations/, rien à faire"); return
    fichiers = sorted(DOSSIER.glob('*.png'))
    if not fichiers:
        print("Aucun PNG dans illustrations/, rien à faire"); return
    print(f"Détourage de {len(fichiers)} image(s) :")
    for f in fichiers:
        traiter(f)


if __name__ == '__main__':
    main()
