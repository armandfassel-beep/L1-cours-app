"""Outils pour fabriquer les fichiers de matière (data/*.json).

Ces scripts ne sont PAS nécessaires pour faire tourner l'appli : ils servent
seulement à générer le contenu en vérifiant automatiquement les calculs
(écritures équilibrées, réponses de QCM valides, etc.).
Lancer : python3 outils/comptabilite.py
"""

def r2(x):
    """Arrondi comptable au centime (arrondi commercial, pas bancaire)."""
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))


def f(x):
    """Format français : 1 234,56 (ou 1 234 si entier)."""
    x = r2(x)
    if abs(x - round(x)) < 1e-9:
        s = f"{int(round(x)):,}".replace(",", " ")
    else:
        s = f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", " ")
    return s


# Numéros de compte acceptés (plusieurs écritures possibles selon le niveau de détail)
A = {
    'tvad': ['44566', '4456'],
    'tvac': ['44571', '4457'],
    'tvai': ['44562', '4456'],
    'caisse': ['531', '530', '53'],
    'banque': ['512'],
    'four': ['401'],
    'cli': ['411'],
    'fimmo': ['404'],
    'achm': ['607'],
    'ventm': ['707'],
    'tvadec': ['44551', '4455'],
    'credtva': ['44567'],
}


def ligne(compte, intitule, debit=0, credit=0):
    d = {'compte': compte if not (isinstance(compte, list) and len(compte) == 1) else compte[0], 'intitule': intitule}
    if debit:
        d['debit'] = r2(debit)
    if credit:
        d['credit'] = r2(credit)
    return d


def D(compte, intitule, montant):
    return ligne(A.get(compte, compte) if isinstance(compte, str) else compte, intitule, debit=montant)


def C(compte, intitule, montant):
    return ligne(A.get(compte, compte) if isinstance(compte, str) else compte, intitule, credit=montant)


def qcm(question, choix, reponse, explication, niveau=1, **kw):
    e = {'type': 'qcm', 'niveau': niveau, 'question': question, 'choix': choix, 'explication': explication}
    if isinstance(reponse, list):
        e['reponses'] = reponse
    else:
        e['reponse'] = reponse
    e.update(kw)
    return e


def vf(question, reponse, explication, niveau=1, **kw):
    e = {'type': 'vf', 'niveau': niveau, 'question': question, 'reponse': reponse, 'explication': explication}
    e.update(kw)
    return e


def courte(question, reponse, explication='', niveau=2):
    e = {'type': 'courte', 'niveau': niveau, 'question': question, 'reponse': reponse}
    if explication:
        e['explication'] = explication
    return e


def calc(question, reponse, explication, niveau=2, unite='€', tolerance=0.01, tableau=None, **kw):
    e = {'type': 'calcul', 'niveau': niveau, 'question': question, 'reponse': r2(reponse), 'explication': explication}
    if unite:
        e['unite'] = unite
    if tolerance != 0.01:
        e['tolerance'] = tolerance
    if tableau:
        e['tableau'] = tableau
    e.update(kw)
    return e


def ecr(question, lignes, explication, niveau=2, tableau=None):
    e = {'type': 'ecriture', 'niveau': niveau, 'question': question, 'lignes': lignes, 'explication': explication}
    if tableau:
        e['tableau'] = tableau
    return e


def tab(entetes, lignes, titre=None):
    t = {'entetes': entetes, 'lignes': lignes}
    if titre:
        t['titre'] = titre
    return t


def notion(id, titre, definition, points, exercices, exemple=None, attention=None, tableau=None):
    fiche = {'definition': definition, 'points': points}
    if exemple:
        fiche['exemple'] = exemple
    if attention:
        fiche['attention'] = attention
    if tableau:
        fiche['tableau'] = tableau
    for i, e in enumerate(exercices):
        e.setdefault('id', 'e%d' % (i + 1))
    return {'id': id, 'titre': titre, 'fiche': fiche, 'exercices': exercices}


def chapitre(id, titre, notions):
    return {'id': id, 'titre': titre, 'notions': notions}


def verifier(matiere):
    """Contrôles automatiques : renvoie la liste des problèmes trouvés."""
    pb = []
    ids = set()
    nb_ex = 0
    for p in matiere['parties']:
        for c in p['chapitres']:
            for n in c['notions']:
                if n['id'] in ids:
                    pb.append('id en double : ' + n['id'])
                ids.add(n['id'])
                if len(n['exercices']) < 8:
                    pb.append('%s : seulement %d exercices' % (n['id'], len(n['exercices'])))
                for e in n['exercices']:
                    nb_ex += 1
                    ou = '%s/%s' % (n['id'], e['id'])
                    t = e['type']
                    if t == 'qcm':
                        reps = e.get('reponses', [e.get('reponse')])
                        if any(r is None or r < 0 or r >= len(e['choix']) for r in reps):
                            pb.append(ou + ' : réponse QCM invalide')
                        if len(set(e['choix'])) != len(e['choix']):
                            pb.append(ou + ' : choix en double')
                    elif t == 'ecriture':
                        d = sum(l.get('debit', 0) for l in e['lignes'])
                        cr = sum(l.get('credit', 0) for l in e['lignes'])
                        if abs(d - cr) > 0.005:
                            pb.append('%s : écriture déséquilibrée (D %.2f / C %.2f)' % (ou, d, cr))
                        for l in e['lignes']:
                            if l.get('debit') and l.get('credit'):
                                pb.append(ou + ' : ligne au débit ET au crédit')
                    elif t == 'vf':
                        if not isinstance(e['reponse'], bool):
                            pb.append(ou + ' : vf non booléen')
                    if not e.get('explication') and t != 'courte':
                        pb.append(ou + ' : pas d’explication')
    return pb, nb_ex
