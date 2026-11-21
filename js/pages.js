/* =========================================================
   pages.js — chaque fonction dessine une page de l'appli
   ========================================================= */

var NIVEAUX = {
  nonvue: 'Non vue',
  arevoir: 'À revoir',
  encours: 'En cours',
  maitrisee: 'Maîtrisée'
};

function badgeMaitrise(niveau) {
  return '<span class="badge ' + niveau + '">' + NIVEAUX[niveau] + '</span>';
}

function jaugeHTML(b) {
  if (!b.total) return '<div class="jauge"></div>';
  function w(x) { return (100 * x / b.total).toFixed(2) + '%'; }
  return '<div class="jauge" title="' + b.maitrisee + ' maîtrisée(s), ' + b.encours + ' en cours, ' + b.arevoir + ' à revoir, ' + b.nonvue + ' non vue(s)">' +
    (b.maitrisee ? '<span class="j-maitrise" style="width:' + w(b.maitrisee) + '"></span>' : '') +
    (b.encours ? '<span class="j-encours" style="width:' + w(b.encours) + '"></span>' : '') +
    (b.arevoir ? '<span class="j-arevoir" style="width:' + w(b.arevoir) + '"></span>' : '') +
    '</div>';
}

function filAriane(liens) {
  return '<nav class="fil" aria-label="Fil d’Ariane">' + liens.map(function (l, i) {
    return (i ? '<span>›</span>' : '') + (l[1] ? '<a href="' + l[1] + '">' + esc(l[0]) + '</a>' : '<span>' + esc(l[0]) + '</span>');
  }).join('') + '</nav>';
}

function lienNotion(m, n) { return '#/m/' + encodeURIComponent(m.id) + '/n/' + encodeURIComponent(n.id); }

function appreciation(note) {
  if (note >= 16) return 'Excellent ! 🎉';
  if (note >= 14) return 'Très bien 👏';
  if (note >= 12) return 'Bien, continue 💪';
  if (note >= 10) return 'C’est la moyenne, encore un effort';
  if (note >= 7) return 'Il faut retravailler ces notions';
  return 'On reprend les fiches et on s’entraîne 📚';
}

