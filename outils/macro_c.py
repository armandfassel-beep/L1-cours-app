"""Macroéconomie — Chapitre 4 (État), 5 (monnaie), 6 (IS-LM)."""
from macro_base import *
import math


def chapitres():
    return [ch4(), ch5(), ch6()]


# Figures IS-LM (exemple du cours : IS Y = 1500 − 50r ; LM Y = 1000 + 50r)
def islm(titre, extra=(), points=None, fleches=()):
    d = [droite(30, -0.02, 1000, 1500, 'IS', 1), droite(-20, 0.02, 1000, 1600, 'LM', 2)] + list(extra)
    return fig('Y', 'r (%)', 1700, 12, d, titre=titre, xmin=900, points=points or [pt(1250, 5, 'E')], guides=[gd(1250, 5)], gradx=[1000, 1250, 1500], grady=[2, 4, 6, 8, 10], fleches=fleches)


FIG_ISLM = islm('Exemple du cours : IS : Y = 1 500 − 50 r ; LM : Y = 1 000 + 50 r ; équilibre E (Y = 1 250 ; r = 5)')
FIG_BUDG = islm('Hausse de la dépense autonome : IS se déplace vers la droite (IS\')', extra=[droite(32, -0.02, 1100, 1600, "IS'", 1, True)], points=[pt(1250, 5, 'E'), pt(1300, 6, "E'")], fleches=[{'de': [1180, 6.6], 'a': [1260, 6.6]}])
FIG_MON = islm('Hausse de l\'offre de monnaie : LM se déplace vers la droite (LM\')', extra=[droite(-22, 0.02, 1100, 1700, "LM'", 2, True)], points=[pt(1250, 5, 'E'), pt(1300, 4, "E''")], fleches=[{'de': [1420, 8.4], 'a': [1490, 7.4]}])


