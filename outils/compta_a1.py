"""Comptabilité générale — Introduction, bilan, compte de résultat, compte, organisation comptable."""
from base import *


def chapitres():
    return [ch0(), ch1(), ch2(), ch3(), ch4()]


# ---------------------------------------------------------------- CH 0
def ch0():
    n1 = notion(
        'intro-compta', 'Définition, histoire et utilisateurs de la comptabilité',
        "La comptabilité est un **système d'information** qui donne une image de l'entreprise à travers ses opérations susceptibles d'une **représentation monétaire**.",
        [
            "**Comptabilité générale (ou financière)** : appréhende les échanges avec l'**extérieur** (clients, fournisseurs, banques, État…).",
            "**Comptabilité analytique (ou de gestion)** : appréhende les opérations **internes** ; ces flux internes n'ont pas de prix pour les évaluer objectivement.",
            "**Utilisateurs** : dirigeants, créanciers, actionnaires, administration fiscale et organismes sociaux, tribunaux de commerce, représentants des salariés.",
            "**Preuve des opérations** : saisie chronologique et **ineffaçable** ; pas de modification après validation ; chaque écriture est justifiée par une **pièce** (facture, relevé, contrat) ; terminologie et documents **communs** à toutes les entreprises.",
            "**Repères historiques** : −3000 tablettes cunéiformes ; 1494 **Luca Pacioli** formalise la **partie double** ; 1673 **Code Colbert** (livre de comptes à valeur de preuve) ; 1807 **Code de commerce** (Napoléon).",
        ],
        [
            vf("La comptabilité générale appréhende principalement les opérations internes à l'entreprise.", False,
               "C'est la comptabilité **analytique** qui s'intéresse aux opérations internes. La comptabilité **générale** enregistre les échanges avec l'extérieur."),
            qcm("Qui a formalisé le principe de la partie double en 1494 ?", ["Luca Pacioli", "Colbert", "Napoléon", "Adam Smith"], 0,
                "**Luca Pacioli**, moine et mathématicien italien, formalise la partie double en 1494."),
            qcm("Quel texte de 1673 donne un caractère de preuve aux documents comptables ?", ["Le Code Colbert", "Le Code civil", "Le Code de commerce", "Le Plan comptable général"], 0,
                "Le **Code Colbert** (ordonnance de 1673) introduit le « livre de comptes ». Le Code de commerce date de 1807."),
            qcm("Parmi ces personnes, lesquelles sont des utilisateurs de l'information comptable ?",
                ["Les créanciers (banques, fournisseurs)", "L'administration fiscale", "Les représentants des salariés", "Les concurrents uniquement"], [0, 1, 2],
                "Le cours cite : dirigeants, créanciers, actionnaires, administration fiscale et organismes sociaux, tribunaux de commerce, représentants des salariés.", niveau=2),
            vf("Une fois une écriture comptable validée, on peut la modifier librement si on s'est trompé.", False,
               "L'enregistrement doit être **ineffaçable** : on ne peut pas modifier une saisie validée (on passe une écriture de correction)."),
            qcm("Pourquoi la comptabilité analytique ne peut-elle pas évaluer ses flux par un prix de marché ?",
                ["Parce que les flux internes ne sont pas échangés contre de l'argent", "Parce qu'elle est facultative", "Parce qu'elle ne concerne que les services", "Parce qu'elle est tenue par l'État"], 0,
                "Les flux physiques internes ne sont **pas échangés contre des flux monétaires** : il n'existe pas de prix pour les évaluer objectivement.", niveau=2),
            courte("Donne la définition de la comptabilité vue en cours.",
                   "Un système d'information qui donne une image de l'entreprise à travers ses opérations susceptibles d'une représentation monétaire.",
                   "Mots-clés : **système d'information**, **image de l'entreprise**, **représentation monétaire**."),
            courte("Cite les 4 caractéristiques qui font de la comptabilité financière une preuve des opérations commerciales.",
                   "1) Saisie chronologique et ineffaçable ; 2) pas de modification après validation ; 3) chaque information est justifiée par une pièce (facture, relevé, contrat) ; 4) terminologie et documents communs à toutes les entreprises.", niveau=3),
        ])

    n2 = notion(
        'principes', 'Réglementation et principes comptables',
        "La comptabilité obéit à des **normes** (Code de commerce, décret comptable, **PCG** en France ; **IAS/IFRS** pour les comptes consolidés des sociétés cotées de l'UE) et à des **principes comptables**.",
        [
            "**Normes françaises** : principes et plan de comptes ; documents obligatoires (journal, grand livre, inventaire) ; fonctionnement des comptes et documents annuels (**bilan, compte de résultat, annexe**) ; méthodes d'évaluation.",
            "**Principes de mesure** : **monétarisation** (tout est exprimé en monnaie), **coûts historiques** (les biens sont enregistrés à leur coût d'acquisition), **prudence** (ne pas surévaluer les actifs ni sous-évaluer les dettes).",
            "**Principes d'observation** : **entité** (l'entreprise est distincte de ses propriétaires), **séparation (indépendance) des exercices**, **continuité de l'exploitation**, **permanence des méthodes**.",
            "**Qualités de l'information** : **régularité et sincérité**, **image fidèle**.",
        ],
        [
            qcm("Le principe selon lequel un bien est enregistré à son coût d'acquisition s'appelle :", ["Principe des coûts historiques", "Principe de prudence", "Principe de permanence des méthodes", "Principe de l'entité"], 0,
                "**Coûts historiques** : les biens sont inscrits à leur valeur d'entrée (coût d'acquisition), même si leur valeur de marché change."),
            qcm("Quel principe interdit de mélanger le patrimoine personnel de l'exploitant et celui de l'entreprise ?", ["Principe de l'entité", "Principe de prudence", "Principe de monétarisation", "Principe de continuité"], 0,
                "**Principe de l'entité** : l'entreprise est une entité distincte de ses propriétaires."),
            qcm("Classe ces principes : lesquels sont des **principes d'observation** ?",
                ["Séparation des exercices", "Continuité de l'exploitation", "Permanence des méthodes", "Prudence"], [0, 1, 2],
                "Principes d'observation : entité, séparation des exercices, continuité de l'exploitation, permanence des méthodes. La **prudence** est un principe de **mesure**.", niveau=2),
            vf("Les normes IAS/IFRS s'appliquent aux comptes consolidés des sociétés cotées dans l'Union européenne.", True,
               "Les normes **IAS/IFRS** ont un contenu similaire aux normes françaises et s'appliquent aux **comptes consolidés des sociétés cotées** de l'UE."),
            vf("Le principe de prudence autorise à surévaluer légèrement les actifs pour donner une image positive.", False,
               "C'est l'inverse : la **prudence** interdit de surévaluer les actifs (et les produits) et de sous-évaluer les dettes (et les charges)."),
            qcm("Quels sont les trois documents annuels (comptes annuels) ?", ["Bilan, compte de résultat, annexe", "Journal, grand livre, balance", "Bilan, journal, inventaire", "Facture, avoir, relevé"], 0,
                "Les **comptes annuels** = bilan + compte de résultat + annexe. Journal, grand livre et inventaire sont des documents **obligatoires** de tenue.", niveau=2),
            qcm("Une entreprise change chaque année sa méthode d'évaluation des stocks pour améliorer son résultat. Quel principe ne respecte-t-elle pas ?",
                ["Permanence des méthodes", "Monétarisation", "Entité", "Coûts historiques"], 0,
                "La **permanence des méthodes** impose d'utiliser les mêmes méthodes d'un exercice à l'autre pour que les comptes soient comparables.", niveau=2),
            courte("Explique le principe de séparation (indépendance) des exercices.",
                   "Chaque exercice (en général un an) doit supporter uniquement les charges et produits qui le concernent : on rattache les opérations à l'exercice auquel elles appartiennent.", niveau=3),
            courte("Cite les deux qualités de l'information comptable vues en cours.", "Régularité et sincérité ; image fidèle.", niveau=2),
        ])

    n3 = notion(
        'flux', 'Les flux : sens, nature, ressources et emplois',
        "Un **flux** est un mouvement de valeur entre deux agents (ou à l'intérieur de l'entreprise). Il a une **origine** (ressource) et une **destination** (emploi).",
        [
            "**Sens** : flux **sortant** (part de l'entreprise) ou **entrant** (arrive dans l'entreprise).",
            "**Flux réels** : mouvements de biens et services. **Flux financiers** : le plus souvent la contrepartie des flux réels — **monétaires** (argent) ou **quasi-monétaires** (délais de paiement : créances, dettes).",
            "Flux **internes** (à l'entreprise) ou **externes** (avec les partenaires).",
            "Le **flux** est égal à la **variation du stock** entre deux dates : un stock se constitue dès que les entrées et sorties sont inégales.",
            "Point de départ = **ressource** (patrimoniale : moyen de financement ; d'exploitation : richesse créée). Point d'arrivée = **emploi** (patrimonial : acquisition ; d'exploitation : emploi définitif ; d'autofinancement).",
        ],
        [
            qcm("Une entreprise reçoit des marchandises de son fournisseur. Pour l'entreprise, il s'agit d'un :", ["Flux réel entrant", "Flux réel sortant", "Flux financier entrant", "Flux financier sortant"], 0,
                "Des marchandises = un **bien** → flux **réel** ; elles arrivent dans l'entreprise → flux **entrant**."),
            qcm("L'entreprise paie son fournisseur par virement. Pour l'entreprise, il s'agit d'un :", ["Flux financier sortant", "Flux réel sortant", "Flux financier entrant", "Flux réel entrant"], 0,
                "De l'argent quitte l'entreprise : flux **financier (monétaire) sortant**, contrepartie du flux réel d'achat."),
            qcm("Une vente à crédit (paiement à 30 jours) crée un flux :", ["Quasi-monétaire", "Monétaire", "Interne", "Réel uniquement"], 0,
                "Le **délai de paiement** (créance client) est un flux **quasi-monétaire**.", niveau=2),
            vf("Le point de départ d'un flux s'appelle un emploi.", False, "Le point de **départ** est la **ressource** ; le point d'**arrivée** est l'**emploi**."),
            calc("Le stock de marchandises était de 4 000 € au 1er janvier. Pendant l'année, les entrées s'élèvent à 25 000 € et les sorties à 23 500 €. Quel est le stock au 31 décembre ?", 5500,
                 "Stock final = stock initial + entrées − sorties = 4 000 + 25 000 − 23 500 = **5 500 €**. La variation (+1 500 €) correspond à l'écart entre flux d'entrée et de sortie.", niveau=2),
            vf("Un flux est égal à la variation du montant d'un stock entre deux dates.", True, "C'est la relation **flux / stock** vue en cours : un stock se constitue dès que les flux d'entrée et de sortie sont inégaux."),
            qcm("Le transfert de matières premières de l'entrepôt vers l'atelier de fabrication est un flux :", ["Interne", "Externe", "Financier", "Quasi-monétaire"], 0,
                "Il a lieu **à l'intérieur** de l'entreprise : c'est un flux **interne** (suivi par la comptabilité analytique).", niveau=2),
            courte("Dans une vente au comptant, décris les deux flux qui circulent entre l'entreprise et son client.",
                   "Un flux réel (les marchandises) va de l'entreprise vers le client ; en contrepartie, un flux financier (l'argent) va du client vers l'entreprise.", niveau=2),
        ])
    return chapitre('ch-intro', 'Introduction : à quoi sert la comptabilité ?', [n1, n2, n3])


