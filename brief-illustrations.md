# Le Yachtomètre — brief d'illustration (phase 3)

## Règles communes, non négociables

- **Une silhouette humaine de 1,75 m sur chaque visuel**, à l'échelle exacte du bateau. C'est ce qui porte la blague.
- Style plat, silhouettes pleines, pas de dégradé, pas de réalisme.
- Palette imposée : noir `#0A0A0B`, coque `#FAF8F5`, gris `#8A8A93`, orange Bitcoin `#F7931A`, mer `#0D1114`.
- Vue de profil stricte, proue à droite, ligne de flottaison horizontale à hauteur constante.
- Format SVG, cadrage large (le bateau n'occupe jamais toute la largeur).

## Équipements déclenchés par la taille

| Seuil | À faire apparaître |
|---|---|
| ≥ 60 m | Hélisurface marquée d'un H, sur le pont avant, **vide** |
| ≥ 80 m | Sous-marin de poche orange, dans le garage arrière |
| ≥ 100 m | Shadow boat, en arrière-plan, ~40 % de la taille du navire principal |
| ≥ 120 m | Deux hélisurfaces, jamais occupées en même temps |

## Les 26 visuels

| # | Palier | Longueur | Classe | Direction |
|---|---|---|---|---|
| 01 | Rien du tout | — | `rien` | Aucun bateau — un ponton vide et une silhouette qui regarde l’horizon. |
| 02 | Bouée canard | 1,1 m | `duck` | Bouée canard gonflable, anneau + tête + bec. |
| 03 | Frite de piscine | 1,6 m | `noodle` | Frite de piscine, cylindre en mousse. |
| 04 | Matelas gonflable Décathlon | 1,9 m | `mattress` | Matelas gonflable rayé, avec un filet de bulles au niveau de la fuite. |
| 05 | Kayak gonflable | 2,0 m | `kayak` | Kayak gonflable une place, pagaie plastique. |
| 06 | Paddle | 3,2 m | `paddle` | Planche de paddle, rameur debout (c’est ici la silhouette de référence). |
| 07 | Pédalo avec toboggan | 3,0 m | `pedalo` | Pédalo deux places, dais, toboggan arrière. |
| 08 | Barque de pêche | 4,5 m | `barque` | Barque de pêche, petit hors-bord, banc central. |
| 09 | Jet-ski « vendu en l'état » | 3,3 m | `jetski` | Jet-ski d’occasion, guidon, carénage fatigué. |
| 10 | Semi-rigide | 5,5 m | `rib` | Semi-rigide, boudins, console centrale. |
| 11 | Bateau open 7 m | 7,0 m | `open` | Bateau open, pare-brise, banquette arrière. |
| 12 | Voilier de croisière | 9,5 m | `sail` | Voilier de croisière, grand-voile + génois. |
| 13 | Vedette 12 m | 12 m | `vedette` | Vedette habitable, cabine vitrée, mât radar. |
| 14 | Yacht 15 m | 15,5 m | `yacht` | Yacht à moteur, coque blanche, 2 à 3 ponts, flybridge. |
| 15 | Yacht 20 m | 20 m | `yacht` | Yacht à moteur, coque blanche, 2 à 3 ponts, flybridge. |
| 16 | Yacht 26 m | 26 m | `yacht` | Yacht à moteur, coque blanche, 2 à 3 ponts, flybridge. |
| 17 | Yacht 32 m | 32 m | `yacht` | Yacht à moteur, coque blanche, 2 à 3 ponts, flybridge. |
| 18 | Superyacht 41 m | 41 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |
| 19 | Superyacht 52 m | 52 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |
| 20 | Superyacht 60 m — héliport | 60 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |
| 21 | Superyacht 72 m | 72 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |
| 22 | Superyacht 80 m — sous-marin | 80 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |
| 23 | Superyacht 100 m — shadow boat | 100 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |
| 24 | Superyacht 120 m | 120 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |
| 25 | Superyacht 140 m | 140 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |
| 26 | Superyacht 180 m | 180 m | `super` | Superyacht, coque profilée, 3 à 5 ponts, mât radar, équipements selon la taille. |

## Les 5 portraits de capitaine

| Niveau | Rôle | Direction |
|---|---|---|
| 0 | Personne | Aucun équipage. Un fauteuil vide et une photo de bateau. |
| 1 | Le mousse | Un ado en tongs qui vapote, casquette à l'envers, ne se lève pas. |
| 2 | Le skipper | Chemise blanche repassée, lunettes de soleil, légèrement condescendant. |
| 3 | Le commandant | Monégasque en blazer, galons dorés, ne te regarde pas dans les yeux. |
| 4 | Son assistant | Un jeune homme en polo brodé, tablette à la main. Le commandant reste invisible. |

---

Total : 26 silhouettes + 5 portraits.
Le fichier `template.html` contient une version SVG procédurale de chaque classe :
elle sert de gabarit de proportions, pas de modèle de style.
Budget observé pour ce volume en style plat : 400 à 900 €.