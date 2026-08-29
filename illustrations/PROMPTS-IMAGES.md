# Les 26 illustrations — version photoréaliste

Direction artistique arrêtée par John : des images réalistes, presque des
photos, sur lesquelles on puisse se projeter. La version en aplats vectoriels
est abandonnée.

## Comment faire

1. Ouvre Gemini ou ChatGPT, en mode image.
2. **Colle d'abord le bloc RÈGLES ci-dessous, une seule fois par conversation.**
   L'outil répondra « compris ».
3. Colle ensuite le bloc du bateau voulu. Un bloc, une image.
4. Regarde le résultat. S'il ne va pas, redemande : c'est gratuit, et le
   deuxième essai est souvent le bon.
5. Télécharge l'image. **PNG ou JPEG, peu importe** : la publication convertit
   ce qu'il faut.
6. Renomme avec le nom indiqué au-dessus du bloc, par exemple `voilier.png`.
7. Dépose dans le dossier `illustrations/` du dépôt GitHub, via
   *Add file → Upload files*. Ça marche depuis un téléphone.

Si après quelques images l'outil recommence à faire du dessin ou des vues de
trois quarts, recolle le bloc RÈGLES : il a oublié.

## Ce que le jeu fait tout seul

Tu n'as **pas** à te soucier du fond, de la taille ni du cadrage :

- Le fond noir est **retiré automatiquement** à la publication, par
  remplissage depuis les bords — les hublots sombres à l'intérieur du bateau
  sont préservés.
- Les marges sont rognées automatiquement.
- Un JPEG est converti en PNG avant tout ça, et une image trop large est
  ramenée à 1600 pixels.
- Le jeu déduit l'échelle de l'image et pose lui-même la silhouette humaine
  de 1,75 m à côté du bateau. C'est pour ça que les règles interdisent toute
  personne dans l'image : un générateur ne sait pas tenir une échelle, le
  code si.
- Le jeu dessine aussi la mer et le quai. D'où le cadrage coupé net à la
  flottaison.

## Vérifier une image en dix secondes

- **Le bateau est-il entier ?** Mât, antenne, proue, poupe : rien ne doit
  toucher le bord de l'image. Un mât coupé se voit tout de suite dans le jeu.
- Vraiment de profil ? Si tu vois le pont d'en haut ou l'avant de face, jette.
- Fond noir bien uni, sans dégradé ni halo ?
- **Rien sous l'objet ?** Pas de reflet, pas d'image miroir, pas d'ombre au sol.
  C'est le défaut le plus fréquent, et le plus traître : le reflet double la
  hauteur mesurée et fausse toute l'échelle.
- **Aucune lettre nulle part ?** Nom, numéro, marque : le générateur adore
  écrire sur les coques. Regarde deux fois.
- Rien sous la flottaison, pas une goutte d'eau ?
- Personne dans l'image ?
- Est-ce que ça ressemble à un bateau de cette longueur-là ?

## Corriger sans tout refaire

Les deux ratés ci-dessus se réparent par retouche, en gardant l'image :

```
Reprends cette image et supprime le reflet sous l'objet. Fond noir uni, l'objet flotte dans le vide, aucune surface réfléchissante, aucune symétrie.
```

```
Reprends cette image et efface toutes les inscriptions sur la coque. Aucun texte, aucun chiffre, aucune marque. La coque doit être entièrement lisse et anonyme.
```

```
Reprends cette image en dézoomant : le bateau doit tenir entièrement dans le cadre, mât et antennes compris, sans que rien ne soit coupé par les bords. Garde le fond noir uni.
```

Et pour un sujet plus haut que large — le voilier — repasser en carré suffit
souvent là où le dézoom échoue :

```
Refais cette image au format carré 1:1, en dézoomant assez pour que le mât entier tienne dans le cadre, tête de mât comprise, avec du noir au-dessus. Même bateau, même lumière, même fond noir uni.
```

---

## RÈGLES — à coller en premier, une fois par conversation

