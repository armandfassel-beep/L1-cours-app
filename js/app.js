/* =========================================================
   app.js — démarrage et navigation entre les pages
   Les adresses ressemblent à : index.html#/m/comptabilite/n/bilan
   ========================================================= */

function appliquerTheme() {
  var t = Stockage.reglage('theme');
  var racine = document.documentElement;
  if (t === 'clair') racine.dataset.theme = 'light';
  else if (t === 'sombre') racine.dataset.theme = 'dark';
  else delete racine.dataset.theme;
  // couleur de la barre d'état de l'iPad
  var meta = document.querySelector('meta[name="theme-color"]');
  if (meta) meta.content = getComputedStyle(document.body).backgroundColor;
}

function router() {
  var app = document.getElementById('app');
  var brut = location.hash.replace(/^#\/?/, '');
  var morceaux = brut.split('?');
  var chemin = morceaux[0].split('/').filter(Boolean).map(decodeURIComponent);
  var params = {};
  (morceaux[1] || '').split('&').forEach(function (kv) {
    if (!kv) return;
    var p = kv.split('=');
    params[decodeURIComponent(p[0])] = decodeURIComponent(p[1] || '');
  });

  // Quitter une série en cours par la navigation = abandon
  if (chemin[0] !== 'serie' && Series.enCours) Series.enCours = null;

  var rubrique = 'accueil';
  if (!chemin.length) Pages.accueil(app);
  else if (chemin[0] === 'm' && chemin.length === 2) Pages.matiere(app, chemin[1]);
  else if (chemin[0] === 'm' && chemin[2] === 'n' && chemin.length === 4) Pages.notion(app, chemin[1], chemin[3]);
  else if (chemin[0] === 'm' && chemin[2] === 'n' && chemin[4] === 'entrainement') Pages.entrainement(app, chemin[1], chemin[3]);
  else if (chemin[0] === 'series') { rubrique = 'series'; Pages.series(app, params); }
  else if (chemin[0] === 'serie') { rubrique = 'series'; Pages.serieEnCours(app); }
  else if (chemin[0] === 'resultat') { rubrique = 'progression'; Pages.resultat(app, chemin[1]); }
  else if (chemin[0] === 'progression') { rubrique = 'progression'; Pages.progression(app); }
  else if (chemin[0] === 'reglages') { rubrique = 'reglages'; Pages.reglages(app); }
  else Pages.introuvable(app);

  $$('.nav a').forEach(function (a) { a.classList.toggle('actif', a.dataset.nav === rubrique); });
  window.scrollTo(0, 0);
}

// Évite de perdre une série en cours en fermant l'onglet par erreur
window.addEventListener('beforeunload', function (e) {
  if (Series.enCours && Series.enCours.details.length) { e.preventDefault(); e.returnValue = ''; }
});

window.addEventListener('hashchange', router);

appliquerTheme();
Donnees.charger()
  .then(router)
  .catch(function (err) {
    var surFichier = location.protocol === 'file:';
    document.getElementById('app').innerHTML =
      '<div class="carte"><h1>Impossible de charger les matières</h1>' +
      (surFichier
        ? '<p>Tu as ouvert le fichier <code>index.html</code> directement : les navigateurs bloquent alors la lecture du dossier <code>data/</code>.</p>' +
          '<p><strong>Solution :</strong> utilise la version en ligne (GitHub Pages) ou lance un petit serveur local (voir le fichier <code>README.md</code>).</p>'
        : '<p>' + esc(err.message) + '</p>') + '</div>';
  });
