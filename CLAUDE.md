# CLAUDE.md — Le Yachtomètre

Lis ce fichier en entier avant toute action. Il contient le contexte, les
invariants, et les raisons derrière les décisions déjà prises. Beaucoup de ces
décisions ont l'air arbitraires vues de l'extérieur : elles ne le sont pas.

---

## 1. Le projet en une phrase

Le Yachtomètre convertit un stack de Bitcoin en **longueur de bateau**, du canard
en plastique au superyacht de 180 mètres, et se moque gentiment du résultat.

Ce n'est pas un outil financier. C'est une **blague avec un moteur sérieux
dessous**. Si un arbitrage oppose la rigueur et le rire, le rire gagne — sauf
sur les chiffres, qui doivent rester défendables.

---

## 2. À qui tu parles — lis cette section deux fois

L'utilisateur s'appelle **John**. Il travaille dans la maintenance aéronautique.
Il est très à l'aise avec les concepts (marchés, cycles Bitcoin, raisonnement
technique) et **débutant en code**.

Ce que ça implique concrètement, appris à ses dépens pendant la phase précédente :

- **Un livrable = un fichier.** On lui a livré un jour un projet Expo de onze
  fichiers avec `npm install`. Réponse : « je sais pas quoi faire de tous ces
  fichiers ». C'était une erreur de conception du livrable, pas un manque de sa
  part. Le produit qu'il utilise doit s'ouvrir d'un double-clic.
- **Zéro terminal dans le chemin critique.** Il peut lancer une commande si on la
  lui donne mot pour mot, mais rien ne doit en dépendre pour que le jeu marche.
- **Il teste sur iPhone**, en hébergeant le HTML sur tiiny.host puis en
  l'ajoutant à l'écran d'accueil. Le fichier doit donc rester **autonome** :
  pas de fichier compagnon, pas de `fetch` vers un fichier local, pas de module ES.
- **Il a un excellent instinct produit.** C'est lui qui a demandé l'affichage en
  millimètres, et il avait raison. Quand il propose quelque chose sur le fond,
  prends-le au sérieux avant de proposer autre chose.
- **Il travaille en français.** Réponds en français, et tout le contenu du jeu est
  en français.

---

## 3. État actuel

Le produit vivant est **`yachtometre.html`** : un fichier HTML autonome de 67 Ko
qui contient le moteur, les 240 textes, les silhouettes de bateaux, la carte de
partage et la mémoire locale. Il tourne dans n'importe quel navigateur, hors
ligne sauf pour le cours du BTC.

Il est aussi **publié et installable** sur
<https://satoshinakajojo.github.io/yachtometre/> : même fichier, servi sous le
nom `index.html`, avec un manifeste et un service worker qui le posent sur
l'écran d'accueil de l'iPhone. C'est le chemin d'accès normal de John
désormais ; tiiny.host n'est plus dans la boucle.

