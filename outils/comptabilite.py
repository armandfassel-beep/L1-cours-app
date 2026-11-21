"""Génère data/comptabilite.json à partir des fichiers compta_*.py.
Usage : python3 outils/comptabilite.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from base import verifier  # noqa: E402
import compta_a1, compta_a2, compta_a3, compta_b  # noqa: E402

COMPTES = {
    '101': 'Capital', '106': 'Réserves', '108': "Compte de l'exploitant", '120': "Résultat de l'exercice (bénéfice)", '129': "Résultat de l'exercice (perte)",
    '131': "Subventions d'équipement", '164': 'Emprunts auprès des établissements de crédit',
    '201': "Frais d'établissement", '203': 'Frais de recherche et de développement', '205': 'Concessions, brevets, licences, marques, logiciels', '207': 'Fonds commercial',
    '211': 'Terrains', '213': 'Constructions', '215': 'Installations techniques, matériel et outillage', '2154': 'Matériel industriel',
    '218': 'Autres immobilisations corporelles', '2181': 'Installations générales, agencements', '2182': 'Matériel de transport', '2183': 'Matériel de bureau et informatique', '2184': 'Mobilier',
    '261': 'Titres de participation', '271': 'Titres immobilisés (droit de propriété)', '272': 'Titres immobilisés (droit de créance)', '274': 'Prêts', '275': 'Dépôts et cautionnements versés',
    '370': 'Stocks de marchandises',
    '401': 'Fournisseurs', '403': 'Fournisseurs – effets à payer', '404': "Fournisseurs d'immobilisations", '4091': 'Fournisseurs – avances et acomptes versés',
    '411': 'Clients', '413': 'Clients – effets à recevoir', '4191': 'Clients – avances et acomptes reçus',
    '421': 'Personnel – rémunérations dues', '425': 'Personnel – avances et acomptes', '431': 'Sécurité sociale', '437': 'Autres organismes sociaux',
    '44551': 'TVA à décaisser', '4455': 'TVA à décaisser', '44562': 'TVA déductible sur immobilisations', '44566': 'TVA déductible sur autres biens et services', '4456': 'TVA déductible',
    '44567': 'Crédit de TVA à reporter', '44571': 'TVA collectée', '4457': 'TVA collectée', '4458': 'TVA à régulariser', '467': 'Autres comptes débiteurs ou créditeurs',
    '503': 'Actions', '506': 'Obligations', '5113': "Effets à l'encaissement", '5114': "Effets à l'escompte", '512': 'Banque', '53': 'Caisse', '530': 'Caisse', '531': 'Caisse',
    '601': 'Achats stockés – matières premières', '602': 'Achats stockés – autres approvisionnements', '604': "Achats d'études et prestations de services", '605': 'Achats de matériel, équipements et travaux',
    '606': 'Achats non stockés de matières et fournitures', '6061': 'Fournitures non stockables (eau, énergie)', '6064': 'Fournitures administratives',
    '607': 'Achats de marchandises', '608': "Frais accessoires d'achat", '609': 'Rabais, remises et ristournes obtenus sur achats',
    '612': 'Redevances de crédit-bail', '613': 'Locations', '614': 'Charges locatives et de copropriété', '615': 'Entretien et réparations', '616': "Primes d'assurances",
    '622': "Rémunérations d'intermédiaires et honoraires", '6222': 'Commissions et courtages sur achats', '623': 'Publicité, publications, relations publiques', '6238': 'Divers (pourboires, dons courants)',
    '6241': 'Transports sur achats', '6242': 'Transports sur ventes', '626': 'Frais postaux et de télécommunications', '627': 'Services bancaires et assimilés',
    '6271': 'Frais sur titres', '6275': 'Frais sur effets', '635': 'Autres impôts, taxes et versements assimilés', '6354': "Droits d'enregistrement",
    '641': 'Rémunérations du personnel', '645': 'Charges de sécurité sociale et de prévoyance',
    '661': "Charges d'intérêts", '6616': 'Intérêts bancaires et sur opérations de financement', '665': 'Escomptes accordés', '666': 'Pertes de change', '667': 'Charges nettes sur cessions de VMP',
    '671': 'Charges exceptionnelles sur opérations de gestion',
    '701': 'Ventes de produits finis', '702': 'Ventes de produits intermédiaires', '706': 'Prestations de services', '707': 'Ventes de marchandises',
    '7085': 'Ports et frais accessoires facturés', '709': 'Rabais, remises et ristournes accordés', '72': 'Production immobilisée', '74': "Subventions d'exploitation",
    '763': 'Revenus des autres créances', '765': 'Escomptes obtenus', '766': 'Gains de change', '767': 'Produits nets sur cessions de VMP', '777': "Quote-part des subventions d'investissement virée au résultat",
}


def construire():
    return {
        'id': 'comptabilite',
        'nom': 'Comptabilité',
        'icone': '📊',
        'description': 'Principes de gestion — L1. Comptabilité générale et monde de l’entreprise (CM de C. Guittard, TD 1 à 5).',
        'comptes': COMPTES,
        'parties': [
            {'id': 'compta-generale', 'titre': 'Partie 1 — Comptabilité générale',
             'chapitres': compta_a1.chapitres() + compta_a2.chapitres() + compta_a3.chapitres()},
            {'id': 'entreprise', 'titre': 'Partie 2 — Le monde de l’entreprise', 'chapitres': compta_b.chapitres()},
        ],
    }


if __name__ == '__main__':
    m = construire()
    pb, nb = verifier(m)
    nb_notions = sum(len(c['notions']) for p in m['parties'] for c in p['chapitres'])
    types = {}
    for p in m['parties']:
        for c in p['chapitres']:
            for n in c['notions']:
                for e in n['exercices']:
                    types[e['type']] = types.get(e['type'], 0) + 1
    print('%d notions, %d exercices' % (nb_notions, nb), types)
    if pb:
        print('PROBLÈMES :')
        print('\n'.join(pb))
        sys.exit(1)
    racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(racine, 'data', 'comptabilite.json'), 'w', encoding='utf-8') as fh:
        json.dump(m, fh, ensure_ascii=False, indent=1)
    print('OK → data/comptabilite.json')
