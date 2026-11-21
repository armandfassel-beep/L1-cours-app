"""Microéconomie — Chapitres 1 (échange) et 2 (offre, demande, élasticité)."""
from macro_base import *


def chapitres():
    return [ch1(), ch2()]


def fpp_fig(titre, bmax_r, pmax_r, bmax_v, pmax_v, ar, av, xmax=12, ymax=22):
    """FPP de Robinson (R) et Vendredi (V) : poisson en abscisse, blé en ordonnée ; droite B = P ; points d'autarcie."""
    return fig('Poisson (P)', 'Blé (B)', xmax, ymax,
               [seg((0, bmax_r), (pmax_r, 0), 'FPP R', 1), seg((0, bmax_v), (pmax_v, 0), 'FPP V', 2), seg((0, 0), (min(xmax, ymax) * 0.95, min(xmax, ymax) * 0.95), 'B = P', 4, True)],
               titre=titre, points=[pt(ar, ar, 'R'), pt(av, av, 'V')], gradx=list(range(2, xmax + 1, 2)), grady=list(range(2, ymax + 1, 2)))


def ch1():
    prod1 = tab(['Productivité horaire', 'Blé (B)', 'Poisson (P)'], [['Robinson', 6, 2], ['Vendredi', 5, 5]], 'TD 1, parties I-II (2 heures de travail chacun)')
    prod3 = tab(['Productivité horaire', 'Blé (B)', 'Poisson (P)'], [['Robinson', 10, 5], ['Vendredi', 4, 4]], 'TD 1, parties III-IV (2 heures de travail chacun)')
    F1 = fpp_fig('TD 1 partie I : FPP de Robinson (B = 12 − 3P) et de Vendredi (B = 10 − P) ; optimum d\'autarcie sur la droite B = P', 12, 4, 10, 10, 3, 5, xmax=12, ymax=14)
    F3 = fpp_fig('TD 1 partie III : FPP de Robinson (B = 20 − 2P) et de Vendredi (B = 8 − P)', 20, 10, 8, 8, 20 / 3, 4, xmax=12, ymax=22)

    n1 = nm(
        'autarcie', "L'autarcie : productivités, frontière des possibilités de production, optimum",
        "L'**autarcie** est une situation **sans aucun échange** : chaque individu vit uniquement de ce qu'il produit. Pour la décrire, on fait des hypothèses sur les **possibilités de production** et sur les **préférences**.",
        [
            "**Productivité (moyenne) du travail** : quantité d'un bien produite par une unité de travail ; par heure : **productivité horaire**.",
            "**Temps nécessaire pour une unité** = 60 / productivité horaire (en minutes).",
            "**Frontière des possibilités de production (FPP)** : ensemble des combinaisons de production réalisables en utilisant **tout** le temps disponible. Ex. Robinson (6 blé/h, 2 poissons/h, 2 h) : 10 B + 30 P = 120 (minutes) ⇔ **B = 12 − 3P**.",
            "**Préférences** du modèle : consommer **autant de blé que de poisson** (biens complémentaires) : **B = P**.",
            "**Optimum d'autarcie** : production = consommation désirée, sans perte ; graphiquement, **intersection de la FPP et de la droite des préférences** ; algébriquement, résolution du système {FPP ; B = P}.",
            "Exemple du cours : Robinson produit et consomme **3 B et 3 P** ; Vendredi **5 B et 5 P**.",
        ],
        [
            S(calc("TD 1 : Robinson produit 6 unités de blé en une heure. Combien de minutes lui faut-il pour produire une unité de blé ?", 10, "60 / 6 = **10 minutes** par unité de blé (et 60 / 2 = 30 minutes par poisson).", niveau=1, unite='min', tableau=prod1), td(1)),
            S(calc("TD 1 : combien de minutes faut-il à Vendredi (5 poissons/h) pour produire 3 unités de poisson ?", 36, "Une unité : 60 / 5 = 12 min ; 3 unités : 3 × 12 = **36 minutes**.", niveau=1, unite='min', tableau=prod1), td(1)),
            S(calc("TD 1 : combien d'unités de blé Robinson peut-il produire au maximum en 2 heures ?", 12, "6 × 2 = **12 unités** (s'il ne produit que du blé).", niveau=1, unite='', tableau=prod1), td(1)),
            S(qcm("TD 1 : quelle équation décrit les possibilités de production de Robinson en 120 minutes ?", ["10 B + 30 P = 120", "6 B + 2 P = 120", "30 B + 10 P = 120", "B + P = 10"], 0,
                  "Chaque unité de blé prend 10 min et chaque poisson 30 min : 10 B + 30 P = 120, soit B = 12 − 3P (ou B/6 + P/2 = 2 en heures).", niveau=2, tableau=prod1), td(1)),
            S(calc("TD 1 : en autarcie, Robinson veut B = P et sa FPP est B = 12 − 3P. Quelle quantité de poisson (et de blé) produit-il ?", 3, "B = P et B = 12 − 3P → P = 12 − 3P → 4P = 12 → **P = B = 3**.", niveau=2, unite='', figure=F1), td(1)),
            S(calc("TD 1 : FPP de Vendredi : 12 B + 12 P = 120 (B + P = 10). Quelle est sa consommation de chaque bien en autarcie ?", 5, "B = P et B + P = 10 → **B = P = 5**.", niveau=2, unite='', figure=F1), td(1)),
            S(calc("TD 1, partie III : Robinson produit 10 B/h et 5 P/h (FPP : B = 20 − 2P). Quelle quantité de chaque bien consomme-t-il en autarcie (au centième) ?", 20 / 3, "B = P → P = 20 − 2P → 3P = 20 → **P = B ≈ 6,67** (6,66 dans le cours).", niveau=3, unite='', tolerance=0.01, figure=F3, tableau=prod3), td(1)),
            S(qcm("Sur le graphique, que représente l'intersection d'une FPP avec la droite B = P ?", ["L'optimum d'autarcie de l'individu", "Un point irréalisable", "Le gain de l'échange", "La spécialisation complète"], 0, "C'est la combinaison qui épuise tout le temps disponible et respecte les préférences.", niveau=1, figure=F1), td(1, True)),
            vf("Un point situé au-delà de la FPP est réalisable si l'individu travaille plus vite.", False, "La FPP est construite avec les productivités et le temps donnés : un point au-delà est **irréalisable** en autarcie (l'échange permettra de consommer au-delà)."),
        ], figure=F1, formules=["Temps par unité = 60 / productivité horaire", "FPP (en minutes) : tB·B + tP·P = temps total", "Optimum d'autarcie : {FPP ; B = P}"])

    n2 = nm(
        'avantage-absolu', "Avantage absolu et gains de la spécialisation",
        "L'**avantage absolu** est l'avantage d'un individu (entreprise, pays) provenant d'une **meilleure productivité** dans la fabrication d'un bien.",
        [
            "Si chacun a un avantage absolu dans un bien, ils ont **toujours intérêt à échanger** en se spécialisant.",
            "Ex. : Robinson (6 B/h contre 5 pour Vendredi) a l'avantage absolu en **blé** ; Vendredi (5 P/h contre 2) en **poisson**.",
            "Spécialisation complète : Robinson produit 12 B, Vendredi 10 P → **12 B et 10 P** à partager, contre 3 + 5 = 8 de chaque en autarcie.",
            "La spécialisation **accroît l'ensemble des possibilités de production** et donc de consommation.",
            "Exemple de partage du cours : Robinson (4 B ; 4 P), Vendredi (6 B ; 6 P) : chacun améliore sa situation (2 B restent inutilisés : solution non optimale).",
        ],
        [
            S(qcm("TD 1 : dans quel bien Robinson (6 B/h, 2 P/h) est-il plus efficace que Vendredi (5 B/h, 5 P/h) ?", ["Le blé", "Le poisson", "Les deux", "Aucun"], 0, "6 > 5 en blé : avantage absolu de Robinson en blé ; Vendredi a l'avantage absolu en poisson (5 > 2).", niveau=1, tableau=prod1), td(1)),
            S(calc("TD 1, partie II : chacun se spécialise intégralement selon son avantage absolu. Quelle quantité totale de blé est produite ?", 12, "Robinson produit 6 × 2 = **12 B** ; Vendredi produit 5 × 2 = 10 P.", niveau=1, unite='', tableau=prod1), td(1)),
            S(calc("Même situation : quelle quantité totale de poisson est produite ?", 10, "Vendredi : 5 × 2 = **10 P**.", niveau=1, unite=''), td(1)),
            S(calc("En autarcie, combien d'unités de blé étaient produites au total (Robinson + Vendredi) ?", 8, "3 + 5 = **8** ; avec la spécialisation on passe à 12 B (et de 8 à 10 P).", niveau=2, unite=''), td(1)),
            qcm("Selon le cours, après spécialisation et échange, Robinson consomme (4 B ; 4 P) et Vendredi (6 B ; 6 P). Que peut-on dire ?", ["Les deux améliorent leur situation par rapport à l'autarcie", "Seul Robinson y gagne", "Seul Vendredi y gagne", "Personne n'y gagne"], 0, "Robinson : 4 > 3 ; Vendredi : 6 > 5. (2 unités de blé sont perdues : la solution n'est pas optimale.)"),
            vf("L'avantage absolu provient d'une meilleure productivité dans la fabrication d'un bien.", True, "Définition du cours."),
            S(courte("TD 1 : propose un échange entre Robinson (12 B) et Vendredi (10 P) qui permette à chacun de consommer plus qu'en autarcie avec B = P.",
                     "Par exemple, Robinson donne 7 B à Vendredi contre 5 P : Robinson consomme (5 B ; 5 P) au lieu de (3 ; 3), Vendredi (7 B ; 5 P) — ou, pour respecter B = P, (5 ; 5) en gardant 2 B inutilisés. Tout partage où chacun dépasse son autarcie convient.", niveau=3), td(1)),
            qcm("Pourquoi la spécialisation accroît-elle la production totale ?", ["Chacun consacre son temps au bien qu'il produit le plus efficacement", "Les individus travaillent plus longtemps", "Les prix baissent", "Les préférences changent"], 0, "Le temps disponible est utilisé là où la productivité est la plus forte.", niveau=2),
        ])

    n3 = nm(
        'avantage-comparatif', "Coût d'opportunité et avantage comparatif",
        "Même si un individu est plus efficace dans **tous** les biens, l'échange reste profitable : chacun doit se spécialiser dans le bien où il a un **avantage comparatif**, c'est-à-dire un **coût d'opportunité plus faible**.",
        [
            "**Coût d'opportunité** d'un bien : ce à quoi il faut **renoncer** pour l'obtenir (ex. aller à l'université : le salaire non gagné).",
            "**Coût d'opportunité du blé en poisson = productivité en poisson / productivité en blé**. Ex. Robinson (10 B, 5 P par heure) : 1 B coûte 5/10 = **0,5 P** ; 1 P coûte **2 B**. Vendredi (4 ; 4) : 1 B = 1 P.",
            "Le coût d'opportunité d'un bien est l'**inverse** de celui de l'autre : un individu ne peut pas avoir l'avantage comparatif dans les deux biens (sauf coûts égaux).",
            "Ici : Robinson a l'avantage absolu dans les deux biens, mais l'avantage **comparatif** en **blé** (0,5 < 1) ; Vendredi en **poisson** (1 < 2).",
            "Exemple du cours : Robinson produit (12 B ; 4 P), Vendredi (0 B ; 8 P) → total (12 ; 12) contre (10,66 ; 10,66) en autarcie. Robinson cède 5 B contre 3 P : Robinson consomme (7 ; 7), Vendredi (5 ; 5).",
            "**Ricardo** : l'Angleterre et le Portugal ont intérêt à échanger même si le Portugal est plus productif partout.",
        ],
        [
            S(calc("TD 1, partie III : Robinson produit 10 B ou 5 P par heure. Combien d'unités de poisson coûte (en renoncement) la production d'une unité de blé ?", 0.5, "En une heure : 10 B ou 5 P → 1 B coûte 5/10 = **0,5 P**.", niveau=1, unite='P', tableau=prod3), td(1)),
            S(calc("Toujours pour Robinson : combien d'unités de blé coûte une unité de poisson ?", 2, "1 P coûte 10/5 = **2 B** (inverse de 0,5).", niveau=1, unite='B', tableau=prod3), td(1)),
            S(qcm("TD 1, partie IV : dans quel bien Vendredi (4 B/h, 4 P/h) a-t-il un avantage comparatif ?", ["Le poisson", "Le blé", "Les deux", "Aucun"], 0, "Pour Vendredi, 1 P coûte 1 B, contre 2 B pour Robinson : coût d'opportunité plus faible en poisson.", niveau=2, tableau=prod3), td(1)),
            vf("Robinson (10 B, 5 P) est plus productif que Vendredi (4 B, 4 P) dans les deux biens : il n'a donc aucun intérêt à échanger.", False, "Il a l'avantage absolu partout, mais l'échange reste profitable grâce aux **avantages comparatifs** : Robinson se spécialise en blé, Vendredi en poisson."),
            calc("Exemple du cours : Robinson produit 12 B et 4 P, Vendredi 8 P. Robinson cède 5 B contre 3 P. Combien de poissons Robinson consomme-t-il ?", 7, "4 + 3 = **7 P** (et 12 − 5 = 7 B) : (7 ; 7) contre (6,66 ; 6,66) en autarcie.", niveau=2, unite=''),
            calc("Ricardo : en Angleterre il faut 100 travailleurs pour une quantité de drap et 120 pour la même quantité de vin. Coût d'opportunité du drap en vin (au centième) ?", 100 / 120, "Produire le drap mobilise 100 travailleurs qui auraient produit 100/120 = **0,83** unité de vin.", niveau=2, unite='', tolerance=0.01),
            calc("Ricardo : au Portugal il faut 90 travailleurs pour le drap et 80 pour le vin. Coût d'opportunité du drap en vin (au centième) ?", 90 / 80, "90/80 = **1,13** > 0,83 : l'Angleterre a l'avantage comparatif dans le drap, le Portugal dans le vin (alors qu'il a l'avantage absolu dans les deux).", niveau=2, unite='', tolerance=0.01),
            calc("Nord : 10 High-tech ou 4 Low-tech ; Sud : 1 High-tech ou 2 Low-tech. Coût d'opportunité d'un bien High-tech en Low-tech pour le Nord ?", 0.4, "4/10 = **0,4** contre 2/1 = 2 pour le Sud : le Nord doit se spécialiser dans le High-tech.", niveau=2, unite=''),
            qcm("L'avantage comparatif repose sur :", ["Un coût d'opportunité plus faible", "Une productivité plus élevée", "Un prix plus bas", "Un temps de travail plus long"], 0, "La productivité plus élevée définit l'avantage **absolu**."),
            courte("Pourquoi un individu ne peut-il pas avoir un avantage comparatif dans les deux biens ?", "Parce que le coût d'opportunité d'un bien est l'inverse de celui de l'autre : si mon coût d'opportunité du blé est plus faible que le tien, mon coût d'opportunité du poisson est forcément plus élevé.", niveau=2),
        ], formules=["CO du blé (en poisson) = productivité poisson / productivité blé", "CO du poisson = 1 / CO du blé"], figure=F3)

    n4 = nm(
        'taux-echange', "Taux d'échange acceptables, commerce international et limites",
        "L'échange n'est accepté que si chacun obtient le bien **moins cher que son propre coût d'opportunité**. Le taux d'échange doit donc se situer **entre les deux coûts d'opportunité**.",
        [
            "Ex. (TD 1, partie IV) : 1 P coûte 2 B à Robinson et 1 B à Vendredi. Vendredi (qui cède le poisson) exige **plus de 1 B** par poisson ; Robinson (qui cède le blé) accepte de donner **moins de 2 B** par poisson → taux acceptable **entre 1 et 2 B par poisson**.",
            "L'exemple du cours (5 B contre 3 P, soit 1,67 B par poisson) est bien dans cet intervalle.",
            "**Commerce international** : les pays développés ont intérêt à acheter aux pays moins avancés pour se spécialiser là où ils sont le plus productifs : avantages du **libre-échange**.",
            "**Limites** : productivités supposées **exogènes et fixes** alors qu'elles évoluent (argument des **industries naissantes** de List, XIXe s., pour un protectionnisme temporaire) ; la théorie ne dit rien des **ajustements internes** (certains secteurs et individus perdent) → politiques d'accompagnement de la mondialisation.",
        ],
        [
            S(calc("TD 1, partie IV : en dessous de combien d'unités de blé par poisson Vendredi (CO du poisson = 1 B) refuse-t-il de céder son poisson ?", 1, "Produire un poisson lui coûte 1 B : il refuse d'en recevoir **moins de 1 B** par poisson.", niveau=2, unite='B'), td(1)),
            S(calc("Au-dessus de combien d'unités de blé par poisson Robinson (CO du poisson = 2 B) refuse-t-il l'échange ?", 2, "Il peut produire lui-même un poisson pour 2 B : il refuse de payer **plus de 2 B** par poisson.", niveau=2, unite='B'), td(1)),
            qcm("Le taux de 5 B contre 3 P (1,67 B par poisson) est-il acceptable par les deux ?", ["Oui, car il est compris entre 1 et 2", "Non pour Robinson", "Non pour Vendredi", "Non pour les deux"], 0, "1 < 1,67 < 2."),
            qcm("Un taux de 2,5 B par poisson serait :", ["Refusé par Robinson", "Refusé par Vendredi", "Accepté par les deux", "Refusé par les deux"], 0, "Robinson produit un poisson pour 2 B : il préfère le produire lui-même.", niveau=2),
            vf("Selon la théorie des avantages comparatifs, tous les pays gagnent globalement au libre-échange.", True, "Chaque pays se retrouve en meilleure situation qu'en autarcie."),
            qcm("Quelles sont des limites de la théorie des avantages comparatifs selon le cours ?", ["Les productivités sont supposées fixes alors qu'elles évoluent", "Elle ignore que certains secteurs d'un pays peuvent perdre", "Elle suppose des avantages absolus", "Elle interdit les échanges internationaux"], [0, 1], "D'où l'argument des industries naissantes et la nécessité de politiques d'accompagnement.", niveau=2),
            qcm("L'argument des « industries naissantes » de List justifie :", ["Un protectionnisme temporaire", "Le libre-échange intégral", "La suppression des impôts", "La spécialisation immédiate"], 0, "Le temps de construire la productivité d'une industrie nouvelle."),
            S(courte("TD 1 : dans quelle mesure ces résultats incitent-ils à préconiser une spécialisation et un échange ?", "Chacun produit le bien dans lequel son coût d'opportunité est le plus faible (Robinson le blé, Vendredi le poisson) : la production totale augmente et, avec un taux d'échange compris entre 1 et 2 B par poisson, chacun consomme plus qu'en autarcie.", niveau=3), td(1)),
        ])
    return chapitre('ch-echange', "Chapitre 1 — Les bénéfices de l'échange", [n1, n2, n3, n4])


