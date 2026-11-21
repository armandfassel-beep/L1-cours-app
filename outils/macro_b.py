"""Macroéconomie — Chapitre 2 (consommation) et chapitre 3 (investissement)."""
from macro_base import *


def chapitres():
    return [ch2(), ch3()]


# Figures du TD 2 (reproduites)
FIG1 = fig('Y', 'C, S', 100, 100, [droite(30, 0.5, 0, 100, 'C', 1)], titre='Figure 1 du TD 2 : fonction de consommation et droite à 45°', bissectrice=True,
           guides=[gd(60, 60, 'Y1', 'A'), gd(80, 70, None, 'B'), gd(80, 80, 'Y2', 'D'), gd(90, 75, None, 'C'), gd(90, 90, 'Y3', 'E')])
FIG2 = fig('Y', 'C, I', 115, 115, [droite(40, 0.2, 10, 112, 'C', 1), droite(65, 0.2, 10, 112, 'C + I', 2)], titre='Figure 2 du TD 2 : consommation, demande C + I et droite à 45°', bissectrice=True,
           guides=[gd(30, 30, 'Y1', 'A'), gd(30, 46, None, 'B'), gd(30, 71, None, 'C'), gd(81.25, 56.25, None, 'D'), gd(81.25, 81.25, 'Y2', 'F'), gd(105, 61, None, 'E'), gd(105, 86, None, 'G'), gd(105, 105, 'Y3', 'H')])
FIG_TD2 = fig('Y (Mds €)', 'C, D', 2200, 2200, [droite(80, 0.6, 0, 2200, 'C', 1), droite(680, 0.6, 0, 2200, 'D = C + I0', 2)], titre='TD 2 : C = 80 + 0,6 Y ; D = 680 + 0,6 Y ; équilibre en Y* = 1 700', bissectrice=True,
              points=[pt(1700, 1700, 'E')], guides=[gd(1700, 1700, 'Y* = 1 700')], gradx=[500, 1000, 1500, 2000], grady=[500, 1000, 1500, 2000])


