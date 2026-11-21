"""Macroéconomie — Introduction et chapitre 1 (comptabilité nationale)."""
from macro_base import *


def chapitres():
    return [intro(), ch1()]


def intro():
    n1 = nm(
        'objet-macro', "Objet de la macroéconomie",
        "La **macroéconomie** analyse les caractéristiques **globales** d'une économie dans son ensemble (croissance, chômage, inflation, politiques économiques) en raisonnant sur des **quantités agrégées**, où les individus sont regroupés en catégories homogènes.",
        [
            "**Microéconomie** : étude des choix des agents individuels (ménages-consommateurs, entreprises-producteurs, gouvernement) et de leurs effets sur les prix, l'allocation des ressources et le bien-être ; ex. arbitrage travail/loisir, choix transports en commun/voiture, combinaison capital/travail.",
            "**Macroéconomie** : approche globale, raisonnement au niveau de l'ensemble du système ; ex. consommation globale, revenu global, production globale.",
            "Un **agrégat** est une grandeur statistique et synthétique (ex. le **PIB** mesure la production globale en unités monétaires) ; mesuré chaque année, il forme une **série statistique**.",
            "Grands agrégats étudiés : PIB, niveau général des prix, consommation, investissement, emploi, chômage.",
            "**Horizons** : **court terme** = 1 à 2 ans ; **moyen terme** = 5 à 10 ans (fluctuations) ; **long terme** = 10 à 20 ans ou plus (croissance).",
            "Une **récession** est une période soutenue de croissance négative.",
        ],
        [
            qcm("Quelle question relève de la **macroéconomie** ?", ["Comment évolue le taux de chômage en France ?", "Pourquoi un consommateur préfère-t-il le train à la voiture ?", "Comment une entreprise combine-t-elle capital et travail ?", "Comment un individu arbitre-t-il entre travail et loisir ?"], 0,
                "Le taux de chômage est une caractéristique **globale** de l'économie ; les trois autres questions portent sur des choix **individuels** (microéconomie)."),
            vf("La macroéconomie raisonne à partir de quantités agrégées dans lesquelles les individus sont regroupés en catégories homogènes.", True, "C'est la définition du cours."),
            qcm("Selon le cours, le **moyen terme** correspond à un horizon de :", ["5 à 10 ans", "1 à 2 ans", "10 à 20 ans", "Quelques mois"], 0, "Court terme 1-2 ans, moyen terme 5-10 ans (fluctuations), long terme 10-20 ans et plus (croissance)."),
            qcm("Lesquels sont des **agrégats** macroéconomiques ?", ["Le PIB", "Le niveau général des prix", "Le taux de chômage", "Le prix d'une baguette dans une boulangerie"], [0, 1, 2], "Le prix d'un bien précis dans un magasin est une donnée microéconomique.", niveau=2),
            vf("Le PIB est un agrégat qui mesure, en unités monétaires, la production globale d'une économie sur une période.", True, "Mesuré chaque année, il permet de constituer une série statistique (ex. PIB de la France de 1950 à 2026)."),
            qcm("Une économie qui connaît une période soutenue de croissance négative est en :", ["Récession", "Expansion", "Inflation", "Désinflation"], 0, "Croissance négative prolongée = **récession** ; croissance positive = expansion."),
            qcm("Les questions de **long terme** en macroéconomie portent surtout sur :", ["La croissance économique", "Les fluctuations conjoncturelles", "Les choix d'un consommateur", "Le prix d'un bien"], 0, "Court et moyen terme : fluctuations ; long terme : croissance.", niveau=2),
            courte("Explique en deux phrases la différence entre microéconomie et macroéconomie.",
                   "La microéconomie étudie les choix des agents individuels (ménages, entreprises) et leurs effets sur les prix et l'allocation des ressources. La macroéconomie étudie l'économie dans son ensemble à partir d'agrégats (PIB, chômage, inflation) et les liens entre ces grandeurs.", niveau=2),
        ])

    n2 = nm(
        'naissance-macro', "Naissance de la macroéconomie : Keynes, les classiques, positif et normatif",
        "La macroéconomie naît dans les années **1930** avec **J. M. Keynes** (1883-1946) et sa *Théorie générale de l'emploi, de l'intérêt et de la monnaie* (**1936**), écrite pour comprendre la **crise de 1929** : c'est la « **révolution keynésienne** ».",
        [
            "**Diagnostic** de Keynes : l'**excès d'épargne sur l'investissement** ; **remède** : le **soutien de la demande globale** par l'intervention de l'État.",
            "Les mécanismes de marché ne corrigent pas toujours spontanément les déséquilibres : les fluctuations ne sont plus vues comme des retournements inévitables.",
            "**Logique classique** : équilibre du marché du travail → salaire réel → emploi → production.",
            "**Logique keynésienne** : **demande anticipée (effective)** → production → emploi → salaire réel.",
            "**M. Friedman** (monétariste, Nobel 1976) : « dans des périodes exceptionnelles de crise, nous devenons tous keynésiens ».",
            "**Économie positive** : décrit le monde **tel qu'il est**, explications objectives sans jugement de valeur. **Économie normative** : dit ce que le monde **devrait être**, recommandations fondées sur des jugements de valeur.",
            "Plan du cours : sphère **réelle** (biens et services, travail) et sphère **monétaire et financière** (monnaie, titres, change), reliées par le taux d'intérêt ; politiques **budgétaire** et **monétaire**.",
        ],
        [
            qcm("En quelle année Keynes publie-t-il la *Théorie générale de l'emploi, de l'intérêt et de la monnaie* ?", ["1936", "1929", "1945", "1776"], 0, "1936, dans le contexte de la Grande Dépression des années 1930."),
            qcm("Quel est le diagnostic de la crise selon Keynes ?", ["Un excès d'épargne sur l'investissement", "Un excès de dépenses publiques", "Une création monétaire trop forte", "Des salaires trop bas"], 0, "Keynes voit dans l'insuffisance de la demande (excès d'épargne) l'origine de la crise."),
            qcm("Dans la logique **keynésienne**, quel est l'enchaînement ?", ["Demande effective → production → emploi → salaire réel", "Salaire réel → emploi → production", "Monnaie → prix → production", "Production → demande → épargne"], 0, "Chez Keynes, c'est la demande anticipée qui détermine la production et donc l'emploi. La logique classique part du marché du travail."),
            vf("Pour les économistes classiques, le niveau de production est déterminé par l'équilibre sur le marché du travail.", True, "Équilibre du travail → salaire réel → emploi → production."),
            qcm("« Il faut baisser les impôts pour relancer la croissance. » Cette phrase relève de l'analyse :", ["Normative", "Positive", "Microéconomique", "Comptable"], 0, "C'est une **recommandation** (« il faut ») fondée sur un jugement : analyse normative."),
            qcm("« Une hausse du taux d'intérêt réduit l'investissement. » Cette phrase relève de l'analyse :", ["Positive", "Normative", "Politique", "Morale"], 0, "Elle décrit une relation entre des faits, sans jugement de valeur : analyse positive.", niveau=2),
            vf("Selon Friedman, chef de file des monétaristes, « dans des périodes exceptionnelles de crise, nous devenons tous keynésiens ».", True, "Citation reprise dans le cours.", niveau=2),
            courte("Pourquoi dit-on que Keynes « crée » l'analyse macroéconomique moderne ?",
                   "Parce qu'il montre que les mécanismes de marché ne parviennent pas toujours à corriger spontanément les déséquilibres (chômage de masse) et qu'il raisonne sur la demande globale ; il justifie ainsi l'intervention de l'État pour relancer puis stabiliser l'activité.", niveau=3),
        ])
    return chapitre('ch-intro-macro', "Introduction — Qu'est-ce que la macroéconomie ?", [n1, n2])


