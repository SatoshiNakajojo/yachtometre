# Le Yachtomètre — feuille de route

Principe directeur : **le risque de ce projet n'est pas technique, il est
comique.** Le code est simple, la blague est fragile. C'est pourquoi la
validation du rire est passée avant toute écriture d'application.

---

## Fait

### Phase 0 — Socle chiffré ✅
Moteur rainbow, courbe prix → longueur, table des 26 paliers.

### Phase 1 — Prototype jouable ✅
**Test décisif, passé.** Envoyé à des testeurs dont plusieurs ne connaissaient
rien au Bitcoin. Tout le monde a ri. C'est ce qui a autorisé la suite.

### Phase 2 — La voix ✅
237 textes dans `contenu.json`. C'était le vrai travail du projet, pas le code.

### Phase 4 — Le bateau vivant ✅ *(version web)*
Mémoire locale de la mesure de la veille, bandeau « Ce matin » au premier
lancement de la journée, seaux de notification par ampleur du mouvement.
**C'est le mécanisme de rétention du jeu.**

### Phase 5 — Le mètre de yacht ✅
Conversion de n'importe quelle dépense en millimètres de coque, avec projection
future. Raccourcis pré-remplis.

### Phase 6 — L'entretien ✅
Les deux bateaux côte à côte : celui qu'on peut acheter, celui qu'on peut
garder. 10 % du prix par an contre un retrait de 4 %.

### Phase 7 — La carte de partage ✅
Carte 1080 × 1080 en canvas, téléchargeable en PNG, légendes rotatives.
Traitée comme une fonctionnalité de premier plan : c'est le seul canal
d'acquisition du jeu.

### Phase 8a — Hébergement et écran d'accueil ✅
Publié sur <https://satoshinakajojo.github.io/yachtometre/>, installable en
Partager → Sur l'écran d'accueil : icône, plein écran, ouverture hors ligne.
Le build et la publication se rejouent tout seuls à chaque modification de
`contenu.json`, y compris depuis le site de GitHub sur téléphone.
**Ce que ça ne donne pas : la notification à 8 h.** Voir phase 8b.

### Phase 9a — Mode paper hands ✅
L'utilisateur déclare combien il a vendu et à quel cours. Le jeu affiche le
bateau fantôme qu'il aurait eu, ce que la vente lui coûte en mètres de coque, et
ce que le fantôme a gagné depuis. S'il a vendu plus haut que le cours du jour,
le jeu le reconnaît — on se moque de la situation, pas de lui.

---

## À faire

### Phase 3 — Les illustrations — *en cours, 22 sur 26*
26 silhouettes + 5 portraits de capitaine. Le brief est prêt
(`brief-illustrations.md`), généré depuis `contenu.json` pour ne jamais diverger.
Les SVG procéduraux actuels tiennent la route mais plafonnent la qualité perçue.
Parallélisable : ça n'empêche aucun autre chantier d'avancer.

**Vingt-deux visuels sont en ligne**, en photoréaliste, 1,5 Mo au total après
compression. Restent le voilier, les superyachts de 120, 140 et 180 m, et les
cinq portraits de capitaine.

**Le branchement est fait, et les prompts sont écrits.** Un PNG ou un SVG
déposé dans `illustrations/`, nommé d'après l'id du palier, remplace la
silhouette de ce palier — dessin par dessin, sans code à écrire, et la
publication se relance seule. Le jeu calcule l'échelle depuis les dimensions du
fichier et pose lui-même la silhouette de 1,75 m, ce qui rend l'invariant n° 1
indépendant de qui dessine.

Deux voies possibles :
- `illustrations/PROMPTS-IMAGES.md` : 31 prompts prêts à coller, gratuits.
  Direction photoréaliste depuis que les aplats vectoriels ont été jugés trop
  enfantins à l'essai.
- `brief-illustrations.md` : la même commande, à envoyer à un prestataire.

Contraintes de livraison dans `illustrations/LISEZMOI.md`.

### Phase 8b — Mobile natif — *priorité 3*
Le seul argument qui reste pour le natif est **la notification du matin**, que ni
un fichier HTML ni la version posée sur l'écran d'accueil ne savent envoyer quand
l'application est fermée. Tout le reste — icône, plein écran, hors ligne — est
déjà acquis en phase 8a.

Expo / React Native. `archive/expo-v0.4/` contient un squelette fonctionnel mais
**périmé** (ancienne palette, anciennes constantes). À resynchroniser depuis
`template.html`.

Prérequis honnête : le vrai bulletin poussé à 8 h demande un petit serveur qui
relève le cours à 7 h 55, parce qu'une notification locale programmée ne connaît
pas le cours au moment où elle sonne. Un cron et une vingtaine de lignes,
hébergeable gratuitement.

À vérifier avant d'y aller : le risque n° 3 ci-dessous. Si personne ne revient le
deuxième matin, la notification ne sauvera rien.

À prévoir aussi : politique de confidentialité, et positionnement en
« divertissement » plutôt qu'en « finance » sur la fiche store, pour éviter les
allers-retours avec Apple.

### Phase 9b — Compléments
- Comparaisons d'échelle visuelles (bateau contre bus, terrain de foot, tour couchée)
- Naufrage par défaut d'entretien — **mécanique la plus risquée du lot**, elle
  peut frustrer plus qu'amuser. À tester séparément.
- Mode multi-actifs : le même moteur marche avec des actions. C'est ce qui
  ouvrirait un second public.
- Bascule de devise
- Cosmétiques payants : pavillon, nom du bateau gravé

---

## Les trois risques réels

1. **Le rire ne prend pas chez les non-initiés.** → Écarté en phase 1.
2. **Les textes deviennent tièdes en grandissant.** → Risque permanent. Le filtre
   reste : une ligne n'entre que si elle fait encore sourire le lendemain.
3. **Un seul usage par personne.** → C'est ce que la phase 4 combat, et ce que la
   phase 8a rend mesurable : le jeu est maintenant à une icône de distance.
   À surveiller avec de vrais utilisateurs : reviennent-ils le deuxième matin ?
