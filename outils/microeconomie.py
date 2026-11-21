"""Génère data/microeconomie.json. Usage : python3 outils/microeconomie.py"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from base import verifier  # noqa: E402
import micro_a, micro_b  # noqa: E402


def construire():
    return {
        'id': 'microeconomie',
        'nom': 'Microéconomie',
        'icone': '🛒',
        'description': 'Microéconomie 1 — Le marché (CM de L. Bach et M. Payen, TD 1 à 5) : échange, offre et demande, surplus, coûts, entreprise en concurrence pure et parfaite.',
        'parties': [{'id': 'micro1', 'titre': 'Microéconomie 1 — Le marché', 'chapitres': micro_a.chapitres() + micro_b.chapitres()}],
    }


if __name__ == '__main__':
    m = construire()
    pb, nb = verifier(m)
    types, sources, figs = {}, {}, 0
    for p in m['parties']:
        for c in p['chapitres']:
            for n in c['notions']:
                for e in n['exercices']:
                    types[e['type']] = types.get(e['type'], 0) + 1
                    src = e.get('source', '')
                    k = src.split(' du ')[0] if src else '(aucune)'
                    sources[k] = sources.get(k, 0) + 1
                    if not src:
                        pb.append('%s/%s : pas de source' % (n['id'], e['id']))
                    if e.get('figure'):
                        figs += 1
    nb_notions = sum(len(c['notions']) for p in m['parties'] for c in p['chapitres'])
    print('%d notions, %d exercices, %d avec graphique' % (nb_notions, nb, figs), types, sources)
    if pb:
        print('PROBLÈMES :\n' + '\n'.join(pb))
        sys.exit(1)
    racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(racine, 'data', 'microeconomie.json'), 'w', encoding='utf-8') as fh:
        json.dump(m, fh, ensure_ascii=False, indent=1)
    print('OK → data/microeconomie.json')
