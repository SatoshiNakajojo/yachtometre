#!/usr/bin/env python3
"""
Le Yachtomètre — réparation des poches de fond enfermées

recadrer.py sait maintenant vider le fond coincé à l'intérieur d'un objet —
sur un voilier, le triangle noir entre la grand-voile, le foc, le mât et la
bôme. Mais il travaille sur les PNG livrés, et ceux des vingt-six bateaux
n'existent plus : seuls les .webp compressés sont au dépôt.

Ce script applique donc la même règle aux .webp déjà publiés, une bonne fois.
Il ne sert qu'à ça : les images livrées après coup passent par recadrer.py et
n'en ont pas besoin. Il demande Pillow, comme en_png.py et comprimer.py, et
n'est donc pas lancé par la publication automatique.

    python3 outils/reparer_poches.py [--essai]

Avec --essai, il annonce ce qu'il ferait sans rien écrire.
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from recadrer import vider_poche, semis

DOSSIER = pathlib.Path(__file__).parent.parent / 'illustrations'
QUALITE = 86   # même réglage que comprimer.py


def main():
    essai = '--essai' in sys.argv
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Pillow absent : pip install Pillow")
    if not DOSSIER.is_dir():
        print("Aucun dossier illustrations/, rien à faire"); return

    for f in sorted(DOSSIER.glob('*.webp')):
        if f.stem.startswith('capitaine-'):
            continue
        im = Image.open(f).convert('RGBA')
        w, h = im.size
        lignes = [bytearray(im.crop((0, y, w, y + 1)).tobytes()) for y in range(h)]

        vide = sum(vider_poche(w, h, lignes, cx, cy) for cx, cy in semis(f.stem))
        if not vide:
            continue
        print(f"  {f.name} : {vide} px ({100 * vide // (w * h)} %) de fond enfermé"
              + (" (essai)" if essai else " vidés"))
        if essai:
            continue
        im2 = Image.frombytes('RGBA', (w, h), b''.join(bytes(l) for l in lignes))
        im2.save(f, 'WEBP', quality=QUALITE, method=6)


if __name__ == '__main__':
    main()
