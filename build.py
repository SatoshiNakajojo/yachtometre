#!/usr/bin/env python3
"""
Le Yachtomètre — build

Injecte contenu.json et les dessins d'illustrations/ dans template.html, écrit
yachtometre.html (le livrable, ouvrable d'un double-clic) et index.html (le même
fichier, servi par l'hébergeur), puis estampille sw.js avec l'empreinte du build
pour que les téléphones déjà installés récupèrent la nouvelle version.
Aucune dépendance.

    python3 build.py
"""
import hashlib, json, pathlib, re, sys

ICI      = pathlib.Path(__file__).parent
TEMPLATE = ICI / 'template.html'
CONTENU  = ICI / 'contenu.json'
SORTIE   = ICI / 'yachtometre.html'
INDEX    = ICI / 'index.html'
SW       = ICI / 'sw.js'
DESSINS  = ICI / 'illustrations'
MARQUEUR = '/*__CONTENU__*/'
MARQ_ILL = '/*__ILLUSTRATIONS__*/'
PLAFOND  = 2_000_000   # au-delà, le fichier devient pénible à ouvrir sur un mobile


def illustrations():
    """Incruste les SVG d'illustrations/, nommés d'après l'id du palier.

    Le nom du fichier fait tout : `voilier.svg` remplace la silhouette du
    voilier, `capitaine-3.svg` donne son portrait au commandant. Dossier vide
    ou absent : le jeu retombe sur les silhouettes procédurales, sans erreur.
    Tout est incrusté dans le HTML, jamais chargé à côté — le livrable doit
    rester un fichier unique.
    """
    dessins = {}
    if not DESSINS.is_dir():
        return dessins
    for f in sorted(DESSINS.glob('*.svg')):
        svg = f.read_text(encoding='utf-8')
        svg = re.sub(r'<\?xml.*?\?>', '', svg, flags=re.S)
        svg = re.sub(r'<!DOCTYPE.*?>', '', svg, flags=re.S)
        svg = re.sub(r'<!--.*?-->', '', svg, flags=re.S)
        svg = re.sub(r'>\s+<', '><', svg).strip()
        if '<svg' not in svg:
            sys.exit(f"illustrations/{f.name} ne contient pas de balise <svg>")
        dessins[f.stem] = svg
    return dessins

def main():
    tpl = TEMPLATE.read_text(encoding='utf-8')
    if MARQUEUR not in tpl:
        sys.exit(f"Marqueur {MARQUEUR} introuvable dans template.html")
    try:
        data = json.loads(CONTENU.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        sys.exit(f"contenu.json invalide, ligne {e.lineno} : {e.msg}")

    if MARQ_ILL not in tpl:
        sys.exit(f"Marqueur {MARQ_ILL} introuvable dans template.html")
    dessins = illustrations()

    out = tpl.replace(MARQUEUR, json.dumps(data, ensure_ascii=False, indent=1))
    out = out.replace(MARQ_ILL, json.dumps(dessins, ensure_ascii=False))
    if len(out) > PLAFOND:
        print(f"Attention : {len(out)//1024} Ko. Des dessins trop lourds rendent "
              f"le fichier pénible à ouvrir sur un mobile.", file=sys.stderr)
    SORTIE.write_text(out, encoding='utf-8')
    INDEX.write_text(out, encoding='utf-8')

    # Le nom du cache change avec le contenu : sans ça, un téléphone qui a
    # déjà posé l'application garderait l'ancienne version indéfiniment.
    version = hashlib.sha1(out.encode('utf-8')).hexdigest()[:10]
    sw = SW.read_text(encoding='utf-8')
    sw, n = re.subn(r"^const VERSION = '.*';$", f"const VERSION = '{version}';",
                    sw, count=1, flags=re.M)
    if not n:
        sys.exit("Ligne VERSION introuvable dans sw.js")
    SW.write_text(sw, encoding='utf-8')

    n  = sum(len(p['punch']) + len(p['dit']) for p in data['paliers'])
    n += sum(len(c['repliques']) for c in data['capitaine'])
    for bloc in ('notifications', 'opportunite', 'entretien'):
        n += sum(len(b['lignes']) for b in data[bloc].values())
    n += len(data['paper_hands']['lignes']) + len(data['paper_hands']['lignes_tout_vendu'])
    n += 4   # vide, prix_manquant, cout, bien_joue
    n += len(data['systeme']['chargement'])
    n += len(data['systeme']['vide']) + len(data['systeme']['erreurs'])
    n += len(data['systeme']['installation']) + len(data['partage'])

    dessine = f"{len(dessins)} dessin{'s' if len(dessins) > 1 else ''}" if dessins \
              else "silhouettes procédurales"
    print(f"yachtometre.html + index.html écrits — {len(data['paliers'])} paliers, "
          f"{n} textes, {dessine}, {len(out)//1024} Ko · cache {version}")

if __name__ == '__main__':
    main()