# --- Graphiques offre / demande ---
def od_fig(titre, extra=(), points=None, guides=(), zones=(), xmax=10, ymax=10, d=(10, -1), o=(0, 1), labels=('D', 'O')):
    dd = [droite(d[0], d[1], 0, (0 - d[0]) / d[1] if d[1] else xmax, labels[0], 1), droite(o[0], o[1], 0, min(xmax, (ymax - o[0]) / o[1]), labels[1], 2)] + list(extra)
    return fig('Q', 'P', xmax, ymax, dd, titre=titre, points=points or [], guides=guides, zones=zones, gradx=list(range(0, xmax + 1, max(1, xmax // 5)))[1:], grady=list(range(0, ymax + 1, max(1, ymax // 5)))[1:])


def ch2():
    n5 = nm(
        'marche-cpp', "Marché, types de marchés et concurrence pure et parfaite",
        "Un **marché** est l'ensemble des acheteurs et des vendeurs d'un bien ou service, ou le lieu où se confrontent l'**offre** (comportement des vendeurs) et la **demande** (comportement des acheteurs).",
        [
            "**Concurrence pure et parfaite (CPP)** : très grand nombre d'entreprises, libre entrée, produit homogène ; ex. certains produits agricoles ; l'entreprise est **preneuse de prix** (demande individuelle horizontale).",
            "**Concurrence monopolistique** : grand nombre, produit **différencié** (menuisiers, restaurants) ; un certain contrôle sur les prix.",
            "**Oligopole** : nombre limité, entrée restreinte (automobile, ciment). **Monopole** : une seule entreprise, entrée bloquée (médicaments, distribution d'eau), fort contrôle sur les prix.",
            "**4 conditions de la CPP** : **homogénéité** du produit ; **atomicité** des agents ; **transparence** (information parfaite) ; **libre entrée et sortie**. (+ biens privés, absence d'externalités.)",
            "Conséquence : en CPP, les agents sont **preneurs de prix**. Ces hypothèses sont restrictives car « modéliser, c'est simplifier ».",
        ],
        [
            qcm("Quelles sont les quatre conditions de la concurrence pure et parfaite ?", ["Homogénéité, atomicité, transparence, libre entrée et sortie", "Monopole, prix fixe, publicité, brevets", "Différenciation, oligopole, transparence, subventions", "Atomicité, différenciation, barrières, information"], 0, "Définition du cours."),
            qcm("L'atomicité signifie que :", ["Les acheteurs et vendeurs sont si nombreux que leur influence individuelle est négligeable", "Le produit est identique", "L'information est parfaite", "Les entreprises peuvent entrer librement"], 0, "Chaque agent est « un atome » du marché."),
            qcm("Sur un marché de CPP, une entreprise :", ["Est preneuse de prix", "Fixe librement son prix", "Est en monopole", "Différencie son produit"], 0, "Sa demande individuelle est horizontale au prix du marché."),
            qcm("Un marché avec un nombre limité d'entreprises et une entrée restreinte (ex. ciment) est :", ["Un oligopole", "Un monopole", "En concurrence monopolistique", "En CPP"], 0, "Tableau des types de marché."),
            qcm("Les restaurants d'une ville, avec des cartes différentes, relèvent plutôt :", ["De la concurrence monopolistique", "De la CPP", "Du monopole", "De l'oligopole"], 0, "Grand nombre d'entreprises mais produits différenciés.", niveau=2),
            vf("Sur un marché de CPP, l'information sur les prix est parfaite.", True, "C'est la condition de transparence."),
            vf("Un monopole est preneur de prix.", False, "Le monopole a un contrôle important sur les prix ; c'est l'entreprise en CPP qui est preneuse de prix."),
            courte("Pourquoi étudie-t-on la CPP alors que ses hypothèses sont peu réalistes ?", "Parce que modéliser, c'est simplifier : on commence par comprendre les mécanismes de marché dans le cas le plus simple, puis on relâche les hypothèses pour étudier des situations plus réalistes.", niveau=2),
        ])

    agr = tab(['Prix d\'un CD', 'Greg', 'Alex', 'Demande de marché'], [[5, 5, 6, 11], [10, 4, 4, 8], [15, 3, 2, 5], [20, 2, 0, 2], [25, 1, 0, 1], [30, 0, 0, 0]], 'Agrégation des demandes (cours)')
    FCD = fig('Q (millions)', 'P (€)', 40, 40, [droite(35, -1, 0, 35, 'D : Q = 35 − P', 1)], titre='Courbe de demande de CD : Q = 35 − P (axes : prix en ordonnée)', gradx=[10, 20, 30], grady=[10, 20, 30])
    n6 = nm(
        'demande', "La demande : déterminants, loi de la demande, types de biens",
        "La **demande de marché** est la quantité d'un bien que les acheteurs sont **prêts et capables** d'acheter ; c'est la **somme des demandes individuelles**.",
        [
            "**Déterminants** (toutes choses égales par ailleurs, TCEPA) : prix du bien, revenu, préférences, anticipations, prix des biens comparables, nombre de consommateurs.",
            "**Loi de la demande** : quand le prix augmente, la quantité demandée diminue. Exception : les **biens de Giffen** (pain en Europe au XVIe s.).",
            "**Bien normal** : demande ↑ quand le revenu ↑. **Bien inférieur** : demande ↓ quand le revenu ↑.",
            "**Biens substituables** : la hausse du prix de l'un **augmente** la demande de l'autre (riz/pâtes). **Complémentaires** : la hausse du prix de l'un **diminue** la demande de l'autre (pâtes/sauce tomate).",
            "**Courbe de demande** : pente négative ; **prix en ordonnée, quantité en abscisse** (c'est la fonction inverse de la demande). Pour une quantité donnée, elle donne le **prix de réserve** (disposition à payer).",
            "Agrégation : on **additionne horizontalement** les quantités demandées à chaque prix.",
        ],
        [
            calc("Demande de CD : Q = 35 − P. Quelle est la quantité demandée (en millions) au prix de 20 € ?", 15, "35 − 20 = **15 millions**.", niveau=1, unite='M', figure=FCD),
            calc("Avec Q = 35 − P, quel est le prix de réserve du consommateur qui achète le 10e million de CD ?", 25, "On lit la courbe à l'envers : P = 35 − Q = 35 − 10 = **25 €**.", niveau=2, figure=FCD),
            calc("Avec le tableau, quelle est la demande de marché au prix de 10 € ?", 8, "Greg 4 + Alex 4 = **8** : on additionne horizontalement.", niveau=1, unite='', tableau=agr),
            qcm("Le prix du café augmente et la demande de thé augmente. Café et thé sont :", ["Substituables", "Complémentaires", "Inférieurs", "De Giffen"], 0, "La hausse du prix de l'un fait augmenter la demande de l'autre."),
            qcm("Le prix des imprimantes baisse et la demande de cartouches d'encre augmente. Ces biens sont :", ["Complémentaires", "Substituables", "Inférieurs", "Normaux uniquement"], 0, "Ils se consomment ensemble."),
            qcm("Quand leur revenu augmente, des ménages achètent moins de pâtes premier prix. Pour eux, ce bien est :", ["Un bien inférieur", "Un bien normal", "Un bien de Giffen", "Un bien de luxe"], 0, "Demande qui diminue quand le revenu augmente."),
            vf("Un bien de Giffen est un bien dont la demande augmente quand son prix augmente.", True, "C'est la seule exception à la loi de la demande."),
            vf("Par convention, sur la courbe de demande, la quantité est en ordonnée et le prix en abscisse.", False, "C'est l'inverse : **prix en ordonnée**, quantité en abscisse."),
            qcm("Quels sont des déterminants de la demande de marché ?", ["Le revenu des consommateurs", "Les anticipations", "Le nombre de consommateurs", "Le coût des matières premières"], [0, 1, 2], "Le coût des facteurs de production est un déterminant de l'**offre**.", niveau=2),
        ], figure=FCD)

    FDEP = fig('Q', 'P', 10, 10, [droite(8, -1, 0, 8, 'D0', 1), droite(6, -1, 0, 6, 'D1', 1, True)], titre='Choc négatif de demande : la courbe se déplace vers la gauche (D0 → D1)', fleches=[{'de': [5.2, 2.5], 'a': [3.6, 2.5]}], gradx=[2, 4, 6, 8], grady=[2, 4, 6, 8])
    n7 = nm(
        'deplacements', "Déplacement de la courbe ou déplacement le long de la courbe",
        "La courbe relie la quantité au **prix**, toutes choses égales par ailleurs. Une variation du **prix** fait se déplacer **le long** de la courbe ; la variation d'un **autre déterminant** **déplace la courbe**.",
        [
            "**Demande** : hausse du revenu (bien normal), hausse du prix d'un **substitut**, hausse du nombre d'acheteurs → courbe vers la **droite** (choc positif). Hausse du prix d'un **complément**, anticipations pessimistes → vers la **gauche** (choc négatif).",
            "**Offre** : déterminants = prix des facteurs de production, **technologie**, anticipations, nombre de vendeurs.",
            "Hausse des salaires ou du coût des matières premières, nouvelle taxe sur la production → offre vers la **gauche** (choc négatif d'offre). Progrès technique, entrée de nouvelles firmes → offre vers la **droite**.",
            "Exemple du cours : le téléchargement légal à prix compétitif se substitue aux CD → la demande de CD se déplace vers la gauche.",
        ],
        [
            qcm("La baisse du prix des CD provoque :", ["Un déplacement le long de la courbe de demande", "Un déplacement de la courbe de demande vers la droite", "Un déplacement de la courbe de demande vers la gauche", "Un déplacement de la courbe d'offre"], 0, "Le prix du bien lui-même fait bouger **le long** de la courbe (quantité demandée ↑)."),
            qcm("Une baisse du prix des lecteurs CD (bien complémentaire) :", ["Déplace la demande de CD vers la droite", "Déplace la demande de CD vers la gauche", "Déplace l'offre de CD", "N'a aucun effet"], 0, "Le complément devient moins cher, on achète plus de lecteurs donc plus de CD.", figure=FDEP),
            qcm("Des prévisions pessimistes sur le pouvoir d'achat :", ["Déplacent la demande vers la gauche", "Déplacent la demande vers la droite", "Déplacent l'offre vers la droite", "N'ont pas d'effet"], 0, "Les anticipations sont un déterminant de la demande."),
            qcm("Une hausse des salaires des employés de l'industrie du CD :", ["Déplace l'offre vers la gauche", "Déplace l'offre vers la droite", "Déplace la demande vers la gauche", "Fait se déplacer le long de l'offre"], 0, "Le coût des facteurs augmente : choc négatif d'offre."),
            qcm("Une amélioration des technologies qui réduit les coûts de production :", ["Déplace l'offre vers la droite", "Déplace l'offre vers la gauche", "Déplace la demande vers la droite", "N'a pas d'effet"], 0, "Choc positif d'offre."),
            qcm("L'entrée de nouvelles firmes sur le marché :", ["Déplace l'offre vers la droite", "Déplace la demande vers la droite", "Déplace l'offre vers la gauche", "Fait baisser la demande"], 0, "Le nombre de vendeurs augmente."),
            S(qcm("Lecture du graphique : la demande passe de D0 à D1. Au prix de 2, la quantité demandée passe de :", ["6 à 4", "4 à 6", "8 à 6", "6 à 8"], 0, "D0 : Q = 8 − P = 6 ; D1 : Q = 6 − P = 4. La courbe s'est déplacée vers la gauche.", niveau=2, figure=FDEP), COURS),
            vf("Une hausse du revenu déplace la demande d'un bien inférieur vers la gauche.", True, "Pour un bien inférieur, la demande diminue quand le revenu augmente.", niveau=2),
            S(qcm("TD 5 : la baisse du prix d'un produit d'un autre marché fait diminuer la demande du marché étudié. Ce produit est :", ["Substituable", "Complémentaire", "Inférieur", "De Giffen"], 0, "Il est devenu moins cher, les consommateurs s'y reportent : c'est un substitut.", niveau=2), td(5)),
        ], figure=FDEP)

    n8 = nm(
        'elasticite-demande', "L'élasticité-prix de la demande",
        "L'**élasticité** mesure la variation en % d'une quantité suite à une variation de 1 % d'un de ses déterminants. **Élasticité-prix de la demande : εD/P = (ΔQ/Q) / (ΔP/P)**, en valeur absolue par convention.",
        [
            "Interprétation : la demande baisse de ε % quand le prix augmente de 1 %.",
            "Sur une droite de demande : **|ε| = |ΔQ/ΔP| × P/Q** (pente de Q par rapport à P × P/Q). Ex. D = 100 − 5P en P = 10 : ε = 5 × 10/50 = **1**.",
            "La **pente** est une mauvaise mesure (dépend des unités) ; l'**élasticité ne dépend pas des unités**.",
            "**Élastique** : |ε| > 1 ; **inélastique (rigide)** : |ε| < 1 ; **unitaire** : |ε| = 1 ; cas limites : élasticité **nulle** (droite verticale) et **infinie** (horizontale).",
            "Déterminants : biens de **première nécessité** (rigides) / de **luxe** (élastiques) ; présence de **substituts** (plus élastique) ; **horizon temporel** (plus élastique à long terme).",
            "Si la demande est **inélastique**, une hausse du prix **augmente la recette** (P × Q).",
        ],
        [
            calc("Exemple du cours : D = 100 − 5P. Quelle est l'élasticité-prix (en valeur absolue) au point P = 10 ?", 1, "Q = 50 ; |ε| = 5 × 10/50 = **1** (élasticité unitaire).", niveau=1, unite=''),
            calc("Stylos : à 0,50 €, 5 000 ventes ; si le prix augmente de 5 %, 4 500 ventes. Élasticité-prix (valeur absolue) ?", 2, "ΔQ/Q = −500/5 000 = −10 % ; ΔP/P = +5 % → |ε| = 10/5 = **2** : demande élastique.", niveau=2, unite=''),
            calc("Consoles : prix 150 €, 200 milliers échangés ; si le prix augmente de 1 %, la demande passe à 199 milliers. Élasticité-prix de la demande ?", 0.5, "ΔQ/Q = −1/200 = −0,5 % pour +1 % → |ε| = **0,5** (rigide). On trouve la même valeur en comptant les consoles à l'unité (−1 000/200 000).", niveau=2, unite=''),
            calc("Baguette : à 0,90 €, 1 000 ventes ; à 1 €, 950 ventes. Élasticité-prix (au centième) ?", (50 / 1000) / (0.1 / 0.9), "ΔQ/Q = −5 % ; ΔP/P = 0,10/0,90 = +11,1 % → |ε| = 5/11,1 = **0,45** : demande inélastique.", niveau=2, unite='', tolerance=0.01),
            calc("Toujours pour la baguette : quelle est la variation de la recette quotidienne du boulanger (en €) ?", 950 - 900, "Avant : 0,90 × 1 000 = 900 € ; après : 1 × 950 = 950 € → **+50 €**. Prévisible : avec une demande inélastique, la hausse du prix augmente la recette.", niveau=2),
            S(calc("TD 3, ex. 2 : demande Q = 80 − 5P. Élasticité-prix au point p = 4 (au centième) ?", 5 * 4 / 60, "Q = 60 ; |ε| = 5 × 4/60 = **0,33**.", niveau=2, unite='', tolerance=0.01), td(3)),
            S(calc("TD 3, ex. 2 : même demande, élasticité au point p = 2 (au centième) ?", 5 * 2 / 70, "Q = 70 ; |ε| = 10/70 = **0,14** : sur une droite, l'élasticité diminue quand le prix baisse.", niveau=2, unite='', tolerance=0.01), td(3)),
            S(calc("TD 5, ex. 3 : la demande de marché est p = 11 − 0,02 Q. Élasticité au point B (Q = 100 ; p = 9) ?", 50 * 9 / 100, "Q = 550 − 50p → |dQ/dp| = 50 ; |ε| = 50 × 9/100 = **4,5** : demande très élastique.", niveau=3, unite=''), td(5)),
            qcm("La demande d'un bien qui a beaucoup de substituts proches est plutôt :", ["Élastique", "Rigide", "D'élasticité nulle", "Croissante avec le prix"], 0, "Le consommateur se reporte facilement sur les substituts."),
            vf("La pente de la courbe de demande est une bonne mesure de la sensibilité de la demande au prix.", False, "Elle dépend des unités (euros ou centimes) ; l'élasticité, non."),
        ], formules=["ε = (ΔQ/Q) / (ΔP/P)", "Droite : |ε| = |dQ/dP| × P/Q", "|ε| > 1 élastique ; < 1 rigide ; = 1 unitaire"])

    n9 = nm(
        'offre', "L'offre : déterminants, courbe d'offre, élasticité-prix de l'offre",
        "L'**offre de marché** est la quantité que les vendeurs sont **prêts et capables** de vendre ; c'est la **somme des offres individuelles**.",
        [
            "**Loi de l'offre** : quand le prix augmente, la quantité offerte augmente → courbe d'offre à **pente positive**.",
            "Déterminants : prix du bien, **prix des facteurs de production**, **technologie**, anticipations, **nombre de vendeurs**.",
            "Lecture : pour un prix donné, quantité que l'on est prêt à vendre ; pour une quantité donnée, **prix minimum** auquel on est prêt à vendre (coût d'opportunité du vendeur marginal).",
            "Exemple du cours (CD) : **QO = 2P/5** (5 € → 2 millions ; 25 € → 10 millions).",
            "**Élasticité-prix de l'offre** εO/P = (ΔO/O)/(ΔP/P), **toujours positive** ; élastique si > 1, rigide si < 1, unitaire si = 1.",
        ],
        [
            calc("Offre de CD : QO = 2P/5. Quelle quantité est offerte (en millions) au prix de 15 € ?", 6, "2 × 15/5 = **6 millions**.", niveau=1, unite='M'),
            calc("Consoles : prix 150 €, 200 milliers ; si le prix augmente de 1 %, l'offre passe à 230 milliers. Élasticité-prix de l'offre ?", 15, "ΔO/O = 30/200 = +15 % pour +1 % → **ε = 15** : offre très élastique.", niveau=2, unite=''),
            S(calc("TD 3, ex. 2 : l'offre passe par (Q = 10 ; P = 2) et (Q = 30 ; P = 4). Quel est le coefficient directeur ΔP/ΔQ de la courbe d'offre ?", 0.1, "(4 − 2)/(30 − 10) = 2/20 = **0,1** → P = 1 + 0,1 Q, soit Q = 10P − 10.", niveau=2, unite=''), td(3)),
            S(calc("Avec l'offre Q = 10P − 10 (TD 3), quelle quantité est offerte au prix de 9 ?", 80, "10 × 9 − 10 = **80** (point (80 ; 9) de l'énoncé ✓).", niveau=1, unite=''), td(3)),
            calc("Offre Q = 10P − 10 : élasticité-prix de l'offre au point P = 6 (au centième) ?", 10 * 6 / 50, "Q = 50 ; ε = 10 × 6/50 = **1,2** : offre élastique.", niveau=3, unite='', tolerance=0.01),
            vf("L'élasticité-prix de l'offre est négative.", False, "Du fait de la loi de l'offre, elle est **positive**."),
            qcm("Pour une quantité donnée, la courbe d'offre indique :", ["Le prix minimum auquel le vendeur est prêt à vendre", "Le prix maximum que l'acheteur est prêt à payer", "Le profit de l'entreprise", "Le coût fixe"], 0, "C'est le coût d'opportunité du vendeur marginal."),
            qcm("Quels sont des déterminants de l'offre ?", ["La technologie", "Le prix des facteurs de production", "Le nombre de vendeurs", "Le revenu des consommateurs"], [0, 1, 2], "Le revenu des consommateurs est un déterminant de la demande.", niveau=2),
        ])

    FEQ = fig('Q (millions)', 'P (€)', 40, 40, [droite(35, -1, 0, 35, 'D : Q = 35 − P', 1), droite(0, 2.5, 0, 14, 'O : Q = 2P/5', 2)], titre='Marché des CD : équilibre en P = 25 €, Q = 10 millions', points=[pt(10, 25, 'E')], guides=[gd(10, 25)], gradx=[10, 20, 30], grady=[10, 20, 25, 30])
    n10 = nm(
        'equilibre', "L'équilibre de marché",
        "L'**équilibre de marché** est la situation où l'offre et la demande se compensent : le **prix d'équilibre** égalise quantité offerte et quantité demandée ; la **quantité d'équilibre** est la quantité échangée à ce prix.",
        [
            "Algébriquement : **QO(P) = QD(P)**. Ex. CD : 2P/5 = 35 − P → **P = 25 €, Q = 10 millions**.",
            "Graphiquement : **intersection** des courbes d'offre et de demande.",
            "**Loi de l'offre et de la demande** : le prix s'ajuste pour équilibrer le marché (hypothèse de convergence).",
            "Si **P > P\\*** : **excès d'offre** → les vendeurs baissent le prix. Si **P < P\\*** : **excès de demande (pénurie)** → le prix monte.",
            "Raisonnement marginaliste : tant que Q < Q\\*, il existe des échanges mutuellement avantageux (disposition à payer > coût).",
            "« Les prix disent tout ce que nous savons et même ce que nous ne savons pas » (Hayek) : le système des prix coordonne les décisions décentralisées.",
        ],
        [
            calc("Marché des CD : QD = 35 − P et QO = 2P/5. Quel est le prix d'équilibre ?", 25, "2P/5 = 35 − P → 7P/5 = 35 → **P = 25 €**.", niveau=1, figure=FEQ),
            calc("Même marché : quantité d'équilibre (en millions) ?", 10, "Q = 35 − 25 = **10 millions**.", niveau=1, unite='M', figure=FEQ),
            calc("Qd = 100 − 10P et Qo = 10P (exercice du chapitre 3). Prix d'équilibre ?", 5, "100 − 10P = 10P → **P = 5** ; Q = 50.", niveau=1, unite=''),
            S(calc("TD 3, ex. 2 : demande Q = 80 − 5P, offre Q = 10P − 10. Prix d'équilibre ?", 6, "80 − 5P = 10P − 10 → 15P = 90 → **P = 6**.", niveau=2, unite='€'), td(3)),
            S(calc("TD 3, ex. 2 : quantité d'équilibre (en millions d'abonnements) ?", 50, "Q = 80 − 5 × 6 = **50 millions**.", niveau=2, unite='M'), td(3)),
            S(calc("TD 3, ex. 2 : déterminer l'équation de la demande. La demande passe par (Q = 30 ; P = 10) et (Q = 60 ; P = 4). Quel est le prix pour lequel la demande est nulle (ordonnée à l'origine) ?", 16, "Pente ΔP/ΔQ = (4 − 10)/(60 − 30) = −0,2 → P = 10 − 0,2(Q − 30) = **16** − 0,2 Q, soit Q = 80 − 5P.", niveau=3, unite='€'), td(3)),
            calc("Marché des CD : au prix de 30 €, quel est l'excès d'offre (en millions) ?", 12 - 5, "QO = 12 ; QD = 5 → excès d'offre de **7 millions** : le prix va baisser.", niveau=2, unite='M', figure=FEQ),
            qcm("Si le prix est inférieur au prix d'équilibre :", ["Il y a pénurie (excès de demande) et le prix augmente", "Il y a excès d'offre et le prix baisse", "Le marché est en équilibre", "Les quantités échangées augmentent"], 0, "Les vendeurs peuvent augmenter leur prix sans perdre de clients."),
            vf("À l'équilibre, toutes les opportunités d'échange mutuellement avantageuses sont exploitées.", True, "Raisonnement marginaliste du cours."),
        ], figure=FEQ, formules=["Équilibre : QO(P*) = QD(P*)"])

    FCHOC = fig('Q', 'P', 10, 10, [droite(9, -1, 0, 9, 'D', 1), droite(1, 1, 0, 9, 'O0', 2), droite(-1, 1, 1, 10, 'O1', 2, True)], titre='Choc positif d\'offre : O0 → O1 ; le prix baisse (5 → 4), la quantité augmente (4 → 5)', points=[pt(4, 5, 'E0'), pt(5, 4, 'E1')], gradx=[2, 4, 6, 8], grady=[2, 4, 6, 8])
    n11 = nm(
        'statique-comparative', "Statique comparative : chocs d'offre et de demande et élasticités",
        "La **statique comparative** compare l'équilibre avant et après un **choc exogène** sur l'offre ou la demande.",
        [
            "**Choc négatif de demande** : demande vers la gauche → excès d'offre à l'ancien prix → **P ↓ et Q ↓**.",
            "**Choc positif de demande** : P ↑ et Q ↑. **Choc positif d'offre** : **P ↓ et Q ↑**. **Choc négatif d'offre** : P ↑ et Q ↓.",
            "**Chocs simultanés** : l'effet sur l'une des deux variables est certain, l'autre dépend de l'ampleur des chocs (ex. forte hausse de la demande + légère baisse de l'offre : P ↑ ; Q ↑).",
            "**Rôle des élasticités** : plus l'offre et/ou la demande sont **rigides**, plus l'ajustement se fait par les **prix** ; plus elles sont **élastiques**, plus il se fait par les **quantités**.",
            "Exemples : essence (demande plus élastique à long terme) ; produits agricoles (demande rigide : le progrès technique a fait chuter les prix → PAC) ; immobilier (offre rigide à court terme : un choc de demande fait chuter les prix).",
        ],
        [
            qcm("Un choc négatif de demande entraîne :", ["Une baisse du prix et de la quantité d'équilibre", "Une hausse du prix et une baisse de la quantité", "Une baisse du prix et une hausse de la quantité", "Une hausse des deux"], 0, "La demande se déplace vers la gauche le long de l'offre."),
            qcm("Un progrès technique (choc positif d'offre) entraîne :", ["Une baisse du prix et une hausse de la quantité", "Une hausse du prix et de la quantité", "Une baisse des deux", "Aucun effet"], 0, "L'offre se déplace vers la droite le long de la demande.", figure=FCHOC),
            S(calc("Lecture du graphique : demande P = 9 − Q ; l'offre passe de P = 1 + Q à P = Q − 1. Quel est le nouveau prix d'équilibre ?", 4, "9 − Q = Q − 1 → Q = 5 ; **P = 4** (contre 5 avant).", niveau=2, unite='', figure=FCHOC), COURS),
            S(qcm("TD 3, situation 3 : progrès technique (offre vers la droite) avec une demande très rigide et une offre très élastique. Effet principal ?", ["Forte baisse du prix, faible hausse de la quantité", "Forte hausse de la quantité, prix stable", "Hausse du prix", "Baisse de la quantité"], 0, "Demande rigide : l'ajustement se fait surtout par les prix.", niveau=3), td(3)),
            S(qcm("TD 3, situation 4 : baisse du coût d'opportunité des offreurs avec une demande très élastique et une offre très rigide. Effet ?", ["Faible baisse du prix, hausse de la quantité", "Forte baisse du prix", "Hausse du prix", "Aucun effet"], 0, "L'offre se déplace vers la droite ; la demande élastique (presque horizontale) limite la baisse du prix.", niveau=3), td(3)),
            S(qcm("TD 3, situation 1 : forte hausse du prix d'un bien complémentaire (demande ↓) et du prix du principal facteur de production (offre ↓). Effet certain ?", ["La quantité baisse ; l'effet sur le prix est indéterminé", "Le prix baisse", "La quantité augmente", "Le prix augmente toujours"], 0, "Les deux chocs réduisent Q ; ils poussent le prix en sens opposés.", niveau=3), td(3)),
            qcm("Aluminium (cours) : les exportations russes augmentent de 600 % et l'économie mondiale entre en récession. Effet certain ?", ["Le prix baisse", "Le prix augmente", "La quantité augmente", "La quantité baisse"], 0, "Offre ↑ et demande ↓ poussent toutes deux le prix à la baisse ; l'effet sur la quantité est indéterminé.", niveau=2),
            vf("Sur le marché de l'immobilier, l'offre étant rigide à court terme, un choc négatif de demande se traduit surtout par une baisse des prix.", True, "Exemple 3 du cours."),
            S(qcm("TD 3, situation 2 : demande très élastique, offre très rigide ; l'État augmente les impôts des consommateurs (demande ↓). Effet ?", ["Forte baisse de la quantité, faible baisse du prix", "Forte baisse du prix, quantité stable", "Hausse du prix", "Aucun effet"], 0,
                  "Attention, avec une offre très rigide (presque verticale) la quantité varie peu… mais la demande très élastique (presque horizontale) se déplace vers le bas : l'ajustement combine les deux ; dans la logique du TD, c'est le côté le plus rigide (l'offre) qui impose un ajustement surtout par le **prix**. Réponse attendue : le prix baisse nettement, la quantité varie peu.", niveau=3), td(3)),
        ], figure=FCHOC)
    # correction de la dernière question : réponse cohérente avec la règle « rigide → ajustement par les prix »
    q = n11['exercices'][-1]
    q['choix'] = ["Le prix baisse, la quantité varie peu (offre rigide)", "La quantité chute fortement, prix stable", "Le prix augmente", "Aucun effet"]
    q['explication'] = "La demande se déplace vers la gauche ; l'offre très rigide (presque verticale) ne laisse guère varier la quantité : l'ajustement se fait surtout par le **prix**, qui baisse."
    return chapitre('ch-forces-marche', 'Chapitre 2 — Les forces du marché : offre, demande, élasticité', [n5, n6, n7, n8, n9, n10, n11])
