# illustrations/

Dépose un fichier ici et il remplace la silhouette correspondante dans le jeu.
Rien d'autre à faire : le recadrage, l'incrustation et la publication se font
tout seuls.

Le dossier peut rester vide. Dans ce cas le jeu utilise ses silhouettes
procédurales, qui ne sont qu'un gabarit de proportions.

**Les prompts prêts à coller sont dans `PROMPTS-IMAGES.md`.**

## Le nom du fichier fait tout

`<id>.png` ou `<id>.svg`, où `<id>` est l'identifiant du palier dans
`contenu.json` :

```
rien     canard   frite    matelas  kayak    paddle   pedalo   barque
jetski   rib      open7    voilier  vedette  y15      y20      y26
y32      s41      s52      s60      s72      s80      s100     s140
s120     s180
```

Et pour les cinq portraits : `capitaine-0.png` à `capitaine-4.png`
(0 personne, 1 le mousse, 2 le skipper, 3 le commandant, 4 son assistant).

Un dessin peut arriver seul : les autres paliers gardent leur silhouette
procédurale en attendant.

## La règle qui compte : l'objet seul, coupé à la flottaison

Un dessin de bateau ne contient **que le bateau**, sur fond transparent,
tranché net à la ligne de flottaison — rien de ce qui est sous l'eau.

C'est le jeu qui dessine la mer, le quai, et surtout **la silhouette humaine
de 1,75 m**, qu'il met à l'échelle exacte à partir des dimensions de l'image :
la largeur du dessin vaut la longueur du bateau. Un générateur d'image ne sait
pas tenir une échelle ; le code, si. C'est pourquoi les dessins ne doivent
jamais contenir de personnage.

Les portraits de capitaine échappent à cette règle : ils s'affichent dans un
carré et gardent leur propre fond.

## Contraintes techniques

Le livrable du jeu est **un fichier HTML unique**. Les dessins y sont recopiés
en base64, pas chargés à côté. Il en découle :

- **PNG de préférence.** JPEG, WebP et SVG sont acceptés, mais seul le PNG
  passe par le détourage automatique.
- **Fond noir uni `#0A0A0B`, ou transparent.** `outils/recadrer.py` retire le
  fond par remplissage depuis les bords — donc les zones sombres *intérieures*
  au bateau, hublots et ouvertures, sont préservées — puis rogne les marges.
  Tout ça à chaque publication : ce n'est pas à toi d'y veiller.
- **Rien d'extérieur dans un SVG** : pas d'image liée, pas de police liée,
  textes vectorisés, pas de `<style>` ni de `<script>`.
- **400 Ko par fichier au maximum.** Le build prévient au-delà de 2 Mo au
  total : à ce stade le jeu devient lourd à ouvrir sur un téléphone.