# ---------------------------------------------------------------- CH 1 BILAN
def ch1():
    n4 = notion(
        'bilan-approches', 'Le bilan : approche patrimoniale et approche fonctionnelle',
        "Le **bilan** est un document comptable normalisé qui exprime, **à une date donnée**, la situation patrimoniale de l'entreprise : c'est une **photographie** du patrimoine.",
        [
            "**Approche patrimoniale** : **actifs** = éléments à valeur économique positive (biens, créances) ; **passifs externes** = dettes ; **capitaux propres** = valeur nette du patrimoine.",
            "**Capitaux propres (situation nette) = Actif − Dettes** (avoirs − dettes).",
            "**Approche fonctionnelle** : le **passif** montre l'**origine des ressources** (apports/capital = ressources permanentes ; dettes = ressources temporaires ; bénéfices = ressources générées par l'activité) ; l'**actif** montre leur **emploi** (emplois permanents liés à l'investissement ; emplois temporaires liés à l'exploitation : stocks, créances, liquidités).",
            "**Emplois = Ressources** : le bilan est toujours **équilibré** (total actif = total passif).",
        ],
        [
            calc("Une entreprise possède 85 000 € d'actifs et doit 32 000 € à ses créanciers. Quel est le montant de ses capitaux propres ?", 53000,
                 "Capitaux propres = Actif − Dettes = 85 000 − 32 000 = **53 000 €**.", niveau=1),
            vf("Le bilan décrit l'activité de l'entreprise pendant toute l'année.", False,
               "Le bilan est une **photographie à une date donnée**. C'est le **compte de résultat** qui est le « film » de l'activité de l'année."),
            qcm("Dans l'approche fonctionnelle, le passif du bilan représente :", ["L'origine des ressources", "L'emploi des ressources", "Les charges de l'exercice", "Les biens de l'entreprise"], 0,
                "Passif = **origine des ressources** (d'où vient l'argent) ; actif = **emploi des ressources** (ce qu'on en a fait)."),
            qcm("Lesquels sont des emplois **temporaires** (liés au cycle d'exploitation) ?", ["Les stocks", "Les créances clients", "Les liquidités", "Les constructions"], [0, 1, 2],
                "Emplois temporaires : stocks, créances, liquidités. Les constructions sont un emploi **permanent** (cycle d'investissement).", niveau=2),
            calc("Les capitaux propres d'une entreprise s'élèvent à 120 000 € et ses dettes à 45 000 €. Quel est le total de son actif ?", 165000,
                 "Actif = Capitaux propres + Dettes = 120 000 + 45 000 = **165 000 €** (total actif = total passif).", niveau=2),
            vf("Les capitaux propres peuvent être négatifs.", True,
               "Si les dettes dépassent les actifs (pertes accumulées), la situation nette est **négative** : l'entreprise ne pourrait pas rembourser toutes ses dettes en vendant ses actifs.", niveau=2),
            calc("Mme Gisèle possède : matériel 20 000 €, marchandises 23 200 €, créances clients 3 000 €, banque 3 400 €, caisse 500 €. Elle doit 19 000 € aux fournisseurs, 7 400 € à l'administration fiscale et 10 000 € d'emprunt. Son apport initial (capital) est de 10 000 €. Quel est son résultat du trimestre ?", 3700,
                 "Actif = 20 000 + 23 200 + 3 000 + 3 400 + 500 = 50 100 €. Dettes = 19 000 + 7 400 + 10 000 = 36 400 €. Capitaux propres = 50 100 − 36 400 = 13 700 €. Résultat = 13 700 − capital 10 000 = **3 700 €** (bénéfice). *(TD 1, ex. 3)*", niveau=3),
            courte("Explique pourquoi le bilan est toujours équilibré.",
                   "Parce que tout ce que l'entreprise possède (actif = emplois) a forcément été financé par une ressource (passif = capitaux propres + dettes) : emplois = ressources. Les capitaux propres sont d'ailleurs calculés comme actif − dettes.", niveau=2),
        ])

    boris = tab(['Élément', 'Montant (€)'], [
        ['Stocks de matières premières', 2500], ['Stocks de produits finis', 5070], ['Emprunt bancaire', 10000], ['Fournisseurs', 11267],
        ['Mobilier', 1970], ['Matériel de bureau et informatique', 9626], ['Découvert bancaire', 3252], ['Caisse', 251],
        ['Compte courant Banque Postale', 492], ['Prêt sur 2 ans accordé à un client', 2000], ['Clients', 16104], ['Local (atelier)', 160000],
        ['Droit au bail', 3000], ['Actions (placement à long terme)', 651], ['Résultat', -22855], ['Capital', 200000]], 'Société Boris au 31/12/N (TD 1, ex. 1)')
    n5 = notion(
        'bilan-structure', 'Structure du bilan et construction d\'un bilan',
        "Le bilan se présente en deux colonnes : **Actif** (emploi des ressources) à gauche, **Passif** (origine des ressources) à droite, chacune classée dans un ordre normalisé.",
        [
            "**Actif immobilisé** (biens durables, > 1 an) : immobilisations **incorporelles** (droit au bail, brevets, fonds commercial), **corporelles** (terrains, constructions, matériel, mobilier), **financières** (titres de participation, prêts accordés, dépôts et cautionnements).",
            "**Actif circulant** : **stocks**, **créances** (clients…), **VMP** (valeurs mobilières de placement), **disponibilités** (banque, caisse), charges constatées d'avance.",
            "**Capitaux propres** : capital, réserves, **résultat de l'exercice** (négatif en cas de perte).",
            "**Provisions pour risques et charges**, puis **dettes** : financières (emprunts, **découvert bancaire**), d'exploitation (fournisseurs, dettes fiscales et sociales), autres dettes, produits constatés d'avance.",
            "Une **perte** se place dans les capitaux propres **en négatif** (et non à l'actif).",
        ],
        [
            qcm("Où se place un découvert bancaire dans le bilan ?", ["Au passif, dans les dettes financières", "À l'actif, dans les disponibilités", "Au passif, dans les capitaux propres", "À l'actif, dans les créances"], 0,
                "Un découvert est une **dette envers la banque** : passif, dettes financières."),
            qcm("Un prêt de 2 ans accordé par l'entreprise à un client est classé en :", ["Immobilisations financières", "Créances clients", "Dettes financières", "Disponibilités"], 0,
                "L'entreprise **prête** de l'argent à long terme : c'est un emploi durable → **immobilisation financière** (compte 274 Prêts).", niveau=2),
            qcm("Le droit au bail est une immobilisation :", ["Incorporelle", "Corporelle", "Financière", "Ce n'est pas une immobilisation"], 0,
                "Le droit au bail est un droit sans substance physique : immobilisation **incorporelle**."),
            calc("Avec les données de la société Boris, calcule le total de l'**actif immobilisé**.", 177247,
                 "Droit au bail 3 000 + local 160 000 + mobilier 1 970 + matériel 9 626 (corporelles) + prêt 2 000 + actions LT 651 (financières) = **177 247 €**.", niveau=2, tableau=boris),
            calc("Toujours pour Boris, calcule le total de l'**actif circulant**.", 24417,
                 "Stocks MP 2 500 + stocks PF 5 070 + clients 16 104 + Banque Postale 492 + caisse 251 = **24 417 €**. Le découvert n'est **pas** à l'actif (c'est une dette).", niveau=2, tableau=boris),
            calc("Toujours pour Boris, quel est le montant des **capitaux propres** ?", 177145,
                 "Capital 200 000 + résultat (−22 855) = **177 145 €**. La perte vient en diminution des capitaux propres.", niveau=2, tableau=boris),
            calc("Toujours pour Boris, quel est le **total du bilan** ?", 201664,
                 "Actif = 177 247 + 24 417 = 201 664 €. Passif = capitaux propres 177 145 + dettes (emprunt 10 000 + fournisseurs 11 267 + découvert 3 252 = 24 519) = **201 664 €** ✓.", niveau=3, tableau=boris),
            calc("M. Bricolo apporte 100 000 € déposés en banque, emprunte 50 000 €, verse un dépôt de garantie de 8 200 €, achète une machine 210 000 € (70 000 € payés par chèque, solde à crédit) et un camion 60 000 € (10 % payés par chèque, le reste financé par un crédit BNP). Quel est le montant de ses **disponibilités** ?", 65800,
                 "100 000 + 50 000 − 8 200 − 70 000 − 6 000 = **65 800 €**. *(TD 1, ex. 4)*", niveau=3),
            calc("Pour M. Bricolo (question précédente), quel est le **total de ses dettes** ?", 244000,
                 "Emprunt Crédit agricole 50 000 + dette fournisseur d'immobilisation (210 000 − 70 000 = 140 000) + crédit BNP (60 000 × 90 % = 54 000) = **244 000 €**. Bilan : actif = dépôt 8 200 + machine 210 000 + camion 60 000 + banque 65 800 = 344 000 = capital 100 000 + dettes 244 000 ✓.", niveau=3),
        ],
        tableau=tab(['ACTIF (emplois)', 'PASSIF (ressources)'], [
            ['**Actif immobilisé** : incorporel, corporel, financier', '**Capitaux propres** : capital, réserves, résultat'],
            ['**Actif circulant** : stocks, créances, VMP, disponibilités', '**Provisions** pour risques et charges'],
            ['', '**Dettes** : financières, d\'exploitation, autres'],
            ['**Total actif**', '**Total passif** (= total actif)']]),
        exemple="Le 2/01/N, trois associés créent la librairie « Lire » et apportent : mobilier 8 000 €, rayonnages 16 200 €, matériel informatique 12 600 €, stock de livres 12 000 €, banque 1 200 €.\nActif immobilisé = 36 800 € ; actif circulant = 13 200 € ; total actif 50 000 € = capital 50 000 €.")
    return chapitre('ch-bilan', 'Chapitre 1 — Le bilan, photographie comptable du patrimoine', [n4, n5])


