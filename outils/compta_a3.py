"""Comptabilité générale — Charges et produits, trésorerie, investissements."""
from base import *


def chapitres():
    return [ch6(), ch7(), ch8()]


def ch6():
    n20 = notion(
        'charges-produits', 'Le classement des autres charges et produits',
        "Les **charges** (classe 6) et les **produits** (classe 7) se classent par **nature** : exploitation, financier, exceptionnel. Leur enregistrement suit la même logique que les achats et les ventes.",
        [
            "**Produits** : prix reçu en contrepartie des biens et services vendus, ou enrichissement sans contrepartie (subventions, gains de change).",
            "Produits d'exploitation : **70** ventes, **74** subventions d'exploitation, **75** autres produits (revenus des immeubles, redevances perçues). Financiers (**76**) : **761** produits de participations / intérêts perçus, **765** escomptes obtenus, **766** gains de change. Exceptionnels : **77**.",
            "**Charges** : prix versé pour les biens et services consommés, ou appauvrissement sans contrepartie (amendes, créances irrécouvrables).",
            "Charges d'exploitation : **60** achats, **61/62** services extérieurs (loyers 613, entretien 615, assurances 616, publicité 623, transports 624, télécom 626, services bancaires 627), **63** impôts et taxes, **64** charges de personnel, **65** autres charges (redevances versées). Financières (**66**) : **661** intérêts, **665** escomptes accordés, **666** pertes de change. Exceptionnelles : **67**.",
            "**Impôts et taxes sur salaires** (selon le cours) : formation professionnelle 1,6 %, effort de construction 0,45 %, taxe d'apprentissage 0,62 % de la masse salariale. Autres : taxe foncière, taxe sur les véhicules de société, droits d'enregistrement.",
        ],
        [
            qcm("Une subvention d'exploitation reçue de l'État s'enregistre au compte :", ["74", "77", "70", "13"], 0, "Subvention **d'exploitation** → **74**. (Une subvention d'**investissement** va au compte 13, au passif.)"),
            qcm("Des intérêts versés sur un découvert bancaire s'enregistrent en :", ["661 Charges d'intérêts", "627 Services bancaires", "665 Escomptes accordés", "761 Produits financiers"], 0, "Intérêts payés = **charge financière 661**. Les frais de tenue de compte (commissions) vont en 627."),
            qcm("Une perte de change sur un achat en devises est :", ["Une charge financière (666)", "Une charge exceptionnelle (67)", "Un produit financier (766)", "Une charge d'exploitation (60)"], 0, "**666 Pertes de change** (charge financière) ; le gain de change est en 766."),
            ecr("Facture de publicité payée par chèque : 2 000 € HT, TVA 20 %.",
                [D(['623', '6231'], 'Publicité, publications', 2000), D('tvad', 'TVA déductible', 400), C('banque', 'Banque', 2400)],
                "Publicité = **service extérieur 623**. *(TD 3, ex. 4 — hôtel Ibisa)*", niveau=1),
            ecr("Facture de réparation du véhicule par le garagiste, payée par chèque : 210 € HT, TVA 20 %.",
                [D(['615', '6155'], 'Entretien et réparations', 210), D('tvad', 'TVA déductible', 42), C('banque', 'Banque', 252)],
                "Réparations = **615 Entretien et réparations** (service extérieur), et non un achat d'immobilisation.", niveau=2),
            ecr("Prélèvement automatique du loyer du mois : 1 200 € HT, TVA 20 %.",
                [D(['613', '6132'], 'Locations', 1200), D('tvad', 'TVA déductible', 240), C('banque', 'Banque', 1440)],
                "Loyer = **613 Locations** ; payé par prélèvement → 512. *(TD 3, ex. 3)*", niveau=2),
            calc("La masse salariale annuelle s'élève à 250 000 €. Selon le cours, quel est le montant de la taxe d'apprentissage (0,62 %) ?", 1550,
                 "250 000 × 0,62 % = **1 550 €** (charge du compte 63 Impôts et taxes).", niveau=2),
            qcm("Quels éléments sont des **produits** pour l'entreprise ?", ["Des loyers perçus pour un local loué", "Des escomptes obtenus d'un fournisseur", "Une subvention d'exploitation", "Une amende payée"], [0, 1, 2],
                "Loyers perçus (75), escomptes obtenus (765), subvention (74) sont des produits ; l'amende est une **charge exceptionnelle**.", niveau=2),
            vf("Le paiement d'un timbre-poste est soumis à la TVA.", False, "Les timbres-poste ne supportent **pas de TVA** : on enregistre 626 au débit / caisse au crédit, sans TVA. *(TD 3)*", niveau=2),
        ])

    n21 = notion(
        'salaire-brut-net', 'Du salaire brut au net à payer',
        "Les **charges de personnel** comprennent le **salaire brut** et les **charges sociales patronales**. Le salarié perçoit un **net à payer** après déduction de ses cotisations et des autres retenues.",
        [
            "**Salaire brut** = salaire de base + heures supplémentaires + primes et gratifications + avantages en nature − absences.",
            "**Salaire de base** (temps plein) = **151,67 h × taux horaire**.",
            "**Heures supplémentaires** (au-delà de 35 h par semaine, selon le cours) : taux normal de la 36e à la 39e heure, **+25 %** de la 40e à la 43e, **+50 %** à partir de la 44e.",
            "**Cotisations** : CSG et CRDS (URSSAF), sécurité sociale, chômage, retraites complémentaires (Agirc-Arrco). Elles sont payées par le salarié (part **salariale**, retenue sur le brut) et par l'employeur (part **patronale**, en plus du brut).",
            "**Net à payer** = brut − cotisations salariales = salaire net de cotisations ; − autres retenues (avances et acomptes, oppositions sur salaire) ; − avantages en nature ; + indemnités (transport).",
            "Les **avantages en nature** entrent dans le brut (donc dans le calcul des cotisations) mais sont **retirés** du net à payer car ils sont déjà reçus en nature.",
        ],
        [
            calc("Un salarié à temps plein est payé 12 € de l'heure. Quel est son salaire de base mensuel ?", 1820.04, "151,67 × 12 = **1 820,04 €**.", niveau=1),
            calc("Selon les règles du cours, un salarié payé 12 €/h travaille 45 h une semaine. Quel est le montant de ses heures supplémentaires de la semaine ?", 144,
                 "36e–39e h : 4 × 12 = 48 € ; 40e–43e h : 4 × 15 (12 × 1,25) = 60 € ; 44e–45e h : 2 × 18 (12 × 1,5) = 36 €. Total = **144 €**.", niveau=3),
            calc("Salaire brut 2 000 € ; cotisations salariales 440 € ; avance déjà versée 200 € ; indemnité de transport 50 €. Quel est le net à payer ?", 1410,
                 "2 000 − 440 = 1 560 (net de cotisations) − 200 (avance) + 50 (indemnité) = **1 410 €**.", niveau=2),
            calc("Salaire de base 1 900 € ; prime 150 € ; avantage en nature (logement) 300 € ; absence décomptée 100 €. Quel est le salaire brut ?", 2250,
                 "1 900 + 150 + 300 − 100 = **2 250 €**. L'avantage en nature est inclus dans le brut.", niveau=2),
            calc("Avec ce brut de 2 250 € (dont 300 € d'avantage en nature) et 495 € de cotisations salariales, quel est le net à payer ?", 1455,
                 "2 250 − 495 = 1 755 (net de cotisations) − 300 (avantage en nature déjà reçu) = **1 455 €**.", niveau=3),
            qcm("Le coût total d'un salarié pour l'employeur est égal à :", ["Salaire brut + cotisations patronales", "Salaire net", "Salaire brut − cotisations salariales", "Salaire net + cotisations salariales"], 0,
                "Charges de personnel = **brut (641) + charges patronales (645)**.", niveau=2),
            vf("Une opposition sur salaire est une somme fixée par un jugement et versée directement au créancier du salarié.", True, "C'est une **retenue** sur le net à payer."),
            qcm("Quel organisme collecte les cotisations de sécurité sociale, la CSG et la CRDS ?", ["L'URSSAF", "L'Agirc-Arrco", "Pôle emploi", "Le Trésor public"], 0, "**URSSAF** : sécurité sociale (maladie, retraite de base, famille) + CSG/CRDS. Agirc-Arrco : retraites complémentaires.", niveau=1),
        ])

    n22 = notion(
        'salaires-compta', 'La comptabilisation des salaires et des cotisations',
        "La paie s'enregistre en plusieurs écritures : salaire brut, retenues salariales, charges patronales, puis paiement du salaire et des cotisations.",
        [
            "**Avance au salarié** : débit **425** Personnel – avances et acomptes / crédit 512.",
            "**Salaires bruts** (+ indemnités) : débit **641** Rémunérations du personnel / crédit **421** Personnel – rémunérations dues.",
            "**Retenues salariales** : débit **421** / crédit **431** Sécurité sociale, **437** Autres organismes sociaux, **425** (avances récupérées).",
            "**Charges patronales** : débit **645** Charges de sécurité sociale et de prévoyance / crédit **431** et **437**.",
            "**Paiement du net** : débit **421** / crédit **512**. **Paiement des cotisations** : débit **431** et **437** / crédit **512**.",
        ],
        [
            ecr("1/6 : l'entreprise Padtune verse par banque des acomptes de 55 000 € à ses salariés.",
                [D(['425'], 'Personnel – avances et acomptes', 55000), C('banque', 'Banque', 55000)], "Avance = créance sur le salarié (**425**).", niveau=1),
            ecr("25/6 : salaires bruts 495 000 € + indemnités de transport 6 700 €. Enregistre la rémunération due.",
                [D(['641'], 'Rémunérations du personnel', 501700), C(['421'], 'Personnel – rémunérations dues', 501700)], "641 au débit pour 495 000 + 6 700 = 501 700 €.", niveau=2),
            ecr("25/6 : retenues sur salaires — cotisations sociales salariales 62 000 €, chômage et retraite complémentaire salariales 46 300 €, acomptes à récupérer 55 000 €.",
                [D(['421'], 'Personnel – rémunérations dues', 163300), C(['425'], 'Personnel – avances et acomptes', 55000), C(['431'], 'Sécurité sociale', 62000), C(['437'], 'Autres organismes sociaux', 46300)],
                "La dette envers les salariés diminue (débit 421) de toutes les retenues : 55 000 + 62 000 + 46 300 = 163 300 €.", niveau=3),
            ecr("25/6 : cotisations patronales — sécurité sociale 120 000 €, chômage et retraite complémentaire 86 000 €.",
                [D(['645'], 'Charges de sécurité sociale et de prévoyance', 206000), C(['431'], 'Sécurité sociale', 120000), C(['437'], 'Autres organismes sociaux', 86000)],
                "Charge supplémentaire pour l'employeur (**645**) et dettes envers les organismes.", niveau=2),
            ecr("30/6 : virement du net à payer aux salariés.",
                [D(['421'], 'Personnel – rémunérations dues', 338400), C('banque', 'Banque', 338400)], "Net = 501 700 − 163 300 = **338 400 €**.", niveau=2),
            ecr("15/7 : paiement par banque des cotisations sociales dues (sécurité sociale 182 000 €, autres organismes 132 300 €).",
                [D(['431'], 'Sécurité sociale', 182000), D(['437'], 'Autres organismes sociaux', 132300), C('banque', 'Banque', 314300)],
                "431 : 62 000 + 120 000 ; 437 : 46 300 + 86 000.", niveau=2),
            ecr("Salaire brut 3 000 € ; cotisations salariales : sécurité sociale 300 €, autres organismes 150 €. Enregistre en une seule écriture le brut et les retenues (sans avances).",
                [D(['641'], 'Rémunérations du personnel', 3000), C(['421'], 'Personnel – rémunérations dues', 2550), C(['431'], 'Sécurité sociale', 300), C(['437'], 'Autres organismes sociaux', 150)],
                "Forme regroupée : 641 au débit pour le brut ; le 421 n'est crédité que du net (3 000 − 450).", niveau=3),
            calc("Padtune : quel est le coût total du personnel pour juin (641 + 645) ?", 707700, "501 700 + 206 000 = **707 700 €**.", niveau=2),
            qcm("Quel compte est débité lors du paiement du net à payer aux salariés ?", ["421", "641", "645", "431"], 0, "On solde la dette envers le personnel : **débit 421**, crédit 512."),
        ])
    return chapitre('ch-charges', 'Chapitre 6 — Les charges et les produits', [n20, n21, n22])


