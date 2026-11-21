/* =========================================================
   utils.js — petites fonctions utiles partout
   ========================================================= */

// Protège un texte avant de l'insérer dans la page (évite les bugs d'affichage).
function esc(texte) {
  return String(texte == null ? '' : texte)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// Mise en forme légère des textes des fichiers de cours :
//   **gras**   *italique*   retour à la ligne   `code`
function fmt(texte) {
  if (Array.isArray(texte)) texte = texte.join('\n');
  return esc(texte)
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[^*])\*(?!\s)(.+?)\*/g, '$1<em>$2</em>')
    .replace(/`(.+?)`/g, '<code>$1</code>')
    .replace(/\n/g, '<br>');
}

// Transforme "1 234,56" ou "1234.56" ou "1 234,56 €" en nombre. Renvoie NaN si impossible.
function lireNombre(saisie) {
  if (typeof saisie === 'number') return saisie;
  if (saisie == null) return NaN;
  var s = String(saisie).replace(/[\s  €%]/g, '').replace(',', '.');
  if (s === '') return NaN;
  return Number(s);
}

// Affiche un nombre à la française : 1 234,56
function nombreFr(n, decimales) {
  if (n == null || isNaN(n)) return '';
  var d = decimales == null ? (Math.round(n) === n ? 0 : 2) : decimales;
  return Number(n).toLocaleString('fr-FR', { minimumFractionDigits: d, maximumFractionDigits: d });
}

// Note sur 20 avec une décimale : "13,5"
function noteFr(n) {
  if (n == null || isNaN(n)) return '–';
  return nombreFr(Math.round(n * 10) / 10, (Math.round(n * 10) % 10 === 0) ? 0 : 1);
}

function dateFr(ts, avecHeure) {
  var d = new Date(ts);
  var opt = { day: 'numeric', month: 'short', year: 'numeric' };
  if (avecHeure) { opt.hour = '2-digit'; opt.minute = '2-digit'; }
  return d.toLocaleDateString('fr-FR', opt);
}

// Mélange un tableau (copie) — algorithme de Fisher-Yates.
function melanger(tab) {
  var t = tab.slice();
  for (var i = t.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var x = t[i]; t[i] = t[j]; t[j] = x;
  }
  return t;
}

function moyenne(tab) {
  if (!tab.length) return null;
  return tab.reduce(function (a, b) { return a + b; }, 0) / tab.length;
}

// Petit message temporaire en bas de l'écran.
function toast(message) {
  var t = document.createElement('div');
  t.className = 'toast';
  t.textContent = message;
  document.body.appendChild(t);
  setTimeout(function () { t.remove(); }, 2600);
}

// Raccourci : récupère un élément de la page.
function $(selecteur, racine) { return (racine || document).querySelector(selecteur); }
function $$(selecteur, racine) { return Array.prototype.slice.call((racine || document).querySelectorAll(selecteur)); }