def ch1():
    # --- TD1 ex1 : TEE
    tee = tab(['Opération', 'Ménages', 'Entreprises', 'État'], [
        ['Travail (W/P)·L', 'offre Ls = 6 000', 'demande Ld = 6 000', ''],
        ['Consommation C', '3 800', '', ''], ['Investissement I', '', '1 000', ''], ['Dépenses publiques G', '', '', '1 200'],
        ['Production Y', '', '6 000', ''], ['Impôts T', '800', '', 'reçoit 800'],
        ['Monnaie ΔM', 'ΔMd = 300', '', 'ΔMs = 300'], ['Titres ΔB', 'ΔBd = 1 100', 'ΔBE = 1 000', 'ΔBG = 100']], 'Données du schéma du TD 1, exercice 1')

    n3 = nm(
        'circuit', "Agents, marchés et circuit économique ; flux et stocks",
        "Une économie regroupe des **unités économiques** (agents) qui échangent sur des **marchés**, chacune étant soumise à une contrainte de revenu. Le **circuit économique** représente ces échanges de façon simplifiée.",
        [
            "**4 marchés** : biens et services, travail, monnaie, actifs financiers (titres).",
            "**Agents** : entreprises, ménages, État, reste du monde, classés en catégories homogènes.",
            "**Entreprises** : produisent Y = F(L, K) au prix P, demandent du travail (Ld) payé au salaire nominal W (salaire réel **W/P**), investissent (I), émettent des titres (BE), versent dividendes et intérêts.",
            "**Ménages** : offrent leur travail (Ls), reçoivent salaires et revenus des titres (R), consomment (C), paient des impôts (T), épargnent (S) et placent cette épargne en monnaie (Md) et en titres (Bd).",
            "**État** : dépense G, perçoit les impôts T, paie des intérêts RG ; finance son déficit par émission d'obligations (BG) ou création monétaire (ΔMs).",
            "**Variable de flux** : mesurée **au cours d'une période** (PIB, inflation, déficit public). **Variable de stock** : mesurée **à une date** (dette publique). Les flux alimentent les stocks (la dette = accumulation des déficits). Image de Mankiw : l'eau du robinet (flux) et l'eau dans la baignoire (stock).",
            "Un flux de titres est une **variation de stock** : B = B1 − B0.",
        ],
        [
            qcm("Lequel est une **variable de stock** ?", ["La dette publique au 31 décembre", "Le PIB de l'année", "Le déficit public de l'année", "L'inflation de l'année"], 0, "La dette est mesurée **à une date** ; les trois autres sont mesurées sur une période (flux)."),
            vf("Le PIB est une variable de flux.", True, "Il mesure la richesse créée **au cours** d'une année."),
            qcm("Dans l'image de la baignoire de Mankiw, l'eau qui coule du robinet représente :", ["Un flux", "Un stock", "Une contrainte budgétaire", "Un agrégat monétaire"], 0, "Le débit est un flux ; l'eau accumulée dans la baignoire est un stock."),
            qcm("Quels sont les quatre marchés du circuit économique étudié ?", ["Biens et services, travail, monnaie, titres", "Biens, services, travail, change", "Monnaie, change, titres, actions", "Biens, capital, travail, État"], 0, "Le cours retient ces 4 marchés (le change intervient en économie ouverte)."),
            calc("Les ménages détenaient 2 500 de titres au début de l'année et 2 800 à la fin. Quelle est leur demande de titres exprimée en flux ?", 300,
                 "Flux = variation du stock : Bd = B1 − B0 = 2 800 − 2 500 = **300**.", niveau=1, unite=''),
            calc("La dette publique était de 2 000 Mds€. L'année suivante, le déficit public est de 150 Mds€. Que devient la dette (sans autre opération) ?", 2150,
                 "Le stock de dette augmente du flux de déficit : 2 000 + 150 = **2 150 Mds€**.", niveau=2, unite='Mds€'),
            qcm("Comment l'État peut-il financer un déficit G − T > 0 selon le cours ?", ["En émettant des obligations", "Par création monétaire", "En augmentant la consommation des ménages", "En vendant des biens de consommation"], [0, 1], "Financement par emprunt (BG) ou par création de monnaie (ΔMs).", niveau=2),
            vf("Le salaire réel est égal au salaire nominal divisé par le niveau des prix (W/P).", True, "Le salaire réel mesure le pouvoir d'achat du salaire."),
            S(courte("Dans le schéma du TD 1, décris les opérations des ménages.",
                     "Ils offrent leur travail (6 000), consomment (3 800), paient des impôts (800), demandent de la monnaie (300) et des titres (1 100). Leurs dépenses (3 800 + 800 + 300 + 1 100 = 6 000) égalent leurs ressources (6 000).", niveau=2), td(1, True), None),
        ])
    n3['exercices'][-1]['tableau'] = tee

    n4 = nm(
        'tee', "Contraintes budgétaires des agents et tableau économique d'ensemble (TEE)",
        "Chaque agent est soumis à une **contrainte budgétaire** : sur une période, la somme de ses **dépenses** est égale à la somme de ses **ressources**. Le **TEE** synthétise toutes les opérations des secteurs institutionnels.",
        [
            "**Entreprises** : I + (W/P)·Ld + RE + TE = Y + BE/P (investissement, salaires, dividendes, taxes = production + émission de titres).",
            "**Ménages** : C + TM + Md/P + Bd/P = (W/P)·Ls + (RE + RG).",
            "**Épargne des ménages** : S = revenus (travail + dividendes et intérêts) − (consommation + impôts) ; **placement** : S = Md/P + Bd/P.",
            "**État** : G + RG = (TM + TE) + Ms/P + BG/P ; d'où **création monétaire = déficit (G + RG − T) − émission de titres publics**.",
            "**TEE** : pour chaque secteur, **emplois à gauche**, **ressources à droite**. **Lecture en colonnes** : contraintes budgétaires de chaque agent. **Lecture en lignes** : équilibre de chaque marché (chaque opération pour l'ensemble des secteurs).",
            "Avec le **TES** (tableau entrées-sorties de **Leontief**), le TEE est l'un des deux tableaux de synthèse de la comptabilité nationale.",
            "**4 catégories d'opérations** : sur **produits** (biens et services), de **répartition**, **financières**, de **patrimoine** (autres opérations d'accumulation).",
        ],
        [
            S(calc("D'après le schéma du TD 1, calcule l'épargne des ménages (revenus − consommation − impôts).", 1400,
                   "S = 6 000 − 3 800 − 800 = **1 400**. Elle est placée en monnaie (300) et en titres (1 100) : 300 + 1 100 = 1 400 ✓.", niveau=2, unite='', tableau=tee), td(1)),
            S(calc("Toujours dans le TD 1, quel est le déficit public G − T ?", 400,
                   "G − T = 1 200 − 800 = **400**, financé par création monétaire (300) et émission de titres publics (100).", niveau=1, unite='', tableau=tee), td(1)),
            S(vf("Dans le TD 1, la contrainte budgétaire des entreprises est vérifiée : I + (W/P)·Ld = Y + ΔBE.", True,
                 "1 000 + 6 000 = 6 000 + 1 000 = 7 000 ✓ (dépenses = ressources).", niveau=2), td(1)),
            qcm("Dans le TEE, la lecture **en colonnes** permet de vérifier :", ["Les contraintes budgétaires de chaque agent", "L'équilibre de chaque marché", "La loi de Walras uniquement", "Le taux de croissance"], 0, "Colonnes = secteurs (agents) ; lignes = opérations (marchés)."),
            qcm("Dans le TEE, pour chaque secteur, où sont inscrits les emplois ?", ["Dans la partie gauche", "Dans la partie droite", "En bas du tableau", "Ils ne sont pas inscrits"], 0, "Emplois à gauche, ressources à droite."),
            qcm("Quelles sont les quatre catégories d'opérations de la comptabilité nationale ?", ["Sur produits, de répartition, financières, de patrimoine", "Achats, ventes, salaires, impôts", "Réelles, monétaires, publiques, privées", "Consommation, investissement, épargne, crédit"], 0, "Définition du cours.", niveau=2),
            calc("L'État dépense G = 500, paie RG = 40 d'intérêts, perçoit T = 480 et émet 35 de titres. Quelle création monétaire assure l'équilibre de sa contrainte ?", 25,
                 "Ms = (G + RG − T) − BG = (500 + 40 − 480) − 35 = 60 − 35 = **25**.", niveau=3, unite=''),
            vf("Le TEE et le TES de Leontief sont les deux tableaux de synthèse de la comptabilité nationale.", True, "C'est ce qu'indique le cours."),
            courte("Écris la contrainte budgétaire des ménages et explique-la.",
                   "C + T + Md/P + Bd/P = (W/P)·Ls + R : ce que les ménages dépensent ou placent (consommation, impôts, monnaie, titres) est égal à leurs revenus (salaires + dividendes et intérêts).", niveau=2),
        ])

    n5 = nm(
        'walras', "Équilibre des marchés, contrainte budgétaire macroéconomique et loi de Walras",
        "En additionnant les contraintes budgétaires de tous les agents, on obtient la **contrainte budgétaire macroéconomique** : la somme des déséquilibres (offre − demande) sur tous les marchés est **nulle**.",
        [
            "**Biens et services** : équilibre si Y = C + I + G ; Y < C + I + G : **demande excédentaire** ; Y > C + I + G : **offre excédentaire**.",
            "**Travail** : (W/P)·Ls = (W/P)·Ld ; si l'offre de travail dépasse la demande : **chômage** (offre excédentaire).",
            "**Monnaie** : Ms/P = Md/P. **Titres** : BE/P + BG/P = Bd/P.",
            "**Contrainte macro** : [Y − (C+I+G)] + [(W/P)(Ls − Ld)] + [(Ms − Md)/P] + [(BE + BG − Bd)/P] = 0.",
            "**Loi de Walras** : dans une économie à n marchés, si n − 1 marchés sont en équilibre, le n-ième l'est aussi.",
            "L'**équilibre comptable** (ressources = emplois) est toujours vérifié ; l'**équilibre macroéconomique** (offre = demande désirée) peut ne pas l'être.",
        ],
        [
            S(vf("Dans le TD 1, le marché des biens et services est en équilibre (Y = C + I + G).", True, "C + I + G = 3 800 + 1 000 + 1 200 = 6 000 = Y ✓.", niveau=1), td(1)),
            S(calc("Dans le TD 1, offre de titres : entreprises 1 000, État 100 ; demande des ménages 1 100. Quel est l'excès d'offre de titres ?", 0,
                   "(1 000 + 100) − 1 100 = **0** : le marché des titres est en équilibre, comme le prévoit la loi de Walras puisque les trois autres marchés le sont.", niveau=2, unite=''), td(1)),
            qcm("Si Y < C + I + G, le marché des biens et services présente :", ["Une demande excédentaire", "Une offre excédentaire", "Un équilibre", "Du chômage"], 0, "La demande dépasse l'offre (production)."),
            qcm("Sur le marché du travail, une offre de travail supérieure à la demande correspond à :", ["Du chômage", "Une pénurie de main-d'œuvre", "Un équilibre", "De l'inflation"], 0, "Offre excédentaire de travail = chômage."),
            qcm("Énoncé de la loi de Walras :", ["Si n − 1 marchés sont en équilibre, le n-ième l'est aussi", "Tous les marchés sont toujours en équilibre", "L'offre crée sa propre demande", "La monnaie est neutre"], 0, "Conséquence de la contrainte budgétaire macroéconomique (somme des déséquilibres nulle)."),
            calc("Dans une économie à 4 marchés : biens et services en offre excédentaire de 30, travail en équilibre, monnaie en demande excédentaire de 10 (Ms − Md = −10). Quel est le déséquilibre (offre − demande) sur le marché des titres ?", -20,
                 "La somme des déséquilibres est nulle : 30 + 0 + (−10) + x = 0 → x = **−20** (demande excédentaire de titres de 20).", niveau=3, unite=''),
            vf("L'équilibre comptable ressources = emplois peut ne pas être respecté.", False, "L'équilibre **comptable** est toujours respecté ; c'est l'équilibre **macroéconomique** (offre = demande désirée) qui peut ne pas l'être.", niveau=2),
            courte("Pourquoi, dans le modèle IS-LM, peut-on ignorer le marché des titres ?", "D'après la loi de Walras : si le marché des biens et services et le marché de la monnaie sont en équilibre (et le travail mis à part), le marché des titres l'est forcément.", niveau=3),
        ])

    fc = tab(['Pays (2010, % PIB)', 'S − I', 'T − G', 'X − Z'], [['Allemagne', 8.91, -2.5, 5.6], ['États-Unis', 5.6, -8.8, -3.2], ['France', 2.6, -4.8, -2.2], ['Japon', 10.3, -6.7, 3.6], ['Italie', -1.3, -2.2, -3.5], ['Zone euro', 4.1, -3.9, 0.2]], 'Identité du flux circulaire (OCDE 2010)')
    n6 = nm(
        'flux-circulaire', "Identité du flux circulaire et déficits jumeaux",
        "En économie ouverte, Y = C + I + G + (X − Z) et le revenu se répartit en Y = C + S + T. On en déduit l'**identité du flux circulaire** : **(S − I) + (T − G) = (X − Z)**.",
        [
            "Économie à 2 agents : production = revenu = consommation ; avec marchés des capitaux : Y = C + I et Y = C + S, donc **S = I**.",
            "Avec l'État : Y = C + I + G ; T représente les **taxes nettes** (impôts − transferts).",
            "**S > I** : le secteur privé est **épargnant net** ; **S < I** : emprunteur net.",
            "**T > G** : le secteur public est épargnant net ; **T < G** : **déficit** (primaire).",
            "**X > Z** : excédent commercial ; **X < Z** : déficit commercial.",
            "**Déficits jumeaux** : G ↑ (ou T ↓) → déficit budgétaire → vente d'obligations → taux d'intérêt ↑ → entrées de capitaux → appréciation de la monnaie → exportations ↓, importations ↑ → **déficit courant**.",
            "Ex. : l'Allemagne finance son déficit public par son épargne privée ; les États-Unis s'endettent auprès du reste du monde.",
        ],
        [
            calc("Dans un pays : S − I = 3 % du PIB et T − G = −5 % du PIB. Quel est le solde commercial X − Z (en % du PIB) ?", -2, "(S − I) + (T − G) = X − Z → 3 + (−5) = **−2 %** : déficit commercial.", niveau=1, unite='%'),
            calc("En France (2010) : S − I = 2,6 % et T − G = −4,8 %. Quel est X − Z (en % du PIB) ?", -2.2, "2,6 − 4,8 = **−2,2 %**, ce qui correspond au tableau.", niveau=1, unite='%', tableau=fc),
            qcm("Si S < I, le secteur privé est :", ["Emprunteur net", "Épargnant net", "En excédent commercial", "En équilibre"], 0, "Il investit plus qu'il n'épargne : il doit emprunter."),
            qcm("Selon le tableau, quel pays finance son déficit public grâce à une épargne privée très importante et dégage un excédent extérieur ?", ["Le Japon", "L'Italie", "Les États-Unis", "La France"], 0, "Japon : S − I = 10,3 ; T − G = −6,7 ; X − Z = +3,6.", niveau=2, tableau=fc),
            qcm("En Italie (S − I = −1,3 ; T − G = −2,2), on constate que :", ["Les secteurs privé et public dépensent plus qu'ils ne perçoivent, d'où un déficit extérieur", "Le pays prête au reste du monde", "Le secteur privé finance l'État", "Le commerce extérieur est excédentaire"], 0, "Les deux soldes sont négatifs : le pays emprunte à l'étranger (X − Z = −3,5).", niveau=2, tableau=fc),
            qcm("Dans l'enchaînement des « déficits jumeaux », une hausse du déficit public entraîne d'abord :", ["Une hausse des taux d'intérêt", "Une baisse des taux d'intérêt", "Une dépréciation de la monnaie", "Une hausse des exportations"], 0, "L'État vend des obligations → taux d'intérêt ↑ → entrées de capitaux → appréciation → déficit courant.", niveau=3),
            vf("Dans une économie fermée sans État, l'équilibre implique S = I.", True, "Y = C + I et Y = C + S donc S = I."),
            calc("Économie : S = 500, I = 450, T = 300, G = 380. Quel est le solde X − Z ?", -30, "(500 − 450) + (300 − 380) = 50 − 80 = **−30** (déficit commercial).", niveau=2, unite=''),
            courte("Explique le mécanisme des « déficits jumeaux ».",
                   "Une hausse des dépenses publiques (ou une baisse des impôts) crée un déficit budgétaire financé par l'émission d'obligations ; les taux d'intérêt montent, attirant des capitaux étrangers ; la monnaie s'apprécie, ce qui réduit les exportations et augmente les importations : le compte courant devient déficitaire.", niveau=3),
        ])

    # TD1 ex2
    td1 = tab(['Donnée (millions €, prix constants)', 'Valeur'], [
        ['Valeur brute de la production', 4800], ['Revenus par l\'activité des entreprises', 600], ['Intérêts et loyers', 270],
        ['Consommation privée', 2200], ['Dépenses publiques courantes', 700], ['FBCF', 760], ['Exportations', 1500], ['Importations', 1200],
        ['Impôts indirects (nets de subventions)', 240], ['Revenus reçus du reste du monde', 100], ['Revenus versés aux non-résidents', 300], ['Produit intérieur net', 2910]], 'TD 1, exercice 2 (année 2016)')
    pib = 2200 + 700 + 760 + 1500 - 1200
    n7 = nm(
        'pib-revenu', "Du PIB au revenu personnel disponible",
        "Le **PIB** exprime le revenu total obtenu à l'intérieur des frontières. Une partie n'arrive pas aux ménages : on passe du PIB au **revenu personnel disponible** en retirant successivement l'amortissement, les impôts indirects, les bénéfices non distribués et les impôts directs.",
        [
            "**Produit intérieur net (PIN) = PIB − amortissement** (dévalorisation du capital, usure des équipements).",
            "**Revenu national = PIN − impôts indirects** (TVA…) : somme des revenus primaires.",
            "La valeur ajoutée nette est distribuée en : **salaires** (et cotisations), **intérêts**, **impôt sur les sociétés**, **profits** (dividendes ou bénéfices non distribués = épargne des entreprises).",
            "**Revenu personnel** = revenus distribués aux ménages + **transferts** de l'État (allocations familiales, chômage…).",
            "**Revenu personnel disponible** = revenu personnel − impôts sur le revenu et autres charges : il est **consommé ou épargné** (C + S).",
            "**Revenu national brut (RNB) = PIB + revenus reçus du reste du monde − revenus versés au reste du monde**.",
            "Grandeurs : consommation finale (satisfaction immédiate des besoins), **FBCF** (biens d'équipement durables utilisés au moins un an), épargne (part des revenus disponible pour accumuler des actifs).",
        ],
        [
            S(calc("TD 1, ex. 2 : calcule le **PIB** (optique de la demande).", pib, "PIB = C + G + FBCF + X − M = 2 200 + 700 + 760 + 1 500 − 1 200 = **3 960**.", niveau=1, unite='M€', tableau=td1), td(1)),
            S(calc("TD 1, ex. 2 : calcule le **revenu national brut** (RNB).", pib + 100 - 300, "RNB = PIB + revenus reçus − revenus versés = 3 960 + 100 − 300 = **3 760**.", niveau=2, unite='M€', tableau=td1), td(1)),
            S(calc("TD 1, ex. 2 : calcule l'**amortissement** (dévalorisation) du produit intérieur.", pib - 2910, "Amortissement = PIB − PIN = 3 960 − 2 910 = **1 050**.", niveau=2, unite='M€', tableau=td1), td(1)),
            S(calc("TD 1, ex. 2 : calcule le **revenu national** (PIN − impôts indirects).", 2910 - 240, "RN = 2 910 − 240 = **2 670**.", niveau=2, unite='M€', tableau=td1), td(1)),
            S(calc("TD 1, ex. 2 : calcule les **salaires** versés (revenu national − revenus des entreprises − intérêts et loyers).", 2670 - 600 - 270,
                   "Le revenu national se répartit en salaires + revenus des entreprises + intérêts et loyers : 2 670 − 600 − 270 = **1 800**.", niveau=3, unite='M€', tableau=td1), td(1)),
            S(calc("TD 1, ex. 2 : part du travail dans la richesse générée (salaires ÷ revenu national), en % au dixième.", 1800 / 2670 * 100,
                   "1 800 ÷ 2 670 = **67,4 %** ; la part du capital (profits + intérêts : 870 ÷ 2 670) est de 32,6 %. (Si l'on rapporte au PIB : 1 800 ÷ 3 960 = 45,5 %.)", niveau=3, unite='%', tolerance=0.1, tableau=td1), td(1)),
            calc("PIB = 2 000 ; amortissement = 300 ; impôts indirects = 200. Quel est le revenu national ?", 1500, "PIN = 2 000 − 300 = 1 700 ; RN = 1 700 − 200 = **1 500**.", niveau=1, unite=''),
            qcm("Le revenu personnel **disponible** est le revenu que les ménages peuvent :", ["Consommer ou épargner", "Seulement consommer", "Verser à l'État", "Investir dans les entreprises uniquement"], 0, "Revenu disponible = C + S."),
            vf("Le produit intérieur net s'obtient en retirant l'amortissement du PIB.", True, "PIN = PIB − amortissements (usure du capital)."),
        ])

    va = tab(['Producteur', 'Ventes', 'Consommations intermédiaires', 'Valeur ajoutée'], [['Agriculteur (blé)', 3, 0, 3], ['Meunier (farine)', 7, 3, 4], ['Pâtissier (gâteau)', 12, 7, 5], ['Total', 22, 10, 12]], 'Exemple du cours (en €)')
    n8 = nm(
        'trois-optiques', "Les trois optiques du PIB et la valeur ajoutée",
        "Le **PIB** mesure la production de biens et services réalisée pendant une période à l'intérieur des frontières. C'est un **flux**. Il peut se calculer selon trois optiques qui donnent le même résultat.",
        [
            "**Optique production** : PIB = **somme des valeurs ajoutées**. **VA = production (ventes) − consommations intermédiaires (CI)**.",
            "Les CI ne sont pas comptées dans le PIB pour éviter le **double comptage** : le PIB n'est **pas** la somme des ventes.",
            "**Optique revenu** : PIB = rémunération des salariés + excédent brut d'exploitation et revenu mixte + impôts sur la production − subventions.",
            "**Optique demande** : PIB = consommation finale + FBCF + exportations − importations (ou PIB + importations = consommation finale + FBCF + Δstocks + exportations).",
            "Parts dans la demande (France) : consommation ≈ 55 %, investissement ≈ 22 %, dépenses publiques ≈ 25 %, X − Z ≈ −2 %. L'investissement, plus volatil, contribue autant que la consommation aux fluctuations.",
        ],
        [
            calc("Exemple du cours : le meunier achète 3 € de blé et vend sa farine 7 €. Quelle est sa valeur ajoutée ?", 4, "VA = 7 − 3 = **4 €**, qui est aussi son revenu.", niveau=1, tableau=va),
            calc("Toujours dans cet exemple, quel est le PIB (somme des valeurs ajoutées) ?", 12, "3 + 4 + 5 = **12 €** = valeur du produit final (le gâteau).", niveau=1, tableau=va),
            qcm("Pourquoi le PIB n'est-il pas égal à la somme des ventes (22 € dans l'exemple) ?", ["Pour éviter de compter plusieurs fois les consommations intermédiaires", "Parce que la TVA est déduite", "Parce que les exportations sont exclues", "Parce que l'amortissement est déduit"], 0, "Le blé serait compté 3 fois et la farine 2 fois : c'est le **double comptage**.", tableau=va),
            S(calc("TD 1, ex. 2 : production brute 4 800, PIB (somme des VA) 3 960. Quel est le montant des consommations intermédiaires ?", 840, "CI = production − VA = 4 800 − 3 960 = **840**.", niveau=2, unite='M€'), td(1)),
            calc("Une économie : consommation finale 1 600, FBCF 500, exportations 700, importations 650. Quel est le PIB ?", 2150, "PIB = 1 600 + 500 + 700 − 650 = **2 150**.", niveau=1, unite=''),
            calc("Une entreprise réalise 850 000 € de chiffre d'affaires et achète pour 520 000 € de matières et services. Valeur ajoutée ?", 330000, "VA = 850 000 − 520 000 = **330 000 €**.", niveau=1),
            qcm("Selon l'optique du **revenu**, le PIB comprend :", ["La rémunération des salariés", "L'excédent brut d'exploitation", "Les impôts sur la production moins les subventions", "Les consommations intermédiaires"], [0, 1, 2], "Les CI ne sont jamais comptées dans le PIB.", niveau=2),
            S(calc("TD 1, ex. 2 : exportations 1 500, importations 1 200, PIB 3 960. Calcule le **degré d'ouverture** (X + M) / (2 × PIB), en % au dixième.", (1500 + 1200) / (2 * 3960) * 100,
                   "(1 500 + 1 200) ÷ (2 × 3 960) = 2 700 ÷ 7 920 = **34,1 %**. (Autre convention : (X + M)/PIB = 68,2 %.)", niveau=3, unite='%', tolerance=0.1), td(1)),
            vf("Les trois optiques (production, revenu, demande) donnent la même valeur du PIB.", True, "Les dépenses des uns sont les revenus des autres dans le circuit économique."),
        ])

    # TD1 ex3
    C1, I1, X1, M1 = 70 / 1.05, 20 / 1.03, 20 / 1.02, 10 / 1.07
    y0 = C1 + I1 + X1 - M1
    g = (100 / y0 - 1) * 100
    contC = (70 - C1) / y0 * 100
    td3 = tab(['', 'Consommation', 'Investissement', 'Exportations', 'Importations'], [['Valeur à l\'année t', 70, 20, 20, 10], ['Variation réelle / t−1', '+5 %', '+3 %', '+2 %', '+7 %']], 'TD 1, exercice 3')
    n9 = nm(
        'pib-reel', "PIB nominal, PIB réel, déflateur et taux de croissance",
        "Une **variable nominale** est exprimée en monnaie courante ; une **variable réelle** en est l'expression une fois retirée l'influence des prix.",
        [
            "**PIB nominal** (en valeur, en euros courants) : aux prix de l'année en cours. **PIB réel** (en volume, en euros constants) : aux prix d'une année de base ; sa hausse ne traduit que la hausse des quantités.",
            "**Déflateur du PIB = PIB nominal ÷ PIB réel** (× 100 en indice) : mesure du niveau des prix.",
            "**Taux de croissance** entre t − 1 et t : g = (Yt / Yt−1 − 1) × 100 = (Yt − Yt−1) / Yt−1 × 100 ≈ ln Yt − ln Yt−1.",
            "Croissance positive = **expansion** ; négative = **récession**.",
            "**Variation du déflateur ≈ croissance du PIB nominal − croissance du PIB réel**.",
            "**Contribution d'une composante à la croissance** = sa variation ÷ PIB de l'année précédente.",
            "La croissance moyenne sur une période est une moyenne simple (ex. +1,6 % par an en France entre 1995 et 2017).",
        ],
        [
            calc("Le PIB réel passe de 2 800 à 2 856 Mds€. Quel est le taux de croissance ?", 2, "(2 856 / 2 800 − 1) × 100 = **2 %**.", niveau=1, unite='%'),
            calc("PIB nominal = 2 200 ; PIB réel = 2 000. Quel est le déflateur du PIB (indice base 100) ?", 110, "2 200 ÷ 2 000 × 100 = **110** : les prix ont augmenté de 10 % depuis l'année de base.", niveau=1, unite=''),
            calc("Le PIB nominal croît de 5 % et le PIB réel de 2 %. De combien le déflateur augmente-t-il approximativement ?", 3, "Variation du déflateur ≈ 5 − 2 = **3 %**.", niveau=2, unite='%'),
            calc("PIB réel = 1 500 et déflateur = 1,2. Quel est le PIB nominal ?", 1800, "PIB nominal = PIB réel × déflateur = 1 500 × 1,2 = **1 800**.", niveau=1, unite=''),
            S(calc("TD 1, ex. 3 : quel est le PIB à l'année t (C + I + X − M) ?", 100, "70 + 20 + 20 − 10 = **100**.", niveau=1, unite='', tableau=td3), td(1)),
            S(calc("TD 1, ex. 3 : quel est le taux de croissance de l'économie entre t − 1 et t (en %, au centième) ?", g,
                   "On retrouve les valeurs de t − 1 : C = 70/1,05 = 66,67 ; I = 20/1,03 = 19,42 ; X = 20/1,02 = 19,61 ; M = 10/1,07 = 9,35. PIB t−1 = %s. Croissance = (100 / %s − 1) × 100 = **%s %%**." % (f(y0), f(y0), f(g)),
                   niveau=3, unite='%', tolerance=0.02, tableau=td3), td(1)),
            S(calc("TD 1, ex. 3 : quelle est la contribution de la consommation à la croissance (en points de %, au centième) ?", contC,
                   "ΔC = 70 − 66,67 = 3,33 ; contribution = 3,33 ÷ %s × 100 = **%s points**, soit l'essentiel de la croissance de %s %%." % (f(y0), f(contC), f(g)),
                   niveau=3, unite='pts', tolerance=0.02, tableau=td3), td(1)),
            vf("Une hausse du PIB nominal signifie forcément que l'on produit davantage de biens et services.", False, "Elle peut venir uniquement de la hausse des prix. Seul le PIB **réel** mesure les quantités."),
            qcm("Le PIB réel est aussi appelé :", ["PIB en volume (euros constants)", "PIB en valeur (euros courants)", "PIB nominal", "Revenu national"], 0, "Réel = volume = euros constants ; nominal = valeur = euros courants."),
        ])

    n10 = nm(
        'inflation-chomage', "Inflation et chômage",
        "L'**inflation** est une hausse **générale et continue** du niveau général des prix ; le **taux d'inflation** est le taux de croissance de ce niveau : π = (Pt − Pt−1) / Pt−1. Le **taux de chômage** est le rapport entre le nombre de chômeurs et la population active.",
        [
            "**Désinflation** : ralentissement de l'inflation (pays européens dans les années 1980-1990 pour respecter Maastricht ; convergence vers 2 %, objectif de la BCE).",
            "**Déflation** : baisse générale et continue des prix (inflation négative) ; menace la croissance (Japon depuis les années 1990).",
            "**Hyperinflation** : inflation **mensuelle supérieure à 50 %** (Allemagne de Weimar : 1 870 000 000 % en 1923).",
            "Effets de l'inflation : perte de pouvoir d'achat des revenus non indexés (retraités) ; impôts plus lourds si les tranches ne sont pas indexées ; baisse de la charge réelle des dettes → **favorable aux emprunteurs**, défavorable aux créanciers (inverse en déflation).",
            "**Taux de chômage u = U / (population active)**, la population active = chômeurs + personnes en emploi.",
            "Le chômage est un **gaspillage** de ressources humaines (production perdue) et un problème social. La **loi d'Okun** relie chômage et croissance du PIB.",
        ],
        [
            calc("L'indice des prix passe de 100 à 103. Quel est le taux d'inflation ?", 3, "(103 / 100 − 1) × 100 = **3 %**.", niveau=1, unite='%'),
            calc("Un pays compte 3 millions de chômeurs pour une population active de 30 millions. Taux de chômage ?", 10, "3 ÷ 30 = **10 %**.", niveau=1, unite='%'),
            calc("Population active 25 millions ; personnes en emploi 23,5 millions. Taux de chômage ?", 6, "Chômeurs = 25 − 23,5 = 1,5 million ; u = 1,5 ÷ 25 = **6 %**.", niveau=2, unite='%'),
            qcm("Un taux d'inflation qui passe de 6 % à 2 % traduit :", ["Une désinflation", "Une déflation", "Une hyperinflation", "Une récession"], 0, "Les prix augmentent encore, mais moins vite : désinflation."),
            qcm("Une baisse générale et continue des prix s'appelle :", ["La déflation", "La désinflation", "La stagflation", "La dévaluation"], 0, "Inflation négative = déflation."),
            qcm("Selon le cours, on parle d'hyperinflation lorsque le taux d'inflation :", ["Mensuel dépasse 50 %", "Annuel dépasse 10 %", "Annuel dépasse 5 %", "Est négatif"], 0, "Seuil retenu : 50 % par mois."),
            vf("L'inflation est favorable aux emprunteurs.", True, "Elle réduit la charge réelle de leur dette (intérêts nominaux diminués de l'inflation)."),
            calc("Un emprunt est contracté au taux nominal de 5 % alors que l'inflation est de 3 %. Quel est le coût réel approximatif de l'emprunt ?", 2, "Taux réel ≈ taux nominal − inflation = 5 − 3 = **2 %**.", niveau=2, unite='%'),
            courte("Pourquoi un retraité dont la pension n'est pas indexée perd-il en cas d'inflation ?", "Parce que sa pension nominale reste la même alors que les prix augmentent : son pouvoir d'achat (revenu réel) diminue.", niveau=2),
        ])
    return chapitre('ch-compta-nat', 'Chapitre 1 — Le cadre d\'analyse : la comptabilité nationale', [n3, n4, n5, n6, n7, n8, n9, n10])
