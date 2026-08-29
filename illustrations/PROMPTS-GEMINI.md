# Les 26 illustrations avec Gemini

Mode d'emploi complet. Aucune connaissance technique nécessaire.

## Comment faire

1. Ouvre Gemini et choisis la génération d'image.
2. Copie **le bloc du bateau voulu** ci-dessous, colle-le, envoie.
3. Regarde le résultat. S'il ne va pas, regénère : c'est gratuit, et le
   deuxième essai est souvent le bon.
4. Télécharge l'image **en PNG**.
5. Renomme le fichier avec le nom indiqué au-dessus du bloc, par exemple
   `voilier.png`.
6. Dépose-le dans le dossier `illustrations/` du dépôt GitHub, via le bouton
   *Add file → Upload files*. Ça marche depuis un téléphone.

Deux minutes plus tard le jeu affiche ton dessin. Tu peux n'en faire qu'un
pour commencer : les 25 autres paliers gardent leur silhouette actuelle.

## Ce que le jeu fait tout seul

Tu n'as **pas** à te soucier de la taille ni du cadrage :

- Les marges transparentes sont rognées automatiquement à la publication.
- Le jeu déduit l'échelle de l'image et pose lui-même la silhouette humaine
  de 1,75 m à côté du bateau. C'est pour ça que les prompts interdisent de
  dessiner un personnage : un générateur d'image ne sait pas tenir une
  échelle, le code si.
- Le jeu dessine aussi la mer, le quai et la ligne de flottaison. D'où le
  fond transparent, qui est la seule contrainte à ne jamais lâcher.

Si Gemini refuse obstinément le fond transparent, demande-lui un fond
**magenta uni #FF00FF** et dis-le-moi : je ferai le nécessaire pour le
retirer au moment du build.

## Vérifier une image en dix secondes

- Fond transparent, ou à défaut damier gris dans l'aperçu.
- Vue de profil, proue à droite.
- Rien sous la flottaison, le bas de l'image est la surface de l'eau.
- Aucun bonhomme, aucun texte.
- Seulement du blanc cassé, de l'orange, du gris et du noir.

---

### 01 · Rien du tout

Fichier à déposer : **`rien.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un ponton de bois vide vu de profil, sur pilotis, avec une bitte d'amarrage et un vieux pneu de défense suspendu au bord. Aucun bateau.
```

### 02 · Bouée canard

Fichier à déposer : **`canard.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : une bouée canard gonflable : anneau flottant, tête ronde dressée, bec plat, un œil.

Longueur réelle de l'objet : 1,1 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 03 · Frite de piscine

Fichier à déposer : **`frite.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : une frite de piscine en mousse, simple cylindre horizontal aux bouts arrondis.

Longueur réelle de l'objet : 1,6 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 04 · Matelas gonflable Décathlon

Fichier à déposer : **`matelas.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un matelas gonflable de plage à rayures, boudins parallèles, un traversin relevé à une extrémité.

Longueur réelle de l'objet : 1,9 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 05 · Kayak gonflable

Fichier à déposer : **`kayak.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un kayak gonflable une place, boudins latéraux, cockpit creux au centre, une pagaie double posée en travers.

Longueur réelle de l'objet : 2,0 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 06 · Paddle

Fichier à déposer : **`paddle.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : une planche de paddle seule, longue et fine, poignée centrale, dérive sous l'arrière, sans rameur.

Longueur réelle de l'objet : 3,2 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 07 · Pédalo avec toboggan

Fichier à déposer : **`pedalo.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un pédalo deux places avec dais rigide sur quatre montants et un toboggan incurvé descendant vers l'arrière.

Longueur réelle de l'objet : 3,0 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 08 · Barque de pêche

Fichier à déposer : **`barque.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : une barque de pêche en bois, banc central, petit hors-bord à l'arrière, une glacière posée à l'avant.

Longueur réelle de l'objet : 4,5 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 09 · Jet-ski « vendu en l'état »

Fichier à déposer : **`jetski.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un jet-ski d'occasion fatigué, guidon haut, carénage marqué, selle longue.

Longueur réelle de l'objet : 3,3 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 10 · Semi-rigide

Fichier à déposer : **`rib.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un bateau semi-rigide : gros boudins latéraux, console centrale avec pare-brise bas, moteur hors-bord.

Longueur réelle de l'objet : 5,5 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 11 · Bateau open 7 m

Fichier à déposer : **`open7.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un bateau open de 7 mètres, pare-brise incliné, banquette arrière, hors-bord.

