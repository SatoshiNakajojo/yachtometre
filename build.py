#!/usr/bin/env python3
"""
Le Yachtomètre — build

Injecte contenu.json dans template.html, écrit yachtometre.html (le livrable,
ouvrable d'un double-clic) et index.html (le même fichier, servi par
l'hébergeur), puis estampille sw.js avec l'empreinte du build pour que les
téléphones déjà installés récupèrent la nouvelle version. Aucune dépendance.

    python3 build.py
"""
import hashlib, json, pathlib, re, sys

ICI      = pathlib.Path(__file__).parent
TEMPLATE = ICI / 'template.html'
CONTENU  = ICI / 'contenu.json'
SORTIE   = ICI / 'yachtometre.html'
INDEX    = ICI / 'index.html'
SW       = ICI / 'sw.js'
MARQUEUR = '/*__CONTENU__*/'

def main():
    tpl = TEMPLATE.read_text(encoding='utf-8')
    if MARQUEUR not in tpl:
        sys.exit(f"Marqueur {MARQUEUR} introuvable dans template.html")
    try:
        data = json.loads(CONTENU.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        sys.exit(f"contenu.json invalide, ligne {e.lineno} : {e.msg}")

    out = tpl.replace(MARQUEUR, json.dumps(data, ensure_ascii=False, indent=1))
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
    n += len(data['paper_hands']['lignes']) + len(data['systeme']['chargement'])
    n += len(data['systeme']['vide']) + len(data['systeme']['erreurs'])
    n += len(data['systeme']['installation']) + len(data['partage'])

    print(f"yachtometre.html + index.html écrits — {len(data['paliers'])} paliers, "
          f"{n} textes, {len(out)//1024} Ko · cache {version}")

if __name__ == '__main__':
    main()
