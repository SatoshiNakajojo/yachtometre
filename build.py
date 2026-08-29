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
import base64, hashlib, json, pathlib, re, struct, sys

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


def dimensions_svg(texte, nom):
    m = re.search(r'viewBox\s*=\s*"([^"]+)"', texte)
    if not m:
        sys.exit(f"illustrations/{nom} n'a pas de viewBox, impossible de le mettre à l'échelle")
    v = [float(x) for x in re.split(r'[\s,]+', m.group(1).strip()) if x]
    if len(v) != 4 or v[2] <= 0 or v[3] <= 0:
        sys.exit(f"illustrations/{nom} a un viewBox inexploitable")
    return v[2], v[3]


def dimensions_png(o, nom):
    if o[:8] != b'\x89PNG\r\n\x1a\n':
        sys.exit(f"illustrations/{nom} porte l'extension .png mais n'en est pas un")
    return struct.unpack('>II', o[16:24])


def dimensions_jpeg(o, nom):
    i = 2
    while i + 9 < len(o):
        if o[i] != 0xFF:
            i += 1
            continue
        marqueur = o[i + 1]
        # SOF0..SOF15, sauf les marqueurs de redémarrage et de tables
        if marqueur in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                        0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h, w = struct.unpack('>HH', o[i + 5:i + 9])
            return w, h
        if marqueur in (0xD8, 0x01) or 0xD0 <= marqueur <= 0xD7:
            i += 2
        else:
            i += 2 + struct.unpack('>H', o[i + 2:i + 4])[0]
    sys.exit(f"illustrations/{nom} : dimensions JPEG introuvables")


def dimensions_webp(o, nom):
    if o[:4] != b'RIFF' or o[8:12] != b'WEBP':
        sys.exit(f"illustrations/{nom} porte l'extension .webp mais n'en est pas un")
    genre = o[12:16]
    if genre == b'VP8X':
        w = int.from_bytes(o[24:27], 'little') + 1
        h = int.from_bytes(o[27:30], 'little') + 1
        return w, h
    if genre == b'VP8 ':
        return (struct.unpack('<H', o[26:28])[0] & 0x3FFF,
                struct.unpack('<H', o[28:30])[0] & 0x3FFF)
    if genre == b'VP8L':
        b = o[21:25]
        return ((b[0] | (b[1] & 0x3F) << 8) + 1,
                ((b[1] >> 6) | b[2] << 2 | (b[3] & 0x0F) << 10) + 1)
    sys.exit(f"illustrations/{nom} : variante WebP non reconnue")


FORMATS = {'.png': ('image/png', dimensions_png),
           '.jpg': ('image/jpeg', dimensions_jpeg),
           '.jpeg': ('image/jpeg', dimensions_jpeg),
           '.webp': ('image/webp', dimensions_webp)}


def illustrations():
    """Incruste les dessins d'illustrations/, nommés d'après l'id du palier.

    Le nom du fichier fait tout : `voilier.png` remplace la silhouette du
    voilier, `capitaine-3.png` donne son portrait au commandant. PNG, JPEG,
    WebP ou SVG — mais seul le PNG passe par le détourage automatique.
    Dossier vide ou absent : le jeu retombe sur les silhouettes procédurales.

    Chaque dessin est incrusté en base64 dans le HTML, jamais chargé à côté —
    le livrable doit rester un fichier unique. On relève aussi ses dimensions :
    c'est ce qui permet au jeu de le poser à l'échelle exacte du bateau, et
    donc de garder le bonhomme de 1,75 m honnête.
    """
    dessins = {}
    if not DESSINS.is_dir():
        return dessins
    for f in sorted(DESSINS.iterdir()):
        ext = f.suffix.lower()
        if ext not in FORMATS and ext != '.svg':
            continue
        octets = f.read_bytes()
        if ext == '.svg':
            texte = octets.decode('utf-8')
            texte = re.sub(r'<\?xml.*?\?>', '', texte, flags=re.S)
            texte = re.sub(r'<!DOCTYPE.*?>', '', texte, flags=re.S)
            texte = re.sub(r'<!--.*?-->', '', texte, flags=re.S)
            texte = re.sub(r'>\s+<', '><', texte).strip()
            if '<svg' not in texte:
                sys.exit(f"illustrations/{f.name} ne contient pas de balise <svg>")
            w, h = dimensions_svg(texte, f.name)
            octets, mime = texte.encode('utf-8'), 'image/svg+xml'
        else:
            mime, mesurer = FORMATS[ext]
            w, h = mesurer(octets, f.name)
        if len(octets) > 400_000:
            print(f"Attention : illustrations/{f.name} pèse {len(octets)//1024} Ko. "
                  f"Au-delà de 400 Ko par image, le jeu devient long à ouvrir.",
                  file=sys.stderr)
        dessins[f.stem] = {
            'u': f'data:{mime};base64,' + base64.b64encode(octets).decode('ascii'),
            'w': w, 'h': h,
        }
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
    n += sum(len(c['repliques']) for c in data['capitaine']) + len(data['bandes'])
    for bloc in ('notifications', 'opportunite', 'entretien'):
        n += sum(len(b['lignes']) for b in data[bloc].values())
    n += len(data['paper_hands']['lignes']) + len(data['paper_hands']['lignes_tout_vendu'])
    n += 4   # vide, prix_manquant, cout, bien_joue
    n += len(data['systeme']['chargement'])
    n += len(data['systeme']['vide']) + len(data['systeme']['erreurs']) + 1  # adresse
    n += len(data['systeme']['installation']) + len(data['partage'])

    dessine = f"{len(dessins)} dessin{'s' if len(dessins) > 1 else ''}" if dessins \
              else "silhouettes procédurales"
    print(f"yachtometre.html + index.html écrits — {len(data['paliers'])} paliers, "
          f"{n} textes, {dessine}, {len(out)//1024} Ko · cache {version}")

if __name__ == '__main__':
    main()