# ---------------------------------------------------------------- CH 2 COMPTE DE RESULTAT
def ch2():
    lire = tab(['Élément', 'Montant (€)'], [['Chiffre d\'affaires', 35000], ['Achats de livres', 15000], ['Fournitures et services consommés', 4800],
                                        ['Charges de personnel', 6960], ['Intérêts du découvert bancaire', 120], ['Stock initial de livres', 12000], ['Stock final de livres', 9500]],
               'Société « Lire », exercice N')
    n6 = notion(
        'compte-resultat', 'Charges, produits et structure du compte de résultat',
        "Le **compte de résultat** est le « **film** » de l'activité : il récapitule les **charges** et les **produits** de l'exercice. **Résultat = Produits − Charges** (bénéfice si positif, perte si négatif).",
        [
            "**Charges** : emplois définitifs, sources d'**appauvrissement** ; elles diminuent le résultat.",
            "**Produits** : ressources internes, sources d'**enrichissement** ; ils augmentent le résultat.",
            "**Exploitation** : achats de marchandises et MP, **variation de stock**, impôts et taxes, salaires et charges sociales, dotations / ventes, production vendue, stockée, immobilisée, reprises.",
            "**Financier** : intérêts (charges) ; produits des participations, revenus des VMP (produits).",
            "**Exceptionnel** : pénalités, amendes (charges) ; cessions d'éléments d'actif (produits). Puis participation des salariés et **impôt sur les bénéfices**.",
            "**Variation de stock de marchandises = stock initial − stock final** (en charges) : si le stock baisse, on a consommé plus que ce qu'on a acheté.",
        ],
        [
            vf("Une charge diminue le résultat de l'entreprise.", True, "Les charges sont des emplois définitifs, source d'**appauvrissement**."),
            qcm("Des intérêts payés sur un emprunt sont des :", ["Charges financières", "Charges d'exploitation", "Charges exceptionnelles", "Produits financiers"], 0,
                "Les intérêts versés sont des **charges financières** (compte 661)."),
            qcm("Une amende payée par l'entreprise est une :", ["Charge exceptionnelle", "Charge d'exploitation", "Charge financière", "Diminution du capital"], 0,
                "Pénalités et amendes : **charges exceptionnelles** (67).", niveau=1),
            calc("Société « Lire » : calcule la **variation de stock** de livres (à inscrire en charges).", 2500,
                 "Variation de stock = stock initial − stock final = 12 000 − 9 500 = **2 500 €**. Le stock a diminué : on a vendu des livres achetés l'année précédente, ce qui augmente les charges.", niveau=2, tableau=lire),
            calc("Société « Lire » : calcule le total des **charges d'exploitation**.", 29260,
                 "Achats 15 000 + variation de stock 2 500 + fournitures et services 4 800 + personnel 6 960 = **29 260 €**. Les intérêts (120 €) sont des charges **financières**.", niveau=2, tableau=lire),
            calc("Société « Lire » : calcule le **résultat** de l'exercice.", 5620,
                 "Produits = 35 000. Charges = 29 260 (exploitation) + 120 (financières) = 29 380. Résultat = 35 000 − 29 380 = **5 620 € (bénéfice)**.", niveau=3, tableau=lire),
            qcm("La société Amada (TD 1, ex. 5) a réalisé ces opérations. Lesquelles n'ont **aucune incidence** sur le résultat ?",
                ["Achat d'un mobilier de bureau 5 000 €", "Remboursement d'une partie de l'emprunt 3 000 €", "Paiement des intérêts de l'emprunt 1 500 €", "Versement du loyer 4 000 €"], [0, 1],
                "L'achat de mobilier est un **investissement** (actif du bilan) et le remboursement d'emprunt diminue une **dette** : aucun des deux n'est une charge. Les intérêts et le loyer sont des charges.", niveau=2),
            calc("Société Amada : charges = achats 70 000, publicité 2 000, fournitures 4 000, assurances 2 500, salaires 30 000, intérêts 1 500, téléphone 3 500, garagiste 2 500, taxes 300, loyer 4 000. Produits = ventes 140 000, produit exceptionnel 300. Quel est le résultat du semestre ?", 20000,
                 "Charges = 120 300 € ; produits = 140 300 € ; résultat = **20 000 €** (bénéfice). Le mobilier (5 000) et le remboursement d'emprunt (3 000) sont exclus.", niveau=3),
        ],
        tableau=tab(['CHARGES', 'PRODUITS'], [
            ['**D\'exploitation** : achats, variation de stock, impôts et taxes, salaires et charges sociales, dotations', '**D\'exploitation** : ventes de marchandises, production vendue, stockée, immobilisée, reprises'],
            ['**Financières** : intérêts', '**Financiers** : produits des participations, revenus des VMP'],
            ['**Exceptionnelles** : pénalités, amendes', '**Exceptionnels** : cessions d\'éléments d\'actif'],
            ['Participation des salariés, impôt sur les bénéfices', ''],
            ['**Résultat : bénéfice** (solde si produits > charges)', '**Résultat : perte** (solde si charges > produits)']]))

    n7 = notion(
        'variation-patrimoine', 'D\'un bilan à l\'autre : la variation du patrimoine',
        "Chaque opération modifie le bilan. Le **résultat** mesure à la fois l'enrichissement de l'activité (compte de résultat) et la **variation des capitaux propres** entre deux bilans (hors apports).",
        [
            "**Apports** : le capital apporté figure au **passif** et, à l'actif, selon sa nature (immobilisations, disponibilités).",
            "**Emprunt** : dette au passif + augmentation des disponibilités à l'actif.",
            "**Investissement** : immobilisation à l'actif au prix d'achat. Payé **au comptant** → les disponibilités baissent (total inchangé) ; **à crédit** → dette fournisseur d'immobilisation au passif.",
            "**Achat de marchandises** : le stock augmente à l'actif ; contrepartie : baisse des disponibilités ou dette fournisseur.",
            "**Vente** : les disponibilités (ou créances clients) augmentent du **prix de vente**, le stock baisse du **prix d'achat** ; la différence (marge) augmente le **résultat** dans les capitaux propres.",
            "**Résultat = Capitaux propres fin − Capitaux propres début** (s'il n'y a eu ni apport ni retrait).",
        ],
        [
            qcm("Une entreprise achète un ordinateur à crédit. Effet sur le bilan :", ["L'actif et le passif augmentent du même montant", "L'actif augmente, le passif ne change pas", "L'actif ne change pas", "Les capitaux propres augmentent"], 0,
                "Immobilisation à l'actif (+) et dette fournisseur d'immobilisation au passif (+) : le bilan reste équilibré."),
            qcm("Une entreprise achète une machine au comptant (par banque). Effet sur le total du bilan :", ["Il reste inchangé", "Il augmente", "Il diminue", "Il double"], 0,
                "Une immobilisation augmente et les disponibilités diminuent du même montant : **le total de l'actif reste inchangé**."),
            vf("Le remboursement d'une partie d'un emprunt diminue le résultat.", False,
               "Le remboursement du capital diminue la **dette** (passif) et la **banque** (actif) : aucun effet sur le résultat. Seuls les **intérêts** sont une charge."),
            calc("M. Virenque achète 50 vélos à 180 € pièce et en revend 35 à 300 € pièce au comptant. Quel est l'enrichissement (marge) réalisé sur ces ventes ?", 4200,
                 "Prix de vente 35 × 300 = 10 500 € ; coût d'achat des vélos vendus 35 × 180 = 6 300 € ; marge = **4 200 €**, qui augmente le résultat.", niveau=2),
            calc("Pour M. Virenque, quelle est la valeur du stock de vélos après ces ventes ?", 2700,
                 "Il reste 50 − 35 = 15 vélos à 180 € = **2 700 €** (le stock est évalué au **prix d'achat**).", niveau=2),
            calc("Société Sylvain : au 31/12/N, actif = 2 555 000 € et dettes = 740 000 €. Le capital apporté à la création était de 1 500 000 €. Quel est le résultat de l'exercice N ?", 315000,
                 "Capitaux propres = 2 555 000 − 740 000 = 1 815 000 €. Résultat = 1 815 000 − 1 500 000 = **315 000 €**. *(TD 1, ex. 2)*", niveau=3),
            calc("Société Sylvain : au 31/12/N+1, actif = 2 840 000 € et dettes = 730 000 €. Sachant que les capitaux propres étaient de 1 815 000 € fin N (sans nouvel apport), quel est le résultat N+1 ?", 295000,
                 "Capitaux propres N+1 = 2 840 000 − 730 000 = 2 110 000 €. Résultat N+1 = 2 110 000 − 1 815 000 = **295 000 €**.", niveau=3),
            courte("Pourquoi une vente avec bénéfice augmente-t-elle les capitaux propres ?",
                   "Parce que l'actif augmente du prix de vente (banque ou créance) mais ne diminue que du coût d'achat (stock) : la différence (la marge) est un enrichissement qui s'ajoute au résultat, donc aux capitaux propres.", niveau=2),
        ],
        exemple="Supercycle : apport 30 000 € (terrain 20 000 + banque 10 000), emprunt 58 000 €, magasin 60 000 € au comptant, mobilier 1 000 € et ordinateur 2 000 € à crédit.\nBilan : terrain 20 000 + magasin 60 000 + mobilier 1 000 + ordinateur 2 000 + banque 8 000 = 91 000 € = capital 30 000 + emprunt 58 000 + dettes fournisseurs d'immobilisations 3 000.")
    return chapitre('ch-resultat', 'Chapitre 2 — Le compte de résultat, film comptable de l\'activité', [n6, n7])


