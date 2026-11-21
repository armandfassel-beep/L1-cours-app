"""Microéconomie — Chapitres 3 (efficacité du marché), 4 (coûts), 5 (entreprise en CPP)."""
from macro_base import *


def chapitres():
    return [ch3(), ch4(), ch5()]


def ch3():
    voit_d = tab(['Individu', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [['Prix de réserve (k€)', 15, 20, 30, 10, 5, 10, 5, 15, 15, 5]], 'Marché de la voiture A (cours)')
    voit_o = tab(['Vendeur', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'], [['Coût (k€)', 5, 2.5, 2.5, 5, 10, 15, 2.5, 10, 25, 25]], 'Vendeurs de la voiture A (cours)')
    # TD3 ex1
    td31 = tab(['Prix de réserve', 70, 60, 50, 40, 30, 20, 10], [['Nombre d\'acheteurs', 10, 10, 10, 20, 20, 20, 10]], 'TD 3, ex. 1 — acheteurs (triés par prix de réserve décroissant)')
    td31o = tab(['Coût d\'opportunité', 10, 20, 30, 40, 50, 60, 70], [['Nombre de vendeurs', 40, 20, 10, 10, 10, 10, 0]], 'TD 3, ex. 1 — vendeurs (triés par coût croissant)')
    FESC = fig('Q', 'P', 110, 80, courbes=[courbe(escalier([(70, 10), (60, 10), (50, 10), (40, 20), (30, 20), (20, 20), (10, 10)]) + [(100, 0)], 'D', 1), courbe(escalier([(10, 40), (20, 20), (30, 10), (40, 10), (50, 10), (60, 10)]), 'O', 2)],
               titre='TD 3, ex. 1 : demande et offre en escalier ; équilibre P = 30, Q = 70', points=[pt(70, 30, 'E')], gradx=[20, 40, 60, 80, 100], grady=[10, 20, 30, 40, 50, 60, 70])

    n12 = nm(
        'surplus-conso', "Le surplus des consommateurs",
        "Le **prix de réserve** est le prix le plus élevé qu'un individu est prêt à payer pour un bien (sa disposition à payer). Le **surplus du consommateur** est la différence entre ce prix de réserve et le prix effectivement payé : **SCi = Pri − Di**.",
        [
            "**Surplus des consommateurs** = somme des surplus individuels.",
            "**Bien discret** : acheté une seule fois sur la période (voiture, maison).",
            "Trois groupes : ceux qui achètent avec un surplus positif ; ceux qui n'achètent pas ; les **indifférents** (prix de réserve = prix, surplus nul).",
            "Courbe de demande d'un bien discret : **en escalier** (consommateurs classés par prix de réserve décroissant).",
            "Graphiquement : **surface entre la courbe de demande et la droite horizontale du prix**. Pour une droite : triangle = ½ × base × hauteur.",
            "**Le SC diminue quand le prix augmente** (et augmente quand le prix baisse : nouveaux acheteurs + anciens qui paient moins).",
        ],
        [
            calc("Voiture A, prix 10 000 € : calcule le surplus des consommateurs (en milliers d'euros).", 45, "Acheteurs avec prix de réserve ≥ 10 : A (5), B (10), C (20), D (0), F (0), H (5), I (5) → SC = **45 k€**.", niveau=1, unite='k€', tableau=voit_d),
            calc("Même marché : le prix passe à 20 000 €. Nouveau SC (en milliers d'euros) ?", 10, "Seuls B (20 − 20 = 0) et C (30 − 20 = 10) achètent : SC = **10 k€** (baisse).", niveau=2, unite='k€', tableau=voit_d),
            calc("Même marché : le prix passe à 5 000 €. Nouveau SC (en milliers d'euros) ?", 80, "Tous achètent : (15 + 20 + 30 + 10 + 5 + 10 + 5 + 15 + 15 + 5) − 10 × 5 = 130 − 50 = **80 k€**.", niveau=3, unite='k€', tableau=voit_d),
            S(calc("TD 3, ex. 1 : à l'équilibre P = 30, calcule le surplus des consommateurs.", 1100, "10 × (70 − 30) + 10 × (60 − 30) + 10 × (50 − 30) + 20 × (40 − 30) + 20 × 0 = 400 + 300 + 200 + 200 = **1 100**.", niveau=3, unite='', tableau=td31, figure=FESC), td(3)),
            calc("Demande Qd = 100 − 10P (P = 10 − Q/10), prix d'équilibre 5, quantité 50. Surplus des consommateurs ?", 125, "Triangle : ½ × 50 × (10 − 5) = **125**.", niveau=2, unite=''),
            S(calc("TD 2 : un acheteur a une valeur de 12 € pour un kilo de pommes et l'achète 9 €. Quel est son surplus ?", 3, "Surplus = valeur − prix = 12 − 9 = **3 €**.", niveau=1), td(2, True)),
            vf("Lorsque le prix augmente, le surplus des consommateurs augmente.", False, "Il **diminue** : certains n'achètent plus et les autres paient plus cher."),
            qcm("Le consommateur marginal est celui qui :", ["N'achète pas mais achèterait si le prix baissait très légèrement", "Achète le premier", "A le prix de réserve le plus élevé", "Revend le bien"], 0, "Définition du cours."),
            qcm("Graphiquement, le surplus des consommateurs est :", ["La surface entre la courbe de demande et la droite du prix", "La surface sous la courbe d'offre", "Le rectangle prix × quantité", "La surface entre l'offre et la demande"], 0, "Au-dessus du prix, sous la demande."),
        ])

    n13 = nm(
        'surplus-prod', "Le surplus des producteurs",
        "Le **surplus du producteur** est la différence entre la recette tirée de la vente et le **coût (variable)** correspondant : **SPj = Rj − Cj**. Le **surplus des producteurs** est la somme des surplus individuels.",
        [
            "Le coût est un **coût d'opportunité** : même un vendeur non producteur renonce à l'usage du bien (valeur qu'il lui accorde s'il le garde).",
            "Le SP **ne tient pas compte des coûts fixes** : il est différent (toujours supérieur) du **profit**.",
            "Courbe d'offre d'un bien discret : **en escalier** (vendeurs classés par coût croissant).",
            "Graphiquement : **surface entre la droite du prix et la courbe d'offre**.",
            "**Le SP augmente avec le prix**.",
        ],
        [
            calc("Voiture A, prix 10 000 € : calcule le surplus des producteurs (en milliers d'euros).", 32.5, "Vendeurs avec coût ≤ 10 : L (5), M (7,5), N (7,5), O (5), P (0), R (7,5), S (0) → SP = **32,5 k€**.", niveau=2, unite='k€', tableau=voit_o),
            calc("Même marché : si le prix passe à 5 000 €, nouveau SP (en milliers d'euros) ?", 7.5, "Vendeurs avec coût ≤ 5 : M, N, R (2,5 chacun) + L et O (0) → SP = **7,5 k€**.", niveau=2, unite='k€', tableau=voit_o),
            calc("Même marché : si le prix passe à 20 000 €, nouveau SP (en milliers d'euros) ?", 107.5, "L 15 + M 17,5 + N 17,5 + O 15 + P 10 + Q 5 + R 17,5 + S 10 = **107,5 k€**.", niveau=3, unite='k€', tableau=voit_o),
            S(calc("TD 3, ex. 1 : à l'équilibre P = 30, calcule le surplus des producteurs.", 1000, "40 × (30 − 10) + 20 × (30 − 20) + 10 × 0 = 800 + 200 = **1 000**.", niveau=3, unite='', tableau=td31o, figure=FESC), td(3)),
            calc("Offre Qo = 10P (P = Q/10), équilibre P = 5, Q = 50. Surplus des producteurs ?", 125, "Triangle : ½ × 50 × 5 = **125**.", niveau=2, unite=''),
            S(calc("TD 2 : un vendeur a un coût de 4 € et vend son kilo de pommes 7 €. Quel est son surplus ?", 3, "Surplus = prix − coût = 7 − 4 = **3 €**.", niveau=1), td(2, True)),
            vf("Le surplus des producteurs est toujours supérieur ou égal au profit.", True, "Il ne déduit pas les coûts fixes."),
            qcm("Graphiquement, le surplus des producteurs est :", ["La surface entre la droite du prix et la courbe d'offre", "La surface sous la courbe de demande", "La recette totale", "Le coût total"], 0, "Sous le prix, au-dessus de l'offre."),
        ])

    F32 = fig('Q (millions)', 'P (€)', 85, 18, [droite(16, -0.2, 0, 80, 'D', 1), droite(1, 0.1, 0, 85, 'O', 2)], titre='TD 3, ex. 2 : équilibre (Q = 50 ; P = 6) — SC en bleu, SP en orange',
              zones=[zone([(0, 16), (0, 6), (50, 6)], 1, 'SC'), zone([(0, 6), (0, 1), (50, 6)], 2, 'SP')], points=[pt(50, 6, 'E')], gradx=[20, 40, 60, 80], grady=[4, 8, 12, 16])
    n14 = nm(
        'surplus-social', "Surplus social et premier théorème du bien-être",
        "Le **surplus social** est le gain total réalisé par l'ensemble des membres de l'économie : **SS = SC + SP**. Graphiquement, c'est la **surface entre les courbes d'offre et de demande** jusqu'à la quantité échangée.",
        [
            "Critère **utilitariste** (Bentham) : on suppose le bien-être mesurable et additionnable ; l'allocation **efficiente** est celle qui **maximise le surplus social** (tous les gains de l'échange sont réalisés, pas de gaspillage).",
            "**Premier théorème du bien-être** : les marchés libres 1) dirigent les biens vers les acheteurs qui leur accordent le plus de valeur ; 2) dirigent la demande vers les producteurs les plus efficaces ; 3) produisent la quantité qui **maximise le surplus social** : l'équilibre de marché est un **optimum social**.",
            "Si Q < Q\\* : des échanges mutuellement avantageux ne sont pas réalisés ; si Q > Q\\* : des échanges désavantageux ont lieu. Dans les deux cas, le SS n'est pas maximal.",
            "Ce résultat suppose la **CPP**. **Défaillances de marché** : pouvoir de marché (monopole, oligopole), barrières à l'entrée, information imparfaite, biens publics et communs.",
        ],
        [
            S(calc("TD 3, ex. 2 : D : P = 16 − 0,2 Q ; O : P = 1 + 0,1 Q ; équilibre Q = 50, P = 6. Surplus des consommateurs (en M€) ?", 250, "½ × 50 × (16 − 6) = **250 M€**.", niveau=2, unite='M€', figure=F32), td(3)),
            S(calc("Même marché : surplus des producteurs (en M€) ?", 125, "½ × 50 × (6 − 1) = **125 M€**.", niveau=2, unite='M€', figure=F32), td(3)),
            S(calc("Même marché : surplus social (en M€) ?", 375, "SS = 250 + 125 = **375 M€**.", niveau=1, unite='M€', figure=F32), td(3)),
            S(calc("TD 3, ex. 1 : surplus social à l'équilibre (SC = 1 100, SP = 1 000) ?", 2100, "SS = **2 100**.", niveau=1, unite='', figure=FESC), td(3)),
            S(calc("TD 3, ex. 1 (question 2) : une expérience donne un surplus social de 1 400. Quelle est la perte par rapport à la théorie ?", 700, "2 100 − 1 400 = **700** : certaines transactions efficaces n'ont pas eu lieu (40 échanges au lieu de 70) ou ont été faites par des agents moins efficaces.", niveau=2, unite=''), td(3)),
            calc("Exercice du cours : Qd = 100 − 10P et Qo = 10P. Surplus social à l'équilibre ?", 250, "SC = 125 et SP = 125 → SS = **250**.", niveau=2, unite=''),
            calc("Marché de la voiture A au prix de 10 000 € (SC = 45 k€, SP = 32,5 k€). Surplus social (k€) ?", 77.5, "45 + 32,5 = **77,5 k€**.", niveau=1, unite='k€'),
            S(vf("Sur un marché en CPP, si la quantité échangée est différente de la quantité d'équilibre, le surplus social n'est pas maximisé.", True, "Premier théorème du bien-être : seule la quantité d'équilibre maximise le SS.", niveau=2), td(5)),
            qcm("Lesquelles sont des défaillances de marché citées par le cours ?", ["Pouvoir de marché d'une ou quelques firmes", "Information imparfaite sur la qualité", "Biens publics et biens communs", "Grand nombre d'acheteurs et de vendeurs"], [0, 1, 2], "Un grand nombre d'agents (atomicité) est au contraire une condition de la CPP.", niveau=2),
        ], figure=F32, formules=["SS = SC + SP", "Droites : SC = ½ × Q* × (Pmax − P*) ; SP = ½ × Q* × (P* − Pmin)"])

    n15 = nm(
        'pareto-equite', "Critères normatifs : Pareto, équité, maximin",
        "Le critère du surplus social suppose qu'on peut mesurer et additionner le bien-être. Les économistes lui préfèrent souvent l'**efficacité au sens de Pareto**.",
        [
            "**Optimum de Pareto** : allocation où il est **impossible d'améliorer la situation d'un individu sans détériorer celle d'un autre**.",
            "Critère de **non-gaspillage**, **ordinal** (pas besoin de mesurer le bien-être), fondé sur l'**unanimité** : A est meilleure que B si chacun est au moins aussi bien loti dans A et au moins un mieux loti.",
            "L'allocation qui maximise le SS est toujours Pareto-optimale, mais **il existe des optimums de Pareto qui ne maximisent pas le SS**.",
            "L'efficience ignore l'**équité** : une situation où un seul individu possède tout peut être Pareto-efficiente.",
            "**Allocation équitable** : répartit de manière juste le bien-être (notion subjective ; l'**égalité** est plus facile à mesurer).",
            "**Critère du maximin (A. Sen)** : la meilleure allocation est celle qui **maximise le surplus de l'individu le moins bien doté**.",
        ],
        [
            calc("Situations (surplus de 3 individus) : A (20, 0, 0), B (15, 5, 5), C (4, 4, 4). Quel est le surplus social de B ?", 25, "15 + 5 + 5 = **25** (A : 20 ; C : 12).", niveau=1, unite=''),
            qcm("Mêmes situations A (20, 0, 0), B (15, 5, 5), C (4, 4, 4). Quelle proposition est vraie ?", ["B est plus juste que C au sens du maximin de Sen", "B et C sont plus efficaces que A", "B domine A au sens de Pareto", "C maximise le surplus social"], 0, "Maximin : min(B) = 5 > min(C) = 4. C (SS = 12) est moins efficace que A (20). B ne domine pas A au sens de Pareto car l'individu 1 perd (15 < 20).", niveau=3),
            vf("Allocation 1 : A gagne 10, B gagne 5. Allocation 2 : A gagne 9, B gagne 7. L'allocation 2 maximise le surplus social et domine l'allocation 1 au sens de Pareto.", False, "Elle maximise le SS (16 > 15) mais **ne domine pas** au sens de Pareto : A y perd (9 < 10).", niveau=2),
            qcm("Une allocation est Pareto-optimale si :", ["On ne peut améliorer la situation d'un individu sans détériorer celle d'un autre", "Tous les individus ont le même revenu", "Le surplus social est nul", "L'État redistribue"], 0, "Définition du cours."),
            vf("Une situation où un seul individu possède toutes les richesses peut être Pareto-efficiente.", True, "Le critère de Pareto ne dit rien sur l'équité."),
            qcm("Le critère du maximin consiste à :", ["Maximiser le surplus du moins bien loti", "Maximiser le surplus total", "Minimiser les inégalités de prix", "Maximiser le profit des entreprises"], 0, "Critère de justice proposé par A. Sen."),
            vf("Le critère de Pareto est cardinal : il suppose de mesurer le bien-être de chacun.", False, "Il est **ordinal** : il suffit de savoir si chacun est mieux ou moins bien loti.", niveau=2),
            calc("Situations de gains (A ; B) : (6 ; 6), (10 ; 1), (8 ; 5), (3 ; 9). Quel est le surplus social maximal ?", 13, "Sommes : 12, 11, 13, 12 → maximum **13** pour (8 ; 5).", niveau=2, unite=''),
            courte("Explique pourquoi un optimum de Pareto peut ne pas être juste.", "Parce que le critère de Pareto ne s'intéresse qu'à l'absence de gaspillage : si un individu possède tout, on ne peut améliorer le sort des autres sans lui prendre quelque chose, donc la situation est Pareto-optimale, bien qu'elle soit très inégalitaire.", niveau=2),
        ])

    F41 = fig('Q', 'P', 10, 10, [droite(10, -1, 0, 10, 'D', 1), droite(0, 1, 0, 10, 'O', 2), seg((0, 8), (9, 8), 'Plancher', 4, True)], titre='TD 4, ex. 1 : D : P = 10 − Q ; O : P = Q ; prix plancher à 8 — perte sèche en rouge',
              zones=[zone([(0, 10), (0, 8), (2, 8)], 1, 'SC'), zone([(0, 8), (2, 8), (2, 2), (0, 0)], 2, 'SP'), zone([(2, 8), (2, 2), (5, 5)], 8, 'PS')], points=[pt(5, 5, 'E')], gradx=[2, 4, 6, 8, 10], grady=[2, 4, 6, 8, 10])
    n16 = nm(
        'intervention-etat', "Intervention de l'État : prix plancher, prix plafond, perte sèche",
        "L'État intervient pour des raisons d'**équité** (redistribution), de **stabilisation** (cycles, inflation) ou d'**efficacité** (externalités, pouvoir de marché). Mais sur un marché en CPP, l'intervention a un **coût** : elle réduit le surplus social.",
        [
            "**Prix plancher** : prix minimum ; **effectif** s'il est **au-dessus** du prix d'équilibre → **excédent de production** (offre > demande). Objectif : soutenir les producteurs. Réponses possibles : quotas, rachat des excédents, subventions aux acheteurs.",
            "**Prix plafond** : prix maximum ; **effectif** s'il est **en dessous** du prix d'équilibre → **pénurie** (demande > offre). Objectif : aider les consommateurs (contrôle des loyers). Réponses : tickets de rationnement (contre le marché noir), production publique, subventions aux offreurs.",
            "Dans les deux cas, la **quantité échangée diminue** : des échanges mutuellement avantageux disparaissent → **perte sèche (charge morte)** = baisse du surplus social par rapport à l'optimum de CPP (« first best »).",
            "Le prix plancher **transfère** du surplus des consommateurs vers les producteurs ; le prix plafond l'inverse (en partie).",
        ],
        [
            S(qcm("TD 4, ex. 1 : équilibre en P = 5. Un prix plancher de 8 € est-il effectif ?", ["Oui, car il est supérieur au prix d'équilibre", "Non, car il est supérieur au prix d'équilibre", "Oui, car il est inférieur au prix d'équilibre", "Cela dépend des quantités"], 0, "Un prix plancher n'est effectif que s'il empêche le prix de **baisser** jusqu'à l'équilibre.", niveau=1, figure=F41), td(4)),
            S(calc("TD 4, ex. 1 : au prix plancher de 8, quel est l'excédent d'offre (quantité offerte − quantité demandée) ?", 6, "Qo = 8 (O : P = Q) ; Qd = 10 − 8 = 2 → excédent d'offre = **6**.", niveau=2, unite='', figure=F41), td(4)),
            S(calc("TD 4, ex. 1 : variation du surplus des consommateurs due au prix plancher ?", -10.5, "Avant : ½ × 5 × 5 = 12,5. Après (Q = 2 au prix 8) : ½ × 2 × 2 = 2. ΔSC = **−10,5**.", niveau=3, unite='', figure=F41), td(4)),
            S(calc("TD 4, ex. 1 : variation du surplus des producteurs ?", 1.5, "Avant : 12,5. Après : 2 × 8 − ½ × 2 × 2 = 14. ΔSP = **+1,5** : le prix plancher favorise les producteurs.", niveau=3, unite='', figure=F41), td(4)),
            S(calc("TD 4, ex. 1 : variation du surplus social (perte sèche) ?", -9, "ΔSS = −10,5 + 1,5 = **−9** (triangle rouge : ½ × (5 − 2) × (8 − 2)).", niveau=3, unite='', figure=F41), td(4)),
            S(qcm("TD 4, ex. 1 : parmi p = 6, p = 5 et p = 3, lequel est un prix plafond effectif ?", ["p = 3", "p = 5", "p = 6", "Aucun"], 0, "Un prix plafond n'est effectif que s'il est **en dessous** du prix d'équilibre (5).", niveau=1), td(4)),
            S(calc("TD 4 : avec un prix plafond de 3, quelle est la pénurie (quantité demandée − quantité offerte) ?", 4, "Qd = 7 ; Qo = 3 → pénurie de **4**.", niveau=2, unite=''), td(4, True)),
            S(calc("TD 3, ex. 2 : le coût augmente de 3 € par utilisateur, entièrement répercuté (offre : P = 4 + 0,1 Q ; demande P = 16 − 0,2 Q). Variation du surplus social (en M€) ?", -135,
                   "Nouvel équilibre : 16 − 0,2Q = 4 + 0,1Q → Q = 40, P = 8. SC = ½ × 40 × 8 = 160 (−90) ; SP = ½ × 40 × 4 = 80 (−45) ; SS = 240 au lieu de 375 → **−135 M€**.", niveau=3, unite='M€'), td(3)),
            qcm("Un prix plafond effectif favorise plutôt :", ["Les consommateurs qui parviennent à acheter", "Les producteurs", "Personne", "L'État"], 0, "Ils paient moins cher, mais certains ne trouvent pas le bien (pénurie) et le SS baisse."),
            vf("Un contrôle des prix (plancher ou plafond effectif) réduit le surplus social.", True, "Il crée une perte sèche."),
        ], figure=F41)
    return chapitre('ch-efficacite', "Chapitre 3 — L'efficacité du marché", [n12, n13, n14, n15, n16])


def ch4():
    art = tab(['Q', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [['CT', 2, 3, 3.6, 3.8, 4, 4.25, 5, 6.2, 9.2, 15.5]], 'Artisan indépendant (cours), CF = 2 €')
    ex1 = tab(['Q', 0, 1, 2, 3, 4, 5, 6], [['CT', 20, 60, 84, 102, 132, 180, 264]], 'Exercice 1 du chapitre 4')
    ex2 = tab(['Q', 0, 1, 2, 3, 4, 5, 6], [['CT', 300, 400, 550, 750, 1000, 1300, 1650]], 'Exercice 2 du chapitre 4 (téléphones)')

    n17 = nm(
        'profit-couts', "Profit et coûts : coût d'opportunité, profit économique et comptable",
        "L'objectif de l'entreprise est de **maximiser son profit** : **Profit = chiffre d'affaires (recettes) − coût total**.",
        [
            "Les économistes raisonnent en **coûts d'opportunité** : tout ce à quoi on renonce, y compris les **coûts implicites**. Ex. artisan : loyer, apprentis, électricité, matières premières **et le salaire qu'il gagnerait ailleurs**.",
            "**Profit comptable = recettes − coûts explicites**.",
            "**Profit économique = recettes − coûts d'opportunité** (explicites + implicites).",
            "Le **profit comptable est toujours supérieur** au profit économique.",
            "L'hypothèse de maximisation du profit comme objectif unique peut être discutée (croissance, part de marché, objectifs sociaux…).",
        ],
        [
            calc("Un artisan a 80 000 € de recettes, 50 000 € de coûts explicites ; il pourrait gagner 25 000 € comme salarié. Profit comptable ?", 30000, "80 000 − 50 000 = **30 000 €**.", niveau=1),
            calc("Même artisan : quel est son profit économique ?", 5000, "80 000 − (50 000 + 25 000) = **5 000 €** : le salaire auquel il renonce est un coût implicite.", niveau=2),
            calc("Une étudiante paie 500 € d'inscription et 1 500 € de matériel ; elle renonce à un emploi payé 12 000 € par an. Coût d'opportunité de son année d'études ?", 14000, "Coûts explicites 2 000 + coût implicite 12 000 = **14 000 €**.", niveau=2),
            S(vf("Le profit comptable est toujours plus élevé que le profit économique.", True, "Il ne déduit pas les coûts implicites (ou il est égal s'il n'y en a pas).", niveau=1), td(5)),
            qcm("Lequel est un coût **implicite** pour un commerçant propriétaire de son local ?", ["Le loyer qu'il pourrait percevoir en louant ce local", "Sa facture d'électricité", "L'achat de marchandises", "Le salaire de son vendeur"], 0, "Il renonce à ce loyer : c'est un coût d'opportunité non décaissé."),
            qcm("Le profit économique se calcule comme :", ["Recettes − coûts d'opportunité", "Recettes − coûts explicites", "Recettes − coûts fixes", "Prix − coût marginal"], 0, "Il inclut les coûts explicites et implicites."),
            vf("Un profit économique nul signifie que l'entreprise ne gagne rien du tout.", False, "Elle couvre tous ses coûts, y compris la rémunération normale de ses facteurs (ce qu'ils gagneraient ailleurs) ; son profit comptable peut être positif.", niveau=3),
            courte("L'objectif unique d'une entreprise est-il toujours de maximiser son profit ? Discute en deux phrases.", "C'est l'hypothèse de base de la théorie, utile pour modéliser. Mais dans la réalité, une entreprise peut aussi viser la croissance, la part de marché, sa survie ou des objectifs sociaux et environnementaux, et ses dirigeants peuvent avoir leurs propres objectifs.", niveau=2),
        ])

    n18 = nm(
        'cout-total', "Coût total, coûts fixes et variables ; court et long terme",
        "Le **coût total (CT)** est le montant engagé pour se procurer et utiliser les facteurs nécessaires à la production d'une quantité donnée (on suppose les inputs utilisés sans gaspillage, au coût le plus bas). **CT = CF + CV**.",
        [
            "**Coûts fixes (CF)** : indépendants de la quantité produite, dus même si la production est nulle (loyer ; salaires à court terme).",
            "**Coûts variables (CV)** : évoluent avec la quantité produite (matières premières).",
            "**CF = CT pour Q = 0**.",
            "Forme classique de CT : croissant, d'abord **concave** (pente décroissante) puis **convexe** (pente croissante).",
            "Fonction de production : **Y = f(C, W)** (capital, travail) ; les inputs entrent, l'output sort.",
            "**Court terme** : certains coûts sont fixes (pas le temps de les ajuster). **Long terme** : **tous les coûts deviennent variables** (le salaire n'est fixe que le temps nécessaire pour licencier).",
        ],
        [
            calc("Artisan (cours) : CT = 3,80 € pour Q = 3 et CF = 2 €. Quel est le coût variable ?", 1.8, "CV = CT − CF = 3,80 − 2 = **1,80 €**.", niveau=1, tableau=art),
            calc("Exercice 1 du chapitre : CT = 20 pour Q = 0. Quel est le coût fixe ?", 20, "À production nulle, CT = CF = **20**.", niveau=1, unite='', tableau=ex1),
            calc("Même exercice : quel est le coût variable pour Q = 4 ?", 112, "CV = 132 − 20 = **112**.", niveau=1, unite='', tableau=ex1),
            S(calc("TD 4, ex. 2 : CF = 4 milliers d'euros, CV = 8 pour Q = 2 tonnes. Coût total ?", 12, "CT = 4 + 8 = **12 milliers d'euros**.", niveau=1, unite='k€'), td(4)),
            qcm("Lequel est un coût fixe à court terme ?", ["Le loyer du local", "Les matières premières", "L'énergie consommée par les machines", "Les emballages"], 0, "Il est dû même si l'on ne produit rien."),
            vf("À long terme, tous les coûts deviennent variables.", True, "Le producteur a le temps d'ajuster tous ses facteurs."),
            qcm("Selon le cours, la courbe de coût total est généralement :", ["Croissante, d'abord concave puis convexe", "Décroissante", "Une droite horizontale", "Toujours convexe"], 0, "La pente décroît puis augmente (artisan : jusqu'à Q = 3 puis au-delà)."),
            vf("Les coûts fixes varient avec la quantité produite.", False, "Par définition, ils sont indépendants de la quantité."),
        ], formules=["CT = CF + CV", "CF = CT(0)"])

    Ftd4 = fig('Q (tonnes)', 'Coûts (k€)', 2.6, 11, courbes=[courbe([(0.6, 10.33), (1, 7.5), (1.4, 6.43), (1.6, 6.25), (2, 6), (2.4, 6.13)], 'CM', 1), courbe([(0.6, 3.67), (1, 3.5), (1.4, 3.57), (1.6, 3.75), (2, 4), (2.4, 4.46)], 'CVM', 3), courbe([(0.6, 3.3), (1, 3.5), (1.4, 4.1), (1.6, 4.6), (2, 6), (2.4, 7.8)], 'Cm', 2)],
               titre='TD 4, ex. 2 : CM, CVM et Cm — Cm coupe CVM en son minimum (Q = 1 ; 3,5) et CM en son minimum (Q = 2 ; 6)', points=[pt(1, 3.5, 'F'), pt(2, 6, 'R')], gradx=[0.5, 1, 1.5, 2, 2.5], grady=[2, 4, 6, 8, 10])
    td42 = tab(['Q (t)', 'CV (k€)', 'Cm (k€)'], [[0.6, 2.2, 3.3], [1, 3.5, 3.5], [1.4, 5, 4.1], [1.6, 6, 4.6], [2, 8, 6], [2.4, 10.7, 7.8]], 'TD 4, ex. 2 (CF = 4 k€)')
    n19 = nm(
        'couts-moyens', "Coût moyen, coût variable moyen, coût marginal",
        "Pour décider combien produire, l'entreprise doit savoir combien coûte **en moyenne** une unité et combien coûte **une unité supplémentaire**.",
        [
            "**Coût moyen CM = CT / Q** ; **coût variable moyen CVM = CV / Q** ; **coût fixe moyen CFM = CF / Q** ; **CM = CVM + CFM**.",
            "**Coût marginal Cm = ΔCT / ΔQ** (= ΔCV / ΔQ) : coût de l'unité supplémentaire.",
            "**Cm** et **CM** ont généralement une **forme en U** ; le **CFM décroît** et tend vers 0 ; le **CVM** est aussi en U.",
            "**La courbe de Cm coupe le CM et le CVM en leur minimum**. Tant que Cm < CM, le CM diminue ; quand Cm > CM, le CM augmente.",
            "Le **CM définit le seuil de profitabilité** : si P > CM, l'entreprise fait des profits ; si P < CM, des pertes.",
        ],
        [
            calc("Exercice 1 du chapitre : CT(2) = 84. Quel est le coût moyen pour Q = 2 ?", 42, "CM = 84 / 2 = **42**.", niveau=1, unite='', tableau=ex1),
            calc("Même exercice : quel est le coût marginal de la 3e unité (CT passe de 84 à 102) ?", 18, "Cm = 102 − 84 = **18**.", niveau=1, unite='', tableau=ex1),
            calc("Même exercice : coût variable moyen pour Q = 3 (CF = 20, au centième) ?", 82 / 3, "CV = 102 − 20 = 82 ; CVM = 82/3 = **27,33**.", niveau=2, unite='', tolerance=0.01, tableau=ex1),
            calc("Exercice 2 (téléphones) : quel est le coût marginal de la 4e unité (CT : 750 → 1 000) ?", 250, "Cm = **250**, égal au CM minimal (750/3 = 1 000/4 = 250) : le Cm passe par le minimum du CM.", niveau=2, unite='', tableau=ex2),
            S(calc("TD 4, ex. 2 : coût moyen pour Q = 1,4 tonne (CV = 5, CF = 4), au centième ?", 9 / 1.4, "CT = 9 ; CM = 9 / 1,4 = **6,43 k€**.", niveau=2, unite='k€', tolerance=0.01, tableau=td42), td(4)),
            S(calc("TD 4, ex. 2 : coût variable moyen pour Q = 1 tonne ?", 3.5, "CVM = 3,5 / 1 = **3,5 k€** : c'est le minimum du CVM, où il est égal au Cm (3,5).", niveau=2, unite='k€', tableau=td42, figure=Ftd4), td(4)),
            S(calc("TD 4, ex. 2 : quel est le minimum du coût moyen (en k€) ?", 6, "CM(2) = (4 + 8)/2 = **6** = Cm(2) : minimum du CM.", niveau=2, unite='k€', tableau=td42, figure=Ftd4), td(4)),
            S(vf("Lorsque le coût marginal est situé en dessous du coût moyen, la courbe de coût moyen est obligatoirement croissante.", False, "C'est l'inverse : si Cm < CM, chaque unité supplémentaire coûte moins que la moyenne, donc le CM **diminue**.", niveau=2), td(5)),
            S(vf("La courbe de coût marginal passe toujours par le minimum des courbes de coût moyen et de coût fixe moyen.", False, "Elle passe par le minimum du CM et du **CVM** ; le CFM est toujours décroissant, il n'a pas de minimum.", niveau=3), td(5)),
            S(vf("Comme le coût total augmente forcément avec la production, la courbe de coût moyen est toujours croissante.", False, "Le CT augmente, mais le CM (CT/Q) est en U : il commence par diminuer.", niveau=2), td(5)),
        ], figure=Ftd4, formules=["CM = CT/Q ; CVM = CV/Q ; CFM = CF/Q", "Cm = ΔCT/ΔQ", "Cm coupe CM et CVM en leur minimum"])
    return chapitre('ch-couts', "Chapitre 4 — Les fondements de l'offre : les coûts", [n17, n18, n19])


def ch5():
    ct5 = [10, 19, 26, 31, 35, 40, 47, 56, 66, 78, 93, 110]
    cm5 = [ct5[i] - ct5[i - 1] for i in range(1, 12)]
    td52 = tab(['Q (milliers)'] + list(range(12)), [['Coût total'] + ct5], 'TD 5, ex. 2')
    sucre = tab(['Q', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [['CT', 50, 75, 95, 125, 175, 250, 350, 475, 625, 800]], 'Entreprise sucrière (cours), p = 100')

    n20 = nm(
        'max-profit', "Maximisation du profit : Rm = Cm, et P = Cm en CPP",
        "Profit = **recette totale RT − coût total CT**. **Recette moyenne RM = RT/Q** ; **recette marginale Rm = ΔRT/ΔQ**.",
        [
            "En CPP, l'entreprise est **preneuse de prix** : RT = P × Q, donc **RM = Rm = P** (doubler la production double le chiffre d'affaires).",
            "**Toute entreprise** maximise son profit en produisant la quantité où **Rm = Cm** ; l'entreprise en CPP produit où **P = Cm**.",
            "Raisonnement à la marge : tant que Cm < Rm, produire une unité de plus augmente le profit ; si Cm > Rm, il faut réduire la production.",
            "**Profit Π = (P − CM) × Q** : rectangle entre le prix et le CM ; positif si P > CM, négatif si P < CM.",
            "Exemple (sucre, P = 100) : profit maximal de 250 pour 5 ou 6 quintaux, là où P = Cm.",
        ],
        [
            S(calc("TD 5, ex. 2 : CT(4) = 35 et CT(5) = 40. Coût marginal de la 5e unité ?", 5, "Cm = 40 − 35 = **5**.", niveau=1, unite='', tableau=td52), td(5)),
            S(calc("TD 5, ex. 2 : avec P = 10, quelle quantité maximise le profit (en milliers) ?", 8,
                   "Cm : %s. On produit tant que Cm ≤ P : le Cm de la 8e unité vaut 10 (= P, transaction à surplus nul réalisée), celui de la 9e vaut 12 > 10 → **Q = 8**." % ' ; '.join(str(x) for x in cm5), niveau=2, unite='', tableau=td52), td(5)),
            S(calc("TD 5, ex. 2 : profit de chaque entreprise avec P = 10 ?", 10 * 8 - 66, "RT = 10 × 8 = 80 ; CT = 66 → profit = **14**.", niveau=2, unite='', tableau=td52), td(5)),
            S(calc("TD 5, ex. 2 : le prix passe à P = 7. Quantité qui maximise le profit ?", 6, "Cm de la 6e unité = 7 = P ; celui de la 7e = 9 > 7 → **Q = 6**.", niveau=2, unite='', tableau=td52), td(5)),
            S(calc("TD 5, ex. 2 : profit avec P = 7 ?", 7 * 6 - 47, "RT = 42 ; CT = 47 → profit = **−5** (perte).", niveau=2, unite='', tableau=td52), td(5)),
            calc("Entreprise sucrière (cours, P = 100) : profit pour Q = 5 ?", 250, "RT = 500 ; CT = 250 → profit = **250** (maximum, comme pour Q = 6).", niveau=1, unite='', tableau=sucre),
            calc("Une entreprise en CPP vend 40 unités au prix de 12 € ; son coût moyen est de 9 €. Quel est son profit ?", 120, "Π = (P − CM) × Q = (12 − 9) × 40 = **120 €**.", niveau=1),
            S(vf("Sur un marché concurrentiel ou non, une firme produit jusqu'au point où sa recette marginale est égale à son coût marginal.", True, "Rm = Cm est la règle générale ; en CPP elle devient P = Cm.", niveau=1), td(5)),
            vf("Pour l'entreprise en CPP, la recette marginale est égale au prix du marché.", True, "Elle vend chaque unité supplémentaire au prix du marché, qu'elle ne peut pas influencer."),
        ], formules=["Π = RT − CT = (P − CM) × Q", "Optimum : Rm = Cm ; en CPP : P = Cm"])

    Ftd4 = fig('Q (tonnes)', 'Prix, coûts (k€)', 2.6, 11, courbes=[courbe([(0.6, 10.33), (1, 7.5), (1.4, 6.43), (1.6, 6.25), (2, 6), (2.4, 6.13)], 'CM', 1), courbe([(0.6, 3.67), (1, 3.5), (1.4, 3.57), (1.6, 3.75), (2, 4), (2.4, 4.46)], 'CVM', 3), courbe([(0.6, 3.3), (1, 3.5), (1.4, 4.1), (1.6, 4.6), (2, 6), (2.4, 7.8)], 'Cm', 2)],
               titre='TD 4, ex. 2 : seuil de fermeture F (P = 3,5) et seuil de rentabilité R (P = 6) ; profit pour P = 7,8 en vert', zones=[zone([(0, 7.8), (2.4, 7.8), (2.4, 6.13), (0, 6.13)], 3, 'Profit')],
               points=[pt(1, 3.5, 'F'), pt(2, 6, 'R')], gradx=[0.5, 1, 1.5, 2, 2.5], grady=[2, 4, 6, 8, 10])
    n21 = nm(
        'seuils', "Seuils de rentabilité et de fermeture ; offre de court terme",
        "L'entreprise concurrentielle produit toujours où P = Cm, et le Cm passe par le minimum du CM et du CVM. On en déduit deux **seuils**.",
        [
            "**Seuil de rentabilité (profitabilité)** : **P = min CM** ; au-dessus, profit positif.",
            "**Seuil de fermeture** : **P = min CVM** à court terme (et min CM à long terme).",
            "**Court terme** : les coûts fixes sont dus même sans produire (profit = −CF si l'on s'arrête). L'entreprise continue tant que **P > CVM** : elle couvre ses coûts variables et une partie des coûts fixes, donc **minimise ses pertes**.",
            "Entre min CVM et min CM : l'entreprise **produit à perte** (ex. compagnies aériennes maintenant des lignes non rentables).",
            "**Courbe d'offre de court terme** de l'entreprise : partie de la courbe de **Cm au-dessus du CVM** (à partir du seuil de fermeture).",
            "**Offre de marché de court terme** : somme des offres individuelles, nombre d'entreprises fixe.",
        ],
        [
            S(calc("TD 4, ex. 2 : quel est le seuil de fermeture (en k€) ?", 3.5, "Seuil de fermeture = min CVM = **3,5** (Q = 1, où Cm = CVM).", niveau=2, unite='k€', figure=Ftd4), td(4)),
            S(calc("TD 4, ex. 2 : quel est le seuil de rentabilité (en k€) ?", 6, "Seuil de rentabilité = min CM = **6** (Q = 2).", niveau=2, unite='k€', figure=Ftd4), td(4)),
            S(calc("TD 4, ex. 2 : si le prix du marché est de 3 k€, quelle quantité l'entreprise produit-elle ?", 0, "3 < 3,5 (seuil de fermeture) : elle **ne produit pas** (Q = 0).", niveau=2, unite='t', figure=Ftd4), td(4)),
            S(calc("Avec p = 3, quel est alors son profit (en k€) ?", -4, "Elle ne produit pas mais paie ses coûts fixes : profit = −CF = **−4 k€**.", niveau=2, unite='k€'), td(4)),
            S(calc("TD 4, ex. 2 : avec p = 7,8, l'entreprise produit 2,4 t (P = Cm). Quel est son profit (en k€, au centième) ?", 7.8 * 2.4 - 14.7, "RT = 7,8 × 2,4 = 18,72 ; CT = 4 + 10,7 = 14,7 → profit = **4,02 k€** (rectangle vert).", niveau=3, unite='k€', tolerance=0.01, figure=Ftd4), td(4)),
            S(qcm("TD 4, ex. 2 : lorsque le prix est compris entre 3,5 et 6, l'entreprise :", ["Fait des pertes mais continue de produire à court terme", "Fait des profits", "Doit fermer immédiatement", "Ne supporte aucun coût"], 0, "P < min CM → pertes ; P > min CVM → elle couvre ses coûts variables et une partie des coûts fixes : produire limite les pertes.", niveau=2, figure=Ftd4), td(4)),
            S(vf("Une entreprise en CPP doit continuer son activité à court terme lorsque le prix est compris entre son coût moyen et son coût variable moyen.", True, "Elle réduit ainsi ses pertes (elle couvre une partie de ses coûts fixes).", niveau=2), td(5)),
            S(courte("TD 5, ex. 2 : avec P = 7, les entreprises perdent 5 (Q = 6, CV = 37). Que vont-elles faire à court terme et pourquoi ?", "Elles continuent de produire : le prix (7) est supérieur à leur CVM (37/6 ≈ 6,17). En produisant, elles perdent 5 ; en s'arrêtant, elles perdraient tout le coût fixe, soit 10.", niveau=3), td(5)),
            qcm("La courbe d'offre de court terme de l'entreprise concurrentielle est :", ["La partie du Cm située au-dessus du CVM", "La courbe de CM", "La partie du Cm située au-dessus du CM uniquement", "La courbe de CVM"], 0, "Pour chaque prix au-dessus du seuil de fermeture, elle indique la quantité qui maximise le profit."),
        ], figure=Ftd4, formules=["Seuil de rentabilité : P = min CM", "Seuil de fermeture (CT) : P = min CVM", "Offre CT = Cm au-dessus du CVM"])

    Flt = fig('Q', 'P', 360, 13, [droite(11, -0.02, 0, 350, 'D', 1), droite(-1, 0.04, 50, 325, 'Offre', 2), droite(8, -0.02, 0, 350, "D'", 1, True)], titre='TD 5, ex. 3 : demande p = 11 − 0,02 Q, offre p = 0,04 Q − 1 ; après le choc, D\' : p = 8 − 0,02 Q',
              points=[pt(0, 11, 'A'), pt(100, 9, 'B'), pt(300, 5, 'C'), pt(200, 7, 'E'), pt(150, 5, "E'")], gradx=[100, 200, 300], grady=[2, 4, 6, 8, 10, 12])
    n22 = nm(
        'long-terme', "Offre et équilibre de long terme en CPP",
        "À **long terme**, les coûts fixes sont nuls (tous les coûts sont variables) et les entreprises peuvent **entrer ou sortir** librement du marché.",
        [
            "Seuils de fermeture et de rentabilité **coïncident** : l'entreprise produit tant que **P > CM (= CVM)** ; sinon elle **cesse définitivement** son activité.",
            "**Offre individuelle de long terme** : partie du **Cm au-dessus du CM**.",
            "Si les entreprises font des **profits**, de nouvelles firmes entrent → l'offre de marché augmente → le prix baisse jusqu'à ce que le profit soit nul.",
            "**Équilibre de long terme : P = Cm = min CM** → **profit économique nul** (mais profit comptable possible) : condition d'efficience des marchés.",
            "**Économies d'échelle** quand le CM diminue avec la quantité ; **déséconomies d'échelle** quand il augmente.",
        ],
        [
            S(vf("Dans le cas de la CPP, à l'équilibre de long terme du marché, le profit (économique) de toutes les entreprises est nul.", True, "Les entrées font baisser le prix jusqu'à P = min CM.", niveau=1), td(5)),
            S(vf("À long terme, en CPP, seules les entreprises qui réalisent des profits très élevés subsistent sur le marché.", False, "À long terme, les entreprises restantes font un profit économique **nul** (P = min CM).", niveau=1), td(5)),
            S(vf("À long terme, la courbe de coût marginal passe toujours par le minimum de la courbe de coût variable moyen.", True, "Le Cm passe toujours par le minimum du CVM ; à long terme, CVM = CM (pas de coût fixe).", niveau=3), td(5)),
            S(calc("TD 5, ex. 3 : la demande passe par A (0 ; 11), B (100 ; 9) et C (300 ; 5). Quelle est sa pente Δp/ΔQ ?", -0.02, "(9 − 11)/100 = **−0,02** → p = 11 − 0,02 Q.", niveau=2, unite='', tolerance=0.001, figure=Flt), td(5)),
            S(calc("TD 5, ex. 3 : avec l'offre p = 0,04 Q − 1, quelle est la quantité d'équilibre du marché ?", 200, "11 − 0,02 Q = 0,04 Q − 1 → 0,06 Q = 12 → **Q = 200** ; p = 7.", niveau=2, unite='', figure=Flt), td(5, True)),
            S(calc("TD 5, ex. 3 : les consommateurs paient 3 € de moins pour chaque unité (p = 8 − 0,02 Q). Nouveau prix d'équilibre ?", 5, "8 − 0,02 Q = 0,04 Q − 1 → Q = 150 ; **p = 5**.", niveau=3, unite='€', figure=Flt), td(5, True)),
            S(qcm("TD 5, ex. 3 : le minimum du coût moyen de l'entreprise LEG est d'environ 5,8 €. Au nouveau prix de 5 €, à long terme, LEG :", ["A intérêt à quitter le marché", "Fait des profits et reste", "Augmente sa production", "Est au seuil de rentabilité"], 0, "À long terme, P < min CM → pertes non compensables : l'entreprise cesse son activité (des sorties feront remonter le prix).", niveau=3), td(5, True)),
            qcm("Que se passe-t-il à long terme si les entreprises d'un marché en CPP réalisent des profits positifs ?", ["De nouvelles entreprises entrent, l'offre augmente et le prix baisse", "Les entreprises augmentent leurs prix", "La demande diminue", "Rien"], 0, "La libre entrée attire de nouvelles firmes jusqu'à un profit nul."),
            qcm("Une entreprise réalise des économies d'échelle lorsque :", ["Son coût moyen diminue quand la production augmente", "Son coût total diminue", "Son coût marginal est nul", "Son prix augmente"], 0, "Sur la partie décroissante du CM.", niveau=2),
        ], figure=Flt, formules=["Long terme : P = Cm = min CM ; profit économique nul"])
    return chapitre('ch-entreprise-cpp', "Chapitre 5 — L'entreprise en concurrence pure et parfaite", [n20, n21, n22])
