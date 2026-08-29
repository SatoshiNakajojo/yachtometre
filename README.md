# Le Yachtomètre

Convertit un stack de Bitcoin en longueur de bateau, du canard en plastique au
superyacht de 180 mètres.

## Pour jouer

**https://satoshinakajojo.github.io/yachtometre/**

Sur iPhone : ouvre l'adresse dans Safari, puis Partager → **Sur l'écran
d'accueil**. Le jeu s'installe comme une application : icône, plein écran, et il
s'ouvre même sans réseau. Le cours du BTC, lui, a besoin d'internet.

Sans internet du tout : `yachtometre.html` s'ouvre d'un double-clic, seul, comme
avant. C'est toujours le même fichier autonome.

## Pour modifier les textes

Depuis le site de GitHub, y compris depuis un téléphone :

1. Ouvre `contenu.json`, clique sur le crayon, modifie ce qui est entre guillemets.
2. Clique sur **Commit changes**.
3. Deux minutes plus tard, l'adresse publique est à jour. Rien d'autre à faire.

En local, si tu préfères : modifie `contenu.json`, lance `python3 build.py`.

Ne modifie jamais `yachtometre.html` ni `index.html` directement : ils sont
regénérés à chaque build et tes changements seraient perdus.

## Les fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | Le jeu, servi à l'adresse publique. Fichier généré, ne pas éditer. |
| `yachtometre.html` | Le même jeu, à garder hors ligne. Fichier généré, ne pas éditer. |
| `contenu.json` | Tous les textes. La source de vérité. |
| `template.html` | Structure, style et logique. |
| `build.py` | Assemble les deux et estampille `sw.js`. |
| `manifest.webmanifest` | Fait du site une application installable. |
| `sw.js` | Garde le jeu ouvrable hors ligne. |
| `icones/` | L'icône de l'application. Régénérable par `outils/icones.py`. |
| `.github/workflows/publier.yml` | Rebuild et publication automatiques. |
| `CLAUDE.md` | Passation complète pour Claude Code. |
| `ROADMAP.md` | Les phases, faites et à faire. |
| `brief-illustrations.md` | La commande à envoyer à un illustrateur. |
| `archive/expo-v0.4/` | Ancien squelette React Native. Périmé, voir CLAUDE.md. |
