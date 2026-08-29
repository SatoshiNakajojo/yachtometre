# ⚠ Ce dossier est périmé

Squelette Expo écrit **avant** la refonte visuelle et la recalibration du moteur.
Il montre une architecture qui fonctionne, mais son contenu a divergé.

Ce qui est faux ici, par rapport à `template.html` à la racine :

| Fichier | Écart |
|---|---|
| `src/theme.js` | Ancienne palette nautique (bleu, craie, laiton). La palette actuelle est Bitcoin : noir `#0A0A0B`, orange `#F7931A`. |
| `src/moteur.js` | `RB_A = 2.0`, `RB_B = -12.364`, bandes à ±0,35 / ±0,70. Valeurs actuelles : `2.1`, `-13.35`, bandes à ±0,28 / ±0,56. |
| `src/moteur.js` | Pas de fonction `mesure()` : les coûts d'opportunité s'affichent en mètres arrondis, donc « 0 m » pour un café. Régression comique. |
| `src/Bateau.js` | Couleurs de l'ancienne palette. La géométrie, elle, est bonne et directement réutilisable. |
| `App.js` | Ne contient ni le mètre de yacht ni la carte de partage. |

**Marche à suivre pour le réutiliser :** repartir de `template.html`, qui est la
référence, et ne récupérer d'ici que la structure (stockage, notifications,
découpage en composants) et la géométrie des coques.
