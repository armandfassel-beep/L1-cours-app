/* =========================================================
   exercices.js — le moteur d'exercices
   5 types : qcm, vf, courte, calcul, ecriture
   Chaque type sait : s'afficher, lire ma réponse, la noter (0 à 1)
   et afficher sa correction.
   ========================================================= */

var LIBELLES_TYPES = {
  qcm: 'QCM',
  vf: 'Vrai ou faux',
  courte: 'Réponse courte',
  calcul: 'Calcul',
  ecriture: 'Écriture comptable'
};

// Tableau de données (utilisé dans les énoncés, les fiches et les corrections)
// format : { titre?, entetes: [...], lignes: [[...], ...], nombres?: [indices de colonnes à aligner à droite] }
function tableauHTML(t) {
  if (!t) return '';
  var nb = t.nombres || [];
  var h = '<div class="tableau-defile"><table class="simple">';
  if (t.titre) h += '<caption class="petit muet" style="text-align:left;padding-bottom:6px">' + fmt(t.titre) + '</caption>';
  if (t.entetes) {
    h += '<thead><tr>' + t.entetes.map(function (x, i) {
      return '<th' + (nb.indexOf(i) >= 0 ? ' class="nombre"' : '') + '>' + fmt(x) + '</th>';
    }).join('') + '</tr></thead>';
  }
  h += '<tbody>' + (t.lignes || []).map(function (l) {
    return '<tr>' + l.map(function (x, i) {
      var v = (typeof x === 'number') ? nombreFr(x) : fmt(x);
      return '<td' + (nb.indexOf(i) >= 0 || typeof x === 'number' ? ' class="nombre"' : '') + '>' + v + '</td>';
    }).join('') + '</tr>';
  }).join('') + '</tbody></table></div>';
  return h;
}

/* ---------------------------------------------------------
   Figures (graphiques simples dessinés en SVG)
   format : {
     titre?, xlabel, ylabel, xmax, ymax,
     bissectrice?: true,                       // droite à 45°
     droites: [{ p1:[x,y], p2:[x,y], label, pointille?, couleur? (1..8) }],
     guides:  [{ x, y, lx?, ly? }],            // pointillés vers les axes + étiquettes
     points:  [{ x, y, label }],
     fleches: [{ de:[x,y], a:[x,y] }],
     courbes: [{ points:[[x,y],…], label, couleur?, pointille? }],
     zones:   [{ points:[[x,y],…], couleur?, label? }],   // surfaces colorées
     gradx?: [valeurs], grady?: [valeurs]      // graduations chiffrées
   }
   --------------------------------------------------------- */