def ch2():
    n11 = nm(
        'demande-globale', "Composantes de la demande globale ; visions néoclassique et keynésienne de la consommation",
        "En économie fermée, l'équilibre s'écrit **Y = C + I + G** ; en économie ouverte, **Y = C + I + G + NX** (NX = X − IM, exportations nettes). On suppose ici que l'**offre s'adapte à la demande** (contraintes de capacité ignorées).",
        [
            "Cet équilibre est toujours vérifié grâce aux **variations de stocks** comptées dans l'investissement (en récession, les invendus s'accumulent en stocks).",
            "Parts dans le PIB (UE) : consommation des ménages **50 à 60 %**, dépenses publiques **20 à 25 %**, investissement **≈ 20 %** (UE-28, 2016).",
            "La consommation et les dépenses publiques varient peu ; l'**investissement fluctue beaucoup** et contribue autant que la consommation aux fluctuations.",
            "**G** : consommation de l'État (traitements des fonctionnaires, fournitures) et investissements publics (routes, bâtiments) ; considérées comme **autonomes** (fixées par l'État) et financées par les recettes fiscales T.",
            "**Consommation finale des ménages** : dépenses en biens et services destinés à la satisfaction de besoins personnels et non productifs.",
            "**Vision néoclassique** (micro) : l'individu choisit d'abord son **épargne** en fonction du **taux d'intérêt** (prix de la renonciation à la consommation présente) ; il consomme le reste.",
            "**Vision keynésienne** (macro) : la consommation dépend du **revenu (disponible)** ; l'**épargne est un résidu** (« fuite » du circuit) ; les prix sont rigides.",
            "Autres déterminants : richesse, anticipations, chômage, incertitude, cycle de vie, structure des revenus (propension à consommer plus forte pour les salaires et transferts que pour les revenus du capital).",
        ],
        [
            qcm("Dans l'analyse **keynésienne**, la principale variable qui détermine la consommation est :", ["Le revenu", "Le taux d'intérêt", "La masse monétaire", "Le niveau des prix"], 0, "Keynes relie la consommation au revenu ; chez les néoclassiques, c'est le taux d'intérêt qui arbitre entre épargne et consommation."),
            qcm("Dans l'analyse **néoclassique**, le taux d'intérêt est interprété comme :", ["Le prix de la renonciation à la consommation présente", "Le coût de la main-d'œuvre", "Le prix de la monnaie fiduciaire", "Un impôt sur l'épargne"], 0, "L'individu épargne davantage si le taux d'intérêt rémunère mieux le report de consommation."),
            vf("Pour Keynes, l'épargne est un résidu : la part du revenu qui n'est pas consommée.", True, "La consommation est la première décision ; l'épargne en découle."),
            calc("Économie ouverte : C = 1 200, I = 450, G = 500, X = 600, IM = 650. Quel est le PIB ?", 2100, "Y = C + I + G + (X − IM) = 1 200 + 450 + 500 − 50 = **2 100**.", niveau=1, unite=''),
            calc("Avec ces données (C = 1 200, Y = 2 100), quelle est la part de la consommation dans le PIB (en %, au dixième) ?", 1200 / 2100 * 100, "1 200 ÷ 2 100 = **57,1 %**, conforme à la fourchette 50-60 % du cours.", niveau=1, unite='%', tolerance=0.1),
            qcm("Quelle composante de la demande est la **plus volatile** ?", ["L'investissement", "La consommation des ménages", "Les dépenses publiques", "Toutes varient autant"], 0, "Bien que minoritaire, l'investissement fluctue fortement."),
            qcm("Comment l'équilibre Y = C + I + G reste-t-il vérifié en période de récession ?", ["Par l'accumulation de stocks d'invendus, comptés dans l'investissement", "Par une baisse automatique des prix", "Par une hausse des importations", "Il n'est pas vérifié"], 0, "Les variations de stocks sont intégrées à l'investissement privé.", niveau=2),
            qcm("Lesquels sont des déterminants de la consommation cités dans le cours ?", ["Le revenu", "La richesse", "Les anticipations de revenus et de prix", "Le nombre d'entreprises"], [0, 1, 2], "S'y ajoutent le chômage, l'incertitude, la position dans le cycle de vie et la structure des revenus.", niveau=2),
            S(courte("En quoi les hypothèses du modèle keynésien diffèrent-elles de l'analyse néoclassique ?",
                     "Chez Keynes : raisonnement macroéconomique, prix rigides, la production s'ajuste à la demande effective, la consommation dépend du revenu courant et l'épargne est un résidu ; le chômage peut durer. Chez les néoclassiques : prix flexibles, marchés qui s'équilibrent, choix individuels où le taux d'intérêt arbitre entre consommation et épargne.", niveau=3), td(2)),
        ])

    n12 = nm(
        'loi-psycho', "Loi psychologique fondamentale et fonction de consommation",
        "« En moyenne et la plupart du temps, les hommes tendent à accroître leur consommation à mesure que leur revenu croît, mais **non d'une quantité aussi grande** que l'accroissement du revenu » (Keynes, 1936).",
        [
            "Deux idées : 1) tout accroissement du revenu disponible accroît la consommation ; 2) le **supplément de consommation est inférieur au supplément de revenu**.",
            "Ce n'est pas une loi scientifique : c'est une **hypothèse** fondée sur la « connaissance de la nature humaine » ; les tests empiriques ne la valident qu'en partie.",
            "**C = f(Y)** ; trois modélisations compatibles : **affine** C = cY + C0 ; **linéaire** C = cY ; **concave** C = f(Y) + C0.",
            "**C0** = consommation **incompressible** (autonome), consommée même si Y = 0 ; **c** = propension marginale à consommer (pente), **0 < c < 1**.",
            "Avec impôts : la consommation dépend du **revenu disponible** : C = c (Y − T) + C0.",
            "La fonction **affine** est la plus utilisée : conforme à Keynes et simple. Keynes suppose que c diminue quand le revenu augmente : la fonction affine est une **approximation d'une fonction concave**.",
        ],
        [
            S(calc("TD 2 : Y = 1 700 Mds€, C = 1 100 Mds€ et PmC = 0,6. Calcule la consommation incompressible C0 (ordonnée à l'origine).", 80,
                   "C = cY + C0 → C0 = 1 100 − 0,6 × 1 700 = 1 100 − 1 020 = **80 Mds€**. La pente de la droite est 0,6.", niveau=2, unite='Mds€', figure=FIG_TD2), td(2)),
            calc("C = 0,75 Y + 200. Quelle est la consommation lorsque Y = 1 000 ?", 950, "C = 0,75 × 1 000 + 200 = **950**.", niveau=1, unite=''),
            calc("C = 0,8 (Y − T) + 100, avec Y = 2 000 et T = 500. Quelle est la consommation ?", 1300, "Revenu disponible = 1 500 ; C = 0,8 × 1 500 + 100 = **1 300**.", niveau=2, unite=''),
            qcm("Dans C = cY + C0, que représente C0 ?", ["La consommation incompressible (autonome)", "La propension marginale à consommer", "L'épargne", "L'investissement"], 0, "C0 est consommé même quand le revenu est nul."),
            qcm("Quelle forme de fonction de consommation **n'a pas** de consommation incompressible ?", ["La fonction linéaire C = cY", "La fonction affine C = cY + C0", "La fonction concave C = f(Y) + C0", "Aucune"], 0, "Linéaire : si Y = 0, alors C = 0."),
            vf("Selon la loi psychologique fondamentale, quand le revenu augmente de 100, la consommation augmente de plus de 100.", False, "Elle augmente, mais **de moins** que 100 (0 < c < 1)."),
            S(vf("Une fonction de consommation affine est conforme aux hypothèses de Keynes.", True,
                 "Elle respecte 0 < c < 1 et une PMC décroissante ; c'est une approximation (c constant) de la fonction concave que suggère Keynes.", niveau=2), td(2)),
            S(qcm("Sur le graphique du TD 2, que représente la pente de la droite C ?", ["La propension marginale à consommer (0,6)", "La consommation incompressible (80)", "Le revenu d'équilibre", "L'investissement"], 0,
                  "La pente d'une droite affine C = cY + C0 est c = 0,6 ; l'ordonnée à l'origine est C0 = 80.", niveau=1, figure=FIG_TD2), td(2)),
            courte("Pourquoi la « loi psychologique fondamentale » n'est-elle pas une véritable loi au sens scientifique ?", "Parce qu'elle ne repose ni sur un modèle théorique ni sur des vérifications empiriques : c'est une hypothèse que Keynes formule à partir de sa connaissance de la nature humaine et de l'expérience.", niveau=2),
        ])

    n13 = nm(
        'propensions', "Propensions moyenne et marginale à consommer ; élasticité",
        "La **propension moyenne à consommer** est la part du revenu consommée ; la **propension marginale à consommer** est la part d'un supplément de revenu qui est consommée.",
        [
            "**PMC = C / Y** ; **PmC = ΔC / ΔY = c** (dérivée de C par rapport à Y).",
            "Fonction **affine** : PMC = c + C0/Y → **décroissante** avec le revenu ; PmC = c **constante** ; **PmC < PMC** ; quand Y → ∞, **PMC → c**.",
            "Keynes justifie la baisse de la PMC par la **hiérarchie et la satiété des besoins**.",
            "Fonction **linéaire** : PMC = PmC = c (constantes).",
            "Fonction **concave** : PMC et PmC **toutes deux décroissantes** (dérivée seconde f''(Y) < 0).",
            "**Élasticité de la consommation au revenu** : ε = (ΔC/C) / (ΔY/Y) = **PmC / PMC < 1** : si le revenu augmente de 1 %, la consommation augmente de moins de 1 %.",
        ],
        [
            calc("C = 0,8 Y + 100. Calcule la PMC pour Y = 1 000.", 0.9, "C = 900 ; PMC = 900 / 1 000 = **0,9**.", niveau=1, unite=''),
            calc("Avec C = 0,8 Y + 100 et Y = 1 000, quelle est l'élasticité de la consommation au revenu (au millième) ?", 0.8 / 0.9, "ε = PmC / PMC = 0,8 / 0,9 = **0,889** < 1.", niveau=2, unite='', tolerance=0.001),
            calc("Le revenu passe de 2 000 à 2 400 et la consommation de 1 700 à 1 980. Quelle est la propension marginale à consommer ?", 0.7, "PmC = ΔC / ΔY = 280 / 400 = **0,7**.", niveau=1, unite=''),
            calc("C = 0,6 Y + 80 (TD 2). Quelle est la PMC lorsque Y = 1 700 (au millième) ?", 1100 / 1700, "PMC = 1 100 / 1 700 = **0,647**, supérieure à la PmC (0,6).", niveau=2, unite='', tolerance=0.001),
            S(qcm("Avec C = cY + C0, la dérivée de la PMC par rapport au revenu vaut :", ["−C0 / Y²", "c", "C0 / Y", "0"], 0,
                  "PMC = c + C0/Y donc d(PMC)/dY = −C0/Y² < 0 : la PMC décroît quand le revenu augmente, ce qui vérifie la loi psychologique fondamentale.", niveau=3), td(2)),
            S(qcm("Vers quelle valeur tend la PMC quand le revenu tend vers l'infini (fonction affine) ?", ["Vers la PmC c", "Vers 0", "Vers 1", "Vers C0"], 0, "C0/Y → 0, donc PMC → c.", niveau=2), td(2)),
            qcm("Pour une fonction de consommation **concave** :", ["La PMC et la PmC décroissent toutes deux avec le revenu", "La PmC est constante", "La PMC est constante", "La PmC augmente"], 0, "La pente (PmC) diminue le long d'une courbe concave."),
            vf("Pour une fonction linéaire C = cY, la PMC est égale à la PmC.", True, "PMC = cY/Y = c = PmC."),
            S(courte("Rappelle la définition de la PmC et l'hypothèse de Keynes sur l'évolution de sa valeur.",
                     "La PmC est la part d'un revenu supplémentaire qui est consommée (ΔC/ΔY), comprise entre 0 et 1. Keynes suppose qu'elle a tendance à diminuer quand le revenu augmente.", niveau=2), td(2)),
        ])

    n14 = nm(
        'epargne', "La fonction d'épargne",
        "L'**épargne** est la partie du revenu qui n'est pas consommée : **S = Y − C**. Avec C = cY + C0, la fonction d'épargne est **S = (1 − c) Y − C0 = sY − C0**.",
        [
            "**PMS = S / Y** ; **PMC + PMS = 1**.",
            "**PmS = ΔS / ΔY = s** ; **PmC + PmS = c + s = 1**, donc s = 1 − c.",
            "PMS = s − C0/Y : **croissante** avec le revenu (car la PMC diminue).",
            "Si Y = 0, S = −C0 : **désépargne**.",
            "**Seuil** où l'épargne devient positive : S = 0 ⇔ **Y = C0 / s** (la droite C coupe la droite à 45°).",
            "Graphiquement, à un revenu donné, l'épargne est l'écart vertical entre la droite à 45° (Y) et la droite de consommation.",
        ],
        [
            calc("C = 0,8 Y + 100. Quelle est l'épargne pour Y = 1 000 ?", 100, "S = Y − C = 1 000 − 900 = **100** (ou S = 0,2 × 1 000 − 100).", niveau=1, unite=''),
            calc("C = 0,8 Y + 100. À partir de quel revenu l'épargne devient-elle positive ?", 500, "S = 0,2 Y − 100 = 0 → Y = 100 / 0,2 = **500**.", niveau=2, unite=''),
            calc("La PmC vaut 0,65. Quelle est la propension marginale à épargner ?", 0.35, "s = 1 − c = **0,35**.", niveau=1, unite=''),
            calc("C = 0,8 Y + 100. Quelle est la PMS pour Y = 2 000 ?", 0.15, "S = 0,2 × 2 000 − 100 = 300 ; PMS = 300 / 2 000 = **0,15** (contre 0,1 pour Y = 1 000 : la PMS augmente).", niveau=2, unite=''),
            S(qcm("Figure 1 du TD 2 : quel est le niveau d'épargne pour le revenu OY1 ?", ["Nul", "OA", "AB", "Négatif"], 0, "En Y1, la droite C coupe la droite à 45° : C = Y = OA, donc S = 0 (seuil d'épargne).", niveau=2, figure=FIG1), td(2)),
            S(qcm("Figure 1 du TD 2 : pour le revenu OY2, la consommation et l'épargne valent :", ["C = OB et S = BD", "C = OD et S = 0", "C = OA et S = AB", "C = OB et S = OB"], 0, "Sur la droite à 45°, Y2 = OD ; la consommation est lue sur C : OB ; l'épargne est l'écart OD − OB = **BD**.", niveau=2, figure=FIG1), td(2)),
            S(qcm("Figure 1 du TD 2 : pour le revenu OY3, l'épargne vaut :", ["CE", "BD", "OC", "OE"], 0, "Y3 = OE ; C = OC ; S = OE − OC = **CE**, plus grande qu'en Y2 : l'épargne augmente avec le revenu.", niveau=2, figure=FIG1), td(2)),
            vf("La propension moyenne à épargner diminue quand le revenu augmente.", False, "Elle **augmente** : PMS = s − C0/Y et PMS = 1 − PMC, or la PMC diminue."),
            vf("Lorsque le revenu est nul, l'épargne est égale à −C0 (désépargne).", True, "S = 0 − C0 = −C0."),
        ], figure=FIG1)

    # TD2 ajustement
    def dyn(y):
        out = []
        for _ in range(4):
            d = 680 + 0.6 * y
            out.append((y, d))
            y = d
        return out
    sous = dyn(1000)
    sur = dyn(2500)
    n15 = nm(
        'demande-effective', "Demande effective, diagramme à 45° et paradoxe de l'épargne",
        "Le **principe de la demande effective** : les entreprises produisent en fonction de la **demande anticipée** ; l'équilibre est atteint quand l'**offre (production Y) est égale à la demande globale D = C + I**. Samuelson (1948) l'a représenté par le **diagramme à 45°**.",
        [
            "En abscisse : le revenu Y (= production = offre globale). En ordonnée : C et I, et la demande D = cY + C0 + I0.",
            "La **droite à 45°** rassemble les points où Y = D ; l'équilibre E est à l'intersection de D et de la droite à 45°.",
            "**Revenu d'équilibre : Y* = (C0 + I0) / (1 − c)** ; on le retrouve par **S = I** : (1 − c) Y − C0 = I0.",
            "Si les entreprises produisent moins que la demande (**sous-production**), elles augmentent leur production à la période suivante ; si elles produisent plus (**sur-production**), les stocks s'accumulent et elles réduisent la production : l'économie converge vers Y*.",
            "L'équilibre n'est **pas forcément de plein-emploi** : un équilibre de sous-emploi dû à une insuffisance de demande = **chômage keynésien**.",
            "**Paradoxe de l'épargne** : si les ménages veulent épargner davantage, la consommation baisse, donc la demande et la production baissent ; à la fin, le revenu a diminué et l'épargne totale n'a pas augmenté (S = I).",
            "Si l'épargne désirée dépasse l'investissement désiré (S > I), le revenu **se contracte** ; si S < I, il **augmente**.",
        ],
        [
            S(calc("TD 2 : C = 80 + 0,6 Y et le revenu d'équilibre est Y = 1 700. Quel est le niveau de l'investissement I0 ?", 600,
                   "À l'équilibre, Y = C + I0 → I0 = 1 700 − 1 100 = **600 Mds€**. Vérification : Y* = (80 + 600) / 0,4 = 1 700 ✓.", niveau=2, unite='Mds€', figure=FIG_TD2), td(2)),
            calc("C = 100 + 0,75 Y et I0 = 150. Quel est le revenu d'équilibre ?", 1000, "Y* = (C0 + I0) / (1 − c) = 250 / 0,25 = **1 000**.", niveau=1, unite=''),
            S(calc("TD 2 (sous-production) : les entreprises produisent %s en t (demande anticipée). La demande effective est D = 680 + 0,6 Y. Quelle est la demande en t ?" % f(1000), sous[0][1],
                   "D(t) = 680 + 0,6 × 1 000 = **1 280** > offre : les entreprises vont produire plus en t + 1.", niveau=2, unite='Mds€'), td(2)),
            S(calc("Toujours en sous-production, l'offre de t + 1 est égale à la demande de t (1 280). Quelle est la demande en t + 1 ?", sous[1][1],
                   "D(t+1) = 680 + 0,6 × 1 280 = **1 448**. Puis t + 2 : offre 1 448, demande %s ; t + 3 : offre %s, demande %s → convergence vers 1 700." % (f(sous[2][1]), f(sous[3][0]), f(sous[3][1])), niveau=3, unite='Mds€'), td(2)),
            S(calc("TD 2 (sur-production) : les entreprises anticipent une demande de 2 500. Quelle est la demande effective en t ?", sur[0][1],
                   "D = 680 + 0,6 × 2 500 = **2 180** < 2 500 : il y a des invendus, la production baisse ensuite (1 988 en t + 2 pour la demande, etc.) jusqu'à 1 700.", niveau=2, unite='Mds€'), td(2)),
            S(qcm("Figure 2 du TD 2 : quelle situation correspond à l'équilibre ?", ["Le revenu OY2", "Le revenu OY1", "Le revenu OY3", "Aucune"], 0, "En Y2, la droite C + I coupe la droite à 45° (point F) : offre = demande, et S = I = DF.", niveau=1, figure=FIG2), td(2)),
            S(qcm("Figure 2 du TD 2 : pour le revenu OY3, l'épargne envisagée et l'investissement envisagé valent :", ["S = EH et I = EG, donc S > I", "S = EG et I = EH", "S = I = DF", "S = 0 et I = EG"], 0,
                  "Y3 = OH, C = OE → S = EH ; I = (C + I) − C = EG. S > I : l'intention d'épargner dépasse l'intention d'investir, le revenu va se **contracter** — c'est la situation du paradoxe de l'épargne.", niveau=3, figure=FIG2), td(2)),
            S(qcm("Si l'intention d'épargner excède l'intention d'investir, le revenu va :", ["Se contracter", "S'accroître", "Rester stable", "Doubler"], 0, "La demande est inférieure à la production : les stocks s'accumulent et la production baisse.", niveau=2), td(2)),
            S(courte("Qu'entend-on par « paradoxe de l'épargne » ?",
                     "Si tous les ménages décident d'épargner davantage, ils consomment moins : la demande globale baisse, donc la production et le revenu baissent. À l'arrivée, l'épargne totale n'augmente pas (elle reste égale à l'investissement) alors que le revenu a diminué : une vertu individuelle devient néfaste collectivement à court terme.", niveau=3), td(2)),
        ], figure=FIG_TD2, formules=["Y* = (C0 + I0) / (1 − c)", "Équilibre : Y = C + I ⇔ S = I"])

    n16 = nm(
        'multiplicateur', "Le multiplicateur keynésien élémentaire",
        "Une hausse de la dépense autonome (investissement ΔI0) entraîne une hausse **plus que proportionnelle** du revenu d'équilibre : **ΔY = k · ΔI0** avec **k = 1 / (1 − c)**.",
        [
            "Mécanisme : ΔI0 crée un revenu ΔY = ΔI0, qui est consommé à hauteur de c ΔI0, ce qui crée un nouveau revenu, etc. (boucle « consommation-revenu-consommation »).",
            "ΔY = ΔI0 (1 + c + c² + c³ + …) : progression géométrique de raison c < 1 → somme **1 / (1 − c)**.",
            "Le multiplicateur est d'autant plus élevé que la **PmC est forte** (k = 1/s).",
            "**Multiplicateur statique** : effet total final (k = 1/(1 − c)). **Multiplicateur dynamique** : effet cumulé au bout de n périodes, quand la consommation dépend du revenu de la période précédente (Ct = c·Yd,t−1) : 1 + c + … + c^(n−1).",
            "Graphiquement, la droite D se déplace vers le haut de ΔI0 ; le nouvel équilibre E1 est plus à droite.",
        ],
        [
            calc("La PmC vaut 0,75. Quel est le multiplicateur d'investissement ?", 4, "k = 1 / (1 − 0,75) = **4**.", niveau=1, unite=''),
            calc("Avec c = 0,75, l'investissement autonome augmente de 100. De combien augmente le revenu d'équilibre ?", 400, "ΔY = 4 × 100 = **400**.", niveau=1, unite=''),
            calc("Le gouvernement veut augmenter le revenu de 600 ; la PmC est de 0,8. De combien doit augmenter la dépense autonome ?", 120, "k = 5 ; ΔI = 600 / 5 = **120**.", niveau=2, unite=''),
            S(calc("Multiplicateur **dynamique** : c = 0,8 et Ct = c·Yd,t−1. Quel est l'effet cumulé sur le revenu au bout de 4 périodes d'une hausse de 1 de la dépense autonome ?", 1 + 0.8 + 0.64 + 0.512,
                   "1 + 0,8 + 0,8² + 0,8³ = 1 + 0,8 + 0,64 + 0,512 = **2,952**, à comparer au multiplicateur statique 1/(1 − 0,8) = 5 atteint à l'infini.", niveau=3, unite='', tolerance=0.001), td(4)),
            calc("c = 0,6. Une hausse de l'investissement de 50 : quel est le supplément de revenu au **deuxième** tour (après le revenu initial de 50) ?", 30, "Deuxième vague = c × 50 = **30** (puis 18, 10,8 …).", niveau=2, unite=''),
            qcm("Le multiplicateur est d'autant plus grand que :", ["La propension marginale à consommer est élevée", "La propension marginale à épargner est élevée", "L'investissement est faible", "Le taux d'intérêt est élevé"], 0, "k = 1/(1 − c) = 1/s : plus on consomme chaque euro supplémentaire, plus l'effet d'entraînement est fort."),
            S(qcm("Qu'est-ce qui distingue le multiplicateur dynamique du multiplicateur statique ?", ["Il décrit l'effet période après période, avec un décalage entre revenu et consommation", "Il ne dépend pas de c", "Il est toujours plus grand", "Il ne concerne que l'État"], 0,
                  "Le statique compare deux équilibres ; le dynamique suit l'ajustement dans le temps (Ct = f(Yd,t−1)) et converge vers le statique.", niveau=2), td(4)),
            vf("Grâce au multiplicateur, une hausse de l'investissement de 100 entraîne une hausse du revenu supérieure à 100 (si 0 < c < 1).", True, "k = 1/(1 − c) > 1."),
            courte("Explique avec des mots pourquoi une dépense de 100 peut augmenter le revenu national de 400.",
                   "Les 100 dépensés deviennent le revenu d'autres agents, qui en consomment une partie (par ex. 75 si c = 0,75) ; cette consommation devient à son tour un revenu, dont une partie est consommée, etc. La somme de ces vagues successives et décroissantes vaut 100 × 1/(1 − c) = 400.", niveau=2),
        ], formules=["k = 1 / (1 − c) = 1 / s", "ΔY = k · ΔI0", "Dynamique : ΔYn = ΔI0 (1 + c + … + c^(n−1))"])

    n17 = nm(
        'nouvelles-conso', "Nouvelles théories de la consommation",
        "Validée à court terme mais pas à long terme, la fonction keynésienne a été complétée par des théories à **fondements microéconomiques** et **dynamiques**, qui tiennent compte de la **richesse** et des **anticipations**.",
        [
            "**Modèle intertemporel** (2 périodes) : y1 = c1 + b1 et y2 + b1(1 + r) = c2 ⇒ **y1 + y2/(1 + r) = c1 + c2/(1 + r)** : la richesse est la valeur actualisée des revenus. Le choix dépend de la **préférence pour le présent** (« cigales » / « fourmis »).",
            "Hausse de r : **effet de substitution** (c1 ↓, c2 ↑, plus d'épargne) et **effet revenu** (la richesse baisse, c1 et c2 ↓).",
            "**Cycle de vie (Modigliani, 1954)** : on s'endette jeune, on épargne pendant la vie active, on désépargne à la retraite pour **lisser sa consommation**. Patrimoine maximal vers 60-69 ans. Si la population vieillit, le taux d'épargne augmente ; si elle rajeunit, il baisse.",
            "Court terme : fonction affine ; long terme : fonction linéaire de pente 1 (PMC = PmC = 1).",
            "**Revenu permanent (Friedman, 1957)** : Y = YP + YT (**permanent** + **transitoire**) ; seule la relation **CP = k·YP** est stable ; un gain transitoire est surtout **épargné**. Revenu permanent yP = r·W.",
            "**Nouveaux keynésiens** (années 1980) : **contrainte de liquidité** (impossibilité d'emprunter : le lissage ne passe que par l'épargne) et **effets d'habitude** / prudence (épargne de précaution face à l'incertitude).",
        ],
        [
            calc("Modèle à deux périodes : y1 = 100, y2 = 55, r = 10 %. Quelle est la richesse actualisée de l'individu ?", 150, "W = y1 + y2/(1 + r) = 100 + 55/1,1 = 100 + 50 = **150**.", niveau=2, unite=''),
            calc("Selon Friedman, un individu dispose d'une richesse W = 200 000 € et le taux d'intérêt est de 3 %. Quel est son revenu permanent annuel ?", 6000, "yP = r × W = 0,03 × 200 000 = **6 000 €**.", niveau=2),
            qcm("Un ménage gagne 5 000 € au loto. Selon la théorie du revenu permanent, il va surtout :", ["Épargner ce gain transitoire", "Le consommer entièrement cette année", "Réduire sa consommation", "Emprunter davantage"], 0, "Un revenu **transitoire** modifie peu le revenu permanent, donc peu la consommation."),
            qcm("Selon la théorie du cycle de vie, à quel âge le patrimoine est-il maximal (France) ?", ["Vers 60-69 ans, à la retraite", "Vers 25 ans", "Vers 40 ans", "Après 80 ans"], 0, "On accumule pendant la vie active puis on désépargne à la retraite."),
            qcm("Selon le cycle de vie, si la population vieillit, le taux d'épargne agrégé :", ["Augmente", "Diminue", "Est nul", "Ne change pas"], 0, "Le cours indique : rajeunissement → taux d'épargne qui chute ; vieillissement → qui augmente.", niveau=2),
            qcm("Une hausse du taux d'intérêt, par l'effet de substitution, conduit à :", ["Consommer moins aujourd'hui et épargner plus", "Consommer plus aujourd'hui", "Ne rien changer", "Emprunter plus"], 0, "Le futur devient relativement moins cher : c1 ↓ et c2 ↑."),
            vf("La contrainte de liquidité empêche certains ménages d'emprunter, de sorte qu'ils ne peuvent lisser leur consommation que par l'épargne.", True, "Idée des nouveaux keynésiens."),
            qcm("Qui a formulé la théorie du revenu permanent ?", ["Milton Friedman (1957)", "Franco Modigliani (1954)", "J. M. Keynes (1936)", "James Tobin (1956)"], 0, "Modigliani : cycle de vie ; Friedman : revenu permanent."),
            courte("Pourquoi une relance budgétaire perçue comme temporaire risque-t-elle d'avoir un faible effet selon Friedman ?", "Les ménages y voient un revenu transitoire qu'ils épargnent plutôt que de le consommer : la PmC effective baisse, donc le multiplicateur diminue.", niveau=3),
        ], formules=["y1 + y2/(1 + r) = c1 + c2/(1 + r)", "Y = YP + YT ; CP = k · YP ; yP = r · W"])
    return chapitre('ch-conso', 'Chapitre 2 — La consommation', [n11, n12, n13, n14, n15, n16, n17])


