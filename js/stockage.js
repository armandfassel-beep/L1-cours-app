/* =========================================================
   stockage.js — sauvegarde de ma progression sur l'appareil
   Tout est rangé dans localStorage sous la clé "revision-l1".
   Structure :
   {
     version: 1,
     tentatives: [ { t, m, n, e, s, mode } ]   // t=date, m=matière, n=notion, e=exercice, s=score 0..1
     series:     [ { id, t, titre, perimetre, nb, note, details:[{m,n,e,s,rep}] } ]
     reglages:   { theme: "auto" | "clair" | "sombre" }
   }
   ========================================================= */

var CLE_STOCKAGE = 'revision-l1';
var MAX_TENTATIVES = 20000;

var Stockage = (function () {
  var etat = charger();

  function vide() {
    return { version: 1, tentatives: [], series: [], reglages: { theme: 'auto' } };
  }

  function charger() {
    try {
      var brut = localStorage.getItem(CLE_STOCKAGE);
      if (!brut) return vide();
      var e = JSON.parse(brut);
      var base = vide();
      return {
        version: 1,
        tentatives: Array.isArray(e.tentatives) ? e.tentatives : [],
        series: Array.isArray(e.series) ? e.series : [],
        reglages: Object.assign(base.reglages, e.reglages || {})
      };
    } catch (err) {
      console.warn('Lecture impossible de la sauvegarde', err);
      return vide();
    }
  }

  function sauver() {
    try {
      if (etat.tentatives.length > MAX_TENTATIVES) {
        etat.tentatives = etat.tentatives.slice(-MAX_TENTATIVES);
      }
      localStorage.setItem(CLE_STOCKAGE, JSON.stringify(etat));
    } catch (err) {
      console.warn('Sauvegarde impossible', err);
      toast('⚠️ Sauvegarde impossible sur cet appareil (navigation privée ?)');
    }
  }

  return {
    get etat() { return etat; },

    ajouterTentative: function (m, n, e, s, mode) {
      etat.tentatives.push({ t: Date.now(), m: m, n: n, e: e, s: Math.round(s * 1000) / 1000, mode: mode || 'entrainement' });
      sauver();
    },

    ajouterSerie: function (serie) {
      etat.series.push(serie);
      sauver();
    },

    serie: function (id) {
      return etat.series.find(function (s) { return s.id === id; });
    },

    reglage: function (cle, valeur) {
      if (valeur === undefined) return etat.reglages[cle];
      etat.reglages[cle] = valeur;
      sauver();
    },

    // ----- Export / import -----
    exporter: function () {
      var contenu = JSON.stringify(Object.assign({ app: 'revision-l1', exporte_le: new Date().toISOString() }, etat), null, 1);
      var blob = new Blob([contenu], { type: 'application/json' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      var jour = new Date().toISOString().slice(0, 10);
      a.href = url;
      a.download = 'revisions-sauvegarde-' + jour + '.json';
      document.body.appendChild(a);
      a.click();
      setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 1000);
    },

    // mode = "remplacer" ou "fusionner"
    importer: function (texte, mode) {
      var e = JSON.parse(texte);
      if (!e || !Array.isArray(e.tentatives) || !Array.isArray(e.series)) {
        throw new Error("Ce fichier n'est pas une sauvegarde de l'appli.");
      }
      if (mode === 'fusionner') {
        var cles = new Set(etat.tentatives.map(function (x) { return x.t + '|' + x.e; }));
        e.tentatives.forEach(function (x) { if (!cles.has(x.t + '|' + x.e)) etat.tentatives.push(x); });
        var ids = new Set(etat.series.map(function (x) { return x.id; }));
        e.series.forEach(function (x) { if (!ids.has(x.id)) etat.series.push(x); });
        etat.tentatives.sort(function (a, b) { return a.t - b.t; });
        etat.series.sort(function (a, b) { return a.t - b.t; });
      } else {
        etat = { version: 1, tentatives: e.tentatives, series: e.series, reglages: Object.assign({ theme: 'auto' }, e.reglages || {}) };
      }
      sauver();
    },

    toutEffacer: function () {
      var theme = etat.reglages.theme;
      etat = vide();
      etat.reglages.theme = theme;
      sauver();
    }
  };
})();

/* =========================================================
   Calculs de progression (maîtrise, moyennes, points faibles)
   ========================================================= */
var Progression = {
  NB_RECENTS: 10, // nombre de tentatives récentes prises en compte pour la maîtrise

  tentativesNotion: function (mid, nid) {
    return Stockage.etat.tentatives.filter(function (t) { return t.m === mid && t.n === nid; });
  },

  // Renvoie { niveau: 'nonvue'|'arevoir'|'encours'|'maitrisee', score: 0..1|null, nb }
  maitrise: function (mid, nid, nbExercices) {
    var ts = this.tentativesNotion(mid, nid);
    if (!ts.length) return { niveau: 'nonvue', score: null, nb: 0 };
    var recents = ts.slice(-this.NB_RECENTS);
    var score = moyenne(recents.map(function (t) { return t.s; }));
    var preuves = Math.min(5, Math.max(1, nbExercices || 5)); // assez de réponses pour juger
    var niveau;
    if (score >= 0.8 && recents.length >= preuves) niveau = 'maitrisee';
    else if (score >= 0.5) niveau = 'encours';
    else niveau = 'arevoir';
    return { niveau: niveau, score: score, nb: ts.length };
  },

  // Note sur 20 d'une série pour une seule matière (une série "toutes matières" compte pour chacune)
  noteSeriePourMatiere: function (serie, mid) {
    var d = serie.details.filter(function (x) { return x.m === mid; });
    if (!d.length) return null;
    return 20 * moyenne(d.map(function (x) { return x.s; }));
  },

  // Moyenne des 5 dernières séries de la matière
  moyenneRecente: function (mid, nb) {
    var self = this;
    var notes = Stockage.etat.series
      .map(function (s) { return self.noteSeriePourMatiere(s, mid); })
      .filter(function (n) { return n != null; });
    return moyenne(notes.slice(-(nb || 5)));
  },

  // Moyenne générale = moyenne des moyennes récentes de chaque matière
  moyenneGenerale: function (matieres) {
    var self = this;
    var ms = matieres.map(function (m) { return self.moyenneRecente(m.id); }).filter(function (x) { return x != null; });
    return moyenne(ms);
  },

  // Statistiques de maîtrise pour une liste de notions
  bilanNotions: function (mid, notions) {
    var self = this;
    var r = { total: notions.length, maitrisee: 0, encours: 0, arevoir: 0, nonvue: 0 };
    notions.forEach(function (n) { r[self.maitrise(mid, n.id, n.exercices.length).niveau]++; });
    r.pourcent = r.total ? Math.round(100 * r.maitrisee / r.total) : 0;
    return r;
  },

  // Dernier score obtenu sur un exercice précis (ou null)
  dernierScore: function (mid, eid) {
    var ts = Stockage.etat.tentatives;
    for (var i = ts.length - 1; i >= 0; i--) if (ts[i].m === mid && ts[i].e === eid) return ts[i].s;
    return null;
  }
};
