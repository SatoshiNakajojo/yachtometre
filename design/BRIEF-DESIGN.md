# Brief design — Le Yachtomètre

Ce dossier est le paquet à remettre à qui travaille le design de l'application.
Il contient ce brief, les jetons de style actuels (`jetons.css`) et les captures
de tous les écrans (`captures/`), prises sur un iPhone 13.

L'application en ligne : <https://satoshinakajojo.github.io/yachtometre/>

---

## 1. Ce que c'est

Le Yachtomètre convertit un stack de Bitcoin en **longueur de bateau**, du
canard en plastique au superyacht de 180 mètres, et se moque gentiment du
résultat. On entre son stack, l'année jusqu'à laquelle on compte tenir, et un
niveau d'optimisme ; le jeu affiche le bateau correspondant et une réplique.

Ce n'est pas un outil financier. C'est **une blague avec un moteur sérieux
dessous**. Si un arbitrage oppose la rigueur et le rire, le rire gagne — sauf
sur les chiffres, qui doivent rester défendables.

Le rituel visé est quotidien : le cours bouge, donc le bateau bouge, et un
bandeau au premier écran du matin dit de combien. C'est le seul mécanisme de
rétention du produit.

## 2. À qui ça s'adresse, et sur quoi

Public : détenteurs de Bitcoin, plutôt jeunes, qui partagent des captures entre
eux. Le produit se diffuse par la carte à collectionner, qui porte l'adresse du
jeu — **c'est le seul canal d'acquisition**.

Usage réel : **iPhone, en portrait, application posée sur l'écran d'accueil.**
C'est le cas à traiter en premier. Le desktop existe mais n'est pas la cible.

## 3. Les écrans

| Capture | Écran |
|---|---|
| `01-accueil.webp` | Le haut : en-tête, les quatre champs, **la carte du jour en grand** |
| `02-regle-et-verdict.webp` | Le mètre de yacht, puis la longueur, le nom du bateau, la réplique, le capitaine, le raccourci vers la collection |
| `03-entretien.webp` | Onglet Entretien : le bateau qu'on peut acheter contre celui qu'on peut garder |
| `04-metre.webp` | Onglet Mètre : ce qu'un achat coûte en millimètres de coque |
| `05-fantome.webp` | Onglet Fantôme : le bateau qu'on aurait sans avoir vendu |
| `06-demain.webp` | Onglet Demain : simulation de variations |
| `07-collection.webp` | Onglet Cartes : la collection, une carte gagnée par jour |
| `00-page-entiere.webp` | La page entière, d'un seul tenant |

L'ordre de la page est : en-tête → champs → **carte** → mètre de yacht →
longueur et réplique → barre d'onglets → panneau ouvert → pied de page.

## 4. Ce qui est ouvert

Tout ce qui suit se refait librement, et mérite d'être refait :

- **La hiérarchie typographique.** Trois familles cohabitent sans système
  clair : Archivo Black pour les titres, JetBrains Mono pour les chiffres et
  les étiquettes, Inter pour le texte courant. Les tailles ont été posées au
  jugé, une par une.
- **Les quatre champs du haut.** Ils fonctionnent mais sont bruts. Deux
  défauts ont été corrigés depuis les captures : « ton niveau de foi » prend
  maintenant toute la largeur avec une police qui se réduit sur les petits
  écrans — quatre noms de bande sur cinq étaient illisibles sur un iPhone 13,
  455 px de texte dans 150 px — et les étiquettes du mètre de yacht s'écartent
  quand les deux bateaux se rapprochent. Le reste est à refaire.
- **Le mètre de yacht** (la règle 1 · 10 · 60 · 180). L'échelle logarithmique
  écrase tout le bas : du canard au voilier, presque rien ne bouge.
- **Les panneaux d'onglets**, qui se ressemblent tous : un titre, un
  sous-titre gris, un bloc de texte. Rien ne distingue visuellement une
  simulation d'un avertissement.
- **La grille de collection** : dense, et la rareté n'y tient qu'à un liseré
  de 4 pixels à gauche.
- **Le portrait de capitaine**, aujourd'hui une vignette de 108 px à côté d'une
  réplique en italique.
- **Le bandeau du matin**, l'espacement général, les états de survol et de
  focus, la page de pied.