```
Je vais te demander une série d'images de bateaux qui doivent former une collection cohérente. Voici les règles communes. Applique-les à chaque image sans exception, et garde-les en mémoire pour toutes les suivantes.

RENDU
Photographie professionnelle, photoréaliste, très haute définition. Matières réelles : gel-coat, inox brossé, teck, toile, vinyle. Aucun style illustré, aucun dessin, aucune bande dessinée, aucun rendu cartoon.

POINT DE VUE
Vue strictement de profil. L'appareil est placé exactement à la hauteur de la ligne de flottaison, très loin, au téléobjectif 300 mm, ce qui écrase toute perspective. Le bateau est parfaitement de côté, proue à droite. Aucune vue de trois quarts, aucune plongée, aucune contre-plongée, aucune fuyante, aucun point de fuite.

LUMIÈRE
Lumière naturelle diffuse de ciel légèrement voilé. Éclairage doux et homogène sur toute la longueur du bateau. Aucune ombre portée, aucun reflet spéculaire violent, aucun contre-jour, aucune heure dorée. Netteté d'un bout à l'autre : aucune profondeur de champ, aucun flou.

FOND
Fond parfaitement uni, noir #0A0A0B, absolument uniforme — aucun dégradé, aucun vignettage, aucune texture, aucun décor. Si ton outil sait produire un fond transparent, c'est encore mieux.

L'objet flotte dans le vide, posé sur rien. Aucun sol, aucune surface brillante, aucune table, et surtout AUCUN REFLET SOUS L'OBJET : ni reflet d'eau, ni reflet de studio, ni image miroir, ni symétrie verticale. Rien ne doit apparaître sous l'objet.

CADRAGE
Le bateau est ENTIER dans l'image. Rien ne sort du cadre : ni le sommet du mât, ni l'antenne, ni le bout de la proue, ni l'arrière. Cadre au plus juste autour de lui, mais sans jamais le rogner — mieux vaut un peu de noir autour qu'un mât coupé.

Aucune eau, aucun reflet dans l'eau, aucune écume, aucun sillage, aucun quai, aucun ciel.

À NE JAMAIS FAIRE
Aucune personne à bord ni à côté.

Aucune inscription d'aucune sorte : pas de nom sur la coque, pas de numéro d'immatriculation, pas de nom de modèle, pas de marque commerciale existante, pas de logo de fabricant, pas de pavillon, pas de signature, pas de filigrane, pas de cadre. Les bateaux sont des modèles génériques, anonymes, sans aucune lettre ni chiffre nulle part.

Réponds simplement « compris » et attends ma première demande.
```

---

### 01 · Rien du tout

Fichier à déposer : **`rien.png`**

```
Image suivante : un ponton de bois vide, vieilles planches grises, une bitte d'amarrage en fonte et un pare-battage suspendu au bord. Aucun bateau, aucune personne.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, bateau entier dans le cadre sans que rien ne soit coupé, aucune eau, aucun reflet ni miroir sous l'objet, aucune personne, aucune inscription ni marque sur la coque.
```

### 02 · Bouée canard

Fichier à déposer : **`canard.png`**

```
Image suivante : une bouée gonflable en forme de canard jaune, vinyle brillant, tête dressée et bec orange, flottant seule.

Longueur réelle : 1,1 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 03 · Frite de piscine

Fichier à déposer : **`frite.png`**

```
Image suivante : une frite de piscine en mousse polyéthylène, cylindre allongé, mousse légèrement granuleuse et bouts arrondis.

Longueur réelle : 1,6 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 04 · Matelas gonflable Décathlon

Fichier à déposer : **`matelas.png`**

```
Image suivante : un matelas gonflable de plage en PVC à rayures, boudins parallèles, valve visible, plastique un peu fatigué.

Longueur réelle : 1,9 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 05 · Kayak gonflable

Fichier à déposer : **`kayak.png`**

```
Image suivante : un kayak gonflable une place, boudins latéraux en toile enduite, cockpit ouvert, une pagaie double posée en travers.

Longueur réelle : 2,0 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 06 · Paddle

Fichier à déposer : **`paddle.png`**

```
Image suivante : une planche de stand-up paddle gonflable, pont antidérapant texturé, poignée centrale, sans rameur.

Longueur réelle : 3,2 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 07 · Pédalo avec toboggan

Fichier à déposer : **`pedalo.png`**

```
Image suivante : un pédalo de location deux places en plastique, dais rigide sur quatre montants, toboggan incurvé à l'arrière, couleurs délavées par le soleil.

Longueur réelle : 3,0 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 08 · Barque de pêche

Fichier à déposer : **`barque.png`**

```
Image suivante : une barque de pêche en bois peint, banc central, petit moteur hors-bord, peinture écaillée, une glacière à l'avant.

Longueur réelle : 4,5 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 09 · Jet-ski « vendu en l'état »

Fichier à déposer : **`jetski.png`**

```
Image suivante : un jet-ski d'occasion visiblement fatigué, carénage rayé, selle usée, guidon haut, autocollants décollés.

Longueur réelle : 3,3 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 10 · Semi-rigide

Fichier à déposer : **`rib.png`**

