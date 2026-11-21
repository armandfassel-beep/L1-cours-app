# Ajouter une matière

1. Crée un fichier `data/ma-matiere.json` (modèle : `demo.json`).
2. Ajoute son nom dans `data/matieres.json` :

```json
{ "matieres": ["comptabilite.json", "ma-matiere.json"] }
```

C'est tout : pas besoin de toucher au code.

## Structure d'un fichier de matière

```
{
  "id": "comptabilite",            // identifiant unique, sans espace
  "nom": "Comptabilité",
  "icone": "📊",
  "description": "…",
  "comptes": { "607": "Achats de marchandises", … },   // facultatif : remplit l'intitulé dans les écritures
  "parties": [
    { "id": "…", "titre": "…", "chapitres": [
      { "id": "…", "titre": "…", "notions": [
        { "id": "…", "titre": "…",
          "fiche": { "definition": "…", "points": ["…"], "exemple": "…", "attention": "…", "tableau": {…} },
          "exercices": [ … ] }
      ]}
    ]}
  ]
}
```

Mise en forme dans les textes : `**gras**`, `*italique*`, `\n` = retour à la ligne.

## Les 5 types d'exercices

Champs communs : `type`, `question`, `niveau` (1 à 3), `explication`, `tableau` (facultatif, données de l'énoncé), `id` (facultatif mais conseillé : ne pas le changer ensuite, sinon l'historique de l'exercice est perdu).

| type | champs propres |
|---|---|
| `qcm` | `choix: [...]`, `reponse: 0` (une bonne réponse) ou `reponses: [0, 2]` (plusieurs) ; `melanger: false` pour garder l'ordre |
| `vf` | `reponse: true` ou `false` |
| `courte` | `reponse: "réponse attendue"` (je m'auto-évalue : juste / à moitié / faux) |
| `calcul` | `reponse: 200`, `unite: "€"`, `tolerance: 0.01` |
| `ecriture` | `lignes: [{ "compte": "607", "intitule": "…", "debit": 1000 }, { "compte": ["44566","4456"], "credit": 200 }]` (plusieurs numéros acceptés possibles) |

Tableau : `{ "titre": "…", "entetes": ["A", "B"], "lignes": [["x", 100], ["y", 200]] }` (les nombres sont alignés à droite et formatés).

## Champs facultatifs (ajoutés avec la Macroéconomie)

- `source` (sur un exercice) : petite étiquette affichée, ex. `"Tiré du TD 2"`, `"Inspiré du TD 4"`, `"D'après le cours"`.
- `figure` (sur un exercice ou dans une fiche) : graphique dessiné par l'appli → l'exercice devient « Lecture de graphique ».

```
"figure": {
  "titre": "…", "xlabel": "Y", "ylabel": "C", "xmin": 0, "xmax": 100, "ymin": 0, "ymax": 100,
  "bissectrice": true,
  "droites": [{ "p1": [0, 30], "p2": [100, 80], "label": "C", "couleur": 1, "pointille": false }],
  "guides":  [{ "x": 60, "y": 60, "lx": "Y1", "ly": "A" }],
  "points":  [{ "x": 60, "y": 60, "label": "E" }],
  "fleches": [{ "de": [40, 70], "a": [55, 70] }],
  "gradx": [50, 100], "grady": [50, 100]
}
```

- `formules` (dans une fiche) : liste de formules affichées dans un encadré.