def ch3():
    # TD3 A
    rec = {1: (7000, 6000), 2: (7000, 5000), 3: (6000, 6000), 4: (6000, 5000), 5: (5000, 6000)}

    def van(r1, r2, r, coef=1):
        return r1 * coef / (1 + r) + r2 * coef / (1 + r) ** 2 - 10000
    v10 = {k: van(a, b, 0.10) for k, (a, b) in rec.items()}
    v20 = {k: van(a, b, 0.20) for k, (a, b) in rec.items()}
    v10b = {k: van(a, b, 0.10, 1.1) for k, (a, b) in rec.items()}
    tdA = tab(['', 'E1', 'E2', 'E3', 'E4', 'E5'], [['Période 1', 7000, 7000, 6000, 6000, 5000], ['Période 2', 6000, 5000, 6000, 5000, 6000]], 'TD 3-A : recettes nettes (coût 10 000 € chacun, valeur de revente nulle)')
    tdB = tab(['Projet', 1, 2, 3, 4, 5, 6, 7, 8], [['Recettes (€)', 1050, 1100, 1130, 1150, 1200, 1300, 1400, 1500]], 'TD 3-B : coût 1 000 €, durée de vie 1 an')
    fig_ir = fig('I (projets réalisés)', 'r (%)', 8, 50, [seg((0, 50), (1, 40), None, 1), seg((1, 40), (2, 30), None, 1), seg((2, 30), (3, 20), None, 1), seg((3, 20), (4, 15), None, 1), seg((4, 15), (5, 13), None, 1), seg((5, 13), (6, 10), None, 1), seg((6, 10), (7, 5), 'I(r)', 1)],
                 titre='TD 3-B : nombre de projets rentables selon le taux d\'intérêt', gradx=[2, 4, 6, 8], grady=[10, 20, 30, 40, 50], guides=[gd(2, 30, None, None), gd(6, 10, None, None)])

    n18 = nm(
        'invest-def', "L'investissement : définition et faits stylisés",
        "L'**investissement** correspond à la **formation brute de capital fixe (FBCF)** : acquisitions moins cessions d'**actifs fixes** (corporels ou incorporels, issus de la production, utilisés au moins **un an**) par les producteurs résidents.",
        [
            "Investir = acheter un bien **durable** pour produire ultérieurement d'autres biens ; ≠ **consommations intermédiaires** (détruites dans la production).",
            "Investissement **privé** (ménages, SNF) ou **public** (APU) ; **matériel** (machines, terrains) ou **immatériel** (R&D, innovation). Les ménages investissent dans le logement.",
            "Un simple achat d'actions n'est **pas** un investissement au sens économique (le stock de capital n'augmente pas).",
            "Part dans le PIB : **22,5 %** (2017) ; contribution à la croissance 1960-2017 : 0,7 point, soit **24 %** de la croissance.",
            "L'investissement est **pro-cyclique** (il accentue les fluctuations) et **2 fois plus volatil** que la consommation (écart-type 4 % contre 2 %).",
            "Corrélation croissance PIB / FBCF ≈ **0,84** ; l'investissement repart avec un léger décalage après la reprise.",
        ],
        [
            qcm("Lequel est un **investissement** au sens de la comptabilité nationale ?", ["L'achat d'une machine par une entreprise", "L'achat d'actions en Bourse par un ménage", "L'achat de farine par un boulanger", "Le paiement des salaires"], 0, "Les actions ne créent pas de capital nouveau ; la farine est une consommation intermédiaire."),
            qcm("Pourquoi l'investissement se distingue-t-il des consommations intermédiaires ?", ["Il porte sur des biens durables utilisés sur plusieurs périodes", "Il est toujours public", "Il est moins cher", "Il est importé"], 0, "Les CI sont détruites ou transformées au cours de la production."),
            vf("L'investissement est une variable pro-cyclique.", True, "Il augmente fortement en reprise et chute en récession : il accentue les fluctuations."),
            qcm("Selon le cours, la volatilité de l'investissement par rapport à celle de la consommation est :", ["Deux fois plus élevée", "Deux fois plus faible", "Identique", "Dix fois plus élevée"], 0, "Écart-type des taux de croissance : 4 % contre 2 % (1960-2017)."),
            calc("En 2017, la FBCF représente 22,5 % d'un PIB de 2 290 Mds€. Quel est son montant (au Md près) ?", 515.25, "0,225 × 2 290 = **515,25 Mds€**.", niveau=1, unite='Mds€', tolerance=0.5),
            calc("La croissance du PIB est de 2,9 % dont 0,7 point dû à l'investissement. Quelle part de la croissance l'investissement explique-t-il (en %, à l'unité) ?", 0.7 / 2.9 * 100, "0,7 ÷ 2,9 ≈ **24 %** (ordre de grandeur cité par le cours).", niveau=2, unite='%', tolerance=0.5),
            qcm("Lesquels sont des investissements **immatériels** ?", ["Des dépenses de recherche et développement", "L'achat d'un logiciel", "Des dépenses d'innovation médicale", "L'achat d'un camion"], [0, 1, 2], "Le camion est un investissement matériel.", niveau=2),
            vf("Une variable contra-cyclique accentue les fluctuations de l'activité.", False, "Elle les **atténue** ; c'est la variable **pro-cyclique** qui les accentue."),
        ])

    n19 = nm(
        'accumulation', "L'accumulation du capital : investissement brut, net et de remplacement",
        "L'investissement (**flux**) alimente le stock de capital (**stock**), qui se **déprécie** (usure, obsolescence liée au progrès technique). **Équation d'accumulation : Kt+1 = Kt (1 − δ) + It**.",
        [
            "δ = **taux de dépréciation** ; δKt = capital usé.",
            "**It = (Kt+1 − Kt) + δKt** : **investissement brut = investissement net + investissement de remplacement**.",
            "Comptabilité nationale : investissement brut = **FBCF** ; remplacement = **consommation de capital fixe (CCF)** = amortissement ; net = **FNCF**.",
            "L'investissement fait à la période t n'est productif qu'à la période t + 1.",
            "1/δ correspond à la **durée de vie** du capital.",
        ],
        [
            calc("K = 1 000, δ = 10 %, I = 150. Quel est le stock de capital à la période suivante ?", 1050, "K' = 1 000 × 0,9 + 150 = **1 050**.", niveau=1, unite=''),
            calc("Même cas : quel est l'investissement de remplacement ?", 100, "δK = 0,1 × 1 000 = **100**.", niveau=1, unite=''),
            calc("Même cas : quel est l'investissement net ?", 50, "Net = brut − remplacement = 150 − 100 = **50** (= K' − K).", niveau=1, unite=''),
            calc("Une entreprise veut maintenir son capital de 5 000 constant ; δ = 8 %. Quel investissement brut doit-elle réaliser ?", 400, "Pour un investissement net nul : I = δK = 0,08 × 5 000 = **400**.", niveau=2, unite=''),
            calc("Une machine a une durée de vie de 5 ans. Quel est le taux de dépréciation annuel δ (en %) ?", 20, "1/δ = 5 → δ = **20 %**.", niveau=2, unite='%'),
            qcm("En comptabilité nationale, l'investissement de remplacement correspond à :", ["La consommation de capital fixe (amortissement)", "La FBCF", "La FNCF", "Les variations de stocks"], 0, "Brut = FBCF ; remplacement = CCF ; net = FNCF."),
            vf("Si l'investissement brut est inférieur à l'investissement de remplacement, le stock de capital diminue.", True, "L'investissement net est alors négatif.", niveau=2),
            calc("K = 2 000, δ = 5 %, I = 60. Quel est l'investissement net ?", -40, "Net = 60 − 0,05 × 2 000 = 60 − 100 = **−40** : le capital diminue.", niveau=2, unite=''),
        ], formules=["Kt+1 = Kt (1 − δ) + It", "It = (Kt+1 − Kt) + δKt (brut = net + remplacement)"])

    n20 = nm(
        'van', "Actualisation et valeur actuelle nette (VAN)",
        "Investir est un pari sur l'avenir : l'entreprise compare le **coût immédiat** C0 aux **recettes nettes futures** Bt = Rt − Ct, ramenées au présent par l'**actualisation**.",
        [
            "**Capitalisation** : 100 € placés au taux r valent 100(1 + r) dans un an, 100(1 + r)² dans deux ans.",
            "**Actualisation** (l'inverse) : 100 € reçus dans un an valent **100/(1 + r)** aujourd'hui ; dans t ans : 100/(1 + r)^t.",
            "Le taux d'intérêt est le « **prix du temps** » (taux de préférence pour le présent) : plus il est élevé, plus la valeur actuelle d'une somme future est faible.",
            "**VA = Σ Bt / (1 + r)^t** ; **VAN = VA − C0**.",
            "Règle : **VAN > 0** → projet rentable (on investit) ; VAN = 0 → indifférent ; VAN < 0 → on n'investit pas.",
            "Le résultat dépend fortement des **anticipations** de recettes.",
        ],
        [
            calc("Exemple du cours : un rendement R = 1 000 € attendu dans un an, r = 5 %. Quelle est sa valeur actuelle ?", 1000 / 1.05, "VA = 1 000 / 1,05 = **952,38 €**.", niveau=1),
            calc("Même exemple avec un coût C0 = 1 000 €. Quelle est la VAN ?", 1000 / 1.05 - 1000, "VAN = 952,38 − 1 000 = **−47,62 €** : on n'investit pas.", niveau=1),
            S(calc("TD 3-A : VAN du projet de l'entreprise 1 au taux de 10 % ?", v10[1], "VAN = 7 000/1,1 + 6 000/1,1² − 10 000 = 6 363,64 + 4 958,68 − 10 000 = **%s €**." % f(v10[1]), niveau=2, tableau=tdA), td(3)),
            S(calc("TD 3-A : VAN du projet de l'entreprise 4 au taux de 10 % ?", v10[4], "6 000/1,1 + 5 000/1,21 − 10 000 = 5 454,55 + 4 132,23 − 10 000 = **%s €** : non rentable." % f(v10[4]), niveau=2, tableau=tdA), td(3)),
            S(calc("TD 3-A : au taux de 10 %, combien de projets sont rentables, donc quelle est la demande d'investissement de l'économie (en €) ?", 30000,
                   "VAN > 0 pour E1 (%s), E2 (%s), E3 (%s) ; négatives pour E4 et E5. Demande d'investissement = 3 × 10 000 = **30 000 €**." % (f(v10[1]), f(v10[2]), f(v10[3])), niveau=3, tableau=tdA), td(3)),
            S(calc("TD 3-A : le taux passe à 20 %. Quelle est la VAN du projet de l'entreprise 1 ?", v20[1], "7 000/1,2 + 6 000/1,44 − 10 000 = 5 833,33 + 4 166,67 − 10 000 = **0** : l'entreprise est indifférente ; tous les autres projets ont une VAN négative. La hausse du taux d'intérêt réduit l'investissement.", niveau=3, tableau=tdA), td(3)),
            S(calc("TD 3-A : regain d'optimisme, les recettes anticipées augmentent de 10 % (taux 10 %). Quelle est la nouvelle VAN du projet de l'entreprise 5 ?", v10b[5],
                   "(5 000 × 1,1)/1,1 + (6 000 × 1,1)/1,21 − 10 000 = 5 000 + 5 454,55 − 10 000 = **%s €** > 0 : les 5 projets deviennent rentables (demande 50 000 €). Les anticipations jouent un rôle clé." % f(v10b[5]), niveau=3, tableau=tdA), td(3)),
            calc("Combien faut-il placer aujourd'hui à 4 % pour disposer de 1 081,60 € dans deux ans ?", 1000, "1 081,60 / 1,04² = 1 081,60 / 1,0816 = **1 000 €**.", niveau=2),
            vf("Plus le taux d'intérêt est élevé, plus la valeur actuelle d'une recette future est faible.", True, "On divise par (1 + r)^t, qui augmente avec r."),
        ], formules=["VA = Σ Bt / (1 + r)^t", "VAN = VA − C0 ; on investit si VAN > 0"])

    tri = {k: (v / 1000 - 1) * 100 for k, v in zip(range(1, 9), [1050, 1100, 1130, 1150, 1200, 1300, 1400, 1500])}
    n21 = nm(
        'tri', "Taux de rendement interne (TRI), efficacité marginale du capital et fonction I(r)",
        "Le **taux de rendement interne** (i), appelé par Keynes **efficacité marginale du capital (EmK)**, est le taux d'actualisation qui **annule la VAN** : C0 = Σ Bt / (1 + i)^t.",
        [
            "Projet sur une période : C0 = R / (1 + i) ⇒ **i = R / C0 − 1**.",
            "Règle : on investit si **i > r** (taux d'intérêt du marché) ; i = r : investissement neutre ; i < r : non rentable. Équivalent à VAN > 0.",
            "Double rôle de r : **coût de l'emprunt** si l'entreprise emprunte, **coût d'opportunité** si elle s'autofinance (elle renonce à prêter au taux r).",
            "Au niveau macroéconomique : en classant les projets par TRI décroissant, une **baisse de r** rend davantage de projets rentables.",
            "**Fonction d'investissement : I = I(r) avec I'(r) < 0** (décroissante du taux d'intérêt). En France, corrélation négative entre taux d'investissement et taux d'intérêt réel.",
        ],
        [
            S(calc("TD 3-B : quel est le TRI du projet 6 (coût 1 000 €, recette 1 300 € dans un an) ?", tri[6], "i = 1 300/1 000 − 1 = **30 %**.", niveau=1, unite='%', tableau=tdB), td(3)),
            S(calc("TD 3-B : au taux de marché de 30 %, quelle est la VAN du projet 8 ?", 1500 / 1.3 - 1000, "VAN = 1 500/1,3 − 1 000 = **153,85 €** > 0 (TRI 50 % > 30 %).", niveau=2, tableau=tdB), td(3)),
            S(calc("TD 3-B : au taux de 30 %, combien de projets ont un TRI strictement supérieur au taux d'intérêt ?", 2, "TRI : 5, 10, 13, 15, 20, 30, 40, 50 %. Seuls les projets 7 et 8 ont i > 30 % (le projet 6 est neutre) : **2 projets**, demande d'investissement 2 000 €.", niveau=2, unite='', tableau=tdB, figure=fig_ir), td(3)),
            S(calc("TD 3-B : le taux passe à 10 %. Combien de projets ont un TRI strictement supérieur ?", 6, "Projets 3 à 8 (13 % à 50 %) : **6 projets** (le projet 2 est neutre). La baisse du taux d'intérêt augmente l'investissement : I'(r) < 0.", niveau=2, unite='', tableau=tdB, figure=fig_ir), td(3)),
            qcm("Une entreprise autofinance son investissement. Le taux d'intérêt r représente alors :", ["Un coût d'opportunité", "Un coût d'emprunt", "Un impôt", "Une subvention"], 0, "Elle renonce au placement de ses fonds au taux r."),
            qcm("Un projet a un TRI de 8 % et le taux d'intérêt est de 6 %. Le projet est :", ["Rentable", "Non rentable", "Neutre", "Impossible à évaluer"], 0, "i > r : la VAN au taux de 6 % est positive."),
            vf("La fonction d'investissement macroéconomique est une fonction croissante du taux d'intérêt.", False, "Elle est **décroissante** : I'(r) < 0."),
            S(qcm("Lecture du graphique : quand le taux d'intérêt baisse de 30 % à 10 %, le nombre de projets réalisés :", ["Passe de 2 à 6", "Passe de 6 à 2", "Reste à 4", "Passe de 0 à 8"], 0, "On se déplace le long de la courbe I(r) décroissante.", niveau=2, figure=fig_ir), td(3, True)),
            calc("Un projet coûte 2 000 € et rapporte 2 240 € dans un an. Quel est son TRI ?", 12, "i = 2 240/2 000 − 1 = **12 %**.", niveau=1, unite='%'),
        ], formules=["C0 = Σ Bt / (1 + i)^t (TRI = EmK)", "Un an : i = R / C0 − 1", "Investir si i > r ; I = I(r), I'(r) < 0"], figure=fig_ir)

    n22 = nm(
        'accelerateur', "Le principe de l'accélérateur",
        "Le **principe de l'accélérateur** (J. Clark, 1917, trafic ferroviaire) : une **variation de la demande** provoque une **variation plus que proportionnelle de l'investissement**, avec un décalage dans le temps.",
        [
            "Fonction de production Yt = F(Kt, Nt) ; **coefficient de capital v = K / Y** (inverse de la productivité moyenne du capital), supposé fixe : Kt = v·Yt.",
            "Avec δ = 0 : **It = Kt+1 − Kt = v·ΔYt+1** : l'investissement net dépend de la **variation** de la demande, pas de son niveau.",
            "L'accélérateur = coefficient de capital, en général **> 1** (la valeur du capital dépasse la production annuelle).",
            "Si la demande baisse, l'investissement net est négatif : on ne remplace pas les machines usées.",
            "Investissement brut = investissement net (accélérateur) + investissement de remplacement.",
            "Hypothèses : ajustement immédiat des capacités, **pas de capital oisif**, prix inchangés. Le **taux d'utilisation des capacités (TUC)** compte : si le TUC < 100 %, l'entreprise utilise d'abord ses capacités inemployées (exemple de la scierie).",
        ],
        [
            calc("Coefficient de capital v = 3. La demande passe de 200 à 210. Quel est l'investissement net induit ?", 30, "I = v × ΔY = 3 × 10 = **30**.", niveau=1, unite=''),
            calc("v = 4 ; la demande baisse de 500 à 490. Quel est l'investissement net ?", -40, "I = 4 × (−10) = **−40** : désinvestissement (machines usées non remplacées).", niveau=2, unite=''),
            calc("v = 2,5 ; la production passe de 1 000 à 1 040 ; investissement de remplacement = 60. Quel est l'investissement brut ?", 160, "Net = 2,5 × 40 = 100 ; brut = 100 + 60 = **160**.", niveau=2, unite=''),
            calc("Une entreprise produit 400 avec un capital de 1 200. Quel est son coefficient de capital ?", 3, "v = K / Y = 1 200 / 400 = **3**.", niveau=1, unite=''),
            qcm("Selon l'accélérateur, l'investissement net dépend :", ["De la variation de la demande", "Du niveau de la demande", "Du taux d'intérêt uniquement", "Du niveau des prix"], 0, "Clark : les commandes de wagons dépendaient de l'**accélération** du trafic."),
            qcm("Une entreprise dont le taux d'utilisation des capacités est de 70 % voit sa demande augmenter. Que fait-elle d'abord ?", ["Elle utilise davantage ses capacités existantes", "Elle investit immédiatement", "Elle licencie", "Elle baisse ses prix"], 0, "L'accélérateur suppose qu'il n'y a pas de capital oisif."),
            vf("Si la demande se stabilise à un niveau élevé, l'investissement net devient nul selon l'accélérateur.", True, "ΔY = 0 donc I net = 0 : l'investissement peut chuter même si la demande reste forte.", niveau=3),
            calc("v = 2. La demande passe de 100 à 110 puis à 115. Quelle est la variation de l'investissement net entre les deux périodes ?", -10, "I1 = 2 × 10 = 20 ; I2 = 2 × 5 = 10 : l'investissement **baisse de 10** alors que la demande augmente encore (effet d'amplification).", niveau=3, unite=''),
        ], formules=["v = K / Y", "Inet,t = v · ΔYt", "Ibrut = Inet + Iremplacement"])

    n23 = nm(
        'autres-det-inv', "Autres déterminants de l'investissement : coût d'usage, profit, Q de Tobin",
        "L'entreprise vise un stock de capital optimal ; elle maximise son profit en égalisant la **productivité marginale du capital** à son **coût d'usage**.",
        [
            "It = (Kt − Kt−1) + δKt−1.",
            "**Coût d'usage du capital = r + δ** : taux d'intérêt réel (coût d'opportunité des fonds) + taux d'amortissement.",
            "**Profits** : bons indicateurs des profits futurs ; forte **corrélation positive** entre croissance des profits et de l'investissement.",
            "**Q de Tobin = valeur boursière de l'entreprise / valeur comptable (de remplacement) du capital**. Si **Q > 1**, l'entreprise a intérêt à investir (le marché valorise plus que ce que coûte l'investissement).",
            "En pratique : **I = I(r + δ, π, Q)** (coût d'usage, croissance du profit, Q de Tobin).",
        ],
        [
            calc("Taux d'intérêt réel 3 % ; taux d'amortissement 10 %. Quel est le coût d'usage du capital ?", 13, "r + δ = 3 + 10 = **13 %**.", niveau=1, unite='%'),
            calc("Valeur boursière d'une entreprise 150 M€ ; valeur de bilan de son capital 120 M€. Quel est son Q de Tobin ?", 1.25, "Q = 150 / 120 = **1,25** > 1 : l'entreprise a intérêt à investir.", niveau=1, unite=''),
            qcm("Si le Q de Tobin est inférieur à 1, l'entreprise :", ["N'a pas intérêt à investir", "Doit investir massivement", "Doit s'endetter", "Fait faillite"], 0, "Le marché valorise ses actifs moins que leur coût de remplacement."),
            qcm("Selon le cours, quelles variables entrent dans la fonction d'investissement utilisée en pratique ?", ["Le coût d'usage r + δ", "La croissance du profit", "Le Q de Tobin", "Le taux de chômage"], [0, 1, 2], "I = I(r + δ, π, Q).", niveau=2),
            vf("Il existe une relation positive forte entre profit et investissement.", True, "Les profits actuels annoncent des profits futurs et fournissent l'autofinancement."),
            calc("Le coût d'usage est de 12 % et le taux d'amortissement de 9 %. Quel est le taux d'intérêt réel ?", 3, "r = 12 − 9 = **3 %**.", niveau=2, unite='%'),
            qcm("Une hausse du taux d'intérêt réel, toutes choses égales par ailleurs :", ["Augmente le coût d'usage et réduit l'investissement", "Réduit le coût d'usage", "N'a pas d'effet", "Augmente le Q de Tobin"], 0, "r + δ augmente : le capital désiré diminue.", niveau=2),
            courte("Explique l'intuition du Q de Tobin.", "Si la Bourse valorise l'entreprise plus cher que ce que coûte son capital (Q > 1), installer une machine supplémentaire crée plus de valeur boursière qu'elle ne coûte : il est rentable d'investir. Si Q < 1, mieux vaut ne pas investir.", niveau=2),
        ], formules=["Coût d'usage = r + δ", "Q = valeur boursière / valeur comptable du capital", "I = I(r + δ, π, Q)"])
    return chapitre('ch-invest', 'Chapitre 3 — L\'investissement', [n18, n19, n20, n21, n22, n23])
