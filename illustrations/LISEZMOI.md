# illustrations/

Dépose un fichier SVG ici et il remplace la silhouette correspondante dans le
jeu. Rien d'autre à faire : le build l'incruste dans le HTML, et la publication
se déclenche toute seule.

Le dossier peut rester vide. Dans ce cas le jeu utilise ses silhouettes
procédurales, qui ne sont qu'un gabarit de proportions.

## Le nom du fichier fait tout

`<id>.svg`, où `<id>` est l'identifiant du palier dans `contenu.json` :

```
rien     canard   frite    matelas  kayak    paddle   pedalo   barque
jetski   rib      open7    voilier  vedette  y15      y20      y26
y32      s41      s52      s60      s72      s80      s100     s120
s140     s180
```

Et pour les cinq portraits : `capitaine-0.svg` à `capitaine-4.svg`
(0 personne, 1 le mousse, 2 le skipper, 3 le commandant, 4 son assistant).

Un dessin peut arriver seul : les 25 autres paliers continuent d'utiliser la
silhouette procédurale en attendant.

## Contraintes techniques

Le livrable du jeu est **un fichier HTML unique**. Les dessins sont donc
recopiés dedans, pas chargés à côté. Il en découle :

- **Un `viewBox`, pas d'attributs `width` ni `height`.** N'importe quelles
  proportions conviennent, le cadre s'y adapte.
- **Rien d'extérieur** : pas de `<image href="http…">`, pas de police liée,
  pas de feuille de style externe. Les textes sont vectorisés.
- **Pas de `<style>` ni de `<script>`** : couleurs et traits en attributs de
  présentation, sinon le style déborde sur le reste de la page.
- **Identifiants préfixés** par le nom du fichier (`voilier-mat`, pas `mat`) :
  un bateau et un portrait cohabitent dans la même page.
- **60 Ko par fichier au maximum**, sinon le jeu devient lourd à ouvrir sur un
  téléphone. Le build prévient au-delà de 2 Mo au total.

Le reste — style, palette, silhouette humaine de 1,75 m, équipements par
seuil — est dans `brief-illustrations.md`, qui est la commande à envoyer.