# ---------------------------------------------------------------- CH 3 LE COMPTE
def ch3():
    caisse = tab(['Débit (entrées)', 'Crédit (sorties)'], [[1000, 1000], [500, 750], [3000, 750]], 'Compte 531 Caisse')
    n8 = notion(
        'compte', 'La notion de compte : solde, clôture, réouverture',
        "Un **compte** est un tableau à deux colonnes qui enregistre les mouvements d'un élément : **débit** à gauche, **crédit** à droite (« compte en T »).",
        [
            "**Solde** = différence entre total débit et total crédit. **Solde débiteur (SD)** si débit > crédit ; **solde créditeur (SC)** si crédit > débit ; **soldé** (nul) si égalité.",
            "**Clôture** : on inscrit le solde du côté le plus faible pour que les deux colonnes aient le même total.",
            "**Réouverture** : le solde est reporté du côté d'origine au début de la période suivante.",
            "Comptes d'**actif** : solde normalement **débiteur**. Comptes de **passif** : solde normalement **créditeur**.",
            "La **caisse** ne peut jamais être créditrice (on ne peut pas sortir plus d'espèces qu'il n'y en a) ; la **banque** peut l'être (découvert).",
        ],
        [
            calc("Compte caisse : débit 1 000 ; 500 ; 3 000 — crédit 1 000 ; 750 ; 750. Quel est le solde ?", 2000,
                 "Total débit 4 500 − total crédit 2 500 = **solde débiteur de 2 000 €**.", niveau=1, tableau=caisse),
            qcm("Un compte dont le total crédit dépasse le total débit présente un :", ["Solde créditeur", "Solde débiteur", "Solde nul", "Compte en déséquilibre"], 0,
                "Crédit > débit → **solde créditeur**."),
            vf("Le compte Caisse peut présenter un solde créditeur.", False,
               "Impossible : on ne peut pas sortir de la caisse plus d'espèces qu'elle n'en contient. Un solde créditeur révèle une erreur. *(TD 2, ex. 1)*"),
            vf("Le compte Banque peut présenter un solde créditeur.", True,
               "Oui : un solde créditeur du compte 512 signifie un **découvert bancaire** (la banque prête de l'argent à l'entreprise)."),
            qcm("À la clôture, où inscrit-on le solde débiteur d'un compte ?", ["Au crédit, pour équilibrer les colonnes", "Au débit", "Nulle part", "Dans un autre compte"], 0,
                "On inscrit le solde du **côté le plus faible** (le crédit pour un solde débiteur) afin que les deux totaux soient égaux. À la réouverture, il repasse au débit.", niveau=2),
            calc("Compte 401 Fournisseurs : crédit 3 600 ; 1 200 ; 840 — débit 3 600 ; 500. Quel est le montant du solde (créditeur) ?", 1540,
                 "Crédit 5 640 − débit 4 100 = **solde créditeur 1 540 €** : l'entreprise doit encore 1 540 € à ses fournisseurs.", niveau=2),
            vf("Un compte client (411) présente normalement un solde créditeur lorsque le client me doit de l'argent.", False,
               "Une créance est un actif : le compte 411 est **débiteur** quand le client me doit de l'argent. *(Quiz du cours)*", niveau=2),
            calc("Compte banque au 1/10 : solde débiteur 2 000 €. Mouvements : virement charges locatives −1 800 ; chèque client +200 ; ventes CB +1 300 ; retrait d'espèces −300 ; chèque mobilier −1 200 ; frais de tenue de compte −8. Quel est le solde final ?", 192,
                 "2 000 − 1 800 + 200 + 1 300 − 300 − 1 200 − 8 = **192 € (solde débiteur)**. *(TD 2, ex. 1 — Haddock)*", niveau=3),
        ])

    n9 = notion(
        'pcg', 'Le Plan Comptable Général (PCG)',
        "Le **PCG** classe tous les comptes par un **numéro** dont le premier chiffre indique la **classe**. Plus le numéro est long, plus le compte est détaillé (6 → 60 → 607).",
        [
            "**Comptes de bilan** : classe **1** capitaux (capital 101, réserves 106, résultat 120/129, emprunts 164) ; **2** immobilisations ; **3** stocks ; **4** tiers (401 fournisseurs, 411 clients, 421 personnel, 445 État-TVA) ; **5** financiers (512 banque, 53 caisse, 50 VMP).",
            "**Comptes de gestion** : classe **6** charges ; classe **7** produits. (Classe 8 : comptes spéciaux.)",
            "Exploitation : charges **60 à 65** (+681), produits **70 à 75** (+781). Financier : **66** / **76**. Exceptionnel : **67** / **77**.",
            "Bénéfice : compte **120** ; perte : compte **129**.",
        ],
        [
            qcm("À quelle classe appartient le compte 411 Clients ?", ["Classe 4 : comptes de tiers", "Classe 1 : capitaux", "Classe 5 : comptes financiers", "Classe 7 : produits"], 0, "Clients, fournisseurs, État, personnel = **classe 4 (tiers)**."),
            qcm("Quel compte enregistre les ventes de marchandises ?", ["707", "607", "411", "701"], 0, "**707** Ventes de marchandises ; 701 = ventes de produits finis ; 607 = achats de marchandises."),
            qcm("Le compte 512 est le compte :", ["Banque", "Caisse", "Capital", "Clients"], 0, "**512 Banque** (classe 5, comptes financiers). La caisse est le 53 (531)."),
            qcm("Les comptes 66 et 76 regroupent :", ["Les charges et produits financiers", "Les charges et produits exceptionnels", "Les charges de personnel", "Les immobilisations"], 0, "66 = charges **financières**, 76 = produits **financiers** ; 67/77 = exceptionnel."),
            qcm("Quels comptes sont des comptes de **bilan** ?", ["213 Constructions", "164 Emprunts", "370 Stock de marchandises", "641 Rémunérations du personnel"], [0, 1, 2],
                "Classes 1 à 5 = bilan. Le 641 (classe 6) est un compte de **gestion** (charge).", niveau=2),
            qcm("Dans quel compte enregistre-t-on une perte de l'exercice ?", ["129", "120", "101", "661"], 0, "**120** = résultat bénéficiaire ; **129** = résultat déficitaire (perte).", niveau=2),
            qcm("Le compte 2184 (Mobilier) est :", ["Une immobilisation corporelle", "Une immobilisation incorporelle", "Un stock", "Une charge"], 0, "Classe 2 = immobilisations ; 21 = **corporelles** (terrains 211, constructions 213, matériel 215, autres 218).", niveau=2),
            vf("Les comptes de la classe 3 enregistrent les stocks.", True, "Classe 3 : stocks et en-cours (ex. 370 stock de marchandises)."),
            courte("Cite les 7 classes de comptes du PCG utilisées en comptabilité générale.",
                   "1 Capitaux ; 2 Immobilisations ; 3 Stocks et en-cours ; 4 Tiers ; 5 Financiers ; 6 Charges ; 7 Produits.", niveau=2),
        ])

    n10 = notion(
        'partie-double', 'La partie double et la double détermination du résultat',
        "Toute opération est enregistrée dans **au moins deux comptes** : un **emploi** au **débit**, une **ressource** au **crédit**, pour le même montant. **Emploi = Ressource ⇔ Débit = Crédit**.",
        [
            "La **ressource** est l'**origine** du flux (moyen de financement) → **crédit** (partie droite).",
            "L'**emploi** est la **destination** du flux (utilisation du financement) → **débit** (partie gauche).",
            "**Actif et charges** (emplois) : augmentent au **débit**, diminuent au **crédit**.",
            "**Passif et produits** (ressources) : augmentent au **crédit**, diminuent au **débit**.",
            "Pour chaque opération : total débit = total crédit ; donc pour l'ensemble : total des débits = total des crédits.",
            "**Double détermination du résultat** : Résultat = Produits − Charges = Actif − Passif (externe et capital) ⇒ **Charges + Actif = Produits + Passif**.",
        ],
        [
            ecr("Vente de marchandises pour 700 € réglée par chèque bancaire (sans TVA).",
                [D('banque', 'Banque', 700), C('ventm', 'Ventes de marchandises', 700)],
                "La ressource est la vente (produit : **crédit 707**) ; l'emploi est l'encaissement (actif qui augmente : **débit 512**).", niveau=1),
            ecr("Achat de marchandises pour 300 € réglé par chèque bancaire (sans TVA).",
                [D('achm', 'Achats de marchandises', 300), C('banque', 'Banque', 300)],
                "L'achat est une charge (emploi → **débit 607**) ; le paiement diminue un actif (**crédit 512**).", niveau=1),
            qcm("Une augmentation d'un compte de passif s'enregistre :", ["Au crédit", "Au débit", "Au débit ou au crédit selon le montant", "Jamais"], 0, "Passif = ressource → **augmente au crédit**."),
            qcm("Une diminution d'un compte d'actif s'enregistre :", ["Au crédit", "Au débit", "Dans un compte de charges", "Au passif"], 0, "Actif = emploi : il augmente au débit et **diminue au crédit**."),
            vf("Les comptes de produits sont toujours crédités car ils enrichissent l'entreprise.", False,
               "Ils sont **normalement** crédités, mais on peut les débiter, par exemple pour annuler une vente (retour de marchandises, ristourne 709). *(Quiz du cours)*", niveau=2),
            vf("Une ressource est toujours un flux financier.", False, "Une ressource peut être un flux **réel** ou **financier** (ex. : la vente de marchandises est une ressource). *(Quiz du cours)*", niveau=2),
            ecr("L'exploitant apporte 20 000 € en espèces qu'il dépose sur le compte bancaire de l'entreprise à sa création.",
                [D('banque', 'Banque', 20000), C(['101', '108'], 'Capital', 20000)],
                "L'argent arrive en banque (**débit 512**) ; la ressource est l'apport de l'exploitant (**crédit 101 Capital**).", niveau=2),
            ecr("L'entreprise obtient un emprunt bancaire de 15 000 € versé sur son compte.",
                [D('banque', 'Banque', 15000), C(['164', '16'], 'Emprunts auprès des établissements de crédit', 15000)],
                "Les disponibilités augmentent (**débit 512**) ; la dette envers la banque est une ressource (**crédit 164**).", niveau=2),
            calc("Au cours d'un exercice : total des charges 80 000 €, total des produits 92 000 €. Au bilan de fin, quel montant apparaîtra dans le poste « résultat de l'exercice » ?", 12000,
                 "Résultat = produits − charges = 92 000 − 80 000 = **12 000 €** (bénéfice, compte 120). Le même montant est obtenu par actif − passif : c'est la double détermination du résultat.", niveau=2),
            vf("Le compte de résultat est un document indépendant du bilan.", False,
               "Les deux sont liés : le **résultat** du compte de résultat figure dans les **capitaux propres** du bilan (double détermination). *(Quiz du cours)*", niveau=2),
        ])
    return chapitre('ch-compte', 'Chapitre 3 — Le compte, outil d\'analyse des opérations', [n8, n9, n10])