def ch4():
    n24 = nm(
        'role-etat', "Le rôle de l'État : État-gendarme, État-providence, biens publics",
        "L'État remplit des fonctions d'**allocation**, de **redistribution** et de **stabilisation**. Son rôle oppose deux courants : les **classiques** et les **keynésiens**.",
        [
            "**Classiques** (Smith → début XXe s.) : État **minimal**, « laisser-faire, laisser-passer », **main invisible** ; fonctions **régaliennes** : défense, police, justice (+ infrastructures non rentables pour le privé) : **État-gendarme**.",
            "**Keynes** : face aux défaillances du marché (crise de 1929, puis 2008), l'État intervient par les politiques économiques : **État-providence** (avec la protection sociale, après 1945).",
            "Remise en cause à partir des années 1970 (monétaristes, nouveaux classiques), mais la crise de 2008 a rappelé le rôle régulateur de l'État.",
            "**Bien public** (Samuelson, 1954) : **non-rival** (ma consommation ne réduit pas celle des autres) et **non-exclusif** (on ne peut exclure personne). Ex. : l'**éclairage public**.",
            "Problème du **passager clandestin** : on profite du bien sans payer → seule la **production publique** financée par l'**impôt** est adaptée. Forme **interne** (fonctionnaires) ou **externe** (délégation au privé, ex. ramassage des ordures).",
            "**Réglementation** : intervention sur le fonctionnement du marché (entrée, prix, quantités). **Régulation** : établir des normes, attribuer des licences, surveiller les tarifs. Objectif : atténuer les **externalités**.",
        ],
        [
            qcm("Quelles sont les fonctions **régaliennes** de l'État ?", ["Défense, police, justice", "Éducation, santé, retraites", "Monnaie, crédit, change", "Production, distribution, consommation"], 0, "Ce sont les seules fonctions que les classiques reconnaissent à l'État-gendarme."),
            qcm("Un bien public est :", ["Non rival et non exclusif", "Rival et exclusif", "Produit uniquement par des entreprises privées", "Gratuit à produire"], 0, "Définition de Samuelson (1954)."),
            qcm("Lequel est un exemple de bien public pur ?", ["L'éclairage public", "Une baguette de pain", "Un abonnement de téléphone", "Un billet de cinéma"], 0, "On ne peut ni exclure ni épuiser l'usage d'un réverbère."),
            qcm("Le « passager clandestin » est un agent qui :", ["Profite d'un bien public sans en payer le prix", "Fraude le fisc", "Travaille sans contrat", "Importe illégalement"], 0, "D'où la nécessité de financer le bien public par l'impôt."),
            vf("Pour Keynes, le marché s'autorégule toujours et l'État doit rester minimal.", False, "C'est la position **classique** ; Keynes justifie l'intervention de l'État."),
            qcm("Le ramassage des ordures financé par une commune mais réalisé par une entreprise privée est une production publique de forme :", ["Externe", "Interne", "Régalienne", "Marchande"], 0, "Forme externe : production confiée au privé, financement public.", niveau=2),
            qcm("Quelles sont les trois grandes fonctions économiques de l'État ?", ["Allocation", "Redistribution", "Stabilisation", "Spéculation"], [0, 1, 2], "Définition du cours.", niveau=2),
            courte("Pourquoi le marché ne peut-il pas produire efficacement un bien public ?", "Parce qu'on ne peut pas exclure ceux qui ne paient pas (non-exclusion) : chacun a intérêt à se comporter en passager clandestin, donc aucune entreprise ne peut se faire payer. L'État, qui peut lever l'impôt, doit le financer.", niveau=2),
        ])

    n25 = nm(
        'budget-etat', "Le budget des administrations publiques et les soldes",
        "Le budget des **APU** comprend les **recettes publiques** (dont les impôts) et les **dépenses publiques**. **Solde public = recettes − dépenses** : excédent s'il est positif, **déficit** s'il est négatif.",
        [
            "**Recettes** (Insee) : recettes de production, revenus de la propriété, **impôts et cotisations sociales** (≈ 90 % des recettes), autres transferts.",
            "**Taux de prélèvements obligatoires = prélèvements obligatoires / PIB** ; sa hausse vient surtout des **cotisations sociales** (protection sociale, vieillissement).",
            "**Impôt = taux × base (assiette)**. À court terme, **T = t·Y + T0** (t taux marginal, T0 forfaitaire) ; impôts exogènes : T = T0.",
            "**Dépenses** (Insee) : fonctionnement, **intérêts** (charge de la dette), prestations sociales et transferts, acquisitions d'actifs non financiers. Les achats publics sont **exogènes** : G = G0.",
            "**Solde public = solde structurel + solde conjoncturel** ; le conjoncturel est « l'impact mécanique des fluctuations de l'activité sur le solde public » ; le structurel corrige de ce cycle.",
            "**Solde primaire** = solde **avant paiement des intérêts de la dette** ; il révèle la situation budgétaire « réelle ». Solde public = solde primaire − intérêts de la dette.",
        ],
        [
            calc("Recettes publiques 1 300 Mds€ ; dépenses 1 450 Mds€. Quel est le solde public ?", -150, "1 300 − 1 450 = **−150 Mds€** : déficit.", niveau=1, unite='Mds€'),
            calc("Le solde public est de −150 Mds€ et les intérêts de la dette s'élèvent à 50 Mds€. Quel est le solde primaire ?", -100, "Solde primaire = solde public + intérêts = −150 + 50 = **−100 Mds€** (avant charge de la dette).", niveau=2, unite='Mds€'),
            calc("Prélèvements obligatoires 1 100 Mds€ ; PIB 2 400 Mds€. Taux de prélèvements obligatoires (en %, au dixième) ?", 1100 / 2400 * 100, "1 100 ÷ 2 400 = **45,8 %**.", niveau=1, unite='%', tolerance=0.1),
            calc("Fonction d'imposition T = 0,25 Y + 40. Quel est le montant des impôts pour Y = 2 000 ?", 540, "T = 0,25 × 2 000 + 40 = **540**.", niveau=1, unite=''),
            calc("Solde public −90 ; solde conjoncturel −35. Quel est le solde structurel ?", -55, "Solde public = structurel + conjoncturel → structurel = −90 − (−35) = **−55**.", niveau=2, unite=''),
            qcm("Le solde conjoncturel correspond :", ["À l'impact mécanique des fluctuations de l'activité sur le solde public", "Au solde corrigé du cycle", "Au solde hors intérêts", "À la dette publique"], 0, "Définition de la Commission européenne et de l'OCDE."),
            vf("La hausse du taux de prélèvements obligatoires en France vient surtout des impôts.", False, "Elle vient surtout des **cotisations sociales** (meilleure protection sociale, vieillissement).", niveau=2),
            qcm("Un impôt est égal à :", ["Taux d'imposition × base d'imposition", "Recettes − dépenses", "PIB × déficit", "Dette / PIB"], 0, "La base est aussi appelée assiette fiscale."),
        ], formules=["Solde public = recettes − dépenses", "Solde public = structurel + conjoncturel", "Solde primaire = solde public + intérêts de la dette", "T = t·Y + T0"])

    n26 = nm(
        'politique-budgetaire', "Politique budgétaire, politique fiscale et stabilisateurs automatiques",
        "En modifiant ses dépenses ou ses recettes, l'État cherche à **stabiliser** l'activité : la **relancer** (dépenses ↑, impôts ↓) ou la **ralentir** (dépenses ↓, impôts ↑).",
        [
            "Politique budgétaire **discrétionnaire** : décision délibérée de modifier le budget.",
            "**Stabilisateurs automatiques** : sans décision, les recettes augmentent en expansion (TVA, impôts) et les dépenses (chômage) diminuent ; l'inverse en récession → effet **contra-cyclique** qui lisse les fluctuations.",
            "**Politique fiscale** : agir sur les **taux** d'imposition (baisse pour relancer) ou sur la **base** d'imposition (élargir ou réduire la liste des revenus imposables).",
            "Autres politiques : monétaire, commerciale, de la concurrence, industrielle, de l'emploi.",
            "Les deux grandes politiques de stabilisation étudiées : **budgétaire** et **monétaire**.",
        ],
        [
            qcm("Pour relancer l'activité, l'État peut :", ["Augmenter les dépenses publiques", "Baisser les impôts", "Augmenter les impôts", "Réduire les dépenses publiques"], [0, 1], "Relance = politique budgétaire expansionniste."),
            qcm("En récession, les allocations chômage augmentent et les recettes de TVA baissent sans décision de l'État. C'est :", ["L'effet des stabilisateurs automatiques", "Une politique discrétionnaire", "Une politique monétaire", "Le théorème de Haavelmo"], 0, "Ils jouent un rôle contra-cyclique."),
            vf("Les stabilisateurs automatiques amplifient les fluctuations de l'activité.", False, "Ils les **atténuent** (effet contra-cyclique)."),
            qcm("Élargir la liste des revenus imposables est une action sur :", ["La base d'imposition", "Le taux d'imposition", "Les dépenses publiques", "La masse monétaire"], 0, "Politique fiscale par l'assiette."),
            qcm("Une politique budgétaire est dite discrétionnaire lorsque :", ["L'État décide délibérément de modifier ses dépenses ou ses recettes", "Elle résulte automatiquement de la conjoncture", "Elle est décidée par la banque centrale", "Le budget est équilibré"], 0, "Par opposition aux stabilisateurs automatiques."),
            vf("En période de forte croissance, les stabilisateurs automatiques freinent l'activité.", True, "Les impôts augmentent et les dépenses sociales diminuent, ce qui modère la demande.", niveau=2),
            S(courte("Pourquoi peut-on parler de « stabilisateur fiscal » lorsque l'impôt dépend du revenu (T = T0 + τY) ?",
                     "Parce qu'un choc négatif réduit le revenu, donc les impôts payés : le revenu disponible baisse moins, la consommation aussi, et le multiplicateur est plus faible (1/(1 − c(1 − τ)) au lieu de 1/(1 − c)). La baisse du revenu est amortie.", niveau=3), td(4)),
            courte("Donne un exemple de politique fiscale de relance et explique son effet.", "Baisser le taux de l'impôt sur le revenu : le revenu disponible des ménages augmente, leur consommation aussi, ce qui augmente la demande et, par le multiplicateur, la production.", niveau=2),
        ])

    # TD4 ex2
    c = 0.75
    Y1 = (350 + 350 + 450) / (1 - c); C1 = 350 + c * Y1
    T0 = 400
    Y4 = (1150 - c * T0) / (1 - c); C4 = 350 + c * (Y4 - T0)
    Y7 = (1150 - c * T0) / (1 - c * 0.8); C7 = 350 + c * (Y7 - T0 - 0.2 * Y7)
    n27 = nm(
        'multiplicateurs-budget', "Multiplicateurs des dépenses publiques, des impôts et des transferts",
        "Dans Y = C + I + G avec C = c·Yd + C0, une hausse des dépenses publiques ΔG accroît le revenu de **ΔY = ΔG / (1 − c)** : c'est le **multiplicateur des dépenses publiques** (ex. c = 0,8 → k = 5).",
        [
            "**Impôt forfaitaire (T = T0)** : kG = 1/(1 − c) ; **kT = −c/(1 − c)** ; kR (transferts) = c/(1 − c).",
            "**Impôt proportionnel (T = T0 + tY)** : kG = **1/(1 − c(1 − t))** ; kT = −c/(1 − c(1 − t)) ; kR = c/(1 − c(1 − t)). Ex. c = 0,8, t = 0,3 → kG = 2,27.",
            "Revenu d'équilibre : Y = [C0 + I0 + G0 − c·T0 + c·R] / (1 − c(1 − t)).",
            "|kT| < kG : une baisse d'impôt est **moins efficace** qu'une hausse équivalente des dépenses, car une partie du revenu rendu est épargnée.",
            "L'impôt proportionnel **réduit** le multiplicateur : c'est un stabilisateur automatique.",
            "Le multiplicateur est plus élevé en récession (capacités oisives) qu'au plein-emploi ; il est difficile à mesurer ; il baisse si les ménages épargnent un revenu perçu comme temporaire (Friedman).",
        ],
        [
            calc("c = 0,8 et impôts forfaitaires. Quel est le multiplicateur des dépenses publiques ?", 5, "k = 1/(1 − 0,8) = **5** : 100 de dépenses → 500 de revenu.", niveau=1, unite=''),
            calc("Exemple du cours : c = 0,8 et t = 0,3. Quel est le multiplicateur des dépenses publiques (au centième) ?", 1 / (1 - 0.8 * 0.7), "k = 1/(1 − 0,8 × 0,7) = 1/0,44 = **2,27**.", niveau=2, unite='', tolerance=0.01),
            S(calc("TD 4, ex. 1 : c = 0,8 et t = 0,25. Quel est le multiplicateur des dépenses publiques ?", 2.5, "kG = 1/(1 − 0,8 × 0,75) = 1/0,4 = **2,5**.", niveau=2, unite=''), td(4)),
            S(calc("TD 4, ex. 1 : même économie (c = 0,8 ; t = 0,25). Quel est le multiplicateur des impôts forfaitaires Tx ?", -2, "kTx = −c/(1 − c(1 − t)) = −0,8/0,4 = **−2** ; celui des transferts vaut +2.", niveau=2, unite=''), td(4)),
            S(calc("TD 4, ex. 2 : C = C0 + 0,75 Y avec C0 = I0 = 350 et G0 = 450. Quel est le revenu d'équilibre ?", Y1, "Y = (350 + 350 + 450)/(1 − 0,75) = 1 150/0,25 = **4 600** ; C = 350 + 0,75 × 4 600 = %s." % f(C1), niveau=2, unite=''), td(4)),
            S(calc("TD 4, ex. 2 : l'État augmente G de 50 (financé par emprunt). Quelle est la hausse du revenu ?", 200, "ΔY = 50/(1 − 0,75) = **200** ; ΔC = 0,75 × 200 = 150.", niveau=2, unite=''), td(4)),
            S(calc("TD 4, ex. 2 (question 4) : on introduit des impôts forfaitaires T0 avec un déficit G0 − T0 = 50 (donc T0 = 400). Quel est le revenu d'équilibre ?", Y4,
                   "Y = (C0 + I0 + G0 − c·T0)/(1 − c) = (1 150 − 300)/0,25 = **3 400** ; C = 350 + 0,75 × (3 400 − 400) = %s." % f(C4), niveau=3, unite=''), td(4)),
            S(calc("TD 4, ex. 2 (question 5) : effet sur le revenu d'une **baisse d'impôts** de 30 ?", 90, "ΔY = −c/(1 − c) × ΔT = −3 × (−30) = **+90**, contre +120 pour une hausse de G de 30 : la dépense publique est plus efficace.", niveau=2, unite=''), td(4)),
            S(calc("TD 4, ex. 2 (question 7) : on reprend T0 = 400 et on ajoute un impôt proportionnel τ = 20 % (T = 400 + 0,2 Y). Quel est le revenu d'équilibre ?", Y7,
                   "Y = (1 150 − 0,75 × 400)/(1 − 0,75 × 0,8) = 850/0,4 = **%s** ; C = %s." % (f(Y7), f(C7)), niveau=3, unite=''), td(4, True)),
            S(calc("TD 4, ex. 2 (question 8) : avec τ = 20 %, l'investissement baisse de 50. De combien baisse le revenu ?", -125, "ΔY = −50/0,4 = **−125**, contre −200 sans impôt proportionnel : l'impôt joue le rôle de **stabilisateur fiscal**.", niveau=3, unite=''), td(4)),
        ], formules=["Forfaitaire : kG = 1/(1 − c) ; kT = −c/(1 − c) ; kR = c/(1 − c)", "Proportionnel : kG = 1/(1 − c(1 − t)) ; kT = −c/(1 − c(1 − t))", "Y = (C0 + I0 + G0 − cT0 + cR)/(1 − c(1 − t))"])

    n28 = nm(
        'haavelmo', "Le théorème de Haavelmo (budget équilibré)",
        "Si l'État finance **entièrement** une hausse de ses dépenses par une hausse **égale** des impôts forfaitaires (ΔG0 = ΔT0), le revenu augmente du même montant : **le multiplicateur du budget équilibré vaut 1**.",
        [
            "ΔY = ΔG/(1 − c) − c·ΔT/(1 − c) = (1 − c)/(1 − c) · ΔG = **ΔG**.",
            "Une relance à budget équilibré n'est donc **pas neutre** : elle est expansionniste.",
            "Avec un impôt proportionnel (t > 0), le multiplicateur de budget équilibré devient (1 − c)/(1 − c(1 − t)), **inférieur à 1**.",
            "Intuition : la dépense publique est entièrement dépensée, alors qu'une partie de l'impôt aurait de toute façon été épargnée.",
        ],
        [
            calc("Haavelmo : l'État augmente G de 30 et les impôts forfaitaires de 30 (c = 0,75). De combien augmente le revenu ?", 30, "Multiplicateur de budget équilibré = 1 : ΔY = **30**.", niveau=1, unite=''),
            S(calc("TD 4, ex. 2 (question 6) : relance de 30 en maintenant le déficit à 50 (ΔG = ΔT = 30). Nouveau revenu d'équilibre, en partant de Y = 3 400 ?", 3430, "ΔY = ΔG = 30 → **3 430** ; la consommation reste à 2 600 (le revenu disponible ne change pas : 3 430 − 430 = 3 000).", niveau=2, unite=''), td(4)),
            calc("c = 0,6, impôts forfaitaires. Effet sur le revenu de ΔG = 100 seul ?", 250, "1/(1 − 0,6) × 100 = **250**.", niveau=1, unite=''),
            calc("Même économie (c = 0,6) : effet de ΔT = +100 seul ?", -150, "−0,6/0,4 × 100 = **−150** ; total avec ΔG = 100 : 250 − 150 = 100 = ΔG ✓ (Haavelmo).", niveau=2, unite=''),
            vf("Selon le théorème de Haavelmo, une hausse des dépenses financée par une hausse égale des impôts est sans effet sur le revenu.", False, "Elle augmente le revenu du montant de la dépense (multiplicateur égal à 1)."),
            calc("Avec un impôt proportionnel : c = 0,8 et t = 0,25. Quel est le multiplicateur de budget équilibré (1 − c)/(1 − c(1 − t)) ?", 0.5, "(1 − 0,8)/(1 − 0,6) = 0,2/0,4 = **0,5** < 1.", niveau=3, unite=''),
            qcm("Pourquoi une hausse d'impôt de 100 réduit-elle moins la demande qu'une hausse de dépenses de 100 ne l'augmente ?", ["Parce qu'une partie du revenu prélevé aurait été épargnée", "Parce que l'État épargne l'impôt", "Parce que les impôts augmentent les prix", "Parce que les ménages empruntent"], 0, "Seule la part c du revenu prélevé aurait été consommée."),
            S(courte("Quel intérêt présente une relance à budget équilibré pour un État soumis au Pacte de stabilité (déficit maximal) ?", "Elle permet de soutenir l'activité (le revenu augmente du montant de la dépense) sans creuser le déficit public, puisque la dépense est financée par l'impôt.", niveau=3), td(4)),
        ], formules=["ΔG = ΔT0 ⇒ ΔY = ΔG (multiplicateur = 1)"])

    n29 = nm(
        'economie-ouverte', "Équilibre et multiplicateur en économie ouverte",
        "En économie ouverte, Y = (C + I + G) + (X − Z) : **demande interne + demande externe**. Les importations constituent une **fuite** : le multiplicateur est plus faible.",
        [
            "**Importations** Z = m·Y + Z0 : elles augmentent avec le revenu (m = **propension marginale à importer**, 0 < m < 1) et diminuent avec le prix relatif des produits étrangers (taux de change réel Q = E·P*/P).",
            "**Exportations** X : dépendent de l'activité du reste du monde Y* et du taux de change réel (X ↑ si Q ↑).",
            "**Solde commercial** NX = X − Z : une hausse du revenu national le dégrade (dNX/dY = −m).",
            "**Multiplicateur en économie ouverte : 1/(1 − c(1 − t) + m)**. Ex. c = 0,8, t = 0,3, m = 0,3 : il passe de 2,27 à **1,35**.",
            "La relance profite en partie aux producteurs étrangers : d'où l'intérêt de **coordonner** les relances (UE). Avec un partenaire identique, le multiplicateur remonte à 1,61 ; si les deux relancent ensemble, les effets s'amplifient.",
            "Le multiplicateur est faible pour une économie très ouverte, fort pour une économie peu ouverte.",
        ],
        [
            calc("c = 0,8 ; t = 0,3 ; m = 0,3. Quel est le multiplicateur des dépenses publiques en économie ouverte (au centième) ?", 1 / (1 - 0.8 * 0.7 + 0.3), "1/(1 − 0,56 + 0,3) = 1/0,74 = **1,35**.", niveau=2, unite='', tolerance=0.01),
            calc("c = 0,75 ; impôts forfaitaires ; m = 0,25. Quel est le multiplicateur ?", 2, "1/(1 − 0,75 + 0,25) = 1/0,5 = **2** (contre 4 en économie fermée).", niveau=2, unite=''),
            calc("Avec ce multiplicateur de 2 et m = 0,25, l'État augmente G de 100. De combien varie le solde commercial ?", -50, "ΔY = 200 ; ΔZ = m·ΔY = 50 → ΔNX = **−50**.", niveau=3, unite=''),
            qcm("Pourquoi le multiplicateur est-il plus faible en économie ouverte ?", ["Une partie de la demande supplémentaire part en importations", "Les exportations baissent toujours", "L'État dépense moins", "Les prix augmentent"], 0, "Les importations sont une fuite hors du circuit national."),
            qcm("Une hausse du revenu national, toutes choses égales par ailleurs :", ["Dégrade le solde commercial", "Améliore le solde commercial", "N'a pas d'effet sur les importations", "Augmente les exportations"], 0, "Les importations augmentent (dNX/dY = −m)."),
            vf("Pour un pays très ouvert, une relance budgétaire isolée est très efficace.", False, "Le multiplicateur est faible quand l'économie est très ouverte : d'où l'intérêt de coordonner les relances."),
            qcm("Selon le cours, que se passe-t-il si les pays voisins coordonnent leurs relances budgétaires ?", ["Les effets multiplicateurs s'amplifient via le commerce extérieur", "Les effets s'annulent", "Le multiplicateur devient nul", "Seuls les importateurs gagnent"], 0, "Les importations des uns sont les exportations des autres.", niveau=2),
            qcm("Les exportations d'un pays dépendent positivement :", ["De l'activité du reste du monde", "Du taux de change réel Q (prix relatif des produits étrangers)", "Du revenu national uniquement", "Des impôts nationaux"], [0, 1], "X = X(Y*, Q) avec des dérivées positives.", niveau=2),
        ], formules=["Y = C + I + G + (X − Z)", "Z = mY + Z0", "k = 1/(1 − c(1 − t) + m)"])

    fig_is = fig('Y', 'r (%)', 1700, 12, [droite(30, -0.02, 1000, 1500, 'IS', 1), droite(32, -0.02, 1100, 1600, "IS'", 1, True)], titre='Courbe IS : Y = 1 500 − 50 r ; IS\' après une hausse de la demande autonome', xmin=900, gradx=[1000, 1250, 1500], grady=[2, 4, 6, 8, 10], fleches=[{'de': [1180, 6.6], 'a': [1260, 6.6]}])
    n30 = nm(
        'courbe-is', "L'équilibre du bloc réel : la courbe IS",
        "La courbe **IS** rassemble les couples (Y, r) pour lesquels le **marché des biens et services est en équilibre** (Y = C + I + G, soit I + G = S + T).",
        [
            "Avec I = I0 − α·r : Y = [C0 − c·T0 + I0 + G0 − α·r] / (1 − c(1 − t)).",
            "**IS est décroissante** dans le plan (Y, r) : r ↑ → investissement ↓ → demande ↓ → revenu ↓.",
            "Pente : Δr/ΔY = −(1 − c(1 − t)) / α.",
            "Une baisse de r → **déplacement le long** de IS.",
            "**Déplacement de IS vers la droite** : optimisme des agents (C ou I ↑), politique budgétaire expansionniste (G ↑) ou baisse des impôts ; s'y ajoute l'effet multiplicateur.",
            "Écriture alternative : **I(r) = S(Y) + (T − G)**.",
        ],
        [
            calc("Exemple du cours : C = 100 + 0,6 Y et I = 500 − 20 r. Quel est Y sur la courbe IS lorsque r = 5 ?", 1250, "IS : S = I → −100 + 0,4 Y = 500 − 20 r → Y = 1 500 − 50 r ; pour r = 5 : **1 250**.", niveau=2, unite='', figure=fig_is),
            calc("Avec IS : Y = 1 500 − 50 r, quel taux d'intérêt correspond à Y = 1 400 ?", 2, "1 400 = 1 500 − 50 r → r = **2 %**.", niveau=1, unite='%'),
            qcm("Pourquoi la courbe IS est-elle décroissante ?", ["Une hausse du taux d'intérêt réduit l'investissement donc la demande et le revenu", "Une hausse du revenu augmente la demande de monnaie", "La banque centrale fixe le taux", "Les prix baissent"], 0, "C'est le lien taux d'intérêt → investissement → revenu.", figure=fig_is),
            qcm("Une hausse des dépenses publiques :", ["Déplace IS vers la droite", "Déplace IS vers la gauche", "Fait se déplacer le long de IS", "Déplace LM"], 0, "À taux d'intérêt donné, la demande et donc le revenu d'équilibre augmentent.", figure=fig_is),
            qcm("Une baisse du taux d'intérêt provoque :", ["Un déplacement le long de IS vers un revenu plus élevé", "Un déplacement de IS vers la droite", "Un déplacement de IS vers la gauche", "Aucun effet"], 0, "Le taux d'intérêt est la variable de l'axe vertical : on se déplace sur la courbe.", niveau=2),
            calc("C = 100 + 0,6 Y, I = 500 − 20 r. La demande autonome augmente de 40. Quelle est la nouvelle équation IS : Y = a − 50 r ; donne a.", 1600, "−100 + 0,4 Y = 540 − 20 r → Y = 1 600 − 50 r : IS se déplace de 40/0,4 = 100 vers la droite ; **a = 1 600**.", niveau=3, unite='', figure=fig_is),
            calc("c = 0,8, t = 0,25, α = 20. Quelle est la pente Δr/ΔY de IS ?", -0.02, "−(1 − 0,8 × 0,75)/20 = −0,4/20 = **−0,02**.", niveau=3, unite='', tolerance=0.001),
            vf("Une vague d'optimisme des entreprises déplace la courbe IS vers la droite.", True, "L'investissement augmente à taux d'intérêt donné."),
        ], formules=["IS : Y = (C0 − cT0 + I0 + G0 − αr) / (1 − c(1 − t))", "I(r) = S(Y) + (T − G)"], figure=fig_is)
    return chapitre('ch-etat', 'Chapitre 4 — Les dépenses publiques et le rôle de l\'État', [n24, n25, n26, n27, n28, n29, n30])


