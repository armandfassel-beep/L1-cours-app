# Révisions L1

Application web personnelle de révision (iPad + ordinateur), en HTML/CSS/JavaScript pur : aucune installation, aucun serveur, aucun compte.

- `index.html` : la page de l'appli
- `css/style.css` : l'apparence (mode clair / sombre)
- `js/` : le code (`exercices.js` = moteur d'exercices, `pages.js` = les pages, `stockage.js` = sauvegarde)
- `data/` : **les matières** (un fichier JSON par matière, listés dans `data/matieres.json`) — voir `data/LISEZMOI.md`

La progression est enregistrée dans le navigateur de l'appareil (localStorage). Réglages → Exporter / Importer pour la sauvegarder ou la transférer.

## Ouvrir l'appli sur l'ordinateur

Ouvrir `index.html` d'un double-clic ne marche pas (le navigateur bloque la lecture du dossier `data/`). Dans un terminal, depuis ce dossier :

```
python3 -m http.server 8000
```

puis ouvrir http://localhost:8000 dans le navigateur.

## En ligne (GitHub Pages)

Settings → Pages → Source : « Deploy from a branch », branche `main`, dossier `/ (root)` → Save. L'adresse sera `https://<pseudo>.github.io/L1-cours-app/`.

## Contenu des matières

`data/comptabilite.json` et `data/macroeconomie.json` sont générés par les scripts du dossier `outils/` (`python3 outils/comptabilite.py`, `python3 outils/macroeconomie.py`), qui vérifient automatiquement les calculs (écritures équilibrées, réponses valides). Les PDF de cours ne sont pas publiés dans le dépôt.
