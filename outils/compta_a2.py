"""Comptabilité générale — Achats, ventes et TVA."""
from base import *


def chapitres():
    return [ch5()]


def tva(x, t=0.2):
    return r2(x * t)


def ch5():
    # ------------------------------------------------ 13 facture simple
    n13 = notion(
        'facture-simple', 'La facture simple : achat et vente au comptant ou à crédit',
        "Toute opération d'achat ou de vente est justifiée par une **facture**. C'est la **réception (ou l'émission) de la facture** qui déclenche l'enregistrement comptable.",
        [
            "**Achat** : charge au **HT** (60x) au débit + **TVA déductible** (44566) au débit ; au crédit : **512 Banque** (comptant) ou **401 Fournisseurs** (à crédit) pour le **TTC**.",
            "**Vente** : **512** (comptant) ou **411 Clients** (à crédit) au débit pour le **TTC** ; au crédit : vente au **HT** (70x) + **TVA collectée** (44571).",
            "Au **règlement** d'une facture à crédit : l'acheteur solde sa dette (débit 401 / crédit 512) ; le vendeur solde sa créance (débit 512 / crédit 411).",
            "Comptes d'achats : **601** MP, **602** autres approvisionnements, **604** prestations de services, **605** matériel, **606** achats non stockés (6061 eau-énergie, 6064 fournitures administratives), **607** marchandises.",
            "Comptes de ventes : **701** produits finis, **702** produits intermédiaires, **706** prestations de services, **707** marchandises.",
            "**Mentions obligatoires** : identité du vendeur (nom, forme juridique, capital, n° SIREN, n° TVA), identité de l'acheteur, date de la vente et du règlement, quantités, prix unitaire HT, réductions, TVA, total TTC.",
        ],
        [
            ecr("Achat de marchandises au comptant par chèque : 1 000 € HT, TVA 20 %.",
                [D('achm', 'Achats de marchandises', 1000), D('tvad', 'TVA déductible sur ABS', 200), C('banque', 'Banque', 1200)],
                "Charge au HT (**607**), TVA récupérable au débit (**44566**), paiement du TTC (**512**).", niveau=1),
            ecr("Vente de marchandises à crédit au client Simi : 2 540 € HT, TVA 20 %.",
                [D('cli', 'Clients', 3048), C('ventm', 'Ventes de marchandises', 2540), C('tvac', 'TVA collectée', 508)],
                "Créance client au TTC (**411** : 2 540 × 1,2 = 3 048) ; produit au HT (**707**) ; TVA collectée = dette envers l'État (**44571** : 508). *(TD 3, ex. 3)*", niveau=1),
            ecr("Achat de marchandises à crédit au fournisseur Vallet : 1 300 € HT, TVA 20 %.",
                [D('achm', 'Achats de marchandises', 1300), D('tvad', 'TVA déductible sur ABS', 260), C('four', 'Fournisseurs', 1560)],
                "Achat à crédit : la dette fournisseur (**401**) est enregistrée pour le TTC (1 560 €). *(TD 3, ex. 3)*", niveau=1),
            ecr("Le chèque n° 102 est envoyé au fournisseur Vallet pour régler sa facture de 1 560 € TTC.",
                [D('four', 'Fournisseurs', 1560), C('banque', 'Banque', 1560)],
                "Au règlement, on **solde la dette** : débit 401, crédit 512. Pas de TVA ici : elle a déjà été enregistrée sur la facture.", niveau=1),
            ecr("Achat de fournitures de papeterie payées par chèque : 168 € HT, TVA 20 %.",
                [D(['6064', '606'], 'Fournitures administratives', 168), D('tvad', 'TVA déductible sur ABS', 33.6), C('banque', 'Banque', 201.6)],
                "Les fournitures de bureau sont des **achats non stockés** (**6064**). TVA = 168 × 20 % = 33,60 €.", niveau=2),
            ecr("Vente de produits finis fabriqués par l'entreprise, encaissée par virement : 4 750 € HT, TVA 20 %.",
                [D('banque', 'Banque', 5700), C(['701'], 'Ventes de produits finis', 4750), C('tvac', 'TVA collectée', 950)],
                "Produits **fabriqués** par l'entreprise → **701** (et non 707, réservé aux marchandises revendues en l'état).", niveau=2),
            calc("Une facture de vente porte sur 3 600 € HT au taux normal. Quel est le net à payer TTC ?", 4320,
                 "TTC = HT × 1,20 = 3 600 × 1,2 = **4 320 €**.", niveau=1),
            qcm("Parmi ces mentions, lesquelles sont obligatoires sur une facture ?", ["Le numéro SIREN du vendeur", "Le prix unitaire HT", "Le taux et le montant de TVA", "La marge réalisée par le vendeur"], [0, 1, 2],
                "La marge n'apparaît jamais sur une facture. Sont obligatoires : identité du vendeur et de l'acheteur, date, quantités, PU HT, réductions, TVA, total TTC.", niveau=2),
            qcm("Une entreprise de conseil facture une mission à son client. Quel compte de produit utilise-t-elle ?", ["706 Prestations de services", "707 Ventes de marchandises", "701 Ventes de produits finis", "604 Achats de prestations"], 0,
                "Une mission de conseil est un **service** → **706**.", niveau=1),
        ])

    # ------------------------------------------------ 14 TVA principe
    n14 = notion(
        'tva-principe', 'La TVA : principe, taux, TVA collectée et déductible',
        "La **TVA** (taxe sur la valeur ajoutée) est un **impôt indirect sur la consommation finale**. L'entreprise la **collecte** sur ses ventes et **récupère** celle payée sur ses achats : elle ne la supporte pas.",
        [
            "**Taux** : **20 %** (normal), **10 %** (intermédiaire), **5,5 %** (réduit : eau, produits alimentaires…), **2,1 %** (particulier : presse, médicaments remboursables).",
            "**TVA collectée** (ventes) = PV TTC − PV HT → **44571**, dette envers l'État ; la vente est enregistrée **HT** en produits.",
            "**TVA déductible** (achats) = PA TTC − PA HT → **44566** (biens et services) ou **44562** (immobilisations), créance sur l'État ; l'achat est enregistré **HT** en charges.",
            "**Versement à l'État = TVA collectée − TVA déductible**.",
            "Formules : **TVA = HT × taux** ; **TTC = HT × (1 + taux)** ; **HT = TTC ÷ (1 + taux)**.",
            "Certaines opérations ne sont **pas soumises à la TVA** : assurances, salaires, intérêts bancaires, timbres-poste…",
        ],
        [
            calc("Une facture d'achat s'élève à 2 500 € HT au taux normal. Montant de la TVA ?", 500, "TVA = 2 500 × 20 % = **500 €**.", niveau=1),
            calc("Un client paie 1 440 € TTC (taux normal). Quel est le montant HT ?", 1200, "HT = 1 440 ÷ 1,20 = **1 200 €**.", niveau=1),
            calc("La SARL Imri réalise en janvier 390 000 € de ventes TTC au taux normal. Quelle TVA a-t-elle collectée ?", 65000,
                 "HT = 390 000 ÷ 1,2 = 325 000 € ; TVA = 390 000 − 325 000 = **65 000 €** (ou 390 000 × 20/120). *(TD 3, ex. 1)*", niveau=2),
            calc("Imri vend aussi pour 8 366 € TTC de produits au taux de 5,5 %. Quelle TVA a-t-elle collectée sur ces ventes ? (au centime)", 436.14,
                 "HT = 8 366 ÷ 1,055 = 7 929,86 € ; TVA = 8 366 − 7 929,86 = **436,14 €**.", niveau=3),
            calc("La société PEGE reçoit une facture d'eau de 336 € HT (taux réduit de 5,5 %). Montant de la TVA ?", 18.48,
                 "336 × 5,5 % = **18,48 €**. *(TD 3, ex. 2)*", niveau=2),
            ecr("Facture de la Société des Eaux reçue : 336 € HT, TVA 5,5 %, à payer plus tard.",
                [D(['6061', '606'], 'Fournitures non stockables (eau, énergie)', 336), D('tvad', 'TVA déductible sur ABS', 18.48), C('four', 'Fournisseurs', 354.48)],
                "Eau et énergie : **6061** ; TVA au taux réduit 5,5 % = 18,48 € ; dette fournisseur TTC = 354,48 €.", niveau=2),
            ecr("Paiement par chèque de la prime d'assurance incendie : 800 € (non soumise à TVA).",
                [D(['616'], "Primes d'assurances", 800), C('banque', 'Banque', 800)],
                "Les assurances **ne sont pas soumises à la TVA** : aucune ligne 44566.", niveau=2),
            calc("Au cours du mois : TVA collectée 9 800 €, TVA déductible 6 350 €. Quel montant l'entreprise doit-elle verser à l'État ?", 3450,
                 "TVA à décaisser = collectée − déductible = 9 800 − 6 350 = **3 450 €**.", niveau=1),
            vf("La TVA est une charge pour l'entreprise.", False,
               "Non : l'entreprise **collecte** la TVA pour le compte de l'État et **récupère** celle payée sur ses achats. Seul le **consommateur final** la supporte."),
            qcm("Quel est le taux de TVA applicable à un abonnement à une revue de presse ?", ["2,1 %", "5,5 %", "10 %", "20 %"], 0, "La presse bénéficie du taux particulier de **2,1 %** (TD 3, ex. 2).", niveau=2),
        ])

    # ------------------------------------------------ 15 TVA à décaisser
    imri = tab(['', 'Janvier', 'Février', 'Mars'], [
        ['Ventes TTC (20 %)', 390000, 275000, 320000], ['Ventes TTC à 5,5 %', 8366, 10550, 8967.5], ['Ventes TTC à 2,1 %', 3037.48, 1613.18, 0],
        ['Achats de marchandises HT', 72000, 175000, 95000], ['Charges diverses HT', 67300, 90000, 56000], ["Achat d'immobilisations TTC", 23920, 150000, 6578]], 'SARL Imri — 1er trimestre (TD 3, ex. 1)')
    n15 = notion(
        'tva-decaisser', 'TVA à décaisser, crédit de TVA et déclaration',
        "En fin de mois, l'entreprise compare la TVA collectée et la TVA déductible : elle a soit une **TVA à décaisser** (dette envers l'État), soit un **crédit de TVA** (créance reportée sur le mois suivant).",
        [
            "**Fait générateur** : livraison du bien / exécution de la prestation. **Exigibilité** (moment où l'État peut réclamer la taxe) : **biens → à la livraison (TVA sur les débits)** ; **services → à l'encaissement**.",
            "**TVA à décaisser = TVA collectée − TVA déductible − crédit de TVA du mois précédent** (si positif).",
            "Écriture de liquidation : on **solde** 44571 (débit) et 44566/44562 (crédit) ; la différence va en **44551 TVA à décaisser** (crédit) ou en **44567 Crédit de TVA à reporter** (débit).",
            "**Paiement** le mois suivant (entre le 15 et le 24) : débit 44551 / crédit 512.",
            "Un crédit de TVA est **imputé** sur la TVA due du mois suivant (crédit 44567).",
        ],
        [
            ecr("Fin janvier : TVA collectée 80 €, TVA déductible 100 €. Enregistre la liquidation de la TVA.",
                [D('tvac', 'TVA collectée', 80), D('credtva', 'Crédit de TVA à reporter', 20), C('tvad', 'TVA déductible', 100)],
                "Déductible > collectée : on solde les deux comptes et la différence (20 €) est un **crédit de TVA** (débit 44567), reporté sur février. *(Exemple du cours)*", niveau=2),
            ecr("Fin février : TVA collectée 145 €, TVA déductible 75 €, crédit de TVA de janvier 20 €. Enregistre la liquidation.",
                [D('tvac', 'TVA collectée', 145), C('credtva', 'Crédit de TVA à reporter', 20), C('tvad', 'TVA déductible', 75), C('tvadec', 'TVA à décaisser', 50)],
                "145 − 75 − 20 = **50 € à décaisser** : on solde 44571, 44566 et 44567 ; la dette envers l'État est en **44551**.", niveau=3),
            ecr("Le 15 mars, la TVA à décaisser de février (50 €) est payée par virement.",
                [D('tvadec', 'TVA à décaisser', 50), C('banque', 'Banque', 50)],
                "Le paiement solde la dette envers l'État : débit **44551**, crédit **512**.", niveau=1),
            calc("SARL Imri, janvier : calcule la **TVA collectée** totale (3 taux), au centime.", 65498.62,
                 "20 % : 390 000 × 20/120 = 65 000,00 ; 5,5 % : 8 366 − 8 366/1,055 = 436,14 ; 2,1 % : 3 037,48 − 3 037,48/1,021 = 62,48. Total = **65 498,62 €**.", niveau=3, tableau=imri),
            calc("SARL Imri, janvier : calcule la **TVA déductible** totale, au centime.", 31846.67,
                 "Marchandises 72 000 × 20 % = 14 400 ; charges 67 300 × 20 % = 13 460 ; immobilisations 23 920 × 20/120 = 3 986,67. Total = **31 846,67 €**.", niveau=3, tableau=imri),
            calc("SARL Imri, janvier : quel est le montant de la **TVA à décaisser** ?", 33651.95,
                 "65 498,62 − 31 846,67 = **33 651,95 €**, à payer le 20 février.", niveau=2, tableau=imri),
            calc("SARL Imri, février : TVA collectée 46 416,51 € ; TVA déductible 78 000 € (35 000 + 18 000 + 25 000). Quel est le **crédit de TVA** à reporter ?", 31583.49,
                 "46 416,51 − 78 000 = −31 583,49 → **crédit de TVA de 31 583,49 €** (gros achat d'immobilisations de 150 000 € TTC), imputé sur mars.", niveau=3, tableau=imri),
            vf("Pour une prestation de services, la TVA est en principe exigible à l'encaissement du prix.", True,
               "**Biens** : TVA exigible à la **livraison** (« TVA sur les débits ») ; **services** : à l'**encaissement** (sauf option pour les débits)."),
            qcm("Le crédit de TVA est enregistré dans le compte :", ["44567", "44551", "44571", "44566"], 0, "**44567 Crédit de TVA à reporter** (débit) ; 44551 = TVA à décaisser (crédit).", niveau=1),
        ])

    # ------------------------------------------------ 16 Réductions
    n16 = notion(
        'reductions', 'Les réductions sur facture : rabais, remise, ristourne, escompte',
        "Les réductions diminuent le prix. Elles sont **commerciales** (rabais, remise, ristourne) ou **financières** (escompte de règlement) et se calculent **en cascade**.",
        [
            "**Rabais** : réduction ponctuelle pour **dédommagement** (défaut de qualité, retard de livraison).",
            "**Remise** : réduction **habituelle** liée aux **quantités** achetées.",
            "**Ristourne** : réduction calculée sur l'**ensemble des opérations** réalisées avec un client sur une période (prime de fidélité).",
            "**Escompte de règlement** : réduction accordée au client qui **paie avant l'échéance** normale.",
            "**Cascade** : Prix brut − réductions commerciales = **Net commercial** − escompte = **Net financier (HT)** + TVA = **Net à payer (TTC)**. Plusieurs remises successives se calculent chacune sur le montant précédent.",
            "En comptabilité, les **réductions commerciales n'apparaissent jamais** : on enregistre directement le **net commercial** (607/707).",
            "L'**escompte** est toujours enregistré : **charge financière 665 Escomptes accordés** chez le vendeur ; **produit financier 765 Escomptes obtenus** chez l'acheteur.",
        ],
        [
            calc("Marchandises brutes 8 000 € ; remise 10 % ; escompte 2 % ; TVA 20 %. Quel est le **net à payer** ?", 8467.2,
                 "Net commercial = 8 000 − 800 = 7 200 ; escompte 2 % = 144 → net financier 7 056 ; TVA = 1 411,20 ; **net à payer = 8 467,20 €**.", niveau=2),
            ecr("L'entreprise Albert vend ces marchandises à crédit à son client Mayer (brut 8 000 €, remise 10 %, escompte 2 %, TVA 20 %). Comptabilise la facture chez **le vendeur**.",
                [D('cli', 'Clients', 8467.2), D('665', 'Escomptes accordés', 144), C('ventm', 'Ventes de marchandises', 7200), C('tvac', 'TVA collectée', 1411.2)],
                "Vente au **net commercial** (7 200) ; la remise n'apparaît pas ; l'escompte est une **charge financière (665)** ; TVA calculée sur le net financier (7 056 × 20 %).", niveau=3),
            ecr("Même facture (brut 8 000 €, remise 10 %, escompte 2 %, TVA 20 %) : comptabilise-la chez **l'acheteur** Mayer.",
                [D('achm', 'Achats de marchandises', 7200), D('tvad', 'TVA déductible', 1411.2), C('four', 'Fournisseurs', 8467.2), C('765', 'Escomptes obtenus', 144)],
                "Achat au net commercial ; l'escompte obtenu est un **produit financier (765)** au crédit.", niveau=3),
            calc("American Store achète 90 T-shirts à 8,50 € HT pièce avec deux remises successives de 5 % et 3 %. Quel est le **net commercial** (au centime) ?", 704.95,
                 "Brut = 90 × 8,50 = 765 € ; après 5 % : 765 × 0,95 = 726,75 ; après 3 % : 726,75 × 0,97 = **704,95 €**. Les remises successives ne s'additionnent pas (≠ 8 %). *(TD 4, ex. 1)*", niveau=2),
            ecr("17/09 : American Store achète 10 jeans à 45 € HT, rabais 8 %, escompte 3 % pour paiement rapide ; paiement immédiat par chèque (TVA 20 %).",
                [D('achm', 'Achats de marchandises', 414), D('tvad', 'TVA déductible', 80.32), C('banque', 'Banque', 481.9), C('765', 'Escomptes obtenus', 12.42)],
                "Brut 450 − rabais 36 = **414** (net commercial) ; escompte 3 % = 12,42 → net financier 401,58 ; TVA 80,32 ; TTC **481,90** payé par chèque.", niveau=3),
            ecr("Facture n° 112 de la SA Mamuse au client Cora : marchandises 5 000 €, remise 10 %, escompte 1 %, TVA 20 %, à crédit. Comptabilise-la chez Mamuse (vendeur).",
                [D('cli', 'Clients', 5346), D('665', 'Escomptes accordés', 45), C('ventm', 'Ventes de marchandises', 4500), C('tvac', 'TVA collectée', 891)],
                "Net commercial 4 500 ; escompte 45 → net financier 4 455 ; TVA 891 ; net à payer **5 346 €**. *(TD 4, ex. 2)*", niveau=3),
            calc("Vente de produits finis, brut HT 77 500 €, remises successives de 2 % et 3 %. Quel est le **net à payer TTC** (TVA 20 %) ?", 88405.8,
                 "77 500 × 0,98 = 75 950 ; × 0,97 = 73 671,50 (net commercial = HT) ; TVA 14 734,30 ; **TTC = 88 405,80 €**. *(TD 4, ex. 4 — société MAD)*", niveau=3),
            qcm("Une réduction accordée à un client parce que la livraison est arrivée en retard est :", ["Un rabais", "Une remise", "Une ristourne", "Un escompte"], 0, "Dédommagement ponctuel (défaut, retard) = **rabais**."),
            qcm("Une réduction accordée en fin d'année sur l'ensemble du chiffre d'affaires réalisé avec un client fidèle est :", ["Une ristourne", "Une remise", "Un rabais", "Un escompte"], 0, "Réduction sur l'ensemble des opérations d'une période = **ristourne**."),
            vf("Dans le journal, on enregistre l'achat au prix brut puis la remise obtenue dans un compte de produit.", False,
               "Les réductions commerciales figurant **sur la facture** ne sont **jamais** enregistrées : on comptabilise directement le **net commercial**.", niveau=2),
        ])

    # ------------------------------------------------ 17 Frais accessoires
    n17 = notion(
        'frais-accessoires', 'Les frais accessoires d\'achat et de vente',
        "**Coût d'achat = prix d'achat + frais accessoires**. Les frais accessoires d'achat sont les **frais de transport, commissions, primes d'assurance** engagés pour réaliser l'achat.",
        [
            "Vente **« départ »** : le transport est **à la charge du client** → pour lui, ce sont des frais accessoires d'achat (facturés par le vendeur ou par un transporteur).",
            "Vente **« franco de port »** : le transport est **à la charge du fournisseur** → pour le client, ce ne sont pas des frais accessoires ; pour le vendeur, c'est une **charge** (**6242** Transports sur ventes).",
            "Chez l'**acheteur**, les frais accessoires peuvent être enregistrés : dans un compte de **services extérieurs** par nature (**6241** Transports sur achats, **622** Commissions et courtages…), dans le compte **608** (frais accessoires d'achat), ou **incorporés** au compte d'achat (607).",
            "Chez le **vendeur**, les frais refacturés au client sont un produit : **7085 Ports et frais accessoires facturés**.",
            "Les frais accessoires sont **soumis à la TVA** comme le reste de la facture.",
        ],
        [
            ecr("Facture d'achat : marchandises 900 € HT + frais de port facturés 100 € HT, TVA 20 %, à crédit. Comptabilise chez l'**acheteur** (frais accessoires en compte 608 ou 6241).",
                [D('achm', 'Achats de marchandises', 900), D(['608', '6241', '624'], 'Frais accessoires d\'achat', 100), D('tvad', 'TVA déductible', 200), C('four', 'Fournisseurs', 1200)],
                "Les frais de port sont des frais accessoires d'achat (**608** ou **6241**) ; la TVA porte sur 1 000 € HT.", niveau=2),
            ecr("Même facture (marchandises 900 € HT + port 100 € HT, TVA 20 %, à crédit) : comptabilise chez le **vendeur**.",
                [D('cli', 'Clients', 1200), C('ventm', 'Ventes de marchandises', 900), C(['7085', '708'], 'Ports et frais accessoires facturés', 100), C('tvac', 'TVA collectée', 200)],
                "Le vendeur refacture le transport : produit **7085**.", niveau=2),
            ecr("M. Lajoie achète 2 000 bouteilles à un viticulteur 6 000 € HT et paie un transporteur 1 000 € HT (même fournisseur pour simplifier), TVA 20 %, à crédit. Il utilise les comptes de services extérieurs.",
                [D('achm', 'Achats de marchandises', 6000), D(['6241', '624'], 'Transports sur achats', 1000), D('tvad', 'TVA déductible', 1400), C('four', 'Fournisseurs', 8400)],
                "Méthode demandée : frais en **services extérieurs (6241)**. *(TD 4, ex. 3)*", niveau=3),
            calc("Pour M. Lajoie (6 000 € HT de vin + 1 000 € HT de transport pour 2 000 bouteilles), quel est le **coût d'achat d'une bouteille** ?", 3.5,
                 "Coût d'achat = (6 000 + 1 000) ÷ 2 000 = **3,50 €** par bouteille.", niveau=2),
            ecr("M. Lajoie achète 5 000 bouteilles à un courtier pour 11 000 € HT au total, dont 1 000 € de courtage ; TVA 20 % ; à crédit.",
                [D('achm', 'Achats de marchandises', 10000), D(['6222', '622'], 'Commissions et courtages sur achats', 1000), D('tvad', 'TVA déductible', 2200), C('four', 'Fournisseurs', 13200)],
                "Le courtage est un frais accessoire enregistré en services extérieurs (**6222** Commissions et courtages sur achats).", niveau=3),
            ecr("M. Lajoie vend à une grande surface 10 000 € HT de vin et lui facture 400 € HT de frais d'expédition (livraison par le vendeur), TVA 20 %, à crédit.",
                [D('cli', 'Clients', 12480), C('ventm', 'Ventes de marchandises', 10000), C(['7085', '708'], 'Ports et frais accessoires facturés', 400), C('tvac', 'TVA collectée', 2080)],
                "Frais d'expédition refacturés : **7085** ; TVA sur 10 400 € = 2 080 €.", niveau=3),
            qcm("Dans une vente « franco de port », qui supporte le coût du transport ?", ["Le vendeur (fournisseur)", "Le client", "Le transporteur", "L'État"], 0,
                "**Franco** = transport payé par le **vendeur** : pour lui c'est une charge (6242 Transports sur ventes)."),
            ecr("Vente franco de port : le vendeur reçoit la facture du transporteur pour la livraison à son client : 300 € HT, TVA 20 %, à payer.",
                [D(['6242', '624'], 'Transports sur ventes', 300), D('tvad', 'TVA déductible', 60), C('four', 'Fournisseurs', 360)],
                "Le transport sur ventes est une **charge** du vendeur (**6242**) ; il n'est pas refacturé au client.", niveau=2),
            courte("Quelles sont les trois façons possibles de comptabiliser les frais accessoires d'achat chez l'acheteur ?",
                   "1) Dans les comptes de services extérieurs selon leur nature (6241 transports sur achats, 6222 commissions…) ; 2) dans le compte 608 Frais accessoires d'achat ; 3) en les incorporant au compte d'achat concerné (607, 601…).", niveau=2),
        ])

    # ------------------------------------------------ 18 Avoirs
    n18 = notion(
        'avoirs', 'Les factures d\'avoir : réductions hors facture et retours',
        "La **facture d'avoir** est établie par le fournisseur quand il **doit** quelque chose à son client après la facture initiale : réduction accordée après coup ou retour de marchandises. Elle s'enregistre **en sens inverse** de la facture.",
        [
            "Facture « **doit** » : le client doit au fournisseur ; facture d'**avoir** : le fournisseur doit au client.",
            "**Réduction commerciale hors facture** (rabais, remise, ristourne accordés après coup) : comptes spécifiques **709 RRR accordés** (débit, vendeur) et **609 RRR obtenus** (crédit, acheteur). La TVA et la créance/dette diminuent.",
            "**Escompte supplémentaire** : **665** au débit chez le vendeur, **765** au crédit chez l'acheteur, + baisse de la TVA et de la créance/dette.",
            "**Retour de marchandises** : mêmes conditions que la facture d'origine (mêmes réductions) ; on **contrepasse** l'écriture initiale avec les **mêmes comptes** (707, 607…) pour le montant retourné.",
            "Vendeur : crédit **411** (la créance diminue). Acheteur : débit **401** (la dette diminue).",
        ],
        [
            ecr("Albert adresse à Mayer une facture d'avoir : ristourne sur ventes du trimestre 200 €, TVA 20 % 40 €, net 240 €. Comptabilise chez **Albert (vendeur)**.",
                [D(['709', '7097'], 'Rabais, remises et ristournes accordés', 200), D('tvac', 'TVA collectée', 40), C('cli', 'Clients', 240)],
                "Ristourne hors facture → **709** au débit ; la TVA collectée et la créance client diminuent.", niveau=2),
            ecr("Même avoir (ristourne 200 € HT + TVA 40 €) : comptabilise chez **Mayer (acheteur)**.",
                [D('four', 'Fournisseurs', 240), C(['609', '6097'], 'Rabais, remises et ristournes obtenus', 200), C('tvad', 'TVA déductible', 40)],
                "Chez l'acheteur : **609 RRR obtenus** au crédit ; la dette fournisseur et la TVA déductible diminuent.", niveau=2),
            ecr("Avoir d'escompte supplémentaire : escompte 150 €, TVA 30 €, net 180 €. Comptabilise chez le **vendeur**.",
                [D('665', 'Escomptes accordés', 150), D('tvac', 'TVA collectée', 30), C('cli', 'Clients', 180)],
                "**Attention** : la créance client diminue du **net** de l'avoir, 180 € (le support du cours indique 130 € par erreur, et un ancien taux de 19,6 %).", niveau=2),
            ecr("Retour de marchandises par le client Mayer : brut 1 000 €, remise 10 %, escompte 2 %, TVA 20 % ; net porté au compte 1 058,40 €. Comptabilise chez le **vendeur** Albert.",
                [D('ventm', 'Ventes de marchandises', 900), D('tvac', 'TVA collectée', 176.4), C('cli', 'Clients', 1058.4), C('665', 'Escomptes accordés', 18)],
                "On contrepasse la facture : 707 débité du net commercial (900), 4457 débité (176,40), 665 crédité de l'escompte (18), 411 crédité du net (1 058,40).", niveau=3),
            ecr("Même retour (brut 1 000, remise 10 %, escompte 2 %, TVA 20 %) : comptabilise chez **l'acheteur** Mayer.",
                [D('four', 'Fournisseurs', 1058.4), D('765', 'Escomptes obtenus', 18), C('achm', 'Achats de marchandises', 900), C('tvad', 'TVA déductible', 176.4)],
                "Contrepassation de la facture d'achat : 401 et 765 au débit, 607 et 44566 au crédit.", niveau=3),
            ecr("Avoir n° 78 de la SA Mamuse à Cora : rabais exceptionnel 400 €, TVA 80 €, net 480 €. Comptabilise chez Mamuse.",
                [D(['709', '7097'], 'RRR accordés', 400), D('tvac', 'TVA collectée', 80), C('cli', 'Clients', 480)],
                "Rabais **hors facture** → 709. *(TD 4, ex. 2)*", niveau=2),
            calc("American Store retourne un blouson acheté 320 € HT, avec rabais 6 % et escompte 3 % (TVA 20 %). Quel est le **net de l'avoir** TTC (au centime) ?", 350.14,
                 "320 − 6 % = 300,80 ; escompte 3 % = 9,02 → 291,78 ; TVA 58,36 ; **net = 350,14 €**. Le retour reprend les conditions de la facture d'origine. *(TD 4, ex. 1)*", niveau=3),
            qcm("Dans quel compte le vendeur enregistre-t-il une remise accordée après coup par facture d'avoir ?", ["709", "707", "665", "609"], 0, "Réductions commerciales **hors facture** : **709 RRR accordés** (vendeur) / 609 RRR obtenus (acheteur)."),
            vf("Un retour de marchandises s'enregistre avec les mêmes comptes que la facture initiale, mais en sens inverse.", True, "On utilise les mêmes comptes (707/607, TVA, 411/401, 665/765) pour un montant opposé."),
        ])

    # ------------------------------------------------ 19 Acomptes
    n19 = notion(
        'acomptes', 'Acomptes et exigibilité de la TVA (synthèse)',
        "Un **acompte** est une avance versée **avant** la facture. Il est enregistré dans un compte de tiers spécifique : **4091 Fournisseurs – avances et acomptes versés** (acheteur) ou **4191 Clients – avances et acomptes reçus** (vendeur). *(Thème approfondi en S2.)*",
        [
            "On considère toujours l'acompte **TTC**. **TVA comprise dans l'acompte = acompte ÷ (1 + t) × t**.",
            "La TVA sur acompte est enregistrée avec le compte d'attente **4458 TVA à régulariser** (selon la synthèse du cours).",
            "**TVA sur les débits** (biens, ou services avec option) : TVA exigible à la **facturation** → 44571 au crédit (vendeur) / 44566 au débit (acheteur) à la date de la facture.",
            "**TVA sur les encaissements** (services sans option) : à la facture, la TVA va en **4458** (attente) ; elle devient exigible à l'**encaissement** : on solde alors 4458 par 44571 (vendeur) ou 44566 (acheteur).",
            "À la facture, l'acompte est **soldé** : on crédite 4091 (acheteur) ou on débite 4191 (vendeur) ; le fournisseur/client n'est plus dû que du **net à payer**.",
        ],
        [
            calc("Un acompte de 1 200 € TTC est versé (TVA 20 %). Quel montant de TVA contient-il ?", 200, "TVA = 1 200 ÷ 1,2 × 0,2 = **200 €**.", niveau=1),
            ecr("Versement par chèque d'un acompte de 1 200 € TTC à un fournisseur (TVA 20 %, enregistrement de la TVA selon la synthèse du cours).",
                [D(['4091', '409'], 'Fournisseurs – avances et acomptes versés', 1200), D('tvad', 'TVA déductible', 200), C(['4458'], 'TVA à régulariser', 200), C('banque', 'Banque', 1200)],
                "L'avance est une **créance** sur le fournisseur (**4091**) ; la TVA de l'acompte (200) est constatée en 44566 avec contrepartie 4458.", niveau=3),
            ecr("Facture reçue (bien, TVA sur les débits) : net 10 000 €, TVA 2 000 €, TTC 12 000 €, acompte déjà versé 1 200 € (voir écriture précédente) ; net à payer 10 800 €. Enregistre la facture (compte d'achat 607).",
                [D('achm', 'Achats', 10000), D('tvad', 'TVA déductible', 1800), D(['4458'], 'TVA à régulariser', 200), C(['4091', '409'], 'Fournisseurs – acomptes versés', 1200), C('four', 'Fournisseurs', 10800)],
                "TVA totale 2 000 dont 200 déjà constatés sur l'acompte → 1 800 en 44566 et on solde le 4458 (200). L'acompte est soldé (crédit 4091) ; la dette fournisseur = 10 800 €. *(Synthèse du cours)*", niveau=3),
            ecr("Règlement par chèque du solde de 10 800 € dû au fournisseur.",
                [D('four', 'Fournisseurs', 10800), C('banque', 'Banque', 10800)],
                "Facture de **biens** (TVA sur les débits) : au règlement, rien à faire pour la TVA.", niveau=1),
            ecr("Service **sans option** pour les débits : à la réception de la facture (net 10 000 €, TVA 2 000 €, acompte 1 200 € versé, net à payer 10 800 €), toute la TVA va en compte d'attente. Enregistre la facture (compte 604).",
                [D(['604', '6'], 'Achats de prestations de services', 10000), D(['4458'], 'TVA à régulariser', 2000), C(['4091', '409'], 'Fournisseurs – acomptes versés', 1200), C('four', 'Fournisseurs', 10800)],
                "TVA sur les encaissements : la TVA n'est pas encore déductible → **4458 au débit** pour l'intégralité. *(Synthèse du cours)*", niveau=3),
            ecr("Règlement du solde (10 800 €) de ce service sans option : la TVA devient exigible, on solde le compte d'attente pour 1 800 €.",
                [D('four', 'Fournisseurs', 10800), D('tvad', 'TVA déductible', 1800), C(['4458'], 'TVA à régulariser', 1800), C('banque', 'Banque', 10800)],
                "Au paiement, la TVA devient déductible : on solde 4458 par 44566. *(Synthèse du cours)*", niveau=3),
            qcm("Chez le vendeur, un acompte reçu d'un client est enregistré dans le compte :", ["4191", "4091", "411", "707"], 0, "**4191 Clients – avances et acomptes reçus** (dette envers le client tant que la livraison n'a pas eu lieu)."),
            vf("Pour une vente de biens, la TVA devient exigible à l'encaissement du prix.", False, "Pour les **biens**, la TVA est exigible à la **livraison/facturation** (TVA sur les débits). L'encaissement concerne les **services**."),
            calc("Société MAD : vente de produits finis, brut HT 46 500 € ; le client a versé un acompte de 20 % du HT le 5 octobre. Montant de l'acompte ?", 9300,
                 "20 % × 46 500 = **9 300 €**. *(TD 4, ex. 4)*", niveau=1),
        ])

    return chapitre('ch-achats-ventes', 'Chapitre 5 — Les achats et les ventes', [n13, n14, n15, n16, n17, n18, n19])