function figureHTML(f) {
  if (!f) return '';
  var L = 460, H = 350, mg = { g: 46, d: 56, h: 18, b: 40 };
  var lw = L - mg.g - mg.d, lh = H - mg.h - mg.b;
  var xmax = f.xmax || 100, ymax = f.ymax || 100, xmin = f.xmin || 0, ymin = f.ymin || 0;
  function X(v) { return mg.g + (v - xmin) / (xmax - xmin) * lw; }
  function Y(v) { return mg.h + lh - (v - ymin) / (ymax - ymin) * lh; }
  function txt(x, y, t, anc, cls) { return '<text x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" text-anchor="' + (anc || 'middle') + '" class="' + (cls || '') + '">' + esc(t) + '</text>'; }
  var s = '<svg class="figure" viewBox="0 0 ' + L + ' ' + H + '" role="img" aria-label="' + esc(f.titre || 'Graphique') + '">';
  s += '<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fig-pointe"/></marker></defs>';
  (f.gradx || []).forEach(function (v) { s += '<line class="fig-grille" x1="' + X(v) + '" x2="' + X(v) + '" y1="' + Y(ymin) + '" y2="' + Y(ymax) + '"/>' + txt(X(v), Y(ymin) + 16, nombreFr(v), 'middle', 'fig-grad'); });
  (f.grady || []).forEach(function (v) { s += '<line class="fig-grille" x1="' + X(xmin) + '" x2="' + X(xmax) + '" y1="' + Y(v) + '" y2="' + Y(v) + '"/>' + txt(X(xmin) - 6, Y(v) + 4, nombreFr(v), 'end', 'fig-grad'); });
  s += '<line class="fig-axe" x1="' + X(xmin) + '" y1="' + Y(ymin) + '" x2="' + (X(xmax) + 10) + '" y2="' + Y(ymin) + '" marker-end="url(#fl)"/>';
  s += '<line class="fig-axe" x1="' + X(xmin) + '" y1="' + Y(ymin) + '" x2="' + X(xmin) + '" y2="' + (Y(ymax) - 8) + '" marker-end="url(#fl)"/>';
  s += txt(X(xmax), Y(ymin) + 32, f.xlabel || '', 'end', 'fig-axe-t') + txt(X(xmin) + 6, Y(ymax) - 2, f.ylabel || '', 'start', 'fig-axe-t');
  if (!xmin && !ymin) s += txt(X(0) - 8, Y(0) + 16, '0', 'end', 'fig-grad');
  if (f.bissectrice) {
    var m = Math.min(xmax, ymax);
    s += '<line class="fig-bis" x1="' + X(0) + '" y1="' + Y(0) + '" x2="' + X(m) + '" y2="' + Y(m) + '"/>' + txt(X(m) - 4, Y(m) - 6, '45°', 'end', 'fig-grad');
  }
  (f.guides || []).forEach(function (g) {
    s += '<polyline class="fig-guide" points="' + X(g.x) + ',' + Y(ymin) + ' ' + X(g.x) + ',' + Y(g.y) + ' ' + X(xmin) + ',' + Y(g.y) + '"/>';
    if (g.lx) s += txt(X(g.x), Y(ymin) + 16, g.lx, 'middle', 'fig-lab');
    if (g.ly) s += txt(X(xmin) - 6, Y(g.y) + 4, g.ly, 'end', 'fig-lab');
  });
  // surfaces colorées (surplus, pertes, profit) : polygones
  (f.zones || []).forEach(function (z) {
    var c = 'var(--serie-' + (z.couleur || 1) + ')';
    s += '<polygon class="fig-zone" style="fill:' + c + '" points="' + z.points.map(function (p) { return X(p[0]).toFixed(1) + ',' + Y(p[1]).toFixed(1); }).join(' ') + '"/>';
    if (z.label) {
      var cx = 0, cy = 0;
      z.points.forEach(function (p) { cx += p[0]; cy += p[1]; });
      cx /= z.points.length; cy /= z.points.length;
      s += txt(X(cx), Y(cy) + 4, z.label, 'middle', 'fig-lab fig-zone-t');
    }
  });
  // courbes (lignes brisées : coûts en U, offre/demande en escalier…)
  (f.courbes || []).forEach(function (k) {
    var c = 'var(--serie-' + (k.couleur || 1) + ')';
    s += '<polyline class="fig-droite' + (k.pointille ? ' pointille' : '') + '" style="fill:none;stroke:' + c + '" points="' + k.points.map(function (p) { return X(p[0]).toFixed(1) + ',' + Y(p[1]).toFixed(1); }).join(' ') + '"/>';
    if (k.label) { var d = k.points[k.points.length - 1]; s += txt(X(d[0]) + 6, Y(d[1]) - 6, k.label, 'start', 'fig-lab'); }
  });
  (f.droites || []).forEach(function (d) {
    var c = 'var(--serie-' + (d.couleur || 1) + ')';
    s += '<line class="fig-droite' + (d.pointille ? ' pointille' : '') + '" style="stroke:' + c + '" x1="' + X(d.p1[0]) + '" y1="' + Y(d.p1[1]) + '" x2="' + X(d.p2[0]) + '" y2="' + Y(d.p2[1]) + '"/>';
    if (d.label) s += txt(X(d.p2[0]) + 6, Y(d.p2[1]) - 6, d.label, 'start', 'fig-lab');
  });
  (f.fleches || []).forEach(function (a) {
    s += '<line class="fig-fleche" x1="' + X(a.de[0]) + '" y1="' + Y(a.de[1]) + '" x2="' + X(a.a[0]) + '" y2="' + Y(a.a[1]) + '" marker-end="url(#fl)"/>';
  });
  (f.points || []).forEach(function (p) {
    s += '<circle class="fig-point" cx="' + X(p.x) + '" cy="' + Y(p.y) + '" r="5"/>';
    if (p.label) s += txt(X(p.x) + 8, Y(p.y) - 8, p.label, 'start', 'fig-lab');
  });
  s += '</svg>';
  return '<figure class="figure-boite">' + s + (f.titre ? '<figcaption>' + fmt(f.titre) + '</figcaption>' : '') + '</figure>';
}