def ch5():
    n31 = nm(
        'fonctions-monnaie', "Les fonctions de la monnaie ; la monnaie, actif de patrimoine",
        "La monnaie remplit trois fonctions : **unité de compte** (calcul économique), **instrument de paiement** (échange) et **réserve de valeur** (transfert du pouvoir d'achat dans le temps).",
        [
            "**Unité de compte** : mesure la valeur de biens hétérogènes ; ramène les prix relatifs à un prix absolu (nominal) → économie d'information et de calcul.",
            "**Instrument de paiement** : « équivalent général » accepté par tous ; son transfert éteint définitivement les dettes ; repose sur la **confiance**, renforcée par le **pouvoir libératoire et légal** donné par l'État/la banque centrale.",
            "**Réserve de valeur** : permet de différer l'utilisation du pouvoir d'achat (si les prix sont stables).",
            "Le patrimoine se compose d'**actifs réels** (immeubles, machines, biens durables), d'**actifs financiers** (actions, obligations, TCN) et d'**actifs monétaires** ; les agents arbitrent selon le **risque** et le **rendement**.",
            "La monnaie est l'**actif le plus liquide** : valeur nominale **stable** (pas de risque en capital) et **immédiatement disponible** pour régler des transactions, sans coût ni délai ; elle est divisible.",
        ],
        [
            qcm("Quelles sont les trois fonctions de la monnaie ?", ["Unité de compte, instrument de paiement, réserve de valeur", "Production, échange, consommation", "Crédit, épargne, investissement", "Impôt, dépense, emprunt"], 0, "Définition du cours."),
            qcm("Exprimer le prix de tous les biens en euros relève de la fonction :", ["D'unité de compte", "D'instrument de paiement", "De réserve de valeur", "De crédit"], 0, "La monnaie sert d'étalon commun."),
            qcm("Garder des billets pour acheter un vélo l'an prochain relève de la fonction :", ["De réserve de valeur", "D'unité de compte", "D'instrument de paiement", "De spéculation"], 0, "On transfère du pouvoir d'achat dans le temps."),
            vf("La monnaie est l'actif le plus liquide.", True, "Valeur nominale stable et disponibilité immédiate pour les paiements."),
            qcm("Un actif liquide se caractérise par :", ["Une valeur nominale stable", "Une disponibilité immédiate, sans coût, pour payer", "Un rendement élevé", "Un risque en capital important"], [0, 1], "Liquidité = stabilité de la valeur + convertibilité immédiate en moyens de paiement.", niveau=2),
            qcm("Les actions et obligations font partie des :", ["Actifs financiers", "Actifs réels", "Actifs monétaires", "Dettes"], 0, "Actifs réels : biens ; actifs financiers : titres ; actifs monétaires : monnaie."),
            vf("La fonction de réserve de valeur est mieux assurée en période d'inflation élevée.", False, "L'inflation érode le pouvoir d'achat de la monnaie détenue : la réserve de valeur suppose la stabilité des prix.", niveau=2),
            courte("Sur quoi repose l'acceptation de la monnaie comme moyen de paiement ?", "Sur la confiance (consensus social) : chacun croit pouvoir obtenir à tout moment n'importe quel bien en échange de monnaie. Cette confiance est renforcée par l'État et la banque centrale, qui donnent à la monnaie un pouvoir libératoire légal.", niveau=2),
        ])

    agr = tab(['Composante', 'Montant (Mds€)'], [['Billets et pièces', 1100], ['Dépôts à vue', 6500], ['Dépôts à terme ≤ 2 ans', 1100], ['Dépôts avec préavis ≤ 3 mois (livrets)', 2300], ['Pensions, titres d\'OPCVM monétaires, titres ≤ 2 ans', 700]], 'Zone euro (chiffres arrondis, fictifs)')
    n32 = nm(
        'agregats', "Les agrégats monétaires",
        "Les **agrégats monétaires** (« masse monétaire ») mesurent la quantité de monnaie disponible pour acheter des biens et services ; ils sont classés selon le **degré de liquidité** de leurs composants.",
        [
            "**M0** (base monétaire, monnaie centrale) : billets et pièces en circulation + avoirs des banques auprès de la banque centrale.",
            "**M1** (monnaie au sens **strict**) : billets et pièces + **dépôts à vue**.",
            "**M2** = M1 + **dépôts à terme ≤ 2 ans** + **dépôts avec préavis ≤ 3 mois** (livret A, LDDS, CEL, LEP…).",
            "**M3** (sens **large**) = M2 + instruments négociables émis par les IFM : **pensions**, **titres d'OPCVM monétaires**, titres de créance ≤ 2 ans.",
            "**M4** = M3 + **TCN** (bons du Trésor, billets de trésorerie, bons à moyen terme des sociétés non financières).",
            "Plus on va de M1 vers M3, moins les composants sont liquides.",
        ],
        [
            calc("Avec le tableau, calcule M1.", 7600, "M1 = billets et pièces + dépôts à vue = 1 100 + 6 500 = **7 600 Mds€**.", niveau=1, unite='Mds€', tableau=agr),
            calc("Calcule M2.", 11000, "M2 = M1 + dépôts à terme ≤ 2 ans + dépôts avec préavis ≤ 3 mois = 7 600 + 1 100 + 2 300 = **11 000 Mds€**.", niveau=2, unite='Mds€', tableau=agr),
            calc("Calcule M3.", 11700, "M3 = M2 + instruments négociables = 11 000 + 700 = **11 700 Mds€**.", niveau=2, unite='Mds€', tableau=agr),
            qcm("Un livret A fait partie de :", ["M2 (et donc M3), mais pas de M1", "M1", "M0", "M4 uniquement"], 0, "C'est un dépôt avec préavis ≤ 3 mois."),
            qcm("La monnaie au sens strict correspond à :", ["M1", "M0", "M2", "M3"], 0, "Billets, pièces et dépôts à vue."),
            qcm("Les bons du Trésor et les billets de trésorerie apparaissent dans :", ["M4", "M1", "M2", "M0"], 0, "M4 = M3 + TCN."),
            vf("Un compte courant (dépôt à vue) fait partie de M1.", True, "M1 = numéraire + dépôts à vue."),
            qcm("Classe les agrégats du plus liquide au moins liquide :", ["M1, M2, M3", "M3, M2, M1", "M2, M1, M3", "M1, M3, M2"], 0, "Chaque agrégat ajoute des actifs un peu moins liquides.", niveau=2),
        ], tableau=tab(['Agrégat', 'Contenu'], [['M0', 'Base monétaire : billets, pièces, réserves des banques à la BC'], ['M1', 'Billets et pièces + dépôts à vue'], ['M2', 'M1 + dépôts à terme ≤ 2 ans + dépôts avec préavis ≤ 3 mois'], ['M3', 'M2 + pensions, OPCVM monétaires, titres ≤ 2 ans'], ['M4', 'M3 + TCN (bons du Trésor, billets de trésorerie…)']]))

    n33 = nm(
        'theorie-quantitative', "Motifs de détention de la monnaie et théorie quantitative",
        "Keynes distingue trois motifs de demande de monnaie : **transaction** (dépenses courantes), **précaution** (imprévus) et **spéculation** (arbitrage entre liquidité et placement).",
        [
            "**Théorie quantitative (Fisher)** : **MV = PT** (équation des échanges) ; M masse monétaire, V vitesse de circulation, P prix, T transactions.",
            "Hypothèses : **T exogène** (plein-emploi), **V exogène** (habitudes, institutions) ⇒ **M détermine P** : si M augmente de x %, P augmente de x %.",
            "Pour contrôler l'inflation, il suffit de contrôler la masse monétaire. La monnaie est **neutre** (n'agit pas sur la production) : vision **dichotomique** (réel / monétaire séparés).",
            "**Équation de Cambridge** (Marshall, Pigou) : **Md = k·P·Y**, soit Md/P = kY avec **k = 1/V** : la demande de monnaie est proportionnelle au revenu.",
        ],
        [
            calc("M = 500, V = 4, T = 1 000. Quel est le niveau des prix P selon MV = PT ?", 2, "P = MV/T = 500 × 4 / 1 000 = **2**.", niveau=1, unite=''),
            calc("Selon la théorie quantitative, si la masse monétaire augmente de 10 % (V et T constants), de combien augmentent les prix ?", 10, "P = MV/T : P augmente dans la même proportion que M : **10 %**.", niveau=1, unite='%'),
            calc("La vitesse de circulation de la monnaie est de 5. Quel est le coefficient k de l'équation de Cambridge ?", 0.2, "k = 1/V = **0,2**.", niveau=1, unite=''),
            calc("Équation de Cambridge : k = 0,25, P = 1, Y = 2 400. Quelle est la demande de monnaie ?", 600, "Md = k·P·Y = 0,25 × 2 400 = **600**.", niveau=1, unite=''),
            qcm("Garder de l'argent liquide pour faire face à une panne imprévue de voiture relève du motif :", ["De précaution", "De transaction", "De spéculation", "De réserve légale"], 0, "Imprévus budgétaires = précaution."),
            qcm("Selon la théorie quantitative, la monnaie est :", ["Neutre : elle n'agit que sur les prix", "Active : elle stimule la production", "Inutile", "Une marchandise rare"], 0, "Conception dichotomique de l'économie."),
            vf("Dans la théorie quantitative, la vitesse de circulation de la monnaie dépend des habitudes et des institutions.", True, "V est exogène."),
            qcm("Arbitrer entre garder de la monnaie et acheter des obligations selon l'évolution attendue des taux relève du motif :", ["De spéculation", "De transaction", "De précaution", "De consommation"], 0, "Choix entre liquidité (valeur stable) et placements (valeur variable)."),
        ], formules=["MV = PT (Fisher)", "Md = k·P·Y, k = 1/V (Cambridge)"])

    PY, cc, r = 2000, 2, 0.005
    Ms = math.sqrt(cc * PY / (2 * r))
    n34 = nm(
        'baumol-tobin', "Le modèle de Baumol-Tobin : l'encaisse optimale de transaction",
        "Baumol (1952) et Tobin (1956) : un ménage dépense uniformément son revenu mensuel PY ; il peut placer une partie de son encaisse en **obligations** (intérêt r) mais chaque conversion coûte **c**. Il choisit l'encaisse moyenne qui **minimise son coût total**.",
        [
            "Encaisse moyenne avec n conversions : **M = PY / (2n)**.",
            "**Coût d'opportunité** de la monnaie (intérêts perdus) : CO = r·M ; **coût de transaction** : CT = c·n = c·PY/(2M).",
            "Coût total C = r·M + c·PY/(2M) ; minimum quand dC/dM = r − c·PY/(2M²) = 0.",
            "**Encaisse optimale : M* = √(c·PY / (2r))** ; en termes réels : (M/P)* = √(cR·Y / (2r)).",
            "La demande de monnaie dépend **négativement de r**, **positivement de Y** et du coût de transaction ; elle augmente **moins que proportionnellement** au revenu (économies d'échelle) : élasticités 0,5 et −0,5.",
        ],
        [
            calc("Revenu mensuel PY = 2 000 €, dépensé uniformément, avec n = 4 conversions dans le mois. Quelle est l'encaisse moyenne ?", 250, "M = PY/(2n) = 2 000/8 = **250 €**.", niveau=1),
            calc("PY = 2 000 €, coût par conversion c = 2 €, taux d'intérêt mensuel r = 0,5 %. Quelle est l'encaisse optimale M* (au centime) ?", Ms, "M* = √(2 × 2 000 / (2 × 0,005)) = √400 000 = **%s €**." % f(Ms), niveau=3),
            calc("Avec M = 250 € et r = 0,5 % par mois, quel est le coût d'opportunité mensuel ?", 1.25, "CO = r·M = 0,005 × 250 = **1,25 €**.", niveau=2),
            calc("Avec n = 4 conversions à 2 € chacune, quel est le coût de transaction mensuel ?", 8, "CT = c·n = **8 €**.", niveau=1),
            qcm("Selon Baumol-Tobin, une hausse du taux d'intérêt :", ["Réduit la demande de monnaie", "Augmente la demande de monnaie", "N'a aucun effet", "Augmente les prix"], 0, "Détenir de la monnaie coûte plus cher en intérêts perdus."),
            qcm("Si le revenu est multiplié par 4, l'encaisse optimale est multipliée par :", ["2", "4", "16", "1"], 0, "M* est proportionnelle à √Y : √4 = 2 (économies d'échelle).", niveau=3),
            vf("Dans le modèle de Baumol-Tobin, la demande de monnaie est proportionnelle au revenu, comme dans la théorie quantitative.", False, "Elle augmente **moins** que le revenu (élasticité 0,5)."),
            qcm("Le modèle de Baumol-Tobin s'applique surtout à :", ["M1 (motif de transaction)", "M3", "La base monétaire", "Le motif de spéculation"], 0, "Seul le motif de transaction est pris en compte.", niveau=2),
        ], formules=["M = PY / (2n)", "C = r·M + c·PY/(2M)", "M* = √(c·PY / (2r))"])

    rc = 0.10 / 1.10 * 100
    n35 = nm(
        'speculation', "Demande de monnaie pour motif de spéculation : obligations et taux critique",
        "Le **cours (prix) des obligations varie en sens inverse du taux d'intérêt**. Les spéculateurs arbitrent entre monnaie (valeur stable) et obligations (coupon + gain ou perte en capital).",
        [
            "Obligation perpétuelle de coupon fixe : **PB = coupon / r** (pour un revenu de 1 : PB = 1/r).",
            "Ex. : obligation de 1 000 € à 10 % (coupon 100) ; si les taux tombent à 8 %, son cours monte à **1 250 €** (100/1 250 = 8 %).",
            "Gain en capital anticipé : **ge = r / re − 1** (re = taux anticipé) ; rendement total anticipé : Re = r + ge.",
            "**Taux critique (Tobin) : rc = re / (1 + re)**. Si r > rc : portefeuille **tout en obligations** (Md = 0) ; si r < rc : **tout en monnaie**.",
            "Au niveau macro, en agrégeant des agents aux anticipations différentes : demande spéculative **décroissante** du taux d'intérêt.",
            "**Md = L(Y) + L(r)** : transaction (∂L/∂Y > 0) + spéculation (∂L/∂r < 0).",
        ],
        [
            calc("Une obligation perpétuelle verse un coupon de 100 € par an. Les taux de marché sont à 8 %. Quel est son cours ?", 1250, "PB = 100 / 0,08 = **1 250 €**.", niveau=1),
            calc("Même obligation (coupon 100 €) : les taux montent à 12,5 %. Quel est son cours ?", 800, "PB = 100 / 0,125 = **800 €** : les taux montent, les cours baissent.", niveau=1),
            calc("Le taux d'intérêt anticipé est re = 10 %. Quel est le taux critique rc (en %, au centième) ?", rc, "rc = re/(1 + re) = 0,10/1,10 = **9,09 %**.", niveau=2, unite='%', tolerance=0.01),
            qcm("Avec re = 10 % (rc = 9,09 %) et un taux actuel r = 12 %, le spéculateur détient :", ["Uniquement des obligations", "Uniquement de la monnaie", "Moitié-moitié", "Rien"], 0, "r > rc : le rendement total anticipé des obligations est positif."),
            calc("Taux actuel r = 4 %, taux anticipé re = 5 %. Quel est le gain (ou la perte) en capital anticipé ge (en %) ?", -20, "ge = r/re − 1 = 0,04/0,05 − 1 = **−20 %** : on anticipe une baisse du cours.", niveau=3, unite='%'),
            qcm("Quand le taux d'intérêt est très bas, les agents préfèrent détenir de la monnaie car :", ["Ils anticipent une hausse des taux, donc une baisse du cours des obligations", "La monnaie rapporte beaucoup", "Les obligations sont interdites", "Les prix baissent"], 0, "Ils évitent une perte en capital.", niveau=2),
            vf("Le cours des obligations et le taux d'intérêt évoluent dans le même sens.", False, "Ils évoluent en **sens inverse** : PB = coupon/r."),
            qcm("La demande de monnaie totale s'écrit Md = L(Y, r) avec :", ["∂L/∂Y > 0 et ∂L/∂r < 0", "∂L/∂Y < 0 et ∂L/∂r > 0", "∂L/∂Y > 0 et ∂L/∂r > 0", "∂L/∂Y = 0"], 0, "Transaction : croît avec Y ; spéculation : décroît avec r.", niveau=2),
        ], formules=["PB = coupon / r", "ge = r / re − 1 ; Re = r + ge", "rc = re / (1 + re)", "Md = L(Y) + L(r)"])

    n36 = nm(
        'offre-monnaie', "L'offre de monnaie et la banque centrale",
        "La monnaie est créée par la **banque centrale** (« banque des banques ») et par les **banques de second rang**. Pour simplifier, la banque centrale **contrôle l'offre de monnaie**, qui est **exogène** : **Ms = M0** (indépendante de r et de Y).",
        [
            "**Monnaie banque centrale** (billets, pièces) = **base monétaire** M0 : **B = C + RO** (billets et pièces + réserves des banques auprès de la BC).",
            "Bilan de la BC : **actif** = crédits à l'État (bons du Trésor), refinancement des banques, réserves de change ; **passif** = billets en circulation et réserves des banques.",
            "Bilan des banques : actif = réserves, crédits, titres ; passif = dépôts à vue, refinancement, capitaux propres.",
            "**Masse monétaire M = C + D** (billets et pièces détenus par le public + dépôts à vue).",
            "Chaque banque a un compte à la BC pour les règlements interbancaires. La BC peut être **indépendante** du gouvernement.",
            "Un déficit public financé par la vente de bons du Trésor à la BC crée de la monnaie.",
        ],
        [
            calc("Billets et pièces C = 200 ; réserves obligatoires des banques RO = 50. Quelle est la base monétaire ?", 250, "B = C + RO = **250**.", niveau=1, unite=''),
            calc("Billets et pièces détenus par le public C = 200 ; dépôts à vue D = 800. Quelle est la masse monétaire (sens étroit) ?", 1000, "M = C + D = **1 000**.", niveau=1, unite=''),
            qcm("Que trouve-t-on au **passif** du bilan de la banque centrale ?", ["Les billets en circulation et les réserves des banques", "Les crédits à l'État", "Les réserves de change", "Le refinancement des banques"], 0, "Ces éléments constituent la base monétaire."),
            qcm("Dans le modèle du cours, l'offre de monnaie est :", ["Exogène, fixée par la banque centrale", "Croissante avec le taux d'intérêt", "Croissante avec le revenu", "Déterminée par les ménages"], 0, "Ms = M0, indépendante de r et de Y."),
            vf("On appelle la banque centrale la « banque des banques ».", True, "Elle alimente en liquidité les banques de second rang et régule le marché monétaire."),
            qcm("Les banques de second rang sont :", ["Les banques commerciales", "La banque centrale", "Le Trésor public", "Les compagnies d'assurance"], 0, "Elles participent à la création monétaire en accordant des crédits."),
            calc("Masse monétaire M = 1 200 ; dépôts à vue D = 950. Quel est le montant des billets et pièces détenus par le public ?", 250, "C = M − D = **250**.", niveau=2, unite=''),
            courte("Comment un déficit public peut-il conduire à une création de monnaie ?", "L'État émet des bons du Trésor pour financer l'excès de ses dépenses sur ses recettes ; s'il les vend à la banque centrale en échange de billets, ces billets sont mis en circulation lorsqu'il paie ses dépenses : la masse monétaire augmente.", niveau=3),
        ], formules=["B = C + RO (base monétaire)", "M = C + D (masse monétaire)", "Ms = M0 (exogène)"])

    fig_lm = fig('Y', 'r (%)', 4600, 12, [droite(-10, 0.005, 2000, 4400, 'LM', 2), droite(-12, 0.005, 2400, 4600, "LM'", 2, True)], titre='Courbe LM : r = (k/h)·Y − M0/h avec k = 0,25, h = 50, M0 = 500 ; LM\' après une hausse de M0 à 600', xmin=1800, gradx=[2000, 3000, 4000], grady=[2, 4, 6, 8, 10])
    n37 = nm(
        'courbe-lm', "L'équilibre du marché de la monnaie : la courbe LM",
        "La courbe **LM** rassemble les couples (Y, r) pour lesquels le **marché de la monnaie** (et des titres) est en équilibre : **M/P = L(Y, r)**.",
        [
            "Avec Md/P = kY − h·r et Ms = M0 (P = 1) : **r = (k/h)·Y − M0/h**.",
            "**LM est croissante** : si Y ↑, la demande de monnaie de transaction ↑ ; à offre donnée, il faut une hausse de r (le « prix de la monnaie ») pour réduire la demande spéculative et rétablir l'équilibre.",
            "**Politique monétaire restrictive** (M ↓) : excès de demande de monnaie → r ↑ → **LM se déplace vers le haut** (à gauche).",
            "**Politique monétaire expansionniste** (M ↑) : **LM se déplace vers le bas** (à droite).",
            "Le marché des titres est implicite (loi de Walras ou substituabilité monnaie/titres).",
        ],
        [
            calc("Md = 0,25 Y − 50 r ; Ms = 500. Quel est le taux d'intérêt d'équilibre pour Y = 3 000 ?", 5, "0,25 × 3 000 − 50 r = 500 → 750 − 500 = 50 r → r = **5 %**.", niveau=2, unite='%', figure=fig_lm),
            calc("Exemple du cours : Mt = 0,2 Y ; Msp = 200 − 10 r ; Ms = 400. Quel est Y sur LM pour r = 5 ?", 1250, "0,2 Y + 200 − 10 r = 400 → Y = 1 000 + 50 r = **1 250**.", niveau=2, unite=''),
            calc("Même exemple : la banque centrale porte l'offre de monnaie à 420. Pour r = 5, quel est le nouveau Y sur LM ?", 1350, "0,2 Y + 200 − 50 = 420 → 0,2 Y = 270 → Y = **1 350** : LM s'est déplacée vers la droite.", niveau=3, unite=''),
            qcm("Pourquoi la courbe LM est-elle croissante ?", ["Une hausse du revenu augmente la demande de monnaie, ce qui fait monter le taux d'intérêt", "Une hausse du taux d'intérêt augmente l'investissement", "La banque centrale augmente M quand Y augmente", "Les prix augmentent"], 0, "À offre de monnaie donnée, il faut un r plus élevé pour réduire la demande spéculative.", figure=fig_lm),
            qcm("Une politique monétaire restrictive (baisse de M) :", ["Déplace LM vers le haut (à gauche)", "Déplace LM vers le bas (à droite)", "Déplace IS", "Fait se déplacer le long de LM"], 0, "À revenu donné, le taux d'intérêt d'équilibre augmente.", figure=fig_lm),
            S(qcm("Lecture du graphique : après le passage de M0 = 500 à M0 = 600, pour Y = 3 000, le taux d'intérêt d'équilibre :", ["Baisse de 5 % à 3 %", "Monte de 5 % à 7 %", "Reste à 5 %", "Devient nul"], 0, "Sur LM' : r = 0,005 × 3 000 − 12 = 3 %. Une politique expansionniste fait baisser r.", niveau=2, figure=fig_lm), COURS),
            vf("Sur la courbe LM, une hausse du revenu s'accompagne d'une hausse du taux d'intérêt.", True, "LM est croissante dans le plan (Y, r)."),
            calc("Md = kY − hr avec k = 0,25 et h = 50. Quelle est la pente Δr/ΔY de LM ?", 0.005, "Pente = k/h = 0,25/50 = **0,005**.", niveau=2, unite='', tolerance=0.0001),
        ], formules=["LM : Ms/P = kY − hr ⇒ r = (k/h)Y − M0/h"], figure=fig_lm)
    return chapitre('ch-monnaie', 'Chapitre 5 — La sphère monétaire : le marché de la monnaie', [n31, n32, n33, n34, n35, n36, n37])


