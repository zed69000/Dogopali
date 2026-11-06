# Dogopali

**Every dog needs a friend.**

Un jeu 3D tout doux pour les enfants de 5 à 9 ans : on garde des chiots trop mignons, on les câline, on joue à la balle, on leur donne le bain, on les promène en forêt et on les regarde grandir. Ton premier chien est à toi pour toujours ; les autres ont un maître, passent la journée au jardin et reviennent le lendemain.

Un jeu Musclor Duck Games.

- **Jouer (version de test)** : https://games-catalog.sebastienalzamora.workers.dev/test/nourrice-de-chiens/
- **Fiche, GDD et analyse Marché** : dans le catalogue (`zed69000/games-catalog`, id `nourrice-de-chiens`)

## Contenu

| Chemin | Rôle |
|---|---|
| `src/template.html` | Le jeu entier : HTML, CSS et JavaScript (Three.js r128 chargé depuis cdnjs), sons synthétisés en Web Audio |
| `src/photos.json` | Photos des vraies races, intégrées dans la page au moment de la construction |
| `version.txt` | Numéro de version affiché dans le jeu |
| `build.py` | Construit `dist/index.html` et vérifie la syntaxe du JavaScript |
| `dist/index.html` | La page jouable, autonome |

## Construire

```sh
python3 build.py      # demande Node.js pour la vérification de syntaxe
```

Puis ouvrir `dist/index.html` dans un navigateur (il faut Internet pour Three.js et les polices).

## À vérifier avant une sortie en boutique

- La source et la licence des photos de races dans `src/photos.json`.
- Les règles « Familles » de Google Play (public enfant).