Longueur réelle de l'objet : 7,0 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 12 · Voilier de croisière

Fichier à déposer : **`voilier.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un voilier de croisière habitable, mât unique portant grand-voile et génois déployés, roof bas avec hublots.

Longueur réelle de l'objet : 9,5 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 13 · Vedette 12 m

Fichier à déposer : **`vedette.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : une vedette habitable, cabine vitrée, flybridge ouvert, mât radar court.

Longueur réelle de l'objet : 12 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 14 · Yacht 15 m

Fichier à déposer : **`y15.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un yacht à moteur, coque blanche, deux ponts et un flybridge, ligne de hublots.

Longueur réelle de l'objet : 15,5 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 15 · Yacht 20 m

Fichier à déposer : **`y20.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un yacht à moteur, coque blanche, deux ponts et un flybridge, annexe sur le pont arrière.

Longueur réelle de l'objet : 20 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 16 · Yacht 26 m

Fichier à déposer : **`y26.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un yacht à moteur, coque blanche, trois ponts, flybridge couvert, mât radar.

Longueur réelle de l'objet : 26 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 17 · Yacht 32 m

Fichier à déposer : **`y32.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un yacht à moteur, coque blanche, trois ponts, grand flybridge, jacuzzi sur le pont supérieur.

Longueur réelle de l'objet : 32 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 18 · Superyacht 41 m

Fichier à déposer : **`s41.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht, coque profilée, quatre ponts étagés, mât radar, annexe en pontée.

Longueur réelle de l'objet : 41 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 19 · Superyacht 52 m

Fichier à déposer : **`s52.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht, coque profilée, quatre ponts étagés, piscine sur le pont principal, mât radar.

Longueur réelle de l'objet : 52 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 20 · Superyacht 60 m — héliport

Fichier à déposer : **`s60.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht, coque profilée, quatre ponts étagés, et sur le pont avant une hélisurface circulaire marquée d'un H, vide.

Longueur réelle de l'objet : 60 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 21 · Superyacht 72 m

Fichier à déposer : **`s72.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht, coque profilée, cinq ponts étagés, plage arrière ouverte en beach club, mât radar.

Longueur réelle de l'objet : 72 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 22 · Superyacht 80 m — sous-marin

Fichier à déposer : **`s80.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht, coque profilée, cinq ponts étagés, hélisurface marquée d'un H sur le pont avant, et un petit sous-marin de poche orange visible dans le garage arrière ouvert.

Longueur réelle de l'objet : 80 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 23 · Superyacht 100 m — shadow boat

Fichier à déposer : **`s100.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht, coque profilée, cinq ponts étagés, hélisurface marquée d'un H sur le pont avant, sous-marin de poche orange dans le garage arrière ouvert.

Longueur réelle de l'objet : 100 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 24 · Superyacht 120 m

Fichier à déposer : **`s120.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht, coque profilée, cinq ponts étagés, deux hélisurfaces circulaires marquées d'un H, l'une à l'avant l'autre à l'arrière, toutes deux vides.

Longueur réelle de l'objet : 120 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 25 · Superyacht 140 m

Fichier à déposer : **`s140.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht, coque profilée, cinq ponts étagés, deux hélisurfaces marquées d'un H, piscine, mât radar élancé.

Longueur réelle de l'objet : 140 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

### 26 · Superyacht 180 m

Fichier à déposer : **`s180.png`**

```
Illustration vectorielle plate pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun reflet, aucun réalisme photographique.

Palette stricte, aucune autre couleur : blanc cassé #FAF8F5 pour les coques et les volumes principaux, orange #F7931A pour un seul accent, gris #8A8A93 pour les mâts et les pièces fines, noir #0A0A0B pour les ouvertures et les creux.

Cadrage : vue de profil strictement latérale, proue tournée vers la droite, aucune perspective, aucun angle de trois quarts.

Contraintes impératives :
- FOND TRANSPARENT. Aucun fond, aucun ciel, aucune mer, aucun décor.
- L'objet est coupé net à la ligne de flottaison : ne dessine rien de ce qui serait sous l'eau. Le bord bas de l'image est la surface de l'eau.
- L'objet touche les quatre bords de l'image, sans marge.
- Aucun personnage, aucune silhouette humaine, aucun animal.
- Aucun texte, aucun chiffre, aucun logo, aucune signature, aucun cadre, aucune bordure.
- Un seul objet, entier, rien d'autre dans l'image.

Sujet : un superyacht immense, coque profilée très longue, cinq ponts étagés, deux hélisurfaces marquées d'un H, piscine, garage arrière ouvert.

Longueur réelle de l'objet : 180 mètres. Respecte les proportions d'un objet de cette taille (nombre de ponts, finesse de la coque, hauteur relative).
```