```
Image suivante : un bateau semi-rigide, gros boudins en hypalon gris, console centrale avec pare-brise bas, moteur hors-bord noir.

Longueur réelle : 5,5 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 11 · Bateau open 7 m

Fichier à déposer : **`open7.png`**

```
Image suivante : un bateau à moteur open de 7 mètres, coque blanche, pare-brise incliné, banquette arrière en skaï, hors-bord.

Longueur réelle : 7,0 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 12 · Voilier de croisière

Fichier à déposer : **`voilier.png`**

> **Celui-ci est le seul difficile.** Un voilier est aussi haut que long : son
> mât ne rentre pas dans une image large, et le générateur le coupe. La
> parade tient en une phrase — **demande une image carrée**. C'est la
> première ligne du bloc ci-dessous, ne la retire pas.

```
Image au format CARRÉ, 1:1. C'est impératif : le bateau est aussi haut que long, une image large lui couperait le mât.

Image suivante : un voilier de croisière habitable, mât unique, grand-voile et génois déployés, roof bas avec hublots, coque blanche. Le mât entier, de la coque à la tête de mât girouette comprise, doit tenir dans l'image avec un peu de noir au-dessus.

Longueur réelle : 9,5 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 13 · Vedette 12 m

Fichier à déposer : **`vedette.png`**

```
Image suivante : une vedette habitable à moteur, coque blanche, cabine vitrée, flybridge ouvert, mât radar court.

Longueur réelle : 12 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 14 · Yacht 15 m

Fichier à déposer : **`y15.png`**

```
Image suivante : un yacht à moteur, coque blanche brillante, deux ponts surmontés d'un flybridge, ligne de hublots teintés.

Longueur réelle : 15,5 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 15 · Yacht 20 m

Fichier à déposer : **`y20.png`**

```
Image suivante : un yacht à moteur, coque blanche brillante, deux ponts et un flybridge, annexe arrimée sur le pont arrière.

Longueur réelle : 20 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 16 · Yacht 26 m

Fichier à déposer : **`y26.png`**

```
Image suivante : un yacht à moteur, coque blanche, trois ponts, flybridge couvert, mât radar, passerelle de coupée relevée.

Longueur réelle : 26 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 17 · Yacht 32 m

Fichier à déposer : **`y32.png`**

```
Image suivante : un yacht à moteur, coque blanche, trois ponts, vaste flybridge, jacuzzi sur le pont supérieur, baies vitrées teintées.

Longueur réelle : 32 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 18 · Superyacht 41 m

Fichier à déposer : **`s41.png`**

```
Image suivante : un superyacht, coque blanche profilée, quatre ponts étagés, mât radar, annexe en pontée, lignes tendues.

Longueur réelle : 41 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 19 · Superyacht 52 m

Fichier à déposer : **`s52.png`**

```
Image suivante : un superyacht, coque blanche profilée, quatre ponts étagés, piscine sur le pont principal, mât radar.

Longueur réelle : 52 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 20 · Superyacht 60 m — héliport

Fichier à déposer : **`s60.png`**

```
Image suivante : un superyacht, coque blanche profilée, quatre ponts étagés, et sur le pont avant une hélisurface circulaire marquée d'un grand H blanc, vide, sans hélicoptère.

Longueur réelle : 60 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 21 · Superyacht 72 m

Fichier à déposer : **`s72.png`**

```
Image suivante : un superyacht, coque blanche profilée, cinq ponts étagés, plage arrière ouverte aménagée en beach club, mât radar.

Longueur réelle : 72 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 22 · Superyacht 80 m — sous-marin

Fichier à déposer : **`s80.png`**

```
Image suivante : un superyacht, coque blanche profilée, cinq ponts étagés, hélisurface marquée d'un H sur le pont avant, et un petit sous-marin de poche orange visible dans le garage arrière ouvert.

Longueur réelle : 80 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 23 · Superyacht 100 m — shadow boat

Fichier à déposer : **`s100.png`**

```
Image suivante : un superyacht, coque blanche profilée, cinq ponts étagés, hélisurface marquée d'un H sur le pont avant, sous-marin de poche orange dans le garage arrière ouvert.

Longueur réelle : 100 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 24 · Superyacht 120 m

Fichier à déposer : **`s120.png`**

```
Image suivante : un superyacht, coque blanche profilée, cinq ponts étagés, deux hélisurfaces circulaires marquées d'un H, l'une à l'avant l'autre à l'arrière, toutes deux vides.

Longueur réelle : 120 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 25 · Superyacht 140 m

Fichier à déposer : **`s140.png`**

```
Image suivante : un superyacht, coque blanche profilée, cinq ponts étagés, deux hélisurfaces marquées d'un H, piscine, mât radar élancé.

Longueur réelle : 140 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

