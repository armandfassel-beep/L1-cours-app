"""Outils spécifiques à la matière Macroéconomie (sources, figures, fiches avec formules)."""
from base import *  # noqa: F401,F403
from base import notion, r2

COURS = "D'après le cours"


def td(n, inspire=False):
    return ('Inspiré du TD %d' if inspire else 'Tiré du TD %d') % n


def S(e, source=None, figure=None):
    """Ajoute la source et/ou une figure à un exercice."""
    if source:
        e['source'] = source
    if figure:
        e['figure'] = figure
    return e


def nm(id, titre, definition, points, exercices, formules=None, figure=None, exemple=None, attention=None, tableau=None):
    n = notion(id, titre, definition, points, exercices, exemple=exemple, attention=attention, tableau=tableau)
    if formules:
        n['fiche']['formules'] = formules
    if figure:
        n['fiche']['figure'] = figure
    for e in n['exercices']:
        e.setdefault('source', COURS)
    return n


# ---------- figures ----------
def droite(a, b, x0, x1, label=None, couleur=1, pointille=False):
    """Droite y = a + b x tracée entre x0 et x1."""
    d = {'p1': [x0, r2(a + b * x0)], 'p2': [x1, r2(a + b * x1)], 'couleur': couleur}
    if label:
        d['label'] = label
    if pointille:
        d['pointille'] = True
    return d


def seg(p1, p2, label=None, couleur=1, pointille=False):
    d = {'p1': list(p1), 'p2': list(p2), 'couleur': couleur}
    if label:
        d['label'] = label
    if pointille:
        d['pointille'] = True
    return d


def fig(xlabel, ylabel, xmax, ymax, droites=(), titre=None, bissectrice=False, guides=(), points=(), fleches=(), gradx=None, grady=None, xmin=0, ymin=0, courbes=(), zones=()):
    f = {'xlabel': xlabel, 'ylabel': ylabel, 'xmax': xmax, 'ymax': ymax, 'droites': list(droites)}
    if courbes:
        f['courbes'] = list(courbes)
    if zones:
        f['zones'] = list(zones)
    if xmin:
        f['xmin'] = xmin
    if ymin:
        f['ymin'] = ymin
    if titre:
        f['titre'] = titre
    if bissectrice:
        f['bissectrice'] = True
    if guides:
        f['guides'] = list(guides)
    if points:
        f['points'] = list(points)
    if fleches:
        f['fleches'] = list(fleches)
    if gradx:
        f['gradx'] = gradx
    if grady:
        f['grady'] = grady
    return f


def pt(x, y, label=None):
    p = {'x': x, 'y': y}
    if label:
        p['label'] = label
    return p


def gd(x, y, lx=None, ly=None):
    g = {'x': x, 'y': y}
    if lx:
        g['lx'] = lx
    if ly:
        g['ly'] = ly
    return g


def courbe(points, label=None, couleur=1, pointille=False):
    k = {'points': [[r2(x), r2(y)] for x, y in points], 'couleur': couleur}
    if label:
        k['label'] = label
    if pointille:
        k['pointille'] = True
    return k


def zone(points, couleur=1, label=None):
    z = {'points': [[r2(x), r2(y)] for x, y in points], 'couleur': couleur}
    if label:
        z['label'] = label
    return z


def escalier(paliers, sens='demande'):
    """Courbe en escalier : paliers = [(prix, nombre)] ; demande triée par prix décroissant, offre par prix croissant."""
    pts, q = [], 0
    for p, n in paliers:
        pts.append((q, p))
        q += n
        pts.append((q, p))
    return pts