var Pages = {

  /* =================== ACCUEIL =================== */
  accueil: function (app) {
    var ms = Donnees.matieres;
    var mg = Progression.moyenneGenerale(ms);
    var nbSeries = Stockage.etat.series.length;
    var h = '';
    if (Donnees.erreurs.length) {
      h += '<div class="carte encadre attention"><strong>Certains fichiers de matière n’ont pas pu être chargés :</strong><br>' + Donnees.erreurs.map(esc).join('<br>') + '</div>';
    }
    h += '<div class="carte hero"><div><div class="muet petit">Moyenne générale récente</div>' +
      '<div class="valeur">' + noteFr(mg) + '<small> / 20</small></div></div>' +
      '<div class="espace"><p class="muet" style="margin:0">' + (mg == null ? 'Fais ta première série notée pour obtenir une moyenne.' : appreciation(mg) + ' · ' + nbSeries + ' série' + (nbSeries > 1 ? 's' : '') + ' réalisée' + (nbSeries > 1 ? 's' : '')) + '</p></div>' +
      '<div class="ligne"><a class="btn primaire" href="#/series">📝 Nouvelle série</a>' +
      '<a class="btn" href="#/series?type=faibles">🎯 Points faibles</a></div></div>';

    h += '<h1 style="margin-top:28px">Mes matières</h1>';
    if (!ms.length) {
      h += '<div class="carte vide">Aucune matière pour l’instant.<br>Ajoute un fichier dans le dossier <code>data/</code> et inscris-le dans <code>data/matieres.json</code>.</div>';
    } else {
      h += '<div class="grille">' + ms.map(function (m) {
        var b = Progression.bilanNotions(m.id, m.notions);
        var moy = Progression.moyenneRecente(m.id);
        return '<a class="carte carte-matiere" href="#/m/' + encodeURIComponent(m.id) + '" style="border-top:4px solid var(--serie-' + m.couleurIndex + ')">' +
          '<div class="ligne"><div class="pastille">' + esc(m.icone || '📘') + '</div><div><h2 style="margin:0">' + esc(m.nom) + '</h2>' +
          '<div class="petit muet">' + m.notions.length + ' notion' + (m.notions.length > 1 ? 's' : '') + '</div></div></div>' +
          '<div class="stat"><span>Moyenne récente</span><b>' + (moy == null ? '–' : noteFr(moy) + ' / 20') + '</b></div>' +
          '<div class="stat"><span>Notions maîtrisées</span><b>' + b.pourcent + ' %</b></div>' +
          jaugeHTML(b) + '</a>';
      }).join('') + '</div>';
    }
    app.innerHTML = h;
  },

  /* =================== MATIÈRE =================== */
  matiere: function (app, mid) {
    var m = Donnees.matiere(mid);
    if (!m) return Pages.introuvable(app);
    var b = Progression.bilanNotions(m.id, m.notions);
    var moy = Progression.moyenneRecente(m.id);
    var h = filAriane([['Accueil', '#/'], [m.nom]]);
    h += '<div class="carte"><div class="ligne"><div class="pastille" style="width:52px;height:52px;border-radius:14px;display:grid;place-items:center;font-size:1.8rem;background:var(--surface-2)">' + esc(m.icone || '📘') + '</div>' +
      '<div class="espace"><h1 style="margin:0">' + esc(m.nom) + '</h1>' + (m.description ? '<div class="muet">' + fmt(m.description) + '</div>' : '') + '</div>' +
      '<a class="btn primaire" href="#/series?type=matiere&m=' + encodeURIComponent(m.id) + '">📝 Série sur la matière</a></div>' +
      '<div class="stat"><span>Moyenne récente</span><b>' + (moy == null ? '–' : noteFr(moy) + ' / 20') + '</b></div>' +
      '<div class="stat"><span>Notions maîtrisées</span><b>' + b.maitrisee + ' / ' + b.total + ' (' + b.pourcent + ' %)</b></div>' +
      jaugeHTML(b) +
      '<div class="legende">' + ['maitrisee', 'encours', 'arevoir', 'nonvue'].map(function (k) { return badgeMaitrise(k) + '<span class="petit muet" style="margin-right:8px">' + b[k] + '</span>'; }).join('') + '</div></div>';

    if (!m.parties.length) h += '<div class="carte vide">Cette matière ne contient encore aucune notion.</div>';

    m.parties.forEach(function (p) {
      h += '<section class="partie"><h2>' + esc(p.titre) + '</h2>';
      p.chapitres.forEach(function (c) {
        var bc = Progression.bilanNotions(m.id, c.notions);
        var nbEx = c.notions.reduce(function (s, n) { return s + n.exercices.length; }, 0);
        h += '<div class="carte chapitre"><div class="chapitre-tete"><h3>' + esc(c.titre) + '</h3>' +
          '<span class="petit muet">' + bc.maitrisee + '/' + bc.total + ' maîtrisée' + (bc.maitrisee > 1 ? 's' : '') + '</span>' +
          (nbEx ? '<a class="btn petit-btn" href="#/series?type=chapitre&m=' + encodeURIComponent(m.id) + '&c=' + encodeURIComponent(c.id) + '">📝 Série</a>' : '') +
          '</div>';
        c.notions.forEach(function (n) {
          var mt = Progression.maitrise(m.id, n.id, n.exercices.length);
          h += '<a class="notion-lien" href="' + lienNotion(m, n) + '"><span class="titre">' + esc(n.titre) + '</span>' +
            '<span class="petit muet">' + n.exercices.length + ' exo' + (n.exercices.length > 1 ? 's' : '') + '</span>' +
            badgeMaitrise(mt.niveau) + '<span class="fleche">›</span></a>';
        });
        h += '</div>';
      });
      h += '</section>';
    });
    app.innerHTML = h;
  },

  /* =================== NOTION (fiche) =================== */
  notion: function (app, mid, nid) {
    var m = Donnees.matiere(mid);
    var n = Donnees.notion(mid, nid);
    if (!m || !n) return Pages.introuvable(app);
    var f = n.fiche;
    var mt = Progression.maitrise(m.id, n.id, n.exercices.length);
    var i = m.notions.indexOf(n);
    var prec = m.notions[i - 1], suiv = m.notions[i + 1];

    var h = filAriane([['Accueil', '#/'], [m.nom, '#/m/' + encodeURIComponent(m.id)], [n.chapitre.titre]]);
    h += '<div class="ligne" style="margin-bottom:12px"><h1 style="margin:0" class="espace">' + esc(n.titre) + '</h1>' + badgeMaitrise(mt.niveau) + '</div>';
    if (mt.score != null) h += '<p class="petit muet">Réussite récente : ' + Math.round(mt.score * 100) + ' % sur ' + mt.nb + ' réponse' + (mt.nb > 1 ? 's' : '') + '.</p>';

    h += '<article class="carte fiche">';
    if (f.definition) h += '<h2>Définition</h2><div class="encadre">' + fmt(f.definition) + '</div>';
    if (f.points && f.points.length) h += '<h2>Points clés</h2><ul>' + f.points.map(function (p) { return '<li>' + fmt(p) + '</li>'; }).join('') + '</ul>';
    if (f.tableau) h += '<h2>' + esc(f.tableau.nom || 'Tableau') + '</h2>' + tableauHTML(f.tableau);
    if (f.figure) h += '<h2>Graphique</h2>' + figureHTML(f.figure);
    if (f.formules && f.formules.length) h += '<h2>Formules</h2><ul class="formules">' + f.formules.map(function (x) { return '<li>' + fmt(x) + '</li>'; }).join('') + '</ul>';
    if (f.exemple) h += '<h2>Exemple</h2><div class="encadre exemple">' + fmt(f.exemple) + '</div>';
    if (f.attention) h += '<h2>Attention</h2><div class="encadre attention">' + fmt(f.attention) + '</div>';
    if (!f.definition && !f.points && !f.exemple) h += '<p class="muet">Pas encore de fiche pour cette notion.</p>';
    h += '</article>';

    h += '<div class="actions">' +
      (n.exercices.length
        ? '<a class="btn primaire large" href="' + lienNotion(m, n) + '/entrainement">🏋️ S’entraîner (' + n.exercices.length + ' exercice' + (n.exercices.length > 1 ? 's' : '') + ')</a>'
        : '<p class="muet">Aucun exercice pour cette notion pour l’instant.</p>') + '</div>';
    h += '<div class="actions">' +
      (prec ? '<a class="btn" href="' + lienNotion(m, prec) + '">← ' + esc(prec.titre) + '</a>' : '') +
      '<span class="espace"></span>' +
      (suiv ? '<a class="btn" href="' + lienNotion(m, suiv) + '">' + esc(suiv.titre) + ' →</a>' : '') + '</div>';
    app.innerHTML = h;
  },

  /* =================== ENTRAÎNEMENT sur une notion =================== */
  entrainement: function (app, mid, nid, liste) {
    var m = Donnees.matiere(mid);
    var n = Donnees.notion(mid, nid);
    if (!m || !n) return Pages.introuvable(app);
    var exos = liste || n.exercices.slice(); // ordre du fichier = difficulté progressive
    var i = 0;
    var resultats = [];

    function etape() {
      if (i >= exos.length) return bilan();
      var e = exos[i];
      app.innerHTML = filAriane([['Accueil', '#/'], [m.nom, '#/m/' + encodeURIComponent(m.id)], [n.titre, lienNotion(m, n)], ['Entraînement']]) +
        '<div class="ligne"><h1 class="espace" style="margin:0">' + esc(n.titre) + '</h1><span class="muet">Exercice ' + (i + 1) + ' / ' + exos.length + '</span></div>' +
        '<div class="progres"><span style="width:' + (100 * i / exos.length) + '%"></span></div>' +
        '<div class="carte zone-exo"></div>' +
        '<div class="actions"><a class="btn" href="' + lienNotion(m, n) + '">📄 Revoir la fiche</a></div>';
      Exercices.afficher($('.zone-exo', app), e, {
        mode: 'entrainement',
        matiere: m,
        dernier: i === exos.length - 1,
        onResultat: function (score, rep) {
          resultats.push({ exo: e, s: score });
          Stockage.ajouterTentative(m.id, n.id, e.uid, score, 'entrainement');
        },
        onSuivant: function () { i++; window.scrollTo(0, 0); etape(); }
      });
    }

    function bilan() {
      var total = resultats.reduce(function (s, r) { return s + r.s; }, 0);
      var rates = resultats.filter(function (r) { return r.s < 0.999; }).map(function (r) { return r.exo; });
      var mt = Progression.maitrise(m.id, n.id, n.exercices.length);
      app.innerHTML = filAriane([['Accueil', '#/'], [m.nom, '#/m/' + encodeURIComponent(m.id)], [n.titre, lienNotion(m, n)], ['Bilan']]) +
        '<div class="carte centre"><h1>Bilan de l’entraînement</h1>' +
        '<div class="note-finale">' + nombreFr(Math.round(total * 10) / 10) + '<small> / ' + exos.length + '</small></div>' +
        '<p class="muet" style="margin-top:10px">Niveau de maîtrise de la notion : ' + badgeMaitrise(mt.niveau) + '</p>' +
        '<div class="actions" style="justify-content:center">' +
        (rates.length ? '<button class="btn primaire refaire-erreurs">🔁 Refaire mes ' + rates.length + ' erreur' + (rates.length > 1 ? 's' : '') + '</button>' : '') +
        '<button class="btn recommencer">Tout recommencer</button>' +
        '<a class="btn" href="' + lienNotion(m, n) + '">📄 Retour à la fiche</a>' +
        '<a class="btn" href="#/m/' + encodeURIComponent(m.id) + '">Retour à la matière</a></div></div>';
      var be = $('.refaire-erreurs', app);
      if (be) be.addEventListener('click', function () { Pages.entrainement(app, mid, nid, rates); });
      $('.recommencer', app).addEventListener('click', function () { Pages.entrainement(app, mid, nid); });
    }

    if (!exos.length) { app.innerHTML = '<div class="carte vide">Aucun exercice pour cette notion.</div>'; return; }
    etape();
  },

  /* =================== CHOIX D'UNE SÉRIE NOTÉE =================== */
  series: function (app, params) {
    var ms = Donnees.matieres;
    var choix = {
      type: params.type || (params.c ? 'chapitre' : (params.m ? 'matiere' : 'matiere')),
      m: params.m || (ms[0] && ms[0].id),
      c: params.c || '',
      nb: Number(params.nb) || 10
    };
    if (choix.type === 'chapitre' && !choix.c) {
      var m0 = Donnees.matiere(choix.m);
      choix.c = m0 && m0.chapitres[0] ? m0.chapitres[0].id : '';
    }

    function dessiner() {
      var m = Donnees.matiere(choix.m);
      var h = filAriane([['Accueil', '#/'], ['Séries notées']]) + '<h1>Nouvelle série notée</h1>';
      h += '<div class="carte"><label class="etiquette">Périmètre</label><div class="segment type">' +
        [['chapitre', '📖 Un chapitre'], ['matiere', '📘 Une matière'], ['toutes', '📚 Toutes les matières'], ['faibles', '🎯 Points faibles']]
          .map(function (t) { return '<button type="button" data-v="' + t[0] + '" class="' + (choix.type === t[0] ? 'actif' : '') + '">' + t[1] + '</button>'; }).join('') + '</div>';

      if (choix.type === 'chapitre' || choix.type === 'matiere') {
        h += '<label class="etiquette" for="sel-m">Matière</label><select id="sel-m" class="champ">' +
          ms.map(function (x) { return '<option value="' + esc(x.id) + '"' + (x.id === choix.m ? ' selected' : '') + '>' + esc(x.nom) + '</option>'; }).join('') + '</select>';
      }
      if (choix.type === 'chapitre' && m) {
        h += '<label class="etiquette" for="sel-c">Chapitre</label><select id="sel-c" class="champ">' +
          m.parties.map(function (p) {
            return '<optgroup label="' + esc(p.titre) + '">' + p.chapitres.map(function (c) {
              return '<option value="' + esc(c.id) + '"' + (c.id === choix.c ? ' selected' : '') + '>' + esc(c.titre) + '</option>';
            }).join('') + '</optgroup>';
          }).join('') + '</select>';
      }
      if (choix.type === 'faibles') {
        h += '<p class="muet" style="margin-top:14px">La série cible automatiquement les notions où tu te trompes le plus (toutes matières), en priorité les exercices que tu as ratés.</p>';
      }
      h += '<label class="etiquette">Nombre de questions</label><div class="segment nb">' +
        [10, 15, 20].map(function (x) { return '<button type="button" data-v="' + x + '" class="' + (choix.nb === x ? 'actif' : '') + '">' + x + ' questions</button>'; }).join('') + '</div>';

      var pool = Series.pool(choix);
      h += '<p class="petit muet" style="margin-top:16px">' + (pool.length
        ? pool.length + ' exercice' + (pool.length > 1 ? 's' : '') + ' disponible' + (pool.length > 1 ? 's' : '') + ' dans ce périmètre' + (pool.length < choix.nb ? ' (la série en comptera ' + pool.length + ')' : '') + '.'
        : (choix.type === 'faibles' ? 'Pas encore assez de résultats pour repérer tes points faibles : entraîne-toi d’abord sur quelques notions.' : 'Aucun exercice dans ce périmètre pour l’instant.')) + '</p>';
      h += '<div class="actions"><button class="btn primaire large lancer"' + (pool.length ? '' : ' disabled') + '>▶️ Commencer la série</button></div></div>';

      app.innerHTML = h;
      $$('.segment.type button', app).forEach(function (b) { b.addEventListener('click', function () { choix.type = b.dataset.v; if (choix.type === 'chapitre') { var mm = Donnees.matiere(choix.m); if (mm && !mm.chapitres.some(function (c) { return c.id === choix.c; })) choix.c = mm.chapitres[0] ? mm.chapitres[0].id : ''; } dessiner(); }); });
      $$('.segment.nb button', app).forEach(function (b) { b.addEventListener('click', function () { choix.nb = Number(b.dataset.v); dessiner(); }); });
      var sm = $('#sel-m', app);
      if (sm) sm.addEventListener('change', function () {
        choix.m = sm.value;
        var mm = Donnees.matiere(choix.m);
        choix.c = mm && mm.chapitres[0] ? mm.chapitres[0].id : '';
        dessiner();
      });
      var sc = $('#sel-c', app);
      if (sc) sc.addEventListener('change', function () { choix.c = sc.value; dessiner(); });
      $('.lancer', app).addEventListener('click', function () { Series.demarrer(choix); });
    }
    dessiner();
  },

  /* =================== SÉRIE EN COURS =================== */
  serieEnCours: function (app) {
    var s = Series.enCours;
    if (!s) { location.hash = '#/series'; return; }
    function etape() {
      if (s.i >= s.questions.length) return Series.terminer();
      var q = s.questions[s.i];
      var m = Donnees.matiere(q.m);
      var e = Donnees.exercice(q.m, q.e);
      app.innerHTML = '<div class="ligne"><h1 class="espace" style="margin:0">' + esc(s.titre) + '</h1>' +
        '<span class="muet">Question ' + (s.i + 1) + ' / ' + s.questions.length + '</span></div>' +
        '<div class="progres"><span style="width:' + (100 * s.i / s.questions.length) + '%"></span></div>' +
        '<p class="petit muet">' + esc(m.nom) + ' › ' + esc(e.notion.titre) + '</p>' +
        '<div class="carte zone-exo"></div>' +
        '<div class="actions"><button class="btn danger abandon">Abandonner la série</button></div>';
      Exercices.afficher($('.zone-exo', app), e, {
        mode: 'serie',
        matiere: m,
        onResultat: function (score, rep) {
          s.details.push({ m: q.m, n: e.notion.id, e: q.e, s: Math.round(score * 1000) / 1000, rep: rep });
          Stockage.ajouterTentative(q.m, e.notion.id, q.e, score, 'serie');
        },
        onSuivant: function () { s.i++; window.scrollTo(0, 0); etape(); }
      });
      $('.abandon', app).addEventListener('click', function () {
        if (confirm('Abandonner la série ? Elle ne sera pas notée (les réponses déjà données comptent quand même pour la maîtrise des notions).')) {
          Series.enCours = null;
          location.hash = '#/series';
        }
      });
    }
    etape();
  },

  /* =================== RÉSULTAT D'UNE SÉRIE =================== */
  resultat: function (app, id) {
    var s = Stockage.serie(id);
    if (!s) return Pages.introuvable(app);
    var erreurs = s.details.filter(function (d) { return d.s < 0.999; });
    var bonnes = s.details.length - erreurs.length;

    // notions à retravailler : celles où j'ai perdu des points, triées par points perdus
    var parNotion = {};
    erreurs.forEach(function (d) {
      var k = d.m + '|' + d.n;
      parNotion[k] = parNotion[k] || { m: d.m, n: d.n, perdu: 0, nb: 0 };
      parNotion[k].perdu += 1 - d.s; parNotion[k].nb++;
    });
    var aRetravailler = Object.keys(parNotion).map(function (k) { return parNotion[k]; }).sort(function (a, b) { return b.perdu - a.perdu; });

    var h = filAriane([['Accueil', '#/'], ['Progression', '#/progression'], ['Résultat']]);
    h += '<div class="carte centre"><div class="muet">' + esc(s.titre) + ' · ' + esc(dateFr(s.t, true)) + '</div>' +
      '<div class="note-finale" style="margin:14px 0">' + noteFr(s.note) + '<small> / 20</small></div>' +
      '<p><strong>' + appreciation(s.note) + '</strong></p>' +
      '<p class="muet">' + bonnes + ' réponse' + (bonnes > 1 ? 's' : '') + ' entièrement juste' + (bonnes > 1 ? 's' : '') + ' sur ' + s.details.length + '</p>' +
      '<div class="actions" style="justify-content:center"><button class="btn primaire refaire">🔁 Nouvelle série (même périmètre)</button><a class="btn" href="#/">Accueil</a></div></div>';

    if (aRetravailler.length) {
      h += '<h2 style="margin-top:28px">Notions à retravailler</h2><div class="carte chapitre">' + aRetravailler.map(function (x) {
        var m = Donnees.matiere(x.m), n = Donnees.notion(x.m, x.n);
        if (!m || !n) return '';
        return '<a class="notion-lien" href="' + lienNotion(m, n) + '"><span class="titre">' + esc(n.titre) + '<br><span class="petit muet">' + esc(m.nom) + ' · ' + esc(n.chapitre.titre) + '</span></span>' +
          '<span class="petit muet">' + x.nb + ' erreur' + (x.nb > 1 ? 's' : '') + '</span><span class="fleche">›</span></a>';
      }).join('') + '</div>';
    }

    if (erreurs.length) {
      h += '<h2 style="margin-top:28px">Mes erreurs et leurs corrections</h2>';
      erreurs.forEach(function (d) {
        var m = Donnees.matiere(d.m), e = Donnees.exercice(d.m, d.e);
        if (!e) { h += '<div class="carte muet">Exercice supprimé depuis.</div>'; return; }
        h += '<div class="carte erreur"><div class="enonce-type">' + esc(e.notion.titre) + ' · ' + LIBELLES_TYPES[e.type] + '</div>' +
          '<div class="question">' + fmt(e.question) + '</div>' +
          (e.figure ? figureHTML(e.figure) : '') +
          (e.tableau ? tableauHTML(e.tableau) : '') +
          Exercices.correctionHTML(e, d.rep, d.s, m) + '</div>';
      });
    } else {
      h += '<div class="carte centre" style="margin-top:20px">🎉 Aucune erreur, bravo !</div>';
    }
    app.innerHTML = h;
    $('.refaire', app).addEventListener('click', function () { Series.demarrer(Object.assign({}, s.perimetre, { nb: s.nb })); });
  },

  /* =================== PROGRESSION =================== */
  progression: function (app) {
    var series = Stockage.etat.series;
    var h = filAriane([['Accueil', '#/'], ['Progression']]) + '<h1>Ma progression</h1>';
    h += '<div class="carte"><h2>Toutes matières</h2><p class="petit muet">Note sur 20 de chaque série, dans l’ordre chronologique. Pointillés = 10/20.</p><div id="g-general"></div></div>';
    Donnees.matieres.forEach(function (m) {
      h += '<div class="carte"><h2><span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:var(--serie-' + m.couleurIndex + ');margin-right:8px"></span>' + esc(m.nom) + '</h2>' +
        '<p class="petit muet">Moyenne récente : ' + noteFr(Progression.moyenneRecente(m.id)) + ' / 20 · ' + Progression.bilanNotions(m.id, m.notions).pourcent + ' % des notions maîtrisées</p>' +
        '<div id="g-' + esc(m.id) + '"></div></div>';
    });

    h += '<h2 style="margin-top:28px">Historique des séries</h2>';
    if (!series.length) {
      h += '<div class="carte vide">Aucune série pour l’instant.</div>';
    } else {
      h += '<div class="carte"><div class="tableau-defile"><table class="simple"><thead><tr><th>Date</th><th>Série</th><th class="nombre">Questions</th><th class="nombre">Note</th><th></th></tr></thead><tbody>' +
        series.slice().reverse().map(function (s) {
          return '<tr><td>' + esc(dateFr(s.t, true)) + '</td><td>' + esc(s.titre) + '</td><td class="nombre">' + s.details.length + '</td>' +
            '<td class="nombre"><b>' + noteFr(s.note) + '</b></td><td><a href="#/resultat/' + encodeURIComponent(s.id) + '">Détail</a></td></tr>';
        }).join('') + '</tbody></table></div></div>';
    }
    app.innerHTML = h;

    Graphiques.courbe($('#g-general', app), series.map(function (s) { return { t: s.t, note: s.note, libelle: s.titre }; }), { couleur: 'var(--accent)', titre: 'Notes toutes matières' });
    Donnees.matieres.forEach(function (m) {
      var pts = series.map(function (s) {
        var note = Progression.noteSeriePourMatiere(s, m.id);
        return note == null ? null : { t: s.t, note: note, libelle: s.titre };
      }).filter(Boolean);
      Graphiques.courbe(document.getElementById('g-' + m.id), pts, { couleur: 'var(--serie-' + m.couleurIndex + ')', titre: 'Notes en ' + m.nom });
    });
  },

  /* =================== RÉGLAGES =================== */
  reglages: function (app) {
    var theme = Stockage.reglage('theme') || 'auto';
    var et = Stockage.etat;
    app.innerHTML = filAriane([['Accueil', '#/'], ['Réglages']]) + '<h1>Réglages</h1>' +
      '<div class="carte"><h2>Apparence</h2><div class="segment theme">' +
      [['auto', '🌗 Automatique'], ['clair', '☀️ Clair'], ['sombre', '🌙 Sombre']].map(function (t) {
        return '<button type="button" data-v="' + t[0] + '" class="' + (theme === t[0] ? 'actif' : '') + '">' + t[1] + '</button>';
      }).join('') + '</div><p class="petit muet" style="margin-top:10px">« Automatique » suit le réglage de ton iPad ou de ton ordinateur.</p></div>' +

      '<div class="carte"><h2>Ma sauvegarde</h2>' +
      '<p>Ta progression est enregistrée automatiquement <strong>sur cet appareil uniquement</strong> (' + et.tentatives.length + ' réponses, ' + et.series.length + ' séries).</p>' +
      '<p class="petit muet">Pour passer de l’ordinateur à l’iPad (ou par sécurité), exporte un fichier de sauvegarde puis importe-le sur l’autre appareil.</p>' +
      '<div class="actions"><button class="btn primaire exporter">⬇️ Exporter ma progression</button>' +
      '<label class="btn" for="fichier-import">⬆️ Importer une sauvegarde</label>' +
      '<input id="fichier-import" type="file" accept=".json,application/json" class="cache"></div>' +
      '<label class="etiquette">À l’import :</label><div class="segment mode-import">' +
      '<button type="button" data-v="fusionner" class="actif">Fusionner avec l’actuelle</button><button type="button" data-v="remplacer">Remplacer l’actuelle</button></div></div>' +

      '<div class="carte"><h2>Zone dangereuse</h2><p class="petit muet">Efface toutes tes réponses et séries sur cet appareil. Pense à exporter avant.</p>' +
      '<button class="btn danger effacer">🗑️ Tout effacer</button></div>' +

      '<p class="petit muet centre">Matières chargées : ' + Donnees.matieres.map(function (m) { return esc(m.nom); }).join(', ') + '</p>';

    $$('.segment.theme button', app).forEach(function (b) {
      b.addEventListener('click', function () {
        Stockage.reglage('theme', b.dataset.v);
        appliquerTheme();
        Pages.reglages(app);
      });
    });
    var modeImport = 'fusionner';
    $$('.segment.mode-import button', app).forEach(function (b) {
      b.addEventListener('click', function () {
        modeImport = b.dataset.v;
        $$('.segment.mode-import button', app).forEach(function (x) { x.classList.toggle('actif', x === b); });
      });
    });
    $('.exporter', app).addEventListener('click', function () { Stockage.exporter(); });
    $('#fichier-import', app).addEventListener('change', function (ev) {
      var f = ev.target.files[0];
      if (!f) return;
      if (modeImport === 'remplacer' && !confirm('Remplacer toute ta progression actuelle par ce fichier ?')) return;
      var lecteur = new FileReader();
      lecteur.onload = function () {
        try {
          Stockage.importer(lecteur.result, modeImport);
          appliquerTheme();
          toast('✅ Sauvegarde importée');
          Pages.reglages(app);
        } catch (err) {
          alert('Import impossible : ' + err.message);
        }
      };
      lecteur.readAsText(f);
    });
    $('.effacer', app).addEventListener('click', function () {
      if (confirm('Effacer définitivement toute ta progression sur cet appareil ?')) {
        Stockage.toutEffacer();
        toast('Progression effacée');
        Pages.reglages(app);
      }
    });
  },

  introuvable: function (app) {
    app.innerHTML = '<div class="carte vide"><h2>Page introuvable</h2><p>Cette page n’existe pas (ou plus).</p><a class="btn primaire" href="#/">Retour à l’accueil</a></div>';
  }
};