---

## Les 5 portraits de capitaine

Ceux-là gardent leur fond : ils s'affichent dans un carré, pas sur la mer.

### Niveau 0 · Personne

Fichier à déposer : **`capitaine-0.png`**

```
Portrait illustré en vectoriel plat pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun réalisme photographique.

Palette stricte, aucune autre couleur : fond gris très sombre #141416, blanc cassé #FAF8F5 pour les vêtements et les visages, orange #F7931A pour un seul accent, gris #8A8A93 pour les détails, noir #0A0A0B pour les creux.

Cadrage carré, buste, personnage centré, aucun texte, aucun logo, aucune bordure. Visage stylisé et simplifié, pas de traits réalistes.

Sujet : un fauteuil de pont vide vu de face, et posé sur l'assise un cadre photo montrant un bateau.
```

### Niveau 1 · Le mousse

Fichier à déposer : **`capitaine-1.png`**

```
Portrait illustré en vectoriel plat pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun réalisme photographique.

Palette stricte, aucune autre couleur : fond gris très sombre #141416, blanc cassé #FAF8F5 pour les vêtements et les visages, orange #F7931A pour un seul accent, gris #8A8A93 pour les détails, noir #0A0A0B pour les creux.

Cadrage carré, buste, personnage centré, aucun texte, aucun logo, aucune bordure. Visage stylisé et simplifié, pas de traits réalistes.

Sujet : un adolescent assis en tongs, casquette à l'envers, short, vapoteuse à la main, avachi, il ne se lève pas.
```

### Niveau 2 · Le skipper

Fichier à déposer : **`capitaine-2.png`**

```
Portrait illustré en vectoriel plat pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun réalisme photographique.

Palette stricte, aucune autre couleur : fond gris très sombre #141416, blanc cassé #FAF8F5 pour les vêtements et les visages, orange #F7931A pour un seul accent, gris #8A8A93 pour les détails, noir #0A0A0B pour les creux.

Cadrage carré, buste, personnage centré, aucun texte, aucun logo, aucune bordure. Visage stylisé et simplifié, pas de traits réalistes.

Sujet : un skipper debout, chemise blanche repassée manches retroussées, lunettes de soleil, bras croisés, air légèrement condescendant.
```

### Niveau 3 · Le commandant

Fichier à déposer : **`capitaine-3.png`**

```
Portrait illustré en vectoriel plat pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun réalisme photographique.

Palette stricte, aucune autre couleur : fond gris très sombre #141416, blanc cassé #FAF8F5 pour les vêtements et les visages, orange #F7931A pour un seul accent, gris #8A8A93 pour les détails, noir #0A0A0B pour les creux.

Cadrage carré, buste, personnage centré, aucun texte, aucun logo, aucune bordure. Visage stylisé et simplifié, pas de traits réalistes.

Sujet : un commandant de bord en blazer bleu marine à galons dorés et casquette d'officier, buste droit, regard tourné de côté, jamais vers le spectateur.
```

### Niveau 4 · Son assistant

Fichier à déposer : **`capitaine-4.png`**

```
Portrait illustré en vectoriel plat pour une application. Style affiche : formes pleines, aplats de couleur, aucun dégradé, aucune texture, aucune ombre portée, aucun réalisme photographique.

Palette stricte, aucune autre couleur : fond gris très sombre #141416, blanc cassé #FAF8F5 pour les vêtements et les visages, orange #F7931A pour un seul accent, gris #8A8A93 pour les détails, noir #0A0A0B pour les creux.

Cadrage carré, buste, personnage centré, aucun texte, aucun logo, aucune bordure. Visage stylisé et simplifié, pas de traits réalistes.

Sujet : un jeune homme en polo brodé tenant une tablette contre lui, sourire poli et fermé, seul dans le cadre.
```