## 5. Ce qui ne se négocie pas

Ces points ne sont pas des préférences. Les changer casse le produit.

**La silhouette humaine de 1,75 m, à l'échelle exacte.** C'est le cœur de la
blague : à côté d'un superyacht de 180 m, elle fait huit pixels de haut. Un
designer voudra l'agrandir pour « équilibrer la composition ». C'est
précisément ce qu'il ne faut pas faire — le déséquilibre *est* le propos. Elle
est calculée, pas dessinée : le jeu déduit l'échelle des dimensions du fichier
photo.

**Un seul fichier livrable.** `yachtometre.html` doit rester autonome et
ouvrable d'un double-clic, sans serveur ni installation. Donc : pas de
framework, pas d'étape de compilation, pas de fichier CSS séparé, pas de
police auto-hébergée en fichier joint. Tout le style vit dans un `<style>`
unique, en CSS simple.

**La palette Bitcoin — noir et `#F7931A`.** Décision explicite du propriétaire
du produit, prise contre une palette nautique bleu-craie qui existait avant.
On peut faire évoluer les gris, les surfaces, les accents secondaires ; l'axe
noir + orange Bitcoin reste.

**Les trois familles déjà chargées.** Archivo Black, Inter, JetBrains Mono
arrivent en un seul `<link>` Google Fonts. En ajouter une coûte une requête et
un repli hors ligne de plus. En retirer une est en revanche bienvenu.

**La barre d'onglets doit tenir sur un iPhone SE** — cinq libellés, sans
défilement horizontal. C'est ce qui limite leur longueur.

**Le ton, dans les textes.** Pince-sans-rire. Jamais de point d'exclamation,
jamais d'emoji, jamais de « lol ». On se moque de la situation, du bateau, du
capitaine — jamais de l'utilisateur. Si une proposition de design demande un
libellé, il suit ces règles.

**L'avertissement légal reste affiché.** Le rainbow chart n'est pas une
prédiction ; c'est écrit, ça doit le rester.

## 6. Le cas particulier de la carte

La carte à collectionner (1080 × 1620) **n'est pas du HTML**. Elle est peinte
en JavaScript dans un `<canvas>` : fond, rayons, holographie, éclats, cadre
métallique, typographie, tout est dessiné au pixel. Le CSS ne peut rien y
changer — seule sa taille d'affichage et son ombre portée sont en CSS.

Une proposition sur la carte est donc **une spécification, pas une feuille de
style** : couleurs, proportions, position des blocs, tailles de texte. Elle
sera transcrite en code. Prévois-le, c'est plus lent qu'un ajustement CSS.

Cinq raretés colorent la carte entière, du bleu acier au orange Bitcoin :
`#6E8CA8` commun, `#4FB3A6` peu commun, `#C8873D` rare, `#E0B04A` très rare,
`#F7931A` légendaire. Les trois dernières portent un effet holographique.

Les photos de bateaux sont détourées sur fond transparent. Elles se posent donc
sur n'importe quel fond — c'est ce qui rend le fond de la carte libre.

## 7. Ce qu'on attend en retour

Utile, dans l'ordre :

1. **Des jetons revus** — un `:root` de remplacement pour `jetons.css`, avec
   une échelle typographique et une échelle d'espacement nommées. C'est ce qui
   s'intègre le plus vite et change le plus.
2. **Des écrans annotés**, à partir des captures, avec le raisonnement. Les
   annotations comptent autant que les images.
3. **Une spécification pour la carte**, si tu veux y toucher.

Peu utile ici : une maquette qui suppose un framework, un système de
composants qui suppose une compilation, ou une remise en Figma seule sans
valeurs exploitables.

## 8. Pour lire le code

- `template.html` — structure, style et logique. **C'est le seul fichier à
  modifier.** Le `<style>` est en tête, autour de la ligne 25 pour les jetons.
- `contenu.json` — les 250 textes. Aucun texte visible n'est écrit ailleurs.
- `build.py` — assemble les deux en `yachtometre.html` et `index.html`, qui
  sont **générés** : ne jamais les éditer à la main.
- `CLAUDE.md` — la passation complète : les décisions déjà tranchées, les
  pièges connus, et les raisons derrière. À lire avant de proposer quoi que ce
  soit qui a l'air d'une évidence.