/* =========================================================
   Séries notées : choix des questions, déroulé, note finale
   ========================================================= */
var Series = {
  enCours: null,

  // Liste des exercices disponibles pour un périmètre
  pool: function (choix) {
    var liste = [];
    function ajouter(m, notions) {
      notions.forEach(function (n) { n.exercices.forEach(function (e) { liste.push({ m: m.id, e: e.uid, n: n.id }); }); });
    }
    if (choix.type === 'chapitre') {
      var c = Donnees.chapitre(choix.m, choix.c);
      if (c) ajouter(Donnees.matiere(choix.m), c.notions);
    } else if (choix.type === 'matiere') {
      var m = Donnees.matiere(choix.m);
      if (m) ajouter(m, m.notions);
    } else if (choix.type === 'toutes') {
      Donnees.matieres.forEach(function (m) { ajouter(m, m.notions); });
    } else if (choix.type === 'faibles') {
      liste = this.poolFaibles(choix.nb || 10);
    }
    return liste;
  },

  // Notions les plus ratées d'abord ; dans chacune, les exercices ratés d'abord
  poolFaibles: function (nb) {
    var notions = [];
    Donnees.matieres.forEach(function (m) {
      m.notions.forEach(function (n) {
        if (!n.exercices.length) return;
        var mt = Progression.maitrise(m.id, n.id, n.exercices.length);
        if (mt.score == null) return;
        notions.push({ m: m, n: n, score: mt.score });
      });
    });
    notions.sort(function (a, b) { return a.score - b.score; });
    var faibles = notions.filter(function (x) { return x.score < 0.8; });
    if (faibles.length < 3) faibles = notions.slice(0, Math.max(3, faibles.length)); // complète avec les moins bonnes
    var liste = [];
    faibles.forEach(function (x) {
      var exos = melanger(x.n.exercices).sort(function (a, b) {
        var sa = Progression.dernierScore(x.m.id, a.uid), sb = Progression.dernierScore(x.m.id, b.uid);
        var pa = sa == null ? 0.5 : sa, pb = sb == null ? 0.5 : sb; // raté (0) avant jamais fait (0.5) avant réussi (1)
        return pa - pb;
      });
      exos.forEach(function (e, rang) { liste.push({ m: x.m.id, e: e.uid, n: x.n.id, rang: rang, poids: x.score }); });
    });
    // tour par tour : 1er exercice de chaque notion faible, puis le 2e, etc.
    liste.sort(function (a, b) { return a.rang - b.rang || a.poids - b.poids; });
    return liste;
  },

  // Tire nb questions en répartissant entre les notions
  tirer: function (pool, nb, garderOrdre) {
    if (garderOrdre) return pool.slice(0, nb);
    var parNotion = {};
    pool.forEach(function (q) { var k = q.m + '|' + q.n; (parNotion[k] = parNotion[k] || []).push(q); });
    var groupes = melanger(Object.keys(parNotion)).map(function (k) { return melanger(parNotion[k]); });
    var res = [];
    while (res.length < nb && groupes.some(function (g) { return g.length; })) {
      groupes.forEach(function (g) { if (g.length && res.length < nb) res.push(g.shift()); });
    }
    return melanger(res);
  },

  titre: function (choix) {
    if (choix.type === 'chapitre') { var c = Donnees.chapitre(choix.m, choix.c); return 'Chapitre : ' + (c ? c.titre : '?'); }
    if (choix.type === 'matiere') { var m = Donnees.matiere(choix.m); return 'Matière : ' + (m ? m.nom : '?'); }
    if (choix.type === 'toutes') return 'Toutes les matières';
    return 'Points faibles';
  },

  demarrer: function (choix) {
    var pool = this.pool(choix);
    if (!pool.length) { toast('Aucun exercice disponible'); return; }
    var questions = this.tirer(pool, choix.nb || 10, choix.type === 'faibles');
    if (choix.type === 'faibles') questions = melanger(questions);
    this.enCours = {
      id: 's' + Date.now().toString(36),
      titre: this.titre(choix),
      perimetre: { type: choix.type, m: choix.m, c: choix.c },
      nb: choix.nb || 10,
      questions: questions.map(function (q) { return { m: q.m, e: q.e }; }),
      i: 0,
      details: []
    };
    if (location.hash === '#/serie') Pages.serieEnCours(document.getElementById('app'));
    else location.hash = '#/serie';
  },

  terminer: function () {
    var s = this.enCours;
    var note = 20 * moyenne(s.details.map(function (d) { return d.s; }));
    var serie = {
      id: s.id, t: Date.now(), titre: s.titre, perimetre: s.perimetre, nb: s.nb,
      note: Math.round(note * 100) / 100, details: s.details
    };
    Stockage.ajouterSerie(serie);
    this.enCours = null;
    location.hash = '#/resultat/' + encodeURIComponent(serie.id);
  }
};
