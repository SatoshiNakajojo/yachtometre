#!/usr/bin/env python3
"""
Le Yachtomètre — compression des illustrations

Une photo détourée en PNG pèse environ un mégaoctet. Vingt-six, incrustées
dans le fichier du jeu, le rendraient impossible à ouvrir. Le même visuel en
WebP pèse dix fois moins, sans différence visible à l'écran.

Ce script convertit en WebP les PNG d'illustrations/, une fois qu'ils ont été
détourés et recadrés. Dernière étape de la chaîne :

    en_png.py  →  recadrer.py  →  comprimer.py  →  build.py

Comme en_png.py, il a besoin de Pillow et ne tourne que sur le robot de
publication. S'il manque, les PNG restent en place et le jeu se construit
quand même, simplement plus lourd.

    python3 outils/comprimer.py
"""
import pathlib, sys

DOSSIER = pathlib.Path(__file__).parent.parent / 'illustrations'
QUALITE = 86          # au-delà le gain ne se voit plus, le poids si :
                      # comparé à 90 et 82 sur la photo la plus texturée,
                      # l'écart moyen est de 0,4 niveau sur 255
PLANCHER = 60_000     # en dessous, le PNG est déjà léger : on le laisse


def main():
    if not DOSSIER.is_dir():
        print("Aucun dossier illustrations/, rien à faire")
        return
    fichiers = sorted(DOSSIER.glob('*.png'))
    if not fichiers:
        print("Aucun PNG à comprimer")
        return

    try:
        from PIL import Image
    except ImportError:
        print(f"Pillow absent : {len(fichiers)} PNG laissés tels quels. Le jeu "
              f"fonctionnera, mais le fichier sera lourd.", file=sys.stderr)
        return

    avant = apres = 0
    print(f"Compression de {len(fichiers)} image(s) en WebP :")
    for f in fichiers:
        poids = f.stat().st_size
        if poids < PLANCHER:
            print(f"  {f.name} : {poids // 1024} Ko, déjà léger")
            avant += poids; apres += poids
            continue
        cible = f.with_suffix('.webp')
        with Image.open(f) as im:
            im.convert('RGBA').save(cible, 'WEBP', quality=QUALITE, method=6)
        f.unlink()
        avant += poids; apres += cible.stat().st_size
        print(f"  {f.name} → {cible.name}   {poids // 1024} Ko → "
              f"{cible.stat().st_size // 1024} Ko")
    if avant:
        print(f"Total : {avant // 1024} Ko → {apres // 1024} Ko "
              f"({100 - apres * 100 // avant} % de moins)")


if __name__ == '__main__':
    main()