Phases terminées : 0 (socle chiffré), 1 (prototype validé — tous les testeurs ont
ri), 2 (banque de textes), 4 (bateau vivant, version web), 5 (mètre de yacht),
6 (entretien), 7 (carte de partage), 8a (hébergement et installation sur l'écran
d'accueil), 9a (paper hands). La phase 3 (illustrations) a son brief prêt et sa
prise posée, mais aucun dessin commandé. La phase 8b (mobile natif, notification
poussée) reste ouverte.

---

## 4. Architecture et règle d'or

```
contenu.json   ──┐                    ┌──►  yachtometre.html  (le livrable hors ligne)
illustrations/ ──┼──►  build.py  ──►  ├──►  index.html        (ce que sert Pages)
template.html  ──┘                    └──►  sw.js             (estampillé, pas réécrit)
```

**`yachtometre.html` et `index.html` sont des fichiers générés, identiques à
l'octet près. Ne les édite jamais à la main.**
Toute modification passe par `template.html` (structure, style, logique) ou
`contenu.json` (textes), puis :

```bash
python3 build.py
```

Le script remplace le marqueur `/*__CONTENU__*/` de `template.html` par le JSON,
écrit les deux sorties, et remplace la ligne `const VERSION` de `sw.js` par
l'empreinte du build. Cette dernière étape n'est pas cosmétique : sans elle, un
téléphone qui a déjà posé l'application garderait l'ancienne version dans son
cache. Aucune dépendance, aucun `node_modules`, rien à installer.

`illustrations/` est la prise où brancher les dessins de la phase 3. Un fichier
PNG ou SVG nommé d'après l'id du palier (`voilier.png`, `s180.png`,
`capitaine-3.png`) est **incrusté en base64** dans le HTML au build et remplace
la silhouette procédurale de ce palier ; les autres gardent la leur. Incrusté,
pas chargé à côté : c'est ce qui préserve l'invariant du fichier unique. Le
dossier peut rester vide sans rien casser.

**L'horizon est peint dans le SVG, pas en CSS.** La mer était un dégradé CSS
qui basculait à 62 % de la hauteur du bloc, alors que la ligne de flottaison est
à 76 % — et jusqu'à 88 % depuis que le cadre s'allonge. L'horizon ne tombait
donc jamais au bon endroit. Il est maintenant dessiné dans le SVG, qui est le
seul à connaître la vraie hauteur d'eau. Ne remets pas de dégradé sur `.scene`.

**Le cadre est mesuré, pas deviné.** `poserScene()` dessine la scène, lit le
`getBBox()` du résultat, et recommence — trois fois au plus — jusqu'à ce que
rien ne dépasse. Elle allonge le cadre en priorité (jusqu'à `VB_HMAX`, 660) et
ne réduit l'échelle qu'en dernier recours ; la silhouette de 1,75 m suivant la
même réduction, le rapport de taille reste exact dans tous les cas. Avant ça,
le cadre était figé à 320 unités et tout ce qui dépassait — le mât du voilier,
les ponts hauts des yachts, la carène sous la flottaison — était tranché. Ne
remplace pas cette mesure par une table de hauteurs par classe : elle serait
fausse dès le premier dessin livré, dont on ne connaît pas les proportions à
l'avance.

**La convention, et la raison derrière.** Un dessin de bateau ne contient que
le bateau, sur fond transparent, coupé net à la flottaison. Le jeu en déduit
l'échelle — la largeur de l'image vaut la longueur du bateau — puis dessine
lui-même la mer, le quai et la silhouette de 1,75 m. Autrement dit
**l'invariant n° 1 n'est plus confié à l'illustrateur, il est calculé.** Un
générateur d'image ne sait pas tenir une échelle ; un humain dessiné dans le
fichier la casserait. `outils/recadrer.py`, appelé à chaque publication, rogne
les marges transparentes qui fausseraient ce calcul.

Quand un dessin est présent, le cadre de la scène s'allonge — jusqu'à 660
unités de haut — plutôt que de rapetisser le bateau pour faire tenir un mât.
Le chemin procédural, lui, garde son cadre plat de 320 : rien n'a changé pour
ce que le jeu affiche aujourd'hui.

Deux outils préparent les fichiers déposés, dans cet ordre, à chaque
publication. `outils/en_png.py` convertit d'abord en PNG ce qui arrive en JPEG
ou en WebP — les générateurs d'images en produisent souvent — et plafonne la
largeur à 1600 pixels. **C'est le seul fichier du projet qui a une dépendance**,
Pillow, installée par le workflow : elle ne tourne jamais chez John, et son
absence est signalée sans faire échouer le build.

`outils/recadrer.py` fait ensuite deux choses sur chaque PNG :
il retire le fond **par remplissage depuis les bords** — d'où la survie des
hublots sombres au milieu d'une coque — puis rogne les marges. C'est pour ça
que les prompts imposent un fond noir uni `#0A0A0B` : uni, il se détoure sans
peine ; noir, le moindre liseré résiduel reste invisible sur la scène du jeu,
qui est noire elle aussi. PNG, JPEG, WebP et SVG sont acceptés au build, mais
seul le PNG passe par ce détourage.

Les prompts sont dans `illustrations/PROMPTS-IMAGES.md`, générés depuis
`contenu.json`. Les contraintes de livraison sont dans
`illustrations/LISEZMOI.md`, reprises à la fin de `brief-illustrations.md`.

`.github/workflows/publier.yml` rejoue exactement ce build à chaque push sur
`main`, recommite les fichiers générés et redéploie Pages. Conséquence utile :
John peut corriger une réplique dans `contenu.json` depuis le site de GitHub, sur
son téléphone, sans terminal.

Si tu trouves une modification faite directement dans `yachtometre.html` ou
`index.html` et absente du template, reporte-la dans `template.html` avant de
rebuilder, sinon tu l'effaces.

---

## 5. Le contenu — c'est le vrai produit

`contenu.json` contient **250 textes** et constitue la source de vérité unique.
Aucun texte visible par l'utilisateur ne doit être écrit en dur ailleurs.

Structure :

| Clé | Contenu |
|---|---|
| `paliers` | 26 paliers, chacun avec `punch` (2 variantes) et `dit` (2 répliques du capitaine) |
| `bandes` | 5 bandes du rainbow : nom affiché et décalage log |
| `capitaine` | 5 niveaux, 10 répliques génériques chacun |
| `notifications` | 7 seaux par ampleur du mouvement, de `krach` à `moon` |
| `opportunite` | 4 seaux selon la longueur perdue |
| `entretien` | 4 états : confortable, juste, intenable, naufrage |
| `paper_hands` | mode phase 9a, branché : le bateau fantôme après une vente déclarée |
| `systeme` | chargement, vides, erreurs, consignes d'installation, avertissement légal |
| `partage` | légendes de la carte |

Les seaux se sélectionnent par la fonction `seau()`, qui lit les bornes
`seuil` / `seuil_m` déclarées dans le JSON. Pour ajouter un seau, il suffit de
l'ajouter au JSON avec ses bornes : le code n'a pas besoin de changer.

Jetons de substitution : `{pct}`, `{delta}`, `{longueur}`, `{annee}`, `{objet}`,
`{montant}`, `{ans}`. Ils sont remplacés par `remplir()`.

### Les règles de ton — la partie la plus fragile du projet

Le code est facile, l'humour est fragile. Si tu écris de nouveaux textes,
respecte ces règles, qui ont été validées par un test réel sur des personnes qui
ne connaissent rien au Bitcoin :

- **Pince-sans-rire.** Le jeu constate, il ne s'enthousiasme pas. Jamais de
  point d'exclamation, jamais d'emoji, jamais de « lol ».
- **Le concret plutôt que l'abstrait.** « Le sauna est parti en premier » vaut
  mieux que « tu as perdu de la valeur ».
- **La chute en dernier mot.** Les meilleures lignes se terminent sur le détail
  qui tue : « dont un boulanger », « il est à moi », « il te mangera quand même ».
- **Ne jamais humilier l'utilisateur.** On se moque de la situation, du bateau,
  du capitaine — pas de lui. Le bas de l'échelle doit être drôle et chaleureux,
  pas méprisant. C'est là que sera la majorité des joueurs.
- **Le capitaine monte en grade avec le bateau** : mousse en tongs → skipper →
  commandant monégasque → assistant du commandant qui ne te parle plus. Cette
  progression est un ressort comique en soi, ne la casse pas.
- **Test de sélection** : une ligne n'entre dans le JSON que si elle fait encore
  sourire à la relecture le lendemain. Dans le doute, on jette.

---

## 6. Les chiffres et leur justification

### Rainbow chart

```
log10(prix en €) = 2,1 · ln(jours depuis le 3 janvier 2009) − 13,35
```

Les constantes ont été ajustées sur les vrais sommets et creux de cycle
convertis en euros (2013, 2015, 2017, 2018, 2021, 2022). Cinq bandes, décalage
en log de −0,56 à +0,56 par pas de 0,28, nommées de « ton beau-frère qui dit que
c'est une bulle » à « Michael Saylor ».

**Point important — la recalibration.** `recalibrer(spot)` déplace toute la
courbe pour qu'elle passe par le cours réel du jour. Conséquence assumée : la
projection est un multiple du prix actuel, donc **le bateau bouge au jour le jour
avec le BTC**. C'est volontaire et c'est ce qui fait vivre le jeu. Sans ça, le
bulletin du matin afficherait toujours zéro. Ne « corrige » pas ce comportement
en croyant à un bug.

### Courbe prix → longueur

Interpolation log-log entre les 26 paliers de `contenu.json`. Elle suit de fait
une loi en longueur^2,8, qui est la vraie relation observée sur le marché du
yacht (le prix suit le volume, pas la longueur). Les prix d'ancrage sont
réalistes : 60 m ≈ 35 M€, 100 m ≈ 150 M€, 180 m ≈ 760 M€.

### Entretien

10 % du prix d'achat par an. C'est la règle du métier, et elle est vraie.
Le « bateau que tu peux entretenir » est celui dont l'entretien annuel tient dans
un retrait de 4 % du stack, soit un bateau coûtant **40 % du stack**. Ce bloc est
à la fois la meilleure blague et la seule vraie leçon du jeu. Ne le supprime pas.

### Affichage des longueurs

Deux fonctions distinctes, ne les confonds pas :

- `metres()` — pour les bateaux : cm sous 1 m, sinon mètres.
- `mesure()` — pour les **écarts et les coûts d'opportunité** : descend jusqu'au
  millimètre. Un café coûte 0,24 mm de yacht, et c'est précisément là qu'est la
  blague. Un « 0 m » arrondi tue l'effet.

---

## 7. Invariants à ne jamais casser

1. **La silhouette humaine de 1,75 m sur chaque bateau**, à l'échelle exacte.
   C'est le cœur visuel de la blague : à 180 m, le bonhomme fait 8 pixels. Un
   illustrateur voudra tricher pour « faire plus joli ». Refuse. Depuis la
   phase 3, l'invariant n'est plus confié à personne : les visuels livrés ne
   contiennent aucun personnage, et le jeu pose la silhouette lui-même à partir
   des dimensions du fichier.
2. **Un seul fichier livrable**, autonome, ouvrable d'un double-clic.
   `manifest.webmanifest`, `sw.js` et `icones/` sont des compagnons
   **facultatifs** : ils ne servent qu'à la version hébergée. `yachtometre.html`
   seul, sur une clé USB, doit continuer à marcher entièrement. Si tu déplaces
   une fonctionnalité du HTML vers un fichier compagnon, tu casses l'invariant.
3. **Aucun texte en dur** hors de `contenu.json`.
4. **Aucune donnée ne quitte l'appareil.** Le stack est dans `localStorage`,
   point. C'est écrit dans le pied de page, ça doit rester vrai.
5. **L'avertissement légal reste affiché** : le rainbow chart n'est pas une
   prédiction. Nécessaire pour la publication sur les stores, et honnête.
6. **Une notification par jour maximum.** Jamais deux.

---

## 8. Ce qui reste à faire

Voir `ROADMAP.md` pour le détail. Par ordre de valeur :

1. **Les 26 illustrations** (phase 3), en **photoréaliste**. Le brief est dans
   `brief-illustrations.md`, les prompts dans `illustrations/PROMPTS-IMAGES.md`,
   tous deux générés depuis `contenu.json`. Les silhouettes SVG actuelles sont
   procédurales et servent de gabarit de proportions, pas de modèle de style. **La prise est posée** : déposer un SVG dans
   `illustrations/` suffit, il n'y a pas de code à écrire à la livraison, y
   compris dessin par dessin.

   Le cadrage a été réparé au passage, pour les deux chemins à la fois : voir
   `poserScene()` ci-dessous.
2. **Le vrai push quotidien** (phase 8b). Voir la limite ci-dessous.
3. **Le mode multi-actifs.** Le même moteur marche avec des actions. C'est ce qui
   ouvrirait un second public.

---

## 9. Limites et pièges connus

- **Pas de notification hors application.** Un fichier HTML ne peut pas notifier
  quand il est fermé. Le bandeau « Ce matin » s'affiche à l'ouverture. Pour une
  vraie notification à 8 h il faut une application native **et** un petit serveur
  qui relève le cours à 7 h 55, parce qu'une notification locale programmée ne
  connaît pas le cours au moment où elle sonne. Ne promets pas à John une
  notification native sans lui expliquer cette contrainte.
- **Les API de cours tombent.** Trois sources en cascade (CoinGecko, Coinbase,
  Binance) et un repli manuel. Si tu en ajoutes une, vérifie qu'elle autorise le
  CORS depuis un navigateur.
- **La clé `localStorage` est `yachtometre-v2`.** Si tu changes la calibration du
  rainbow, incrémente la clé, sinon le premier bulletin après mise à jour
  affichera un écart énorme et faux.
- **`localStorage` est par navigateur.** Ouvrir dans Safari puis Chrome donne deux
  bateaux qui ne se connaissent pas. C'est normal, John le sait.
- **La carte de partage dépend des polices chargées.** Elle se redessine sur
  `document.fonts.ready`. Hors ligne, le titrage retombe sur Impact.
- **Le fantôme mélange deux horizons, et c'est voulu.** Son avance sur le bateau
  réel se lit sur l'année projetée ; son gain « depuis la vente » se lit entre le
  cours de vente et celui d'aujourd'hui. Confondre les deux donnerait un chiffre
  faux. Et `lignes_tout_vendu` n'est tirée que si le stack est à zéro : sinon la
  réplique « ton bateau réel : néant » ment à quelqu'un qui a encore des
  bitcoins.
- **Le poids est le vrai risque du photoréalisme.** Le fichier fait 76 Ko
  aujourd'hui. Vingt-six photos incrustées en base64 le porteront à plusieurs
  mégaoctets. Tant que ça tient sous ~5 Mo, l'invariant du fichier unique est
  préservé et le service worker le met en cache une fois pour toutes. Au-delà,
  la sortie prévue est de servir les images comme fichiers séparés dans
  `index.html` — précachés par le service worker — en gardant l'incrustation
  pour `yachtometre.html`, le fichier hors ligne. Même template, deux sorties :
  ne pars pas sur deux rendus différents.
- **Le service worker sert le réseau d'abord, le cache en repli.** C'est
  délibéré : un cache-d'abord ferait tourner un téléphone sur une version
  périmée pendant des jours. Ne « optimise » pas en inversant. Le cours du BTC
  n'est jamais mis en cache, un prix périmé étant pire qu'un prix absent.
- **Le service worker ne s'enregistre qu'en HTTPS.** Ouvert en `file://`, le jeu
  fonctionne à l'identique, simplement sans mise en cache. Idem pour le bandeau
  d'installation, masqué en local et une fois l'application posée.
- **`archive/expo-v0.4/` est périmé.** Ce squelette React Native a été écrit avant
  la refonte : ancienne palette nautique, anciennes constantes de rainbow,
  ancien `metres()` sans millimètres. Il montre une architecture qui fonctionne,
  mais **resynchronise-le depuis `template.html` avant d'en réutiliser une ligne**.

---

## 10. Décisions déjà tranchées — ne les rejoue pas

| Décision | Pourquoi |
|---|---|
| Le bateau bouge tous les jours avec le cours | C'est le seul mécanisme de rétention. Sans lui, le jeu est un calculateur qu'on ouvre une fois. |
| Palette Bitcoin (noir + `#F7931A`) | Demande explicite de John. C'était auparavant une palette nautique bleu-craie. |
| Illustrations photoréalistes plutôt qu'aplats vectoriels | Décision de John après essai sur Gemini et ChatGPT : le vectoriel plat faisait « dessin pour enfants ». Il veut qu'on puisse se projeter sur l'image. La palette plate reste celle de l'interface. |
| Nom : Le Yachtomètre | Tranché. |
| Un seul fichier HTML plutôt qu'une app native | Choix imposé par le niveau de John et par la vitesse d'itération. Le natif viendra quand le rituel quotidien aura fait ses preuves. |
| La carte de partage est une fonctionnalité de premier plan | C'est le seul canal d'acquisition du jeu. Elle porte l'adresse du jeu, et le bouton passe par la feuille de partage du système : sur iPhone, un lien de téléchargement vers un `data:` ne fait souvent rien, surtout depuis l'application posée sur l'écran d'accueil. |
| Les paliers bas et hauts sont figés | John les a validés nommément. Tu peux en ajouter entre, pas en retirer. |
| Prix en euros | Par défaut. Une bascule de devise serait un plus, pas une correction. |
| PWA hébergée sur GitHub Pages plutôt qu'app native | Donne l'icône, le plein écran et le hors ligne sans rien changer au livrable ni imposer un store. Le natif ne se justifiera que pour la notification poussée à 8 h. |
| Publication automatique à chaque push | Pour que John puisse corriger un texte depuis son téléphone sans terminal. |

---

## 11. Comment vérifier ton travail

Après un build, ces trois vérifications attrapent 90 % des régressions :

```bash
# 1. Le JavaScript compile
node -e "const h=require('fs').readFileSync('yachtometre.html','utf8');
new Function(h.match(/<script>([\s\S]*)<\/script>/)[1]); console.log('OK');"

# 2. Le JSON est valide
node -e "JSON.parse(require('fs').readFileSync('contenu.json')); console.log('OK');"
```

3. Ouvre le fichier et fais glisser le stack de `0` à `300` BTC. Tu dois voir
   passer toute l'échelle sans trou : rien → canard → frite → matelas → kayak →
   paddle → pédalo → barque → jet-ski → semi-rigide → open → voilier → vedette →
   yachts → superyachts, avec l'héliport à 60 m, le sous-marin à 80 m et le
   shadow boat à 100 m.

Un bon réflexe avant de livrer : rejoue le calcul de `0,35 BTC en 2032, bande
médiane`. Le résultat attendu est un voilier de croisière d'environ 10 mètres.
Si tu obtiens un pédalo ou un superyacht, la calibration a bougé.

4. Pour la version hébergée, deux pièges de plus :

```bash
# le service worker compile
node --check sw.js

# les deux sorties sont bien identiques
cmp index.html yachtometre.html && echo 'OK'
```

Et sur le téléphone : après une mise à jour, ferme complètement l'application
posée sur l'écran d'accueil avant de la rouvrir. Sinon tu regardes l'ancien
rendu et tu débugues un fantôme.