function etoiles(niveau) {
  if (!niveau) return '';
  var n = Math.max(1, Math.min(3, niveau));
  return ' · <span class="etoiles" title="Difficulté ' + n + '/3">' + '★'.repeat(n) + '<span style="opacity:.3">' + '★'.repeat(3 - n) + '</span></span>';
}

// Compare deux montants avec une tolérance
function egal(a, b, tol) { return Math.abs((a || 0) - (b || 0)) <= (tol == null ? 0.01 : tol) + 1e-9; }

// Liste des comptes acceptés pour une ligne attendue ("4456" ou ["4456","44566"])
function comptesAcceptes(ligne) {
  var c = ligne.compte;
  return (Array.isArray(c) ? c : [c]).map(function (x) { return String(x).trim(); });
}

/* ---------------------------------------------------------
   Les types d'exercices
   --------------------------------------------------------- */
var TYPES = {

  /* ---------- QCM ---------- */
  qcm: {
    bonnes: function (exo) {
      if (Array.isArray(exo.reponses)) return exo.reponses;
      return [exo.reponse];
    },
    rendu: function (zone, exo, st) {
      var bonnes = this.bonnes(exo);
      st.multiple = bonnes.length > 1 || exo.multiple === true;
      st.ordre = exo.melanger === false ? exo.choix.map(function (_, i) { return i; }) : melanger(exo.choix.map(function (_, i) { return i; }));
      st.sel = new Set();
      zone.innerHTML = (st.multiple ? '<p class="petit muet">Plusieurs réponses possibles.</p>' : '') +
        '<div class="choix' + (st.multiple ? ' multiple' : '') + '">' +
        st.ordre.map(function (i) {
          return '<button type="button" data-i="' + i + '"><span class="case"></span><span>' + fmt(exo.choix[i]) + '</span></button>';
        }).join('') + '</div>';
      $$('.choix button', zone).forEach(function (b) {
        b.addEventListener('click', function () {
          var i = Number(b.dataset.i);
          if (st.multiple) {
            if (st.sel.has(i)) st.sel.delete(i); else st.sel.add(i);
          } else {
            st.sel = new Set([i]);
          }
          $$('.choix button', zone).forEach(function (x) {
            var on = st.sel.has(Number(x.dataset.i));
            x.classList.toggle('selection', on);
            x.querySelector('.case').textContent = on ? '✓' : '';
          });
        });
      });
    },
    lire: function (st) { return st.sel.size ? Array.from(st.sel).sort() : null; },
    noter: function (exo, rep) {
      var bonnes = this.bonnes(exo);
      var nbBonnes = rep.filter(function (i) { return bonnes.indexOf(i) >= 0; }).length;
      var nbFausses = rep.length - nbBonnes;
      if (bonnes.length === 1) return (nbBonnes === 1 && nbFausses === 0) ? 1 : 0;
      return Math.max(0, (nbBonnes - nbFausses) / bonnes.length);
    },
    marquer: function (zone, exo, rep) {
      var bonnes = this.bonnes(exo);
      $$('.choix button', zone).forEach(function (b) {
        var i = Number(b.dataset.i);
        b.disabled = true;
        if (bonnes.indexOf(i) >= 0) b.classList.add('correct');
        else if (rep.indexOf(i) >= 0) b.classList.add('faux');
      });
    },
    correction: function (exo, rep) {
      var bonnes = this.bonnes(exo);
      return '<p><strong>Bonne(s) réponse(s) :</strong></p><ul>' +
        bonnes.map(function (i) { return '<li>' + fmt(exo.choix[i]) + '</li>'; }).join('') + '</ul>' +
        (rep && rep.length ? '<p class="petit"><strong>Ta réponse :</strong> ' + rep.map(function (i) { return fmt(exo.choix[i]); }).join(' ; ') + '</p>' : '');
    }
  },

  /* ---------- Vrai / faux ---------- */
  vf: {
    rendu: function (zone, exo, st) {
      st.val = null;
      zone.innerHTML = '<div class="choix vf">' +
        '<button type="button" data-v="1">Vrai</button><button type="button" data-v="0">Faux</button></div>';
      $$('.choix button', zone).forEach(function (b) {
        b.addEventListener('click', function () {
          st.val = b.dataset.v === '1';
          $$('.choix button', zone).forEach(function (x) { x.classList.toggle('selection', x === b); });
        });
      });
    },
    lire: function (st) { return st.val; },
    noter: function (exo, rep) { return rep === !!exo.reponse ? 1 : 0; },
    marquer: function (zone, exo, rep) {
      $$('.choix button', zone).forEach(function (b) {
        var v = b.dataset.v === '1';
        b.disabled = true;
        if (v === !!exo.reponse) b.classList.add('correct');
        else if (v === rep) b.classList.add('faux');
      });
    },
    correction: function (exo, rep) {
      return '<p><strong>Réponse : ' + (exo.reponse ? 'VRAI' : 'FAUX') + '</strong>' +
        (rep != null ? ' <span class="petit muet">(tu as répondu ' + (rep ? 'vrai' : 'faux') + ')</span>' : '') + '</p>';
    }
  },

  /* ---------- Réponse courte (auto-évaluation) ---------- */
  courte: {
    autoEvaluation: true,
    rendu: function (zone, exo, st) {
      zone.innerHTML = '<textarea class="champ" rows="3" placeholder="Écris ta réponse ici…"></textarea>' +
        '<p class="petit muet" style="margin-top:6px">Tu compareras ensuite avec la réponse attendue.</p>';
      st.champ = $('textarea', zone);
    },
    lire: function (st) { return { texte: st.champ.value.trim() }; },
    marquer: function (zone) { $$('textarea', zone).forEach(function (t) { t.disabled = true; }); },
    correction: function (exo, rep) {
      return '<p><strong>Réponse attendue :</strong></p><div class="encadre">' + fmt(exo.reponse) + '</div>' +
        (rep && rep.texte ? '<p class="petit" style="margin-top:10px"><strong>Ta réponse :</strong> ' + fmt(rep.texte) + '</p>' : '');
    }
  },

  /* ---------- Calcul ---------- */
  calcul: {
    rendu: function (zone, exo, st) {
      zone.innerHTML = '<div class="champ-nombre"><input class="champ" type="text" inputmode="decimal" autocomplete="off" placeholder="Ta réponse">' +
        (exo.unite ? '<span class="unite">' + esc(exo.unite) + '</span>' : '') + '</div>' +
        '<p class="petit muet" style="margin-top:6px">Virgule ou point acceptés' + (exo.tolerance ? ' · tolérance ± ' + nombreFr(exo.tolerance) : '') + '.</p>';
      st.champ = $('input', zone);
    },
    lire: function (st) {
      var v = lireNombre(st.champ.value);
      return isNaN(v) ? null : v;
    },
    noter: function (exo, rep) { return egal(rep, Number(exo.reponse), exo.tolerance == null ? 0.01 : exo.tolerance) ? 1 : 0; },
    marquer: function (zone, exo, rep) {
      var c = $('input', zone);
      c.disabled = true;
      c.classList.add(this.noter(exo, rep) ? 'ok' : 'ko');
    },
    correction: function (exo, rep) {
      return '<p><strong>Résultat attendu : ' + nombreFr(Number(exo.reponse)) + (exo.unite ? ' ' + esc(exo.unite) : '') + '</strong>' +
        (rep != null ? ' <span class="petit muet">(ta réponse : ' + nombreFr(rep) + ')</span>' : '') + '</p>';
    }
  },

  /* ---------- Écriture comptable ---------- */
  ecriture: {
    rendu: function (zone, exo, st, matiere) {
      var comptes = (matiere && matiere.comptes) || {};
      var idListe = 'pcg-' + Math.random().toString(36).slice(2);
      zone.innerHTML =
        '<datalist id="' + idListe + '">' + Object.keys(comptes).map(function (c) {
          return '<option value="' + esc(c) + '">' + esc(comptes[c]) + '</option>';
        }).join('') + '</datalist>' +
        '<div class="tableau-defile"><table class="journal"><thead><tr>' +
        '<th class="c-compte">N° compte</th><th>Intitulé</th><th class="c-montant">Débit</th><th class="c-montant">Crédit</th><th class="c-suppr"></th>' +
        '</tr></thead><tbody></tbody></table></div>' +
        '<div class="totaux"></div>' +
        '<div class="actions" style="margin-top:8px"><button type="button" class="btn petit-btn ajouter">＋ Ajouter une ligne</button></div>';
      var corps = $('tbody', zone);
      var self = this;

      function ajouterLigne() {
        var tr = document.createElement('tr');
        tr.innerHTML =
          '<td><input class="compte" list="' + idListe + '" inputmode="numeric" autocomplete="off" placeholder="607"></td>' +
          '<td><input class="intitule" autocomplete="off" placeholder="Intitulé du compte"></td>' +
          '<td><input class="montant debit" inputmode="decimal" autocomplete="off" placeholder="0,00"></td>' +
          '<td><input class="montant credit" inputmode="decimal" autocomplete="off" placeholder="0,00"></td>' +
          '<td><button type="button" class="suppr" title="Supprimer la ligne" aria-label="Supprimer la ligne">×</button></td>';
        corps.appendChild(tr);
        var c = $('.compte', tr), it = $('.intitule', tr);
        c.addEventListener('input', function () {
          // remplit l'intitulé automatiquement si le compte est connu
          var lib = comptes[c.value.trim()];
          if (lib && (!it.value || it.dataset.auto === '1')) { it.value = lib; it.dataset.auto = '1'; }
        });
        it.addEventListener('input', function () { it.dataset.auto = ''; });
        $$('.montant', tr).forEach(function (m) { m.addEventListener('input', function () { self.totaux(zone); }); });
        $('.suppr', tr).addEventListener('click', function () {
          if ($$('tr', corps).length > 1) tr.remove();
          self.totaux(zone);
        });
        return tr;
      }
      var depart = exo.lignesVides || 2;
      for (var i = 0; i < depart; i++) ajouterLigne();
      $('.ajouter', zone).addEventListener('click', function () { $('.compte', ajouterLigne()).focus(); });
      st.zone = zone;
      this.totaux(zone);
    },

    totaux: function (zone) {
      var d = 0, c = 0;
      $$('tbody tr', zone).forEach(function (tr) {
        d += lireNombre($('.debit', tr).value) || 0;
        c += lireNombre($('.credit', tr).value) || 0;
      });
      var ok = egal(d, c);
      $('.totaux', zone).innerHTML =
        '<span>Total débit : <b>' + nombreFr(d, 2) + '</b></span>' +
        '<span>Total crédit : <b>' + nombreFr(c, 2) + '</b></span>' +
        ((d || c) ? (ok ? '<span class="equilibre">✓ Équilibrée</span>' : '<span class="ecart">Écart : ' + nombreFr(Math.abs(d - c), 2) + '</span>') : '');
    },

    lire: function (st) {
      var lignes = [];
      $$('tbody tr', st.zone).forEach(function (tr) {
        var l = {
          compte: $('.compte', tr).value.trim(),
          intitule: $('.intitule', tr).value.trim(),
          debit: lireNombre($('.debit', tr).value) || 0,
          credit: lireNombre($('.credit', tr).value) || 0
        };
        if (l.compte || l.debit || l.credit) lignes.push(l);
      });
      return lignes.length ? lignes : null;
    },

    // Associe mes lignes aux lignes attendues. Renvoie le détail ligne par ligne.
    comparer: function (exo, rep) {
      var tol = exo.tolerance == null ? 0.01 : exo.tolerance;
      var attendues = exo.lignes;
      var etatAtt = attendues.map(function () { return null; }); // index de ma ligne associée
      var etatRep = rep.map(function () { return 'ko'; });       // ok | montant | ko
      // 1) correspondances exactes (compte + montants)
      attendues.forEach(function (a, i) {
        var cs = comptesAcceptes(a);
        for (var j = 0; j < rep.length; j++) {
          if (etatRep[j] !== 'ko') continue;
          if (cs.indexOf(rep[j].compte) >= 0 && egal(rep[j].debit, a.debit || 0, tol) && egal(rep[j].credit, a.credit || 0, tol)) {
            etatAtt[i] = j; etatRep[j] = 'ok'; break;
          }
        }
      });
      // 2) bon compte mais mauvais montant
      attendues.forEach(function (a, i) {
        if (etatAtt[i] !== null) return;
        var cs = comptesAcceptes(a);
        for (var j = 0; j < rep.length; j++) {
          if (etatRep[j] !== 'ko') continue;
          if (cs.indexOf(rep[j].compte) >= 0) { etatRep[j] = 'montant'; etatAtt[i] = -1; break; }
        }
      });
      var nbOk = etatRep.filter(function (x) { return x === 'ok'; }).length;
      var td = rep.reduce(function (s, l) { return s + l.debit; }, 0);
      var tc = rep.reduce(function (s, l) { return s + l.credit; }, 0);
      return { etatRep: etatRep, nbOk: nbOk, equilibre: egal(td, tc), td: td, tc: tc };
    },

    noter: function (exo, rep) {
      var c = this.comparer(exo, rep);
      var score = c.nbOk / Math.max(exo.lignes.length, rep.length);
      if (!c.equilibre) score = Math.min(score, 0.5); // une écriture déséquilibrée ne peut pas avoir plus de la moitié
      return score;
    },

    marquer: function (zone, exo, rep) {
      var c = this.comparer(exo, rep);
      $('.ajouter', zone).closest('.actions').remove();
      var j = 0;
      $$('tbody tr', zone).forEach(function (tr) {
        $$('input, button', tr).forEach(function (x) { x.disabled = true; });
        var vide = !$('.compte', tr).value.trim() && !lireNombre($('.debit', tr).value) && !lireNombre($('.credit', tr).value);
        if (vide) { tr.style.opacity = .4; return; }
        var e = c.etatRep[j++];
        if (e === 'ok') $$('input', tr).forEach(function (x) { x.classList.add('ok'); });
        else if (e === 'montant') { $('.compte', tr).classList.add('ok'); $$('.montant', tr).forEach(function (x) { if (lireNombre(x.value)) x.classList.add('ko'); }); }
        else $$('input', tr).forEach(function (x) { if (x.value) x.classList.add('ko'); });
      });
    },

    correction: function (exo, rep, matiere) {
      var comptes = (matiere && matiere.comptes) || {};
      var h = '<p><strong>Écriture attendue :</strong></p><div class="tableau-defile"><table class="simple"><thead><tr>' +
        '<th>Compte</th><th>Intitulé</th><th class="nombre">Débit</th><th class="nombre">Crédit</th></tr></thead><tbody>';
      var td = 0, tc = 0;
      exo.lignes.forEach(function (l) {
        var cs = comptesAcceptes(l);
        td += l.debit || 0; tc += l.credit || 0;
        h += '<tr><td><b>' + esc(cs[0]) + '</b>' + (cs.length > 1 ? ' <span class="petit muet">(ou ' + cs.slice(1).map(esc).join(', ') + ')</span>' : '') + '</td>' +
          '<td' + (l.credit && !l.debit ? ' style="padding-left:28px"' : '') + '>' + esc(l.intitule || comptes[cs[0]] || '') + '</td>' +
          '<td class="nombre">' + (l.debit ? nombreFr(l.debit, 2) : '') + '</td>' +
          '<td class="nombre">' + (l.credit ? nombreFr(l.credit, 2) : '') + '</td></tr>';
      });
      h += '<tr><th colspan="2">Totaux</th><th class="nombre">' + nombreFr(td, 2) + '</th><th class="nombre">' + nombreFr(tc, 2) + '</th></tr>';
      h += '</tbody></table></div>';
      if (rep && rep.length) {
        var c = this.comparer(exo, rep);
        h += '<p class="petit"><strong>Tes lignes :</strong> ' + c.nbOk + ' juste(s) sur ' + exo.lignes.length + ' attendue(s)' +
          (rep.length > exo.lignes.length ? ', ' + (rep.length - exo.lignes.length) + ' ligne(s) en trop' : '') +
          (c.equilibre ? '' : ' · ⚠️ ton écriture n’était pas équilibrée (débit ' + nombreFr(c.td, 2) + ' ≠ crédit ' + nombreFr(c.tc, 2) + ')') + '.</p>';
        h += '<div class="tableau-defile"><table class="simple petit"><tbody>' + rep.map(function (l, i) {
          var e = c.etatRep[i];
          var icone = e === 'ok' ? '✅' : (e === 'montant' ? '🟠 montant' : '❌');
          return '<tr><td>' + icone + '</td><td>' + esc(l.compte) + '</td><td>' + esc(l.intitule) + '</td><td class="nombre">' + (l.debit ? nombreFr(l.debit, 2) : '') + '</td><td class="nombre">' + (l.credit ? nombreFr(l.credit, 2) : '') + '</td></tr>';
        }).join('') + '</tbody></table></div>';
      }
      return h;
    }
  }
};

