#!/usr/bin/env python3
"""
Le Yachtomètre — génération des icônes

Dessine l'icône de l'application (silhouette de superyacht noire sur fond
Bitcoin) et écrit les PNG dans icones/. Rasteriseur maison : aucune
dépendance, pas de pip install.

    python3 outils/icones.py
"""
import math, pathlib, struct, zlib

RACINE = pathlib.Path(__file__).parent.parent
DOSSIER = RACINE / 'icones'
ORANGE = (0xF7, 0x93, 0x1A)
NOIR = (0x0A, 0x0A, 0x0B)
SS = 4  # suréchantillonnage pour l'anticrénelage

# Toutes les formes sont décrites en coordonnées 0..1, coin haut-gauche.
# Le contenu tient dans les 80 % centraux pour survivre au masque Android.
COQUE = [(0.125, 0.560), (0.880, 0.498), (0.856, 0.664),
         (0.340, 0.706), (0.140, 0.646)]
PONTS = [(0.200, 0.475, 0.660, 0.556),
         (0.240, 0.394, 0.578, 0.475),
         (0.281, 0.324, 0.492, 0.394)]
MAT = (0.332, 0.196, 0.352, 0.324)
BOULE = (0.342, 0.196, 0.026)
VAGUES = [(0.075, 0.752, 0.925, 0.776),
          (0.210, 0.822, 0.790, 0.846)]


def dans_polygone(x, y, pts):
    dedans = False
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xi:
                dedans = not dedans
    return dedans


def encre(x, y):
    """Vrai si le point (0..1) appartient à la silhouette noire."""
    if dans_polygone(x, y, COQUE):
        return True
    for x1, y1, x2, y2 in PONTS + VAGUES + [MAT]:
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
    cx, cy, r = BOULE
    return (x - cx) ** 2 + (y - cy) ** 2 <= r * r


def png(chemin, taille):
    """Écrit un PNG RGB de côté `taille`, rendu en SS×SS puis moyenné."""
    grand = taille * SS
    # Masque suréchantillonné, ligne par ligne pour rester léger en mémoire.
    masque = []
    for j in range(grand):
        y = (j + 0.5) / grand
        masque.append(bytes(1 if encre((i + 0.5) / grand, y) else 0
                            for i in range(grand)))

    brut = bytearray()
    for j in range(taille):
        brut.append(0)  # filtre PNG : aucun
        lignes = masque[j * SS:(j + 1) * SS]
        for i in range(taille):
            n = sum(l[i * SS + k] for l in lignes for k in range(SS))
            t = n / (SS * SS)
            for c in range(3):
                brut.append(round(ORANGE[c] * (1 - t) + NOIR[c] * t))

    def bloc(nom, data):
        d = nom + data
        return struct.pack('>I', len(data)) + d + struct.pack('>I', zlib.crc32(d))

    entete = struct.pack('>IIBBBBB', taille, taille, 8, 2, 0, 0, 0)
    chemin.write_bytes(b'\x89PNG\r\n\x1a\n'
                       + bloc(b'IHDR', entete)
                       + bloc(b'IDAT', zlib.compress(bytes(brut), 9))
                       + bloc(b'IEND', b''))
    return chemin.stat().st_size


def main():
    DOSSIER.mkdir(exist_ok=True)
    for t in (32, 180, 192, 512, 1024):
        o = png(DOSSIER / f'icone-{t}.png', t)
        print(f'icones/icone-{t}.png — {o // 1024 or 1} Ko')


if __name__ == '__main__':
    main()
