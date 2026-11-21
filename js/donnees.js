/* =========================================================
   donnees.js — chargement des matières (dossier data/)
   - data/matieres.json contient la liste des fichiers à charger
   - chaque matière est un fichier JSON séparé (voir data/LISEZMOI.md)
   ========================================================= */

var Donnees = {
  matieres: [],      // liste des matières chargées
  parId: {},         // matière par identifiant
  erreurs: [],

  charger: function () {
    var self = this;
    return fetch('data/matieres.json', { cache: 'no-cache' })
      .then(function (r) {
        if (!r.ok) throw new Error('data/matieres.json introuvable');
        return r.json();
      })
      .then(function (liste) {
        var fichiers = liste.matieres || [];
        return Promise.all(fichiers.map(function (f) {
          return fetch('data/' + f, { cache: 'no-cache' })
            .then(function (r) { if (!r.ok) throw new Error('fichier introuvable'); return r.json(); })
            .then(function (m) { return self.preparer(m, f); })
            .catch(function (err) { self.erreurs.push(f + ' : ' + err.message); return null; });
        }));
      })
      .then(function (matieres) {
        self.matieres = matieres.filter(Boolean);
        self.matieres.forEach(function (m, i) { m.couleurIndex = (i % 8) + 1; self.parId[m.id] = m; });
      });
  },

  // Ajoute des raccourcis pratiques dans les données (identifiants, liens parent/enfant).
  preparer: function (m, fichier) {
    if (!m.id) m.id = fichier.replace(/\.json$/, '');
    m.parties = m.parties || [];
    m.comptes = m.comptes || {};
    m.notions = [];   // toutes les notions à plat
    m.chapitres = []; // tous les chapitres à plat
    m.notionParId = {};
    m.parties.forEach(function (p, ip) {
      p.id = p.id || ('p' + (ip + 1));
      p.chapitres = p.chapitres || [];
      p.chapitres.forEach(function (c, ic) {
        c.id = c.id || (p.id + '-c' + (ic + 1));
        c.partie = p;
        c.notions = c.notions || [];
        m.chapitres.push(c);
        c.notions.forEach(function (n, inn) {
          n.id = n.id || (c.id + '-n' + (inn + 1));
          n.chapitre = c;
          n.partie = p;
          n.matiere = m;
          n.fiche = n.fiche || {};
          n.exercices = n.exercices || [];
          n.exercices.forEach(function (e, ie) {
            // identifiant unique de l'exercice dans la matière
            e.uid = n.id + '/' + (e.id || (ie + 1));
            e.notion = n;
          });
          m.notions.push(n);
          m.notionParId[n.id] = n;
        });
      });
    });
    return m;
  },

  matiere: function (id) { return this.parId[id]; },

  chapitre: function (mid, cid) {
    var m = this.parId[mid];
    return m && m.chapitres.find(function (c) { return c.id === cid; });
  },

  notion: function (mid, nid) {
    var m = this.parId[mid];
    return m && m.notionParId[nid];
  },

  exercice: function (mid, uid) {
    var m = this.parId[mid];
    if (!m) return null;
    var nid = uid.split('/')[0];
    var n = m.notionParId[nid];
    return n && n.exercices.find(function (e) { return e.uid === uid; });
  },

  // Toutes les notions de toutes les matières
  toutesNotions: function () {
    return this.matieres.reduce(function (acc, m) { return acc.concat(m.notions); }, []);
  }
};
