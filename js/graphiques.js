/* =========================================================
   graphiques.js — courbe d'évolution des notes (SVG fait maison,
   aucune bibliothèque externe). Survol / toucher = infobulle.
   points : [{ t: date, note: 0..20, libelle }]
   ========================================================= */

var Graphiques = {
  courbe: function (conteneur, points, opts) {
    opts = opts || {};
    if (!points.length) {
      conteneur.innerHTML = '<div class="vide">Pas encore de série notée ici.<br>Lance une série pour voir ta courbe apparaître.</div>';
      return;
    }
    var L = 640, H = opts.hauteur || 220;
    var mg = { g: 34, d: 14, h: 14, b: 28 };
    var lw = L - mg.g - mg.d, lh = H - mg.h - mg.b;
    var couleur = opts.couleur || 'var(--serie-1)';
    var n = points.length;
    // Abscisse : rang de la série (régulier, plus lisible que l'échelle de temps)
    function x(i) { return mg.g + (n === 1 ? lw / 2 : i * lw / (n - 1)); }
    function y(v) { return mg.h + lh - (v / 20) * lh; }

    var svg = '<svg class="graph" viewBox="0 0 ' + L + ' ' + H + '" role="img" aria-label="' + esc(opts.titre || 'Évolution des notes') + '">';
    [0, 5, 10, 15, 20].forEach(function (v) {
      svg += '<line class="' + (v === 10 ? 'seuil' : 'grille-l') + '" x1="' + mg.g + '" x2="' + (L - mg.d) + '" y1="' + y(v) + '" y2="' + y(v) + '"/>';
      svg += '<text x="' + (mg.g - 8) + '" y="' + (y(v) + 4) + '" text-anchor="end">' + v + '</text>';
    });
    // dates en bas : première et dernière
    svg += '<text x="' + x(0) + '" y="' + (H - 6) + '" text-anchor="' + (n === 1 ? 'middle' : 'start') + '">' + esc(dateFr(points[0].t)) + '</text>';
    if (n > 1) svg += '<text x="' + x(n - 1) + '" y="' + (H - 6) + '" text-anchor="end">' + esc(dateFr(points[n - 1].t)) + '</text>';

    if (n > 1) {
      svg += '<polyline class="courbe" style="stroke:' + couleur + '" points="' +
        points.map(function (p, i) { return x(i).toFixed(1) + ',' + y(p.note).toFixed(1); }).join(' ') + '"/>';
    }
    points.forEach(function (p, i) {
      svg += '<circle class="point" r="5" cx="' + x(i) + '" cy="' + y(p.note) + '" style="fill:' + couleur + '"/>';
    });
    // dernière valeur étiquetée directement
    var dern = points[n - 1];
    svg += '<text x="' + Math.min(x(n - 1), L - mg.d - 4) + '" y="' + (y(dern.note) - 12) + '" text-anchor="end" style="fill:var(--texte);font-weight:700">' + noteFr(dern.note) + '</text>';
    // zones de survol (plus larges que les points)
    var largeur = n === 1 ? lw : lw / (n - 1);
    points.forEach(function (p, i) {
      svg += '<rect class="cible" data-i="' + i + '" x="' + (x(i) - largeur / 2) + '" y="' + mg.h + '" width="' + largeur + '" height="' + lh + '"/>';
    });
    svg += '</svg>';

    conteneur.innerHTML = '<div class="graph-boite">' + svg + '<div class="infobulle cache"></div></div>';
    var boite = $('.graph-boite', conteneur);
    var bulle = $('.infobulle', conteneur);
    var svgEl = $('svg', conteneur);
    function montrer(i) {
      var p = points[i];
      var r = svgEl.getBoundingClientRect();
      var echelle = r.width / L;
      bulle.innerHTML = '<b>' + noteFr(p.note) + '/20</b> · ' + esc(dateFr(p.t, true)) + (p.libelle ? '<br>' + esc(p.libelle) : '');
      bulle.style.left = (x(i) * echelle) + 'px';
      bulle.style.top = (y(p.note) * echelle) + 'px';
      bulle.classList.remove('cache');
    }
    $$('.cible', conteneur).forEach(function (c) {
      c.addEventListener('mouseenter', function () { montrer(Number(c.dataset.i)); });
      c.addEventListener('click', function () { montrer(Number(c.dataset.i)); });
    });
    boite.addEventListener('mouseleave', function () { bulle.classList.add('cache'); });
  }
};