# ---------------------------------------------------------------- CH 4 ORGANISATION
def ch4():
    n11 = notion(
        'journal', 'Le journal',
        "Le **journal** enregistre toutes les opérations dans l'**ordre chronologique**. C'est un document **obligatoire** qui peut servir de **preuve** devant un tribunal.",
        [
            "Il doit être tenu **sans blanc ni rature**.",
            "Pour chaque écriture : **date**, **numéros de comptes** (débités puis crédités), **libellé** de l'opération, **référence de la pièce justificative**, montants au débit et au crédit.",
            "Chaque écriture est **équilibrée** (total débit = total crédit).",
            "Les opérations en espèces passent par le **53 Caisse** ; par chèque, carte bancaire, virement ou prélèvement par le **512 Banque**.",
            "Comptes utiles : 606/6064 fournitures, 613 loyers, 614 charges locatives, 615 entretien et réparations, 616 assurances, 623 publicité, 626 frais postaux et télécommunications, 627 services bancaires, 641 salaires, 108 compte de l'exploitant (prélèvements personnels).",
        ],
        [
            ecr("1/10 : virement bancaire de 1 800 € pour les charges locatives du trimestre (sans TVA).",
                [D(['614', '613'], 'Charges locatives', 1800), C('banque', 'Banque', 1800)],
                "Charge (**débit 614** Charges locatives et de copropriété) payée par banque (**crédit 512**). *(TD 2, ex. 1)*", niveau=1),
            ecr("7/10 : retrait d'espèces de 300 € au distributeur pour alimenter la caisse.",
                [D('caisse', 'Caisse', 300), C('banque', 'Banque', 300)],
                "Simple **virement interne** de trésorerie : la caisse augmente (**débit 531**), la banque diminue (**crédit 512**). Aucun effet sur le résultat.", niveau=1),
            ecr("8/10 : facture du nouveau mobilier du magasin, 1 200 € payés par chèque (sans TVA).",
                [D(['2184', '218'], 'Mobilier', 1200), C('banque', 'Banque', 1200)],
                "Le mobilier est un bien durable : **immobilisation corporelle (2184)**, et non une charge.", niveau=2),
            ecr("8/10 : l'extrait de compte mentionne 8 € de frais de tenue de compte.",
                [D(['627', '6278'], 'Services bancaires', 8), C('banque', 'Banque', 8)],
                "Les frais bancaires sont une charge (**627 Services bancaires et assimilés**).", niveau=1),
            ecr("4 juin (boulangerie de M. Brun) : l'exploitant prélève 150 € dans la caisse pour ses besoins personnels.",
                [D('108', "Compte de l'exploitant", 150), C('caisse', 'Caisse', 150)],
                "Un prélèvement personnel n'est **pas une charge** de l'entreprise (principe de l'entité) : on débite le **108 Compte de l'exploitant**. *(TD 2, ex. 2)*", niveau=2),
            ecr("10/01 (agence Gulliver) : ventes de prestations au comptant, 2 500 € en espèces et 4 800 € par chèque (sans TVA).",
                [D('caisse', 'Caisse', 2500), D('banque', 'Banque', 4800), C(['706'], 'Prestations de services', 7300)],
                "Une écriture peut avoir plusieurs débits : caisse et banque ; le produit total (**706 Prestations de services**) est crédité de 7 300 €.", niveau=2),
            ecr("03/01 (Gulliver) : acquisition d'un ordinateur portable de 3 000 € à crédit (sans TVA).",
                [D(['2183', '218'], 'Matériel de bureau et informatique', 3000), C(['404'], "Fournisseurs d'immobilisations", 3000)],
                "Une immobilisation achetée à crédit crée une dette envers un **fournisseur d'immobilisations (404)**, distinct du 401 réservé aux achats courants.", niveau=2),
            ecr("Début novembre (Castafiore) : achat d'une voiture au comptant 11 000 € par virement (sans TVA).",
                [D(['2182', '218'], 'Matériel de transport', 11000), C('banque', 'Banque', 11000)],
                "Le véhicule est une **immobilisation corporelle (2182 Matériel de transport)**. *(TD 2, ex. 3)*", niveau=2),
            qcm("Quelles informations doivent figurer sur une écriture du journal ?", ["La date", "Les numéros des comptes", "La référence de la pièce justificative", "Le solde de chaque compte"], [0, 1, 2],
                "Date, comptes, libellé, pièce justificative, montants. Le **solde** des comptes se lit dans le **grand livre**, pas dans le journal.", niveau=2),
            courte("M. Brun, boulanger, enregistre le 2 juin ses ventes de la journée (450 €) et un pourboire de 1 € donné au livreur, tout en espèces. Explique la logique de ces deux écritures.",
                   "Ventes : débit 531 Caisse 450 / crédit 707 (ou 701) Ventes 450 — l'argent entre en caisse et la vente est un produit. Pourboire : débit 6238 Divers (pourboires, dons courants) 1 / crédit 531 Caisse 1 — c'est une charge payée en espèces.", niveau=3),
        ])

    # Castafiore : compte de résultat après opérations
    charges = {'602200 Fournitures consommables': 5676, '606000 Achats non stockés': 10914, '607000 Achats de marchandises': 43475 + 3000,
               '616000 Primes d\'assurances': 6400, '624000 Transport de biens': 894, '626000 Frais postaux et télécom.': 459 + 50,
               '627000 Services bancaires': 974, '635000 Impôts et taxes': 12450, '641000 Rémunération du personnel': 153300,
               '645000 Charges de SS': 60600, '661600 Intérêts bancaires': 2720}
    produits = {'706 Prestations de services': 258851, '707 Ventes de marchandises': 93476 + 800, '708 Produits des activités annexes': 7200, '765 Escomptes obtenus': 850}
    tc = sum(charges.values()); tp = sum(produits.values())
    gav = tab(['N°', 'Intitulé', 'Solde débiteur', 'Solde créditeur'], [
        ['101', 'Capital', '', 100000], ['164', 'Emprunts', '', 20000], ['211', 'Terrains', 27000, ''], ['213', 'Constructions', 40000, ''],
        ['2154', 'Matériels industriels', 49000, ''], ['274', 'Prêts', 1000, ''], ['401', 'Fournisseurs', '', 12000], ['411', 'Clients', 17000, ''],
        ['512', 'Banque', 2500, ''], ['530', 'Caisse', 500, ''], ['601', 'Achats de MP', 120000, ''], ['607', 'Achats de marchandises', 270000, ''],
        ['6242', 'Transports sur ventes', 32500, ''], ['630', 'Impôts et taxes', 30000, ''], ['640', 'Charges de personnel', 145000, ''],
        ['661', "Charges d'intérêts", 9000, ''], ['670', 'Charges exceptionnelles', 11000, ''], ['701', 'Ventes de produits finis', '', 310000],
        ['707', 'Ventes de marchandises', '', 290000], ['770', 'Produits exceptionnels', '', 22500]], 'Balance des Éts Gavroche au 31/12/N (TD 2, ex. 4)')
    n12 = notion(
        'grand-livre-balance', 'Le grand livre et la balance',
        "Le **grand livre** regroupe les mêmes mouvements que le journal, mais **triés par compte** (dans l'ordre du plan de comptes). La **balance** récapitule, pour chaque compte, les totaux et le **solde**.",
        [
            "**Grand livre** : obligatoire ; permet de connaître à tout instant les mouvements et le **solde** de chaque compte (on « reporte » le journal dans les comptes).",
            "**Balance** : pour chaque compte, solde de début, total des mouvements débit et crédit, solde de clôture.",
            "Contrôles de la balance : **total des débits = total des crédits** ; **total des mouvements de la balance = total du journal** ; **total des soldes débiteurs = total des soldes créditeurs**.",
            "Les **documents de synthèse** (bilan, compte de résultat) sont établis à partir de la balance : comptes de classes 1 à 5 → bilan ; classes 6 et 7 → compte de résultat.",
        ],
        [
            qcm("Le grand livre présente les opérations :", ["Classées par compte", "Classées par ordre chronologique", "Classées par montant", "Classées par client"], 0,
                "Le **journal** est chronologique ; le **grand livre** trie les mêmes mouvements **par compte**."),
            vf("Dans une balance correcte, le total des soldes débiteurs est égal au total des soldes créditeurs.", True, "C'est une conséquence de la partie double."),
            vf("Si la balance est équilibrée, il ne peut y avoir aucune erreur dans la comptabilité.", False,
               "Certaines erreurs n'empêchent pas l'équilibre : écriture oubliée, mauvais compte utilisé (ex. 606 au lieu de 607), montant erroné des deux côtés…", niveau=2),
            qcm("Le total des mouvements de la balance doit être égal :", ["Au total du journal", "Au total du bilan", "Au résultat", "Au solde de la banque"], 0, "Total des mouvements de la balance = **total du journal** (mêmes écritures, simplement reclassées)."),
            calc("Éts Gavroche : à partir de la balance, calcule le **résultat** de l'exercice.", 5000,
                 "Produits (701 + 707 + 770) = 310 000 + 290 000 + 22 500 = 622 500 €. Charges (601 + 607 + 6242 + 630 + 640 + 661 + 670) = 617 500 €. Résultat = **5 000 € (bénéfice)**.", niveau=3, tableau=gav),
            calc("Éts Gavroche : calcule le **total du bilan** (actif).", 137000,
                 "Actif = terrains 27 000 + constructions 40 000 + matériels 49 000 + prêts 1 000 + clients 17 000 + banque 2 500 + caisse 500 = **137 000 €**. Passif : capital 100 000 + résultat 5 000 + emprunts 20 000 + fournisseurs 12 000 = 137 000 ✓.", niveau=3, tableau=gav),
            calc("Entreprise Castafiore : après les opérations de novembre, le total des charges est de %s € et le total des produits de %s €. Quel est le résultat ?" % (f(tc), f(tp)), tp - tc,
                 "Résultat = produits − charges = %s − %s = **%s €** (bénéfice). *(TD 2, ex. 3)*" % (f(tp), f(tc), f(tp - tc)), niveau=2),
            calc("Castafiore : banque débitrice de 1 915 €. Opérations : règlement client +200 ; emprunt +10 000 ; vente par chèque +800 ; voiture par virement −11 000 ; téléphone par prélèvement −50. Solde final de la banque ?", 1865,
                 "1 915 + 200 + 10 000 + 800 − 11 000 − 50 = **1 865 € (solde débiteur)**. L'achat de marchandises à crédit ne touche pas la banque.", niveau=2),
            courte("Quelle est la différence entre le journal et le grand livre ?",
                   "Ils contiennent les mêmes mouvements : le journal les classe dans l'ordre chronologique (vue par date), le grand livre les classe par compte selon le plan comptable (vue par compte, avec le solde de chaque compte).", niveau=1),
        ])
    return chapitre('ch-organisation', 'Chapitre 4 — L\'organisation comptable', [n11, n12])