def ch7():
    n23 = notion(
        'modes-reglement', 'Les modes de règlement',
        "Le règlement peut être **immédiat** (au comptant) ou **différé** (à crédit). Les moyens de paiement : **espèces**, **chèque**, **virement**, **prélèvement**, carte bancaire.",
        [
            "**Espèces** : compte **53 Caisse** (solde débiteur ou nul). Une **pièce de caisse** (document interne) justifie chaque mouvement. Selon le cours : transactions commerciales < 750 €, salaires < 1 500 €.",
            "**Chèque** : écrit par lequel le **tireur** (titulaire du compte) ordonne à son banquier, le **tiré**, de payer une somme au **bénéficiaire**.",
            "**Virement** : ordre donné à la banque de prélever une somme et de la transférer sur le compte d'un bénéficiaire. **Prélèvement automatique** : virement permanent au profit d'une personne déterminée.",
            "**512 Banque** — débit : dépôts d'espèces, encaissements de chèques, virements reçus ; crédit : retraits, chèques émis, virements ordonnés, prélèvements.",
            "Dépôt d'espèces en banque ou retrait : simple **transfert** 512 ↔ 53, sans effet sur le résultat.",
        ],
        [
            ecr("31/01 : dépôt à la banque de 15 000 € en espèces prélevés sur la caisse.",
                [D('banque', 'Banque', 15000), C('caisse', 'Caisse', 15000)], "La banque augmente, la caisse diminue : transfert de trésorerie. *(TD 3, ex. 4)*", niveau=1),
            ecr("Remise à la banque d'un chèque de 1 130,06 € reçu du client Passa (facture déjà enregistrée).",
                [D('banque', 'Banque', 1130.06), C('cli', 'Clients', 1130.06)], "La créance client est soldée. *(TD 3, ex. 3)*", niveau=1),
            ecr("Pièce de caisse n° 336 : achat de timbres-poste 56 €.",
                [D(['626', '6261'], 'Frais postaux et de télécommunications', 56), C('caisse', 'Caisse', 56)], "Timbres : **626**, pas de TVA.", niveau=1),
            ecr("Paiement des salaires par virement : 6 000 € (rémunérations déjà enregistrées en 421).",
                [D(['421'], 'Personnel – rémunérations dues', 6000), C('banque', 'Banque', 6000)], "Le virement solde la dette envers le personnel.", niveau=2),
            ecr("Hôtel Ibisa, 25/01 : ventes au comptant du mois (prestations, TVA 20 %) — en espèces 16 000 € TTC, par chèques 22 000 € TTC, par cartes bancaires 75 000 € TTC.",
                [D('caisse', 'Caisse', 16000), D('banque', 'Banque', 97000), C(['706'], 'Prestations de services', r2(113000 / 1.2)), C('tvac', 'TVA collectée', r2(113000 / 1.2 * 0.2))],
                "Chèques et cartes → banque (22 000 + 75 000) ; espèces → caisse. HT = 113 000 ÷ 1,2 = 94 166,67 ; TVA = 18 833,33. *(TD 3, ex. 4)*", niveau=3),
            calc("M. Brun, boulanger : caisse au 1er juin 600 €. Recettes de la semaine 2 445 €. Sorties : pourboire 1, timbres 20, fournitures 60, dépôt en banque 350, prélèvement de l'exploitant 150, fournisseur 180, garagiste 210, cotisation retraite de l'exploitant 840. Solde de caisse au 6 juin ?", 1234,
                 "Sorties = 1 811 € ; 600 + 2 445 − 1 811 = **1 234 €**. *(TD 2, ex. 2)*", niveau=3),
            qcm("Dans un chèque, la banque qui doit payer est appelée :", ["Le tiré", "Le tireur", "Le bénéficiaire", "Le souscripteur"], 0, "Le **tireur** émet le chèque, le **tiré** (sa banque) paie, le **bénéficiaire** reçoit."),
            vf("Un prélèvement automatique est un virement permanent au profit d'une personne déterminée.", True, "C'est la définition du cours."),
            qcm("Fin octobre, la caisse contient 1 480 € ; l'entreprise ramène l'encaisse à 100 € en versant l'excédent à la banque. Quelle écriture ?", ["Débit 512 / Crédit 531 : 1 380 €", "Débit 531 / Crédit 512 : 1 380 €", "Débit 512 / Crédit 531 : 1 480 €", "Débit 512 / Crédit 707 : 1 380 €"], 0,
                "On verse 1 480 − 100 = 1 380 € de la caisse vers la banque : débit 512, crédit 531.", niveau=2),
        ])

    n24 = notion(
        'effets-commerce', 'Les effets de commerce : lettre de change et billet à ordre',
        "Un **effet de commerce** est à la fois un **instrument de paiement** et de **crédit** : le client s'engage à payer à une **échéance** précise.",
        [
            "**Lettre de change (traite, LCR)** : écrit par lequel le **tireur** (le fournisseur) ordonne au **tiré** (le client) de payer une somme à une date déterminée au **bénéficiaire** (lui-même ou un tiers). L'ordre émane du **fournisseur** ; le client l'**accepte**.",
            "**Billet à ordre (BOR)** : écrit par lequel le **souscripteur** (le client) **s'engage** à payer une somme à une date déterminée au bénéficiaire. L'ordre émane du **client**.",
            "Chez le **fournisseur** : effet à recevoir = créance mobilisable → débit **413 Clients – effets à recevoir** / crédit **411**.",
            "Chez le **client** : effet à payer = dette avec engagement → débit **401** / crédit **403 Fournisseurs – effets à payer**.",
            "À l'échéance, le client paie par sa banque : débit **403** / crédit **512** (à réception de l'avis de débit).",
        ],
        [
            ecr("17/12 : Ruquier reçoit de son client Dérec le billet à ordre n° 39 de 4 800 € en règlement d'une facture. Comptabilise chez **Ruquier** (fournisseur).",
                [D(['413'], 'Clients – effets à recevoir', 4800), C('cli', 'Clients', 4800)], "La créance change de forme : du 411 vers le **413**.", niveau=1),
            ecr("Même opération (BOR n° 39 de 4 800 €) chez **Dérec** (client).",
                [D('four', 'Fournisseurs', 4800), C(['403'], 'Fournisseurs – effets à payer', 4800)], "La dette change de forme : du 401 vers le **403**.", niveau=1),
            ecr("3/3 : Dérec reçoit l'avis de débit de 3 500 € relatif au paiement de la LCR n° 14.",
                [D(['403'], 'Fournisseurs – effets à payer', 3500), C('banque', 'Banque', 3500)], "À l'échéance, la dette d'effet est soldée par la banque.", niveau=1),
            ecr("19/12 : Ruquier reçoit la LCR n° 14 de 3 500 € acceptée par son client Dérec.",
                [D(['413'], 'Clients – effets à recevoir', 3500), C('cli', 'Clients', 3500)], "Une fois acceptée, la LCR est un effet à recevoir.", niveau=1),
            qcm("Dans une lettre de change, qui donne l'ordre de payer ?", ["Le fournisseur (tireur)", "Le client (tiré)", "La banque", "Le souscripteur"], 0, "LCR : l'ordre émane du **fournisseur** (tireur). Dans le billet à ordre, c'est le **client** (souscripteur) qui s'engage."),
            qcm("Le billet à ordre est émis par :", ["Le client (souscripteur)", "Le fournisseur (tireur)", "La banque du fournisseur", "L'État"], 0, "Le **souscripteur** (client) s'engage à payer."),
            vf("Pour le fournisseur, un effet à recevoir est une créance mobilisable.", True, "Il peut l'**escompter** ou l'**endosser** avant l'échéance."),
            qcm("Le compte 403 est :", ["Une dette du client envers son fournisseur, sous forme d'effet", "Une créance du fournisseur", "Un compte de trésorerie", "Un compte de charges"], 0, "**403 Fournisseurs – effets à payer** : dette (passif) du client."),
            courte("Quelle différence fais-tu entre une lettre de change et un billet à ordre ?",
                   "Dans la lettre de change, c'est le fournisseur (tireur) qui donne l'ordre au client (tiré) de payer, et le client l'accepte ; dans le billet à ordre, c'est le client (souscripteur) qui s'engage lui-même à payer à l'échéance.", niveau=2),
        ])

    # Animi / Guillaume
    lcr = r2(5670 * 1.2 - 600 - (5170 * 0.03) * 1.2)
    esc = r2(lcr * 0.12 * 70 / 360)
    net = r2(lcr - esc - 4.2 - 0.84)
    n25 = notion(
        'effets-encaissement', 'Encaissement, escompte et endossement des effets',
        "Le détenteur d'un effet a trois possibilités : **attendre l'échéance** (remise à l'encaissement), **le négocier** auprès de sa banque (remise à l'escompte) ou **l'endosser** au profit d'un créancier.",
        [
            "**Remise à l'encaissement** : avant l'échéance, débit **5113 Effets à l'encaissement** / crédit 413. Après l'échéance (bordereau d'encaissement) : débit 512 (net) + **6275 Frais sur effets** (commissions) + **44566** (TVA sur commissions) / crédit 5113.",
            "**Remise à l'escompte** : la banque achète l'effet avant l'échéance contre un **agio** = **escompte** (intérêt) + **commission** + **TVA sur la commission uniquement**. Remise : débit **5114 Effets à l'escompte** / crédit 413. Bordereau : débit 512 (net), **6616 Intérêts bancaires** (escompte), 6275, 44566 / crédit 5114.",
            "**Escompte = nominal × taux × nombre de jours ÷ 360** (jours comptés de la date de négociation à l'échéance).",
            "**Endossement** : le bénéficiaire transmet l'effet à son propre créancier pour éteindre une dette : ancien bénéficiaire débit **401** / crédit **413** ; nouveau bénéficiaire débit **413** / crédit **411**.",
        ],
        [
            ecr("25/2 : Ruquier remet à l'encaissement la LCR n° 14 de 3 500 €.",
                [D(['5113', '511'], "Effets à l'encaissement", 3500), C(['413'], 'Clients – effets à recevoir', 3500)], "L'effet quitte le portefeuille (413) pour la banque (5113).", niveau=1),
            ecr("3/3 : la banque adresse à Ruquier l'avis de crédit de la LCR n° 14 : net encaissé 3 488 €, commissions 10 €, TVA 2 €.",
                [D('banque', 'Banque', 3488), D(['6275', '627'], 'Frais sur effets', 10), D('tvad', 'TVA déductible', 2), C(['5113', '511'], "Effets à l'encaissement", 3500)],
                "Net = 3 500 − 10 − 2 = 3 488 € ; les commissions sont des **services bancaires** soumis à TVA.", niveau=2),
            ecr("15/3 : la société Lémarc remet à l'escompte la LCR n° 27 de 7 500 €.",
                [D(['5114', '511'], "Effets à l'escompte", 7500), C(['413'], 'Clients – effets à recevoir', 7500)], "Compte **5114** pour les effets remis à l'escompte.", niveau=1),
            ecr("20/3 : bordereau d'escompte de la LCR n° 27 (7 500 €) : escompte 50 €, commissions 10 €, TVA 2 €, net encaissé 7 438 €.",
                [D('banque', 'Banque', 7438), D(['6616', '661'], 'Intérêts bancaires', 50), D(['6275', '627'], 'Frais sur effets', 10), D('tvad', 'TVA déductible', 2), C(['5114', '511'], "Effets à l'escompte", 7500)],
                "L'escompte est un **intérêt** (charge financière 6616), non soumis à TVA. (Le support indique « 73438 € » / 7 438,04 : coquilles, le net est 7 500 − 62 = 7 438 €.)", niveau=3),
            calc("Une LCR de 7 200 € est escomptée 60 jours avant son échéance au taux de 9 %. Montant de l'escompte ?", 108, "7 200 × 9 % × 60/360 = **108 €**.", niveau=2),
            calc("Guillaume tire sur Animi une LCR de %s € (solde de la dette après retour et réduction de 3 %%). Il la remet à l'escompte le 22 novembre ; échéance 31 janvier ; taux 12 %%. Montant de l'escompte (au centime) ?" % f(lcr), esc,
                 "Jours : 8 (23→30 nov.) + 31 + 31 = 70. Escompte = %s × 12 %% × 70/360 = **%s €**. *(TD 5, ex. 1)*" % (f(lcr), f(esc)), niveau=3),
            ecr("Comptabilise chez Guillaume le bordereau d'escompte de la LCR de %s € : escompte %s €, commission 4,20 € HT, TVA 20 %%." % (f(lcr), f(esc)),
                [D('banque', 'Banque', net), D(['6616', '661'], 'Intérêts bancaires', esc), D(['6275', '627'], 'Frais sur effets', 4.2), D('tvad', 'TVA déductible', 0.84), C(['5114', '511'], "Effets à l'escompte", lcr)],
                "Net = %s − %s − 4,20 − 0,84 = **%s €**." % (f(lcr), f(esc), f(net)), niveau=3),
            ecr("Une entreprise endosse au profit de son fournisseur un effet de 1 000 € tiré sur un de ses clients, pour régler sa dette. Comptabilise chez l'**ancien bénéficiaire** (celui qui endosse).",
                [D('four', 'Fournisseurs', 1000), C(['413'], 'Clients – effets à recevoir', 1000)], "L'effet sort du portefeuille et éteint la dette fournisseur.", niveau=2),
            qcm("Sur quoi porte la TVA dans un bordereau d'escompte ?", ["Uniquement sur la commission", "Sur l'escompte et la commission", "Sur le nominal de l'effet", "Il n'y a jamais de TVA"], 0, "La TVA est assise **uniquement sur la commission** ; l'escompte (intérêt) n'est pas soumis à TVA.", niveau=2),
        ])

    n26 = notion(
        'effets-incidents', 'Les incidents de paiement : renouvellement et impayé',
        "À l'échéance, le tiré peut ne pas pouvoir payer : il demande un **report** (l'effet est **renouvelé**) ou il est **défaillant** (l'effet est **impayé**).",
        [
            "**Renouvellement** : 1) **annulation** du premier effet (bénéficiaire : débit 411 / crédit 413 ; tiré : débit 403 / crédit 401) ; 2) **tirage d'un nouvel effet** d'un montant supérieur, intégrant les **intérêts de retard** (soumis à TVA selon le cours) : bénéficiaire débit 413 / crédit 411, **763 Revenus des autres créances**, 44571 ; tiré débit 401, **661 Charges d'intérêts**, 44566 / crédit 403.",
            "**Impayé d'un effet remis à l'encaissement** : l'effet est annulé et les frais bancaires sont ajoutés à la dette du client : bénéficiaire débit **411** (nominal + frais) / crédit **5113** et 512 (frais).",
            "**Impayé d'un effet escompté** : la banque, propriétaire de l'effet, se retourne contre le remettant (garant) et prélève **nominal + frais** sur son compte : débit **411** / crédit **512**.",
            "**Endossement** : l'endossataire réclame à l'endosseur le nominal + les frais.",
        ],
        [
            ecr("Renouvellement : le bénéficiaire annule l'effet de 100 € qu'il détenait sur son client.",
                [D('cli', 'Clients', 100), C(['413'], 'Clients – effets à recevoir', 100)], "La créance redevient une créance ordinaire (411).", niveau=1),
            ecr("Puis il tire un nouvel effet de 112 € comprenant le nominal 100 €, des intérêts de retard 10 € et la TVA sur ces intérêts 2 €. Comptabilise chez le **bénéficiaire**.",
                [D(['413'], 'Clients – effets à recevoir', 112), C('cli', 'Clients', 100), C(['763', '7638'], 'Revenus des autres créances', 10), C('tvac', 'TVA collectée', 2)],
                "Les intérêts facturés au client sont un **produit financier (763)**. *(Exemple du cours)*", niveau=3),
            ecr("Même renouvellement chez le **tiré** : annulation de l'effet de 100 € et acceptation du nouvel effet de 112 € (intérêts 10 €, TVA 2 €). Enregistre seulement l'acceptation du nouvel effet.",
                [D('four', 'Fournisseurs', 100), D(['661', '6611'], "Charges d'intérêts", 10), D('tvad', 'TVA déductible', 2), C(['403'], 'Fournisseurs – effets à payer', 112)],
                "Le tiré supporte les intérêts de retard : **charge financière 661**.", niveau=3),
            ecr("Un effet de 100 € remis à l'encaissement revient impayé ; la banque prélève 12 € de frais. Comptabilise chez le **bénéficiaire**.",
                [D('cli', 'Clients', 112), C(['5113', '511'], "Effets à l'encaissement", 100), C('banque', 'Banque', 12)],
                "L'effet est annulé et les frais sont mis à la charge du client (411 = 112).", niveau=3),
            ecr("Un effet de 100 € remis à l'escompte revient impayé ; la banque débite le compte du remettant de 112 € (nominal + frais). Comptabilise chez le **bénéficiaire**.",
                [D('cli', 'Clients', 112), C('banque', 'Banque', 112)], "La banque reprend son argent (nominal + frais) : le bénéficiaire redevient créancier de son client pour 112 €.", niveau=2),
            ecr("Mega : la banque adresse un avis d'impayé pour la LCR n° 77 (escomptée) et débite le compte de 10 611,76 € (dont 11,76 € de TVA). Comptabilise chez Mega selon la méthode du cours.",
                [D('cli', 'Clients', 10611.76), C('banque', 'Banque', 10611.76)], "Effet escompté impayé : on débite le client du montant total prélevé. *(TD 5, ex. 4)*", niveau=2),
            calc("Loret renouvelle un effet de 17 940 € : le nouvel effet, à échéance du 30 septembre au lieu du 31 juillet, intègre des intérêts de retard au taux annuel de 14 %. Montant des intérêts (au centime, sur 61 jours) ?", 425.58,
                 "17 940 × 14 % × 61/360 = **425,58 €**. *(TD 5, ex. 3)*", niveau=3),
            qcm("En cas d'impayé d'un effet escompté, qui supporte le risque vis-à-vis de la banque ?", ["Le remettant (bénéficiaire), garant du paiement", "La banque seule", "L'État", "Personne"], 0, "Le bénéficiaire reste **garant** : la banque prélève nominal + frais sur son compte.", niveau=2),
        ])

    n27 = notion(
        'tresorerie-vmp', 'Gestion de trésorerie : découvert et VMP',
        "La gestion de trésorerie consiste à faire face aux **besoins** (découvert, endossement, escompte d'effets) et à placer les **excédents** (achat de valeurs mobilières de placement).",
        [
            "**Découvert bancaire** : crédit à court terme autorisé par la banque ; il coûte des intérêts (**661**) qui accroissent le découvert. Un découvert = **solde créditeur** du compte 512.",
            "Les excédents ont un **coût d'opportunité** : on les place en **VMP** (compte **50** : **503 Actions**, **506 Obligations**).",
            "**Actions** : droit de **propriété**, revenu **variable** (dividende). **Obligations** : droit de **créance**, revenu **fixe** (intérêt).",
            "**Achat** : débit 503/506 (prix d'achat) + **6271 Frais sur titres** + 44566 (TVA sur frais) / crédit 512.",
            "**Cession** : **±value = prix de cession − prix d'acquisition**. Plus-value → crédit **767 Produits nets sur cessions de VMP** ; moins-value → débit **667 Charges nettes sur cessions de VMP**. On annule les titres au crédit (prix d'achat) et on encaisse le prix de cession en 512.",
        ],
        [
            ecr("Pueblo achète 10 actions au cours unitaire de 620 € ; frais 30 € HT (TVA 20 %) ; paiement par banque.",
                [D(['503', '50'], 'Actions', 6200), D(['6271', '627'], 'Frais sur titres', 30), D('tvad', 'TVA déductible', 6), C('banque', 'Banque', 6236)], "Les titres sont inscrits au prix d'achat ; les frais sont une charge.", niveau=2),
            ecr("Pueblo cède les 10 actions (achetées 620 €) au cours de 622 €, encaissement par banque.",
                [D('banque', 'Banque', 6220), C(['503', '50'], 'Actions', 6200), C(['767'], 'Produits nets sur cessions de VMP', 20)], "Plus-value = 6 220 − 6 200 = 20 € → produit financier **767**.", niveau=2),
            ecr("Si Pueblo avait cédé ses 10 actions (achetées 620 €) à 600 € l'une :",
                [D('banque', 'Banque', 6000), D(['667'], 'Charges nettes sur cessions de VMP', 200), C(['503', '50'], 'Actions', 6200)], "Moins-value = 6 000 − 6 200 = −200 € → charge financière **667**.", niveau=3),
            calc("Achat de 50 obligations à 98 € ; revente des 50 à 101,50 €. Plus-value réalisée ?", 175, "50 × (101,50 − 98) = **175 €**.", niveau=2),
            ecr("La banque prélève 25 € d'intérêts sur le découvert du compte de l'entreprise.",
                [D(['661', '6615'], "Charges d'intérêts", 25), C('banque', 'Banque', 25)], "Les intérêts de découvert sont une **charge financière (661)**, sans TVA.", niveau=1),
            qcm("Une action donne à son détenteur :", ["Un droit de propriété et un revenu variable", "Un droit de créance et un revenu fixe", "Un prêt à la banque", "Une dette"], 0, "Action = propriété (dividende variable) ; obligation = créance (intérêt fixe)."),
            vf("Un compte banque à solde créditeur signifie que l'entreprise est à découvert.", True, "La banque prête alors de l'argent à l'entreprise : c'est une dette (passif)."),
            qcm("Quelles sont des solutions à un besoin de trésorerie ?", ["Demander un découvert bancaire", "Remettre des effets à l'escompte", "Endosser des effets", "Acheter des VMP"], [0, 1, 2], "Acheter des VMP sert à placer un **excédent**, pas à couvrir un besoin.", niveau=2),
        ])

    atol = tab(['Compte 512 (chez Atol)', 'Relevé bancaire (chez la banque)'], [['Solde débiteur 11 690 €', 'Solde créditeur 17 925 €'],
                                                                                 ['Chèque n° 375 de 3 700 € au fournisseur : enregistré', 'Chèque n° 375 : pas encore débité'],
                                                                                 ['Virement client 2 560 € : pas encore enregistré', 'Virement client 2 560 € : crédité'],
                                                                                 ['Intérêts de découvert 25 € : pas encore enregistrés', 'Intérêts 25 € : débités']], 'Entreprise Atol au 30/10')
    ex2 = tab(['Compte 512 (chez l\'entreprise)', 'Relevé bancaire'], [['Solde débiteur 5 430 €', 'Solde créditeur 6 210 €'],
                                                                     ['Chèque n° 88 émis 1 150 € (enregistré)', 'Pas encore débité'],
                                                                     ['Remise de chèques 380 € (enregistrée)', 'Pas encore créditée'],
                                                                     ['—', 'Virement reçu d\'un client 300 €'], ['—', 'Frais bancaires 40 €'], ['—', 'Prélèvement assurance 250 €']], 'Autre entreprise au 31/03')
    n28 = notion(
        'rapprochement', "L'état de rapprochement bancaire",
        "Le compte **512 Banque** de l'entreprise et le **relevé bancaire** sont **réciproques** : leurs soldes devraient être identiques et de sens contraire. Des **décalages** d'enregistrement les font différer ; l'**état de rapprochement** les explique.",
        [
            "**Débit** du compte 512 ↔ **crédit** du relevé (et inversement) : un solde **débiteur** chez l'entreprise correspond à un solde **créditeur** sur le relevé.",
            "Méthode : 1) **pointer** les sommes identiques ; 2) **isoler** les sommes figurant sur un seul des documents ; 3) **corriger** chaque document de ses oublis jusqu'à obtenir le même solde rectifié.",
            "Côté **relevé** : retirer les chèques émis non encore débités ; ajouter les remises non encore créditées.",
            "Côté **compte 512** : ajouter les virements reçus, retirer les frais, agios, prélèvements non encore enregistrés.",
            "On ne passe **en comptabilité** que les opérations figurant sur le **relevé** mais absentes du compte 512.",
        ],
        [
            calc("Atol : quel est le solde rectifié du **relevé bancaire** ?", 14225, "17 925 − 3 700 (chèque non encore débité) = **14 225 €** (créditeur).", niveau=2, tableau=atol),
            calc("Atol : quel est le solde rectifié du **compte 512** ?", 14225, "11 690 + 2 560 (virement client) − 25 (intérêts) = **14 225 €** (débiteur). Les deux soldes concordent ✓.", niveau=2, tableau=atol),
            ecr("Atol : enregistre le virement du client de 2 560 € découvert lors du rapprochement.",
                [D('banque', 'Banque', 2560), C('cli', 'Clients', 2560)], "Opération présente sur le relevé mais absente de la comptabilité : on l'enregistre.", niveau=1, tableau=atol),
            ecr("Atol : enregistre les intérêts de découvert de 25 € découverts lors du rapprochement.",
                [D(['661', '6615'], "Charges d'intérêts", 25), C('banque', 'Banque', 25)], "Charge financière à enregistrer.", niveau=1, tableau=atol),
            vf("Le chèque n° 375 émis par Atol et non encore débité par la banque doit être enregistré dans la comptabilité d'Atol lors du rapprochement.", False,
               "Il est **déjà** enregistré chez Atol ; c'est la **banque** qui ne l'a pas encore débité. Il sert seulement à rectifier le solde du relevé.", niveau=2, ),
            calc("Avec les données du tableau, calcule le solde rectifié du **relevé**.", 5440, "6 210 − 1 150 (chèque non débité) + 380 (remise non créditée) = **5 440 €**.", niveau=3, tableau=ex2),
            calc("Avec les mêmes données, calcule le solde rectifié du **compte 512**.", 5440, "5 430 + 300 − 40 − 250 = **5 440 €** ✓.", niveau=3, tableau=ex2),
            qcm("Un solde débiteur de 4 000 € au compte 512 de l'entreprise correspond, sans décalage, à quel solde sur le relevé ?", ["Créditeur de 4 000 €", "Débiteur de 4 000 €", "Créditeur de 8 000 €", "Nul"], 0, "Comptes **réciproques** : même montant, **sens contraire**."),
            courte("Quelles opérations enregistre-t-on dans le journal après un état de rapprochement ?",
                   "Uniquement celles qui figurent sur le relevé bancaire mais pas encore dans le compte 512 de l'entreprise (virements reçus, frais, agios, prélèvements…). Les opérations déjà enregistrées par l'entreprise mais pas encore par la banque ne donnent lieu à aucune écriture.", niveau=2),
        ])
    return chapitre('ch-tresorerie', 'Chapitre 7 — La trésorerie', [n23, n24, n25, n26, n27, n28])


