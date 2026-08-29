#!/usr/bin/env python3
"""
Le Yachtomètre — normalisation des illustrations en PNG

Les générateurs d'images rendent souvent du JPEG ou du WebP. Or le détourage
automatique (outils/recadrer.py) ne sait lire que le PNG, et sans détourage
l'échelle du bateau est fausse — donc la silhouette de 1,75 m aussi.

Ce script convertit en PNG tout ce qui traîne dans illustrations/ sous un
autre format, et plafonne la largeur pour éviter les fichiers inutilement
lourds. Il tourne à la publication, avant le détourage.

Contrairement à build.py et recadrer.py, celui-ci a besoin de Pillow. C'est
assumé : il ne tourne que sur le robot de publication, jamais chez John. S'il
manque, on le dit et on passe — le jeu continue de se construire.

    python3 outils/en_png.py
"""
import pathlib, sys

DOSSIER = pathlib.Path(__file__).parent.parent / 'illustrations'
A_CONVERTIR = {'.jpg', '.jpeg', '.webp', '.bmp', '.tif', '.tiff'}
LARGEUR_MAX = 1600      # au-delà, on n'ajoute que du poids


def main():
    if not DOSSIER.is_dir():
        print("Aucun dossier illustrations/, rien à faire")
        return
    fichiers = [f for f in sorted(DOSSIER.iterdir())
                if f.suffix.lower() in A_CONVERTIR]
    if not fichiers:
        print("Rien à convertir, tout est déjà en PNG ou en SVG")
        return

    try:
        from PIL import Image
    except ImportError:
        print(f"Pillow absent : {len(fichiers)} fichier(s) laissés tels quels. "
              f"Ils fonctionneront, mais sans détourage ni recadrage, donc à "
              f"une échelle approximative.", file=sys.stderr)
        return

    print(f"Conversion de {len(fichiers)} fichier(s) en PNG :")
    for f in fichiers:
        cible = f.with_suffix('.png')
        with Image.open(f) as im:
            im = im.convert('RGBA')
            if im.width > LARGEUR_MAX:
                h = round(im.height * LARGEUR_MAX / im.width)
                im = im.resize((LARGEUR_MAX, h), Image.LANCZOS)
            im.save(cible, 'PNG', optimize=True)
        avant, apres = f.stat().st_size, cible.stat().st_size
        f.unlink()
        print(f"  {f.name} → {cible.name}   {im.width}×{im.height}, "
              f"{avant // 1024} Ko → {apres // 1024} Ko")


if __name__ == '__main__':
    main()