/* ---------------------------------------------------------
   Affichage d'un exercice complet
   opts = {
     mode: 'entrainement' | 'serie',
     matiere: objet matière,
     onResultat(score, reponse)  -> appelé dès que la réponse est notée
     onSuivant()                 -> passer à la question suivante
     dernier: true si c'est la dernière question
   }
   --------------------------------------------------------- */
var Exercices = {

  afficher: function (zone, exo, opts) {
    var type = TYPES[exo.type];
    if (!type) {
      zone.innerHTML = '<p>Type d’exercice inconnu : ' + esc(exo.type) + '</p>';
      return;
    }
    var st = {};
    zone.innerHTML =
      '<div class="enonce-type">' + (exo.figure ? 'Lecture de graphique · ' : '') + LIBELLES_TYPES[exo.type] + etoiles(exo.niveau) +
      (exo.source ? ' <span class="source">' + esc(exo.source) + '</span>' : '') + '</div>' +
      '<div class="question">' + fmt(exo.question) + '</div>' +
      (exo.figure ? figureHTML(exo.figure) : '') +
      (exo.tableau ? '<div style="margin-bottom:16px">' + tableauHTML(exo.tableau) + '</div>' : '') +
      '<div class="zone-reponse"></div>' +
      '<div class="actions zone-boutons"><button type="button" class="btn primaire valider">Valider</button></div>' +
      '<div class="zone-correction"></div>';

    var zr = $('.zone-reponse', zone);
    var zb = $('.zone-boutons', zone);
    var zc = $('.zone-correction', zone);
    type.rendu(zr, exo, st, opts.matiere);

    var self = this;
    function terminer(score, rep) {
      opts.onResultat(score, rep);
      if (opts.mode === 'serie') { opts.onSuivant(); return; }
      type.marquer(zr, exo, rep);
      zc.innerHTML = self.correctionHTML(exo, rep, score, opts.matiere);
      zb.innerHTML = '<button type="button" class="btn primaire suivant">' + (opts.dernier ? 'Voir le bilan' : 'Question suivante →') + '</button>';
      $('.suivant', zb).addEventListener('click', opts.onSuivant);
      zone.appendChild(zb); // le bouton passe sous la correction
      zc.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    $('.valider', zb).addEventListener('click', function () {
      var rep = type.lire(st);
      if (rep == null) { toast('Réponds d’abord à la question 🙂'); return; }
      if (type.autoEvaluation) {
        // Réponse courte : on montre la réponse attendue puis je m'auto-évalue
        type.marquer(zr);
        zb.innerHTML = '';
        zc.innerHTML = '<div class="correction"><div class="verdict">Compare avec la réponse attendue</div>' +
          type.correction(exo, null) +
          '<p style="margin-top:14px"><strong>Comment as-tu répondu ?</strong></p>' +
          '<div class="segment auto-eval"><button type="button" data-s="1">✅ Juste</button><button type="button" data-s="0.5">🟠 À moitié</button><button type="button" data-s="0">❌ Faux</button></div></div>';
        $$('.auto-eval button', zc).forEach(function (b) {
          b.addEventListener('click', function () {
            var s = Number(b.dataset.s);
            rep.auto = s;
            terminer(s, rep);
          });
        });
        return;
      }
      terminer(type.noter(exo, rep), rep);
    });
  },

  // Bloc de correction (utilisé pendant l'entraînement et dans le bilan des séries)
  correctionHTML: function (exo, rep, score, matiere) {
    var type = TYPES[exo.type];
    var classe = score >= 0.999 ? 'ok' : (score <= 0.001 ? 'ko' : 'partiel');
    var verdict = score >= 0.999 ? '✅ Bonne réponse' : (score <= 0.001 ? '❌ Ce n’est pas ça' : '🟠 Partiellement juste (' + Math.round(score * 100) + ' %)');
    return '<div class="correction ' + classe + '"><div class="verdict">' + verdict + '</div>' +
      type.correction(exo, rep, matiere) +
      (exo.explication ? '<div class="explication" style="margin-top:12px"><strong>Explication :</strong><br>' + fmt(exo.explication) + '</div>' : '') +
      '</div>';
  }
};