def ch8():
    n29 = notion(
        'immobilisations', 'Les immobilisations : définition, classement, coût d\'entrée',
        "**Investir** = acquérir ou fabriquer des **immobilisations**, c'est-à-dire des éléments **détenus ou contrôlés**, **identifiables et valorisables**, ayant une **valeur économique positive** (ressources futures), d'un montant > 500 € (selon le cours).",
        [
            "**Incorporelles (20)** : frais d'établissement 201, frais de R&D 203, brevets-marques-logiciels 205, fonds commercial 207.",
            "**Corporelles (21)** : terrains 211, constructions 213, installations techniques, matériel et outillage 215, autres (218 : transport 2182, bureau 2183, mobilier 2184).",
            "**Financières (26-27)** : titres de participation 261, créances rattachées 267, titres immobilisés 271/272/273, prêts 274, dépôts et cautionnements versés 275.",
            "**Coût d'acquisition HT** = prix d'achat HT (net financier) + frais liés à l'acquisition : frais d'installation (rattachés à l'immobilisation), droits de douane ; frais juridiques et fiscaux (**option** : à l'actif ou en charges).",
            "TVA sur immobilisations : **44562** ; fournisseur : **404 Fournisseurs d'immobilisations**.",
            "Immobilisations **financières** : coût d'acquisition des titres ; les frais sont soit en charges financières, soit intégrés au coût.",
        ],
        [
            ecr("Acquisition à crédit d'une machine 20 000 € HT avec 1 000 € HT de frais d'installation, TVA 20 %.",
                [D(['2154', '215'], 'Matériel industriel', 21000), D('tvai', 'TVA sur immobilisations', 4200), C('fimmo', "Fournisseurs d'immobilisations", 25200)],
                "Les frais d'installation sont **incorporés** au coût d'entrée (21 000) ; TVA sur immobilisations **44562** ; dette en **404**.", niveau=2),
            ecr("Achat à crédit d'un ordinateur 2 500 € HT, TVA 20 %, règlement à 60 jours.",
                [D(['2183', '218'], 'Matériel de bureau et informatique', 2500), D('tvai', 'TVA sur immobilisations', 500), C('fimmo', "Fournisseurs d'immobilisations", 3000)], "Bien durable > 500 € : immobilisation. *(TD 3, ex. 2 — PEGE)*", niveau=1),
            ecr("Acquisition d'un terrain 100 000 € + frais divers 900 € HT (fournisseur) ; frais d'acte du notaire 5 000 € HT et droits d'enregistrement 4 800 € (dus au notaire, compte 467). TVA 20 % sur les frais sauf droits d'enregistrement. **Option 1** : tous les frais incorporés au coût du terrain.",
                [D(['211'], 'Terrains', 110700), D('tvad', 'TVA sur autres biens et services', 1180), C('fimmo', "Fournisseurs d'immobilisations", 101080), C(['467'], 'Autres comptes débiteurs ou créditeurs', 10800)],
                "211 = 100 000 + 900 + 5 000 + 4 800 = 110 700 ; TVA = (900 + 5 000) × 20 % = 1 180 ; 404 = 100 900 + 180 ; 467 = 5 000 + 1 000 + 4 800. (Le support utilise l'ancien taux de 19,6 %.)", niveau=3),
            ecr("Même acquisition de terrain, **option 2** : les frais d'acquisition (frais d'acte 5 000 € et droits d'enregistrement 4 800 €) sont passés en charges.",
                [D(['211'], 'Terrains', 100900), D(['6354', '635'], "Droits d'enregistrement", 4800), D(['622', '6226'], "Rémunérations d'intermédiaires et honoraires", 5000), D('tvad', 'TVA sur autres biens et services', 1180), C('fimmo', "Fournisseurs d'immobilisations", 101080), C(['467'], 'Autres comptes débiteurs ou créditeurs', 10800)],
                "Frais d'acte → 622 ; droits d'enregistrement → 6354 ; le terrain reste à 100 900 €.", niveau=3),
            ecr("Achat par banque de titres détenus pour plus d'un an : 21 000 € ; frais 1 000 € HT (TVA 20 %) passés en charges.",
                [D(['272', '271'], 'Titres immobilisés', 21000), D(['6271', '627'], 'Frais sur titres', 1000), D('tvad', 'TVA déductible', 200), C('banque', 'Banque', 22200)],
                "Titres détenus > 1 an : **immobilisation financière** (272) ; frais en charges (option).", niveau=2),
            calc("Une machine coûte 48 000 € brut, remise 5 %, escompte 2 % ; frais de transport 600 € HT et d'installation 1 400 € HT. Quel est son coût d'acquisition HT ?", 46688,
                 "Net commercial = 45 600 ; net financier = 45 600 × 0,98 = 44 688 ; + 600 + 1 400 = **46 688 €**.", niveau=3),
            qcm("Un brevet acheté par l'entreprise est une immobilisation :", ["Incorporelle", "Corporelle", "Financière", "Ce n'est pas une immobilisation"], 0, "Brevets, marques, logiciels : **205** (incorporelles)."),
            qcm("Un dépôt de garantie versé au propriétaire des locaux est classé en :", ["Immobilisations financières (275)", "Charges (613)", "Créances clients", "Immobilisations corporelles"], 0, "**275 Dépôts et cautionnements versés** : immobilisation financière (il sera restitué).", niveau=2),
            vf("Un petit outil de 80 € HT peut être comptabilisé directement en charges.", True, "Selon le cours, une immobilisation suppose un montant > 500 € : les petits matériels peuvent aller en charges (fournitures non stockables).", niveau=2),
        ])

    n30 = notion(
        'immo-produites', 'Immobilisations produites et décomposables',
        "Une entreprise peut **fabriquer elle-même** une immobilisation, ou acquérir une immobilisation composée d'éléments ayant des **durées d'utilisation différentes**.",
        [
            "**Immobilisation produite** : valeur d'entrée = **coût de production** (coût d'achat des matières + charges de production). Les charges ont déjà été enregistrées en classe 6 : on constate un **produit 72 Production immobilisée** pour les neutraliser.",
            "C'est une **livraison à soi-même** : on constate la **TVA collectée** (44571) et la **TVA déductible sur immobilisations** (44562) du même montant.",
            "**Immobilisation décomposable** : composants à durées d'utilisation différentes ou procurant des avantages à un rythme différent → **ventilation en sous-comptes** (ex. 2181.1 carrosserie, 2181.2 moteur, 2181.3 box).",
            "Le coût d'entrée global n'est pas modifié, mais le **renouvellement** d'un composant à un coût différent modifie la valeur.",
        ],
        [
            ecr("L'entreprise construit elle-même un entrepôt : coût des matières et services 50 000 €, charges de personnel 14 000 €. Enregistre la production immobilisée et la livraison à soi-même (TVA 20 %).",
                [D(['213'], 'Constructions', 64000), D('tvai', 'TVA sur immobilisations', 12800), C(['72', '722', '721'], 'Production immobilisée', 64000), C('tvac', 'TVA collectée', 12800)],
                "Immobilisation au coût de production (64 000) ; produit **72** ; TVA de livraison à soi-même : 64 000 × 20 % = 12 800 (le support utilise 19,6 %).", niveau=3),
            ecr("Achat par banque d'un van pour chevaux 128 000 € HT, TVA 20 %, décomposé en : carrosserie 27 000 €, moteur 69 000 €, box 32 000 €. (Compte 2182 ou 2181 avec sous-comptes ; saisis 2182 sur trois lignes.)",
                [D(['2182', '2181'], 'Matériel de transport – carrosserie', 27000), D(['2182', '2181'], 'Matériel de transport – moteur', 69000), D(['2182', '2181'], 'Matériel de transport – box', 32000), D('tvai', 'TVA sur immobilisations', 25600), C('banque', 'Banque', 153600)],
                "Chaque composant a sa propre ligne car sa durée d'utilisation diffère.", niveau=3),
            qcm("Le compte 72 Production immobilisée est :", ["Un compte de produit", "Un compte de charge", "Un compte d'immobilisation", "Un compte de tiers"], 0, "Classe 7 : il **neutralise** les charges engagées pour fabriquer l'immobilisation."),
            calc("Pour fabriquer une machine, l'entreprise a consommé 18 500 € de matières et 7 300 € de main-d'œuvre. Quelle est la valeur d'entrée de la machine ?", 25800, "Coût de production = 18 500 + 7 300 = **25 800 €**.", niveau=1),
            calc("Avec cette machine de 25 800 € produite par l'entreprise, quel est le montant de TVA de livraison à soi-même (20 %) ?", 5160, "25 800 × 20 % = **5 160 €** (collectée et déductible).", niveau=2),
            vf("Une immobilisation produite par l'entreprise n'a aucun effet sur le résultat.", True,
               "Les charges (classe 6) sont compensées par le produit **72 Production immobilisée** du même montant : l'effet net est nul ; l'actif augmente.", niveau=2),
            qcm("Pourquoi décomposer une immobilisation en composants ?", ["Parce que ses éléments ont des durées d'utilisation différentes", "Pour payer moins de TVA", "Parce que la loi interdit les immobilisations > 100 000 €", "Pour l'enregistrer en charges"], 0, "Chaque composant sera utilisé (et renouvelé) à son propre rythme."),
            courte("Qu'appelle-t-on une « livraison à soi-même » ?",
                   "Le fait pour une entreprise de produire elle-même un bien qu'elle conserve comme immobilisation : elle est considérée comme se le vendant à elle-même, d'où la constatation d'une TVA collectée et d'une TVA déductible du même montant.", niveau=2),
        ])

    n31 = notion(
        'financement', 'Le financement des investissements',
        "Les investissements peuvent être financés par le **délai de paiement** du fournisseur, les **capitaux propres** (apports, augmentation de capital, autofinancement), les **emprunts** (bancaires ou obligataires), le **crédit-bail** ou des **subventions**.",
        [
            "**Emprunt bancaire** : réalisation → débit 512 / crédit **164**. Les **frais d'émission** sont soit en charges, soit incorporés au coût.",
            "**Annuité** = remboursement du capital (**amortissement** de l'emprunt, débit 164) + **intérêts** (charge, débit 661). Les intérêts portent sur le **capital restant dû**.",
            "**Subvention d'investissement** : aide de l'État pour financer des activités de long terme ou acquérir des immobilisations (compte **131**, au passif). Elle est **virée au résultat** (produit exceptionnel **777**) par fractions, au même rythme que l'amortissement du bien.",
            "**Crédit-bail** : **location avec option d'achat** ; l'entreprise n'est pas propriétaire, les loyers sont des charges (**612** Redevances de crédit-bail).",
        ],
        [
            ecr("Obtention d'un emprunt bancaire de 50 000 €, versé sur le compte.",
                [D('banque', 'Banque', 50000), C(['164', '16'], 'Emprunts auprès des établissements de crédit', 50000)], "Ressource durable : dette financière **164**.", niveau=1),
            calc("Emprunt de 50 000 € au taux de 4 %, remboursable par fractions constantes de 10 000 € par an. Montant de la **première annuité** ?", 12000, "Intérêts = 50 000 × 4 % = 2 000 ; annuité = 10 000 + 2 000 = **12 000 €**.", niveau=2),
            calc("Même emprunt : montant des **intérêts de la deuxième année** ?", 1600, "Capital restant dû = 40 000 ; intérêts = 40 000 × 4 % = **1 600 €**.", niveau=2),
            ecr("Paiement par banque de la première annuité : remboursement de 10 000 € et intérêts de 2 000 €.",
                [D(['164', '16'], 'Emprunts', 10000), D(['661', '6611'], 'Intérêts des emprunts', 2000), C('banque', 'Banque', 12000)],
                "Seuls les **intérêts** sont une charge ; le remboursement du capital diminue la dette.", niveau=2),
            ecr("Réception par virement d'une subvention d'investissement de 30 000 €.",
                [D('banque', 'Banque', 30000), C(['131', '13'], "Subventions d'équipement", 30000)], "La subvention d'investissement est inscrite au **passif** (compte 13), pas directement en produit.", niveau=2),
            calc("La subvention de 30 000 € finance un matériel amorti sur 5 ans. Quel montant est viré au résultat chaque année ?", 6000, "30 000 ÷ 5 = **6 000 €** par an (produit exceptionnel 777), au rythme de l'amortissement.", niveau=2),
            qcm("Le crédit-bail est :", ["Une location avec option d'achat", "Un emprunt obligataire", "Une augmentation de capital", "Une subvention"], 0, "Crédit-bail = **location avec option d'achat** en fin de contrat."),
            vf("Le remboursement du capital d'un emprunt est une charge.", False, "Non : il diminue une dette. Seuls les **intérêts** (661) sont des charges."),
            qcm("Quelles sources de financement sont des **capitaux propres** ?", ["Augmentation de capital", "Apports initiaux des associés", "Emprunt bancaire", "Crédit-bail"], [0, 1], "Les apports et augmentations de capital sont des capitaux propres ; l'emprunt est une dette ; le crédit-bail est une location.", niveau=2),
        ])
    return chapitre('ch-investissements', 'Chapitre 8 — Les investissements et leur financement', [n29, n30, n31])
