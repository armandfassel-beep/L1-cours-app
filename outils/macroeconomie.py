"""Génère data/macroeconomie.json. Usage : python3 outils/macroeconomie.py"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from base import verifier  # noqa: E402
import macro_a, macro_b, macro_c  # noqa: E402


def construire():
    return {
        'id': 'macroeconomie',
        'nom': 'Macroéconomie',
        'icone': '🌍',
        'description': 'Macroéconomie 1 — L1 S1 (CM de P. Rondé et M. Sidiropoulos, TD 1 à 4) : comptabilité nationale, consommation, investissement, État, monnaie, IS-LM.',
        'parties': [{'id': 'macro1', 'titre': 'Macroéconomie 1', 'chapitres': macro_a.chapitres() + macro_b.chapitres() + macro_c.chapitres()}],
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
                    sources[src.split(' du ')[0] if src else '(aucune)'] = sources.get(src.split(' du ')[0] if src else '(aucune)', 0) + 1
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
    with open(os.path.join(racine, 'data', 'macroeconomie.json'), 'w', encoding='utf-8') as fh:
        json.dump(m, fh, ensure_ascii=False, indent=1)
    print('OK → data/macroeconomie.json')