### 26 · Superyacht 180 m

Fichier à déposer : **`s180.png`**

```
Image suivante : un superyacht immense à la coque blanche très allongée, cinq ponts étagés, deux hélisurfaces marquées d'un H, piscine, garage arrière ouvert.

Longueur réelle : 180 mètres. Respecte scrupuleusement les proportions et le niveau de détail d'un objet de cette taille.

Rappel des règles : photoréaliste, vue strictement de profil au téléobjectif, proue à droite, fond noir uni #0A0A0B, image coupée net à la ligne de flottaison, aucune eau, aucune personne, aucun texte.
```

---

## Les 5 portraits de capitaine

Ceux-là gardent leur fond : ils s'affichent dans un petit carré, pas sur la mer.

Ces blocs sont autonomes, le bloc RÈGLES ne s'y applique pas.

### Niveau 0 · Personne

Fichier à déposer : **`capitaine-0.png`**

```
Portrait photographique professionnel, photoréaliste, très haute définition. Aucun style illustré, aucun dessin.

Cadrage carré, plan poitrine, personnage centré, léger flou d'arrière-plan. Fond sombre uni, gris très foncé #141416, sans décor.

Lumière douce et latérale, naturelle, aucune ombre dure. Personne fictive, ne ressemblant à aucune personnalité connue.

Aucun texte, aucun logo, aucune marque, aucun filigrane, aucun cadre.

Sujet : un fauteuil de pont vide en teck et toile blanche, vu de face, et posé sur l'assise un cadre photo en argent montrant un bateau. Aucune personne.
```

### Niveau 1 · Le mousse

Fichier à déposer : **`capitaine-1.png`**

```
Portrait photographique professionnel, photoréaliste, très haute définition. Aucun style illustré, aucun dessin.

Cadrage carré, plan poitrine, personnage centré, léger flou d'arrière-plan. Fond sombre uni, gris très foncé #141416, sans décor.

Lumière douce et latérale, naturelle, aucune ombre dure. Personne fictive, ne ressemblant à aucune personnalité connue.

Aucun texte, aucun logo, aucune marque, aucun filigrane, aucun cadre.

Sujet : un jeune homme d'une vingtaine d'années assis, décontracté jusqu'à l'avachissement, tee-shirt délavé, short de bain, tongs, casquette portée à l'envers, une vapoteuse à la main. Il ne se lève pas.
```

### Niveau 2 · Le skipper

Fichier à déposer : **`capitaine-2.png`**

```
Portrait photographique professionnel, photoréaliste, très haute définition. Aucun style illustré, aucun dessin.

Cadrage carré, plan poitrine, personnage centré, léger flou d'arrière-plan. Fond sombre uni, gris très foncé #141416, sans décor.

Lumière douce et latérale, naturelle, aucune ombre dure. Personne fictive, ne ressemblant à aucune personnalité connue.

Aucun texte, aucun logo, aucune marque, aucun filigrane, aucun cadre.

Sujet : un skipper d'une quarantaine d'années debout, chemise blanche impeccablement repassée manches retroussées, lunettes de soleil, bras croisés, expression légèrement condescendante.
```

### Niveau 3 · Le commandant

Fichier à déposer : **`capitaine-3.png`**

```
Portrait photographique professionnel, photoréaliste, très haute définition. Aucun style illustré, aucun dessin.

Cadrage carré, plan poitrine, personnage centré, léger flou d'arrière-plan. Fond sombre uni, gris très foncé #141416, sans décor.

Lumière douce et latérale, naturelle, aucune ombre dure. Personne fictive, ne ressemblant à aucune personnalité connue.

Aucun texte, aucun logo, aucune marque, aucun filigrane, aucun cadre.

Sujet : un commandant de bord d'une cinquantaine d'années, blazer bleu marine à galons dorés, casquette d'officier, chemise blanche, buste très droit, le regard tourné de côté — il ne regarde jamais l'objectif.
```

### Niveau 4 · Son assistant

Fichier à déposer : **`capitaine-4.png`**

```
Portrait photographique professionnel, photoréaliste, très haute définition. Aucun style illustré, aucun dessin.

Cadrage carré, plan poitrine, personnage centré, léger flou d'arrière-plan. Fond sombre uni, gris très foncé #141416, sans décor.

Lumière douce et latérale, naturelle, aucune ombre dure. Personne fictive, ne ressemblant à aucune personnalité connue.

Aucun texte, aucun logo, aucune marque, aucun filigrane, aucun cadre.

Sujet : un jeune homme en polo de marine brodé, tenant une tablette contre lui, sourire poli et fermé, seul dans le cadre.
```