def ch6():
    n38 = nm(
        'islm-equilibre', "Construction et calcul de l'équilibre IS-LM",
        "Le modèle **IS-LM** (**Hicks, 1937**, à partir de Keynes) détermine l'**équilibre macroéconomique global** à prix donnés : l'unique couple (Y, r) qui équilibre **simultanément** le marché des biens et services (IS) et le marché de la monnaie (LM).",
        [
            "Trois marchés : biens et services, monnaie, titres (ce dernier est implicite par la loi de Walras).",
            "**IS** : Y = C(Y) + I(r) + G0 — décroissante. **LM** : M/P = L(Y, r) — croissante.",
            "L'équilibre E est à l'**intersection** de IS et LM.",
            "**Exemple du cours** : C = 100 + 0,6Y ; I = 500 − 20r ; Mt = 0,2Y ; Msp = 200 − 10r ; Ms = 400 ⇒ IS : **Y = 1 500 − 50r** ; LM : **Y = 1 000 + 50r** ⇒ **r = 5 ; Y = 1 250**.",
            "Méthode : écrire IS (S = I ou Y = C + I + G), écrire LM (Md = Ms), égaliser les deux expressions de Y pour trouver r, puis en déduire Y.",
        ],
        [
            calc("Exemple du cours : IS : Y = 1 500 − 50 r et LM : Y = 1 000 + 50 r. Quel est le taux d'intérêt d'équilibre ?", 5, "1 500 − 50 r = 1 000 + 50 r → 100 r = 500 → **r = 5**.", niveau=1, unite='%', figure=FIG_ISLM),
            calc("Même exemple : quel est le revenu d'équilibre ?", 1250, "Y = 1 500 − 50 × 5 = **1 250** (ou 1 000 + 250).", niveau=1, unite='', figure=FIG_ISLM),
            calc("À l'équilibre (Y = 1 250, r = 5), quel est l'investissement (I = 500 − 20 r) ?", 400, "I = 500 − 100 = **400** ; épargne S = −100 + 0,4 × 1 250 = 400 = I ✓.", niveau=2, unite=''),
            calc("Autre économie : IS : Y = 2 000 − 100 r ; LM : Y = 1 400 + 50 r. Quel est le revenu d'équilibre ?", 1600, "2 000 − 100 r = 1 400 + 50 r → r = 4 ; Y = 2 000 − 400 = **1 600**.", niveau=2, unite=''),
            calc("C = 200 + 0,75 Y ; I = 300 − 25 r ; Md = 0,5 Y − 50 r ; Ms = 900. Quel est le taux d'intérêt d'équilibre ?", 4,
                 "IS : 0,25 Y = 500 − 25 r → Y = 2 000 − 100 r. LM : 0,5 Y − 50 r = 900 → Y = 1 800 + 100 r. Égalité : 200 = 200 r → **r = 4** (Y = 1 600).", niveau=3, unite='%'),
            qcm("Qui a proposé le modèle IS-LM et en quelle année ?", ["John Hicks, 1937", "J. M. Keynes, 1936", "Milton Friedman, 1957", "Paul Samuelson, 1948"], 0, "Hicks formalise la Théorie générale de Keynes."),
            qcm("Au point d'intersection de IS et LM :", ["Le marché des biens et services et le marché de la monnaie sont simultanément en équilibre", "Seul le marché du travail est en équilibre", "Le plein-emploi est garanti", "Les prix s'ajustent"], 0, "L'équilibre IS-LM n'est pas forcément de plein-emploi."),
            vf("Dans le modèle IS-LM, le niveau des prix est considéré comme donné.", True, "C'est un équilibre « à prix donnés » (court terme keynésien)."),
        ], figure=FIG_ISLM, formules=["IS : Y = C(Y) + I(r) + G0", "LM : M/P = L(Y, r)", "Équilibre : intersection IS = LM"])

    n39 = nm(
        'islm-politiques', "Politiques budgétaire et monétaire dans IS-LM ; effet d'éviction",
        "Dans IS-LM, une **politique budgétaire** expansionniste déplace **IS vers la droite** ; une **politique monétaire** expansionniste déplace **LM vers la droite (le bas)**.",
        [
            "**Relance budgétaire** (G ↑) : revenu ↑ (multiplicateur) → demande de monnaie de transaction ↑ → **taux d'intérêt ↑** → investissement privé ↓ → la hausse finale du revenu est **inférieure** à l'effet du multiplicateur simple : c'est l'**effet d'éviction**.",
            "**Relance monétaire** (M ↑) : **r ↓ et Y ↑** (l'investissement est stimulé).",
            "**Policy mix** : combinaison des deux politiques ; une relance budgétaire accompagnée d'une hausse de M peut éviter la hausse de r et donc l'éviction.",
            "Multiplicateurs IS-LM (cours) : ΔY/ΔG0 = 1 / [(1 − CY + tCY) + Ir·LY/Lr] > 0, plus faible que le multiplicateur keynésien simple ; ΔY/ΔM0 > 0 ; Δr/ΔM0 < 0.",
            "Exemple (même économie) : dépense autonome +40 → IS : Y = 1 600 − 50r → **Y = 1 300, r = 6** (contre +100 sans hausse de r) ; Ms 400 → 420 → LM : Y = 1 100 + 50r → **Y = 1 300, r = 4**.",
        ],
        [
            calc("Exemple du cours modifié : la dépense autonome augmente de 40, IS devient Y = 1 600 − 50 r ; LM : Y = 1 000 + 50 r. Nouveau revenu d'équilibre ?", 1300, "1 600 − 50 r = 1 000 + 50 r → r = 6 ; Y = **1 300**.", niveau=2, unite='', figure=FIG_BUDG),
            calc("Dans ce cas, le multiplicateur simple (c = 0,6) aurait donné ΔY = 40/0,4 = 100. Quelle est l'ampleur de l'effet d'éviction (baisse du revenu due à la hausse de r) ?", 50, "Sans hausse de r : Y = 1 350 ; avec IS-LM : 1 300 → éviction de **50** (l'investissement a baissé de 20 × 1 = 20, effet multiplié par 2,5).", niveau=3, unite='', figure=FIG_BUDG),
            calc("La banque centrale porte l'offre de monnaie de 400 à 420 (LM : Y = 1 100 + 50 r ; IS inchangée : Y = 1 500 − 50 r). Nouveau taux d'intérêt ?", 4, "1 500 − 50 r = 1 100 + 50 r → **r = 4** ; Y = 1 300.", niveau=2, unite='%', figure=FIG_MON),
            qcm("Une politique monétaire expansionniste entraîne :", ["Une baisse de r et une hausse de Y", "Une hausse de r et une hausse de Y", "Une hausse de r et une baisse de Y", "Une baisse de r et une baisse de Y"], 0, "LM se déplace vers la droite le long de IS.", figure=FIG_MON),
            qcm("Une politique budgétaire expansionniste entraîne :", ["Une hausse de Y et une hausse de r", "Une hausse de Y et une baisse de r", "Une baisse de Y", "Aucun effet sur r"], 0, "IS se déplace vers la droite le long de LM : r monte.", figure=FIG_BUDG),
            qcm("L'effet d'éviction désigne :", ["La baisse de l'investissement privé due à la hausse du taux d'intérêt provoquée par la relance budgétaire", "La baisse de la consommation due aux impôts", "La fuite des capitaux à l'étranger", "La hausse des importations"], 0, "Une partie de la dépense publique « évince » l'investissement privé."),
            S(qcm("Lecture du graphique : quand IS se déplace en IS', le point d'équilibre passe de E à E'. Que se passe-t-il ?", ["Y augmente de 1 250 à 1 300 et r de 5 à 6", "Y baisse et r monte", "Y augmente et r baisse", "Rien ne change"], 0, "La relance budgétaire augmente le revenu mais aussi le taux d'intérêt.", niveau=2, figure=FIG_BUDG), COURS),
            qcm("Quel policy mix permet d'augmenter le revenu sans faire monter le taux d'intérêt ?", ["Relance budgétaire accompagnée d'une hausse de la masse monétaire", "Relance budgétaire avec politique monétaire restrictive", "Hausse des impôts et baisse de M", "Baisse de G et hausse des impôts"], 0, "IS et LM se déplacent toutes deux vers la droite.", niveau=3),
            courte("Explique pas à pas l'effet d'une hausse des dépenses publiques dans le modèle IS-LM.",
                   "G ↑ → la demande et le revenu augmentent (multiplicateur) → la demande de monnaie de transaction augmente → l'offre de monnaie étant fixe, le taux d'intérêt monte → l'investissement privé baisse → le revenu augmente finalement moins que ne le prévoit le multiplicateur simple (effet d'éviction).", niveau=3),
        ], figure=FIG_BUDG, formules=["ΔY/ΔG0 = 1 / [(1 − CY + tCY) + Ir·LY/Lr] > 0", "ΔY/ΔM0 > 0 ; Δr/ΔM0 < 0"])
    return chapitre('ch-islm', 'Chapitre 6 — L\'équilibre macroéconomique : le modèle IS-LM', [n38, n39])
