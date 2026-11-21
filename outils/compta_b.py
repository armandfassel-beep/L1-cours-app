"""Le monde de l'entreprise (CM EG1, EG2 + préambule de PARTIE_1)."""
from base import *


def chapitres():
    return [ch1(), ch2(), ch3()]


def ch1():
    n32 = notion(
        'fonctions-eco', "Les fonctions économiques de l'entreprise",
        "L'entreprise est une **organisation complexe** dont l'activité économique première est la **production** (production et distribution de biens et services marchands). On peut l'analyser sous différents angles : économique, sociologique, historique, financier, comptable…",
        [
            "Les entreprises sont apparues comme spécialisées dans l'**activité productive marchande** ; leur évolution a été provoquée surtout par des facteurs **techniques et commerciaux**.",
            "La production génère un **flux de biens** et, en contrepartie, un **flux de revenus** (salaires, intérêts, profits) distribués aux apporteurs de facteurs de production.",
            "Problème majeur : le **partage de la valeur ajoutée** entre le **travail** (masse salariale) et le **capital** (EBE).",
            "Pour survivre (renouveler les équipements) et se développer (accroître la capacité), l'entreprise **accumule du capital** par l'investissement, financé par les associés, les banques ou l'**autofinancement**.",
            "**Cinq fonctions économiques** : **production**, **distribution** des biens et services, **répartition des revenus**, **accumulation du capital** par l'investissement, **financement**.",
        ],
        [
            qcm("Quelles sont les cinq fonctions économiques de l'entreprise selon le cours ?",
                ["Production, distribution, répartition des revenus, accumulation du capital, financement", "Production, marketing, RH, finance, logistique", "Achat, vente, stockage, transport, comptabilité", "Production, consommation, épargne, investissement, impôt"], 0,
                "Ce sont des fonctions **économiques** (rôle dans l'économie), à ne pas confondre avec les fonctions **de gestion** (marketing, RH…)."),
            vf("L'activité économique première de l'entreprise est la production.", True, "C'est le point de départ du cours : production et distribution de biens et services."),
            qcm("Le partage de la valeur ajoutée oppose principalement :", ["Le travail (masse salariale) et le capital (EBE)", "Les clients et les fournisseurs", "L'État et les banques", "Les salariés et les clients"], 0, "Partage VA = **travail** vs **capital**."),
            qcm("L'autofinancement provient :", ["Des ressources tirées des ventes après paiement des charges", "D'un emprunt bancaire", "D'un apport des associés", "D'une subvention"], 0, "**Autofinancement** = ressources internes dégagées par l'activité."),
            vf("Renouveler ses équipements est pour l'entreprise une exigence de développement, et accroître sa capacité de production une exigence de survie.", False, "C'est l'inverse : renouveler = **survie** ; accroître la capacité = **développement**.", niveau=2),
            qcm("Les revenus distribués par l'entreprise rémunèrent :", ["Les travailleurs", "Les prêteurs", "Les apporteurs de capitaux", "Les clients"], [0, 1, 2], "Salaires (travailleurs), intérêts (prêteurs), profits/dividendes (capitalistes, entrepreneurs).", niveau=2),
            courte("Pourquoi dit-on que la production donne naissance à un double flux ?",
                   "Parce qu'elle crée un flux de biens et services et, en contrepartie, un flux de revenus (salaires, intérêts, profits) distribués à ceux qui ont apporté les facteurs de production.", niveau=2),
            courte("Explique en deux lignes la fonction d'accumulation du capital.",
                   "Pour survivre et se développer, l'entreprise doit investir (renouveler et accroître ses équipements). Elle acquiert du capital technique grâce au capital financier apporté par les associés, les banques ou l'autofinancement.", niveau=3),
        ])

    n33 = notion(
        'entreprise-marche', "L'entreprise et le marché",
        "L'entreprise entretient un **double rapport au marché** : elle est **offreur** de produits sur ses **marchés aval** et **demandeur** de ressources sur ses **marchés amont**. Le marché lui crée des **contraintes** mais lui offre aussi des **opportunités**.",
        [
            "**Marchés aval** : l'entreprise doit satisfaire les besoins externes des clients (acheteurs, utilisateurs, consommateurs) → connaître ces besoins, agir sur eux, adapter ses produits à leur variété et leur évolution.",
            "**Quatre marchés amont** : **marché financier**, **marché des équipements**, **marché des approvisionnements**, **marché du travail**.",
            "Les marchés **guident** ses choix (produits, prix, facteurs, techniques) et **conditionnent** ses performances (résultats, rentabilité, trésorerie).",
            "L'entreprise **influence** les marchés par ses actions commerciales et ses **innovations** ; elle participe à la genèse des besoins (la plupart de nos besoins actuels résultent d'innovations).",
            "Environnement de l'entreprise (préambule) : **marché** (confrontation offre/demande), **filière** (chaîne d'activités jusqu'au produit final), État, financeurs. Partenaires : épargnants, personnel, fournisseurs, institutions financières, État, associés, exploitant, clients.",
        ],
        [
            qcm("Sur ses marchés aval, l'entreprise est :", ["Offreur de produits", "Demandeur de ressources", "Prêteur", "Régulateur"], 0, "Aval = vente de ses produits aux clients : elle est **offreur**."),
            qcm("Lesquels font partie des quatre marchés amont ?", ["Le marché du travail", "Le marché financier", "Le marché des équipements", "Le marché des produits finis"], [0, 1, 2], "Les 4 marchés amont : financier, équipements, approvisionnements, travail. Le marché des produits finis est un marché **aval**.", niveau=2),
            vf("Le rapport de l'entreprise au marché est univoque : elle subit le marché sans pouvoir l'influencer.", False, "Il n'est **pas univoque** : l'entreprise influence les marchés par ses actions commerciales et ses innovations."),
            qcm("Une entreprise recrute des ingénieurs. Sur quel marché intervient-elle ?", ["Le marché du travail (amont)", "Le marché financier (amont)", "Un marché aval", "Le marché des équipements"], 0, "Elle est **demandeur** de travail : marché amont."),
            qcm("Une entreprise émet des actions pour financer une usine. Sur quel marché intervient-elle ?", ["Le marché financier", "Le marché des approvisionnements", "Le marché du travail", "Un marché aval"], 0, "Recherche de capitaux = **marché financier**.", niveau=2),
            qcm("Qu'est-ce qu'une filière ?", ["La chaîne d'activités qui conduisent à la mise sur le marché du produit final", "Un service de l'entreprise", "Une filiale à l'étranger", "Un fournisseur unique"], 0, "Définition du préambule du cours.", niveau=2),
            courte("Donne un exemple montrant que l'entreprise participe à la création des besoins.",
                   "Par exemple les smartphones, les plateformes de streaming ou les réseaux sociaux : ces besoins n'existaient pas avant que des entreprises innovent et créent ces produits.", niveau=2),
            courte("En quoi le marché est-il à la fois une contrainte et une opportunité pour l'entreprise ?",
                   "Contrainte : l'entreprise doit s'adapter aux besoins des clients, aux prix et à la concurrence, ce qui conditionne ses performances. Opportunité : il lui offre des débouchés et elle peut le faire évoluer, voire créer de nouveaux marchés grâce à ses innovations.", niveau=3),
        ])

    n34 = notion(
        'valeur-ajoutee', 'Production et valeur ajoutée',
        "Est **productive** toute activité, matérielle ou immatérielle, aboutissant à une **création de valeur**. La production s'exprime **en valeur** (notion comptable du compte de résultat).",
        [
            "**Production comptable** = production **vendue** + production **stockée** + production **immobilisée**.",
            "Ce total **surestime** la production réelle car il inclut les achats faits à d'autres entreprises (**consommations intermédiaires / externes**).",
            "**Valeur ajoutée = Production − Consommations externes** : c'est la **richesse réellement créée** par l'entreprise.",
            "Au-delà, l'entreprise doit couvrir l'ensemble de ses coûts et dégager un **profit** → notion de **rentabilité des capitaux investis**.",
        ],
        [
            calc("Production vendue 500 000 € ; production stockée 20 000 € ; production immobilisée 30 000 €. Quelle est la production de l'exercice ?", 550000, "500 000 + 20 000 + 30 000 = **550 000 €**.", niveau=1),
            calc("Production 550 000 € ; consommations externes (matières, énergie, services achetés) 310 000 €. Quelle est la valeur ajoutée ?", 240000, "VA = 550 000 − 310 000 = **240 000 €**.", niveau=1),
            calc("Une boulangerie vend 180 000 € de pain ; elle a acheté 45 000 € de farine et d'ingrédients, 12 000 € d'énergie et 8 000 € de services extérieurs. Quelle est sa valeur ajoutée ?", 115000, "VA = 180 000 − (45 000 + 12 000 + 8 000) = **115 000 €**.", niveau=2),
            vf("La production comptable mesure exactement la richesse créée par l'entreprise.", False, "Elle la **surestime** car elle inclut les consommations intermédiaires produites par d'autres entreprises. La richesse créée est la **valeur ajoutée**."),
            qcm("Quels éléments composent la production de l'exercice ?", ["La production vendue", "La production stockée", "La production immobilisée", "Les achats de marchandises"], [0, 1, 2], "Les achats sont des consommations, pas de la production.", niveau=2),
            qcm("Une entreprise fabrique pour elle-même une machine. C'est de la production :", ["Immobilisée", "Stockée", "Vendue", "Consommée"], 0, "Production gardée comme immobilisation = **production immobilisée** (compte 72)."),
            vf("Une activité immatérielle (conseil, logiciel) peut être une activité productive.", True, "Toute activité, matérielle **ou immatérielle**, qui crée de la valeur est productive."),
            courte("Pourquoi retranche-t-on les consommations intermédiaires pour mesurer la richesse créée ?",
                   "Parce que la valeur de ces consommations a été créée par d'autres entreprises (les fournisseurs) : l'entreprise ne fait que la récupérer dans son prix de vente. Seule la différence (valeur ajoutée) est créée par l'entreprise elle-même.", niveau=2),
        ])

    va = tab(['Étape', 'Destinataire'], [['+ Production', 'Clients'], ['− Consommations externes', 'Fournisseurs'], ['= **Valeur ajoutée**', ''],
                                         ['− Rémunérations du personnel', 'Salariés'], ['− Charges sociales', 'Organismes sociaux'], ['− Impôts et taxes', 'État, collectivités'],
                                         ['= **EBE**', ''], ['− Intérêts versés', 'Prêteurs'], ['= Résultat brut', ''], ['− Dividendes', 'Associés'], ['= Résultat net (autofinancement)', 'Entreprise']])
    n35 = notion(
        'repartition-va', 'La répartition de la valeur ajoutée',
        "L'entreprise est une **unité de répartition du revenu** : elle partage la valeur ajoutée entre **six catégories d'acteurs**.",
        [
            "Avant cela, une partie des recettes paie les **consommations externes** : l'entreprise ne répartit pas encore sa propre valeur, elle récupère sur ses clients la valeur créée ailleurs.",
            "**Bénéficiaires → instruments** : personnel → **rémunérations** ; organismes sociaux → **cotisations sociales** ; État → **impôts et taxes** ; prêteurs et banques → **intérêts** ; associés → **dividendes** ; entreprise → **autofinancement**.",
            "**EBE (excédent brut d'exploitation) = VA − rémunérations − charges sociales − impôts et taxes** : c'est la part qui revient aux apporteurs de capitaux.",
        ],
        [
            qcm("Par quel instrument l'État reçoit-il sa part de la valeur ajoutée ?", ["Les impôts et taxes", "Les dividendes", "Les intérêts", "Les cotisations sociales"], 0, "État → **impôts et taxes**."),
            qcm("Les associés reçoivent leur part sous forme de :", ["Dividendes", "Intérêts", "Salaires", "Autofinancement"], 0, "Associés → **dividendes** ; prêteurs → intérêts."),
            calc("VA = 240 000 € ; rémunérations du personnel 110 000 € ; charges sociales 45 000 € ; impôts et taxes 9 000 €. Calcule l'EBE.", 76000, "EBE = 240 000 − 110 000 − 45 000 − 9 000 = **76 000 €**.", niveau=2, tableau=va),
            calc("Avec cet EBE de 76 000 €, l'entreprise verse 6 000 € d'intérêts et 20 000 € de dividendes. Quel montant reste pour l'autofinancement ?", 50000, "76 000 − 6 000 = 70 000 (résultat brut) − 20 000 = **50 000 €**.", niveau=2, tableau=va),
            calc("Avec VA = 240 000 € et rémunérations du personnel = 110 000 €, quelle est la part (en %) de la VA allant au personnel, au dixième près ?", 45.8, "110 000 ÷ 240 000 = **45,8 %** (sans les charges sociales).", niveau=3, unite='%', tolerance=0.1),
            qcm("Combien de catégories d'acteurs se partagent la valeur ajoutée selon le cours ?", ["6", "4", "3", "5"], 0, "Personnel, organismes sociaux, État, prêteurs, associés, entreprise."),
            vf("L'autofinancement est la part de la valeur ajoutée qui reste à l'entreprise elle-même.", True, "Il sert à financer ses investissements futurs."),
            courte("Qu'est-ce que l'EBE et à qui revient-il ?",
                   "L'excédent brut d'exploitation = valeur ajoutée − rémunérations − charges sociales − impôts et taxes. C'est la part de la valeur ajoutée qui revient aux apporteurs de capitaux (prêteurs, associés) et à l'entreprise (autofinancement).", niveau=2),
        ], tableau=va)

    n36 = notion(
        'decision', "L'entreprise, système de décision",
        "L'activité et l'évolution de l'entreprise résultent des **décisions** prises, qui engagent l'avenir : l'entreprise est un **centre autonome de décisions**. La **gestion** est parfois définie comme la **science de la décision sous contraintes**.",
        [
            "Types selon l'objet : décisions de **financement** (augmentation de capital), d'**investissement** (nouvelle usine), d'**exploitation** (programme de production annuel).",
            "Selon l'**échéance** (délai avant les effets et leur durée) : décisions **opérationnelles** (d'exploitation), **de gestion**, **stratégiques** (de direction).",
            "**Procédure** : perception de la nécessité → objectif poursuivi → inventaire des choix → évaluation des conséquences → comparaison objectif / conséquences → sélection.",
            "Il faut un **système d'information** rapide, fiable et pertinent, et un **système de décision** associant tous les organes concernés.",
            "Deux exigences contradictoires : **diviser** le travail et le **coordonner**.",
            "**Performance = efficacité + efficience**. **Efficace** : atteint ses objectifs. **Efficient** : atteint un résultat en consommant le **moins de ressources**.",
            "**Management** (de « ménager » : bien régler, bien disposer) : ensemble des techniques d'organisation et de gestion pour conduire l'action des individus.",
        ],
        [
            qcm("Construire une nouvelle usine est une décision :", ["D'investissement", "D'exploitation", "De financement", "Opérationnelle"], 0, "Exemple du cours : nouvelle usine = **investissement**."),
            qcm("Réaliser une augmentation de capital est une décision :", ["De financement", "D'investissement", "D'exploitation", "Opérationnelle"], 0, "Exemple du cours."),
            qcm("Une entreprise atteint son objectif de 10 000 ventes mais en dépensant deux fois plus que prévu. Elle est :", ["Efficace mais pas efficiente", "Efficiente mais pas efficace", "Efficace et efficiente", "Ni efficace ni efficiente"], 0, "Objectif atteint → **efficace** ; trop de ressources consommées → **pas efficiente**.", niveau=2),
            vf("Performance = efficacité + efficience.", True, "Définition du cours."),
            qcm("Classe ces décisions selon leur échéance, de la plus courte à la plus longue :", ["Opérationnelles → de gestion → stratégiques", "Stratégiques → de gestion → opérationnelles", "De gestion → opérationnelles → stratégiques", "Opérationnelles → stratégiques → de gestion"], 0, "Les décisions **stratégiques** (de direction) engagent l'entreprise sur le plus long terme.", niveau=2),
            qcm("Quelle est la première étape de la procédure de décision ?", ["Percevoir la nécessité de la décision", "Sélectionner une décision", "Évaluer les conséquences", "Inventorier les choix"], 0, "Puis : objectif, inventaire des choix, évaluation, comparaison, sélection."),
            qcm("D'où vient le mot « management » ?", ["Du français « ménager » (bien régler, bien disposer)", "De l'anglais « man »", "Du latin « manus » (main) uniquement", "Du nom d'un économiste"], 0, "Le cours rattache management au français **« ménager »**.", niveau=2),
            courte("Quelles sont les deux exigences contradictoires qu'entraîne la mise en œuvre des décisions ?", "Diviser le travail (spécialiser) et coordonner le travail (faire travailler ensemble).", niveau=2),
            courte("Cite les six étapes de la procédure de décision.",
                   "1) Perception de la nécessité de décider ; 2) détermination de l'objectif ; 3) inventaire des choix possibles ; 4) évaluation de leurs conséquences ; 5) comparaison de l'objectif aux conséquences ; 6) sélection d'une décision.", niveau=3),
        ])

    n37 = notion(
        'finalites-fonctions', "Finalités de l'entreprise et découpage fonctionnel",
        "La **finalité** de l'entreprise est la raison pour laquelle elle a été créée ; elle varie selon le type d'organisation et le système social. La **gestion** (ou management d'entreprise) est « l'ensemble des pratiques, connaissances et discours relatifs à la conduite des organisations ».",
        [
            "**Finalité économique / financière** (entreprises capitalistes) : obtenir le **maximum de profit** — l'entreprise est un **centre de profit** (maximisation sous contraintes).",
            "**Finalité institutionnelle** : satisfaire les divers groupes **prenant part** : apporteurs de travail et de capital, clientèle, fournisseurs, État et collectivités, public.",
            "**Finalité sociale** : centrée sur l'intérieur, la satisfaction des besoins des **salariés**.",
            "**Découpage fonctionnel** : fonctions marketing/commerciale, production et recherche, logistique (achat/vente), comptable et contrôle de gestion, gestion financière, gestion des ressources humaines… Chacune correspond à une **branche de la gestion**.",
            "Ces fonctions sont **cloisonnées** mais leur fonctionnement engendre des **interactions**.",
            "Disciplines complémentaires de la gestion : marketing/communication, stratégie, GRH, gestion de production, gestion comptable et financière.",
        ],
        [
            qcm("Dans une entreprise capitaliste, la finalité principale est :", ["La maximisation du profit", "La satisfaction des salariés", "Le service public", "La stabilité de l'emploi"], 0, "Entreprise fondée et dirigée par des apporteurs de capitaux : but **financier**."),
            qcm("La finalité qui vise la satisfaction des différents groupes participant au fonctionnement de l'entreprise est dite :", ["Institutionnelle", "Sociale", "Financière", "Commerciale"], 0, "Les « prenants part » (parties prenantes) : salariés, actionnaires, clients, fournisseurs, État, public."),
            qcm("La finalité sociale de l'entreprise est centrée sur :", ["La satisfaction des besoins des salariés", "Les clients", "Les actionnaires", "L'État"], 0, "Elle est tournée vers l'**intérieur** de l'entreprise."),
            qcm("Lesquelles sont des fonctions de l'entreprise (découpage fonctionnel) ?", ["Gestion des ressources humaines", "Fonction logistique", "Contrôle de gestion", "Répartition des revenus"], [0, 1, 2], "La répartition des revenus est une fonction **économique**, pas une fonction de gestion de l'organigramme.", niveau=2),
            vf("Les fonctions de l'entreprise fonctionnent de façon totalement indépendante les unes des autres.", False, "Elles sont cloisonnées mais leur fonctionnement engendre des **interactions**."),
            qcm("Parmi ces acteurs, lesquels sont des partenaires de l'entreprise cités dans le cours ?", ["Les fournisseurs", "Les institutions financières", "L'État", "Les concurrents"], [0, 1, 2], "Partenaires : épargnants, personnel, fournisseurs, institutions financières, État, associés, exploitant, clients.", niveau=2),
            courte("Cite les trois finalités possibles d'une entreprise.", "Économique (financière : profit), institutionnelle (satisfaction des parties prenantes) et sociale (satisfaction des salariés).", niveau=1),
            courte("Pourquoi peut-il y avoir des conflits entre les finalités de l'entreprise ? Donne un exemple.",
                   "Parce que les parties prenantes ont des intérêts différents : par exemple, augmenter les dividendes (actionnaires) peut se faire au détriment des salaires (salariés) ou des prix (clients).", niveau=3),
        ])
    return chapitre('ch-entreprise', "Chapitre 1 — L'entreprise", [n32, n33, n34, n35, n36, n37])


def ch2():
    n38 = notion(
        'contexte-production', 'Le contexte historique de la production',
        "La **fonction de production** englobe l'ensemble des activités qui **transforment des inputs en biens et services (outputs)**. Elle est historiquement marquée par l'évolution des **technologies** et des **comportements des consommateurs**.",
        [
            "**Production industrielle de masse (1920-1950)** : **demande > offre** ; recherche d'**économies d'échelle** et d'**effet d'expérience** ; produits **standardisés** ; **taylorisme et fordisme** (division du travail) ; production nettement séparée des autres fonctions.",
            "**Remise en cause (1950-1980)** : demande ≈ offre, demande de **variété** ; **flexibilité** (polyvalence) ; essor du **marketing** ; production liée au contrôle de gestion (comptabilité analytique). Ex. : Ford T (1 variante) → R18 (60 000 variantes en 1982).",
            "**Retour du productivisme (1980-)** : **offre > demande** ; multiplication de la diversité ; **durée de vie des produits réduite** ; **focalisation / segmentation** (unités plus spécialisées) ; intégration avec les autres fonctions ; **conception modulaire** ; personnel plus **polyvalent**.",
        ],
        [
            qcm("Pendant la période de production de masse (1920-1950), la situation du marché était :", ["Demande > offre", "Offre > demande", "Offre = demande", "Absence de demande"], 0, "Il fallait produire beaucoup : la demande dépassait l'offre."),
            qcm("Le taylorisme et le fordisme reposent sur :", ["La division du travail et la standardisation", "La polyvalence des salariés", "La personnalisation des produits", "Le juste-à-temps"], 0, "Organisation scientifique du travail, tâches parcellisées, produits standardisés."),
            qcm("Depuis les années 1980, la situation est plutôt :", ["Offre > demande", "Demande > offre", "Demande sans offre", "Stable"], 0, "Retour du productivisme : l'offre dépasse la demande, d'où la course à la diversité."),
            vf("Entre 1950 et 1980, la demande de variété a conduit à introduire de la flexibilité dans la production.", True, "Ex. de Renault : de 11 variantes (R4) à 60 000 (R18)."),
            qcm("Quelles caractéristiques correspondent à la période après 1980 ?", ["Réduction de la durée de vie des produits", "Conception modulaire des produits", "Personnel plus polyvalent", "Production unique et standardisée (un seul modèle)"], [0, 1, 2], "Le modèle unique (Ford T) correspond à la production de masse.", niveau=2),
            qcm("Rechercher des économies d'échelle signifie :", ["Diminuer le coût unitaire en produisant de grandes quantités", "Réduire le nombre de salariés", "Augmenter les prix", "Produire à la commande"], 0, "Plus on produit, plus les coûts fixes se répartissent : le coût unitaire baisse.", niveau=2),
            courte("Qu'est-ce que l'effet d'expérience ?", "La baisse du coût unitaire de production liée à l'accumulation de la production : plus on a produit, plus on maîtrise le processus, donc on produit moins cher.", niveau=3),
            courte("Pourquoi la production s'est-elle rapprochée des autres fonctions de l'entreprise après 1980 ?",
                   "Parce que l'offre dépasse la demande : il faut produire ce que veulent les clients (diversité, renouvellement rapide), ce qui impose une intégration étroite avec le marketing, la R&D et la logistique.", niveau=3),
        ])

    n39 = notion(
        'systemes-production', 'Organisation et typologie des systèmes de production',
        "La fonction de production doit répondre à **quatre questions interdépendantes** : **que** produire (définition du produit), **combien** (volume), **comment et avec qui** (qualité et coût), **quand et où** (délais).",
        [
            "**Selon le processus technique** : **continu** (flux linéaire, efficacité élevée REP 80-100 %, lignes rigides, gestion simple) ou **discontinu** (flux complexe, REP plus faible, ateliers flexibles, gestion complexe).",
            "**REP (ratio d'efficacité du processus) = temps de travail effectif ÷ temps total** (y compris les temps d'attente).",
            "**Selon la quantité** : production **unitaire / petite série** (fusées, centrales nucléaires, grands travaux) ou **grande série** (électroménager, journaux, articles de mode) ; lancements répétitifs ou non.",
            "**Selon la relation client** : production **sur stock** (anticipation) ou **à la commande**. Pour les services : **servuction** (contraction de service et production), avec **front office** et **back office**.",
            "**Selon variété des produits × mode de gestion** : **projet** (besoin très spécifique, organisation éphémère — tunnel sous la Manche) ; **atelier** (produits différenciés, organisation flexible — satellites) ; **masse et modulaire** (combinaisons de modules standardisés — électroménager) ; **masse et continue** (produit unique, automatisation poussée — cimenterie).",
            "Liens avec les autres fonctions : finance (besoins d'investissement), commerciale (besoins clients), RH (qualifications), R&D-qualité (innovations).",
        ],
        [
            calc("Sur une journée de 8 h, un produit passe 2 h en transformation effective et 6 h en attente. Quel est son REP (en %) ?", 25, "REP = 2 ÷ 8 = **25 %** : processus typique d'une production discontinue.", niveau=2, unite='%'),
            qcm("Un REP de 90 % caractérise plutôt :", ["Un processus continu", "Un processus discontinu", "Une production unitaire", "Un projet"], 0, "Continu : flux linéaire, REP élevé (80-100 %)."),
            qcm("La construction du tunnel sous la Manche relève d'une organisation :", ["Par projet", "En atelier", "De masse et continue", "De masse et modulaire"], 0, "Besoin très spécifique, organisation éphémère : **projet**."),
            qcm("Une cimenterie relève d'une production :", ["De masse et continue", "Par projet", "En atelier", "Unitaire"], 0, "Produit unique, automatisation poussée, interdépendance produit/processus."),
            qcm("Des appareils électroménagers différenciés par combinaison de modules standards relèvent d'une production :", ["De masse et modulaire", "Par projet", "De masse et continue", "Unitaire"], 0, "Exemple du cours."),
            qcm("Le terme « servuction » désigne :", ["Le processus de création d'un service", "Une production de masse", "Un service après-vente", "La sous-traitance"], 0, "Contraction de **serv**ice et prod**uction**."),
            qcm("Quelles sont les caractéristiques d'un processus discontinu ?", ["Flux complexe", "Ateliers flexibles", "Système de gestion complexe", "REP élevé (80-100 %)"], [0, 1, 2], "Le REP élevé caractérise le processus **continu**.", niveau=2),
            qcm("« Assurer l'approvisionnement et le transport, respecter les délais, minimiser les coûts de stockage » répond à la question :", ["Quand et où fabriquer ?", "Que produire ?", "Combien produire ?", "Comment et avec qui produire ?"], 0, "Domaine d'action : le **délai**.", niveau=2),
            courte("Quelles sont les quatre questions auxquelles doit répondre la fonction de production ?", "Que produire ? Combien produire ? Comment et avec qui produire ? Quand et où fabriquer ?", niveau=1),
        ])

    n40 = notion(
        'gestion-production', 'Gestion et pilotage de la production',
        "La **gestion de production** vise à assurer de façon **optimale la combinaison des facteurs de production**. Elle repose sur deux axes : la **gestion des priorités** et la **gestion des capacités**.",
        [
            "**Décisions stratégiques** : capacité, produit, taille, implantation, **faire ou faire-faire**, planification du budget.",
            "**Décisions opérationnelles** : prévoir (direction de production → programme), organiser (bureau d'études, bureau des méthodes → processus, stocks, logistique), planifier (chef de production), piloter/contrôler (chef de production, service qualité → normes).",
            "**Difficultés** : harmonisation vente/production, développement technologique, changement organisationnel.",
            "**Pilotage par l'amont** : très prévisionnel, informatisé (**MRP**). **Pilotage par l'aval** : **juste-à-temps (JAT)** — « 5 zéros » : zéro stock, zéro délai, zéro défaut, zéro panne, zéro papier — et **kanban**.",
            "**Contrôle** : approche **classique** (en fin de processus, en temps différé, par sondage, élimination des défauts, peu propice à la correction) ; **évolution** : contrôle en ligne, permanent, en **temps réel**, **TQM** (Total Quality Management).",
        ],
        [
            qcm("Le juste-à-temps est un pilotage :", ["Par l'aval (la demande)", "Par l'amont (les prévisions)", "Purement informatique (MRP)", "Par la finance"], 0, "On produit ce qui est **demandé**, quand c'est demandé."),
            qcm("Quels sont les « 5 zéros » du juste-à-temps ?", ["Stock, délai, défaut, panne, papier", "Stock, salarié, défaut, client, coût", "Délai, prix, défaut, panne, concurrence", "Stock, papier, prix, retard, client"], 0, "Zéro stock, zéro délai, zéro défaut, zéro panne, zéro papier."),
            qcm("La méthode MRP correspond à un pilotage :", ["Par l'amont, très prévisionnel et informatisé", "Par l'aval", "Sans prévision", "Uniquement manuel"], 0, "MRP = planification des besoins à partir des prévisions."),
            qcm("Le kanban est :", ["Un outil de pilotage par l'aval (étiquettes déclenchant la production)", "Un logiciel de comptabilité", "Une méthode de contrôle par sondage", "Un type de stock"], 0, "Outil du juste-à-temps, issu de Toyota.", niveau=2),
            vf("Dans l'approche classique, le contrôle de production se fait en fin de processus, en temps différé et par sondage.", True, "D'où son défaut : il élimine les défauts plutôt que de corriger les erreurs."),
            qcm("Quelles caractéristiques correspondent à l'évolution moderne du contrôle de production ?", ["Contrôle en ligne", "Contrôle en temps réel", "Total Quality Management", "Contrôle uniquement en fin de chaîne"], [0, 1, 2], "Le contrôle en fin de chaîne est l'approche **classique**.", niveau=2),
            qcm("La décision « faire ou faire-faire » est une décision de production :", ["Stratégique", "Opérationnelle", "De contrôle qualité", "Commerciale"], 0, "Elle engage l'entreprise à long terme (sous-traitance ou non)."),
            courte("Quels sont les deux axes principaux de la gestion de production ?", "La gestion des priorités et la gestion des capacités.", niveau=1),
            courte("Compare le pilotage par l'amont et le pilotage par l'aval.",
                   "Par l'amont : on produit selon des prévisions de ventes (planification, MRP), avec un risque de stocks. Par l'aval : c'est la demande réelle qui déclenche la production (juste-à-temps, kanban), ce qui réduit les stocks mais exige une grande réactivité.", niveau=3),
        ])

    n41 = notion(
        'rd-innovation', 'La R&D et l\'innovation',
        "La **R&D** regroupe la recherche **fondamentale**, la recherche **appliquée** et le **développement**. L'**innovation** est l'**application industrielle d'une invention** mise sur le marché.",
        [
            "**Recherche fondamentale** : travaux scientifiques sans finalité économique immédiate ; but : améliorer l'état des connaissances.",
            "**Recherche appliquée** : application pratique des découvertes fondamentales → donne lieu à un **brevet**.",
            "**Développement** : développer des applications industrielles / commerciales à partir d'une invention → **innovation** sur le marché.",
            "**Schumpeter (1912)** — cinq formes d'innovation : 1) **produit nouveau** pour des besoins anciens ; 2) satisfaction d'un **besoin nouveau** ; 3) **amélioration de la qualité** d'un produit ; 4) **conquête de débouchés** ; 5) **nouvelle méthode de production**.",
            "Innovations à dominante **technologique**, **commerciale**, **organisationnelle**, **socio-institutionnelle**.",
            "Problèmes managériaux : méconnaissance et absence de valorisation du patrimoine technologique, cloisonnement des services, **syndrome NIH** (*Not Invented Here* : rejet de ce qui n'a pas été inventé en interne).",
            "Accès aux technologies : **croissance interne** (autofinancement, aides publiques / crédit d'impôt, dépôt de brevet) ou **externe** (accord de coopération, rachat d'entreprise, sous-traitance, achat de licence).",
        ],
        [
            qcm("La recherche qui vise à améliorer l'état des connaissances, sans finalité économique, est la recherche :", ["Fondamentale", "Appliquée", "De développement", "Commerciale"], 0, "Définition du cours."),
            qcm("Quelle étape de la R&D aboutit généralement à un brevet ?", ["La recherche appliquée", "La recherche fondamentale", "Le développement", "La commercialisation"], 0, "Application pratique des découvertes → **brevet**."),
            vf("Une invention et une innovation sont la même chose.", False, "L'innovation est l'**application industrielle** d'une invention, mise sur le marché."),
            qcm("Selon Schumpeter, lesquelles sont des formes d'innovation ?", ["Une nouvelle méthode de production", "La conquête de débouchés", "L'amélioration de la qualité d'un produit", "La baisse des salaires"], [0, 1, 2], "Les 5 formes : produit nouveau, besoin nouveau, qualité, débouchés, méthode de production.", niveau=2),
            qcm("Le syndrome NIH désigne :", ["Le rejet des idées qui n'ont pas été inventées dans l'entreprise", "Une maladie professionnelle", "Un type de brevet", "Une norme de qualité"], 0, "*Not Invented Here*."),
            qcm("Acheter une licence pour utiliser une technologie relève de la croissance :", ["Externe", "Interne", "Organique", "Financière uniquement"], 0, "Accès externe : coopération, rachat, sous-traitance, **licence**.", niveau=2),
            qcm("Le crédit d'impôt recherche permet d'accéder aux technologies par croissance :", ["Interne", "Externe", "Commerciale", "Aucune des deux"], 0, "Autofinancement, aides publiques/crédit d'impôt, dépôt de brevet = croissance **interne**.", niveau=2),
            courte("Donne un exemple d'innovation organisationnelle.", "Par exemple le travail à la chaîne, le juste-à-temps, le télétravail ou l'organisation en équipes autonomes.", niveau=2),
            courte("Cite les cinq formes d'innovation selon Schumpeter.",
                   "1) Un produit nouveau pour des besoins anciens ; 2) la satisfaction d'un besoin nouveau ; 3) l'amélioration de la qualité d'un produit ; 4) la conquête de débouchés ; 5) une nouvelle méthode de production.", niveau=3),
        ])
    return chapitre('ch-production', 'Chapitre 2 — Fonctions production et R&D', [n38, n39, n40, n41])


def ch3():
    n42 = notion(
        'approvisionnement', 'La fonction approvisionnement et la politique d\'achat',
        "La fonction **approvisionnement** a « l'obligation de fournir matières premières et composants **en quantité et qualité suffisantes**, **au moment voulu** et **au coût le plus bas possible** ». Elle est importante sur les plans **financier**, **commercial** et **stratégique** et n'est **pas autonome**.",
        [
            "**Politique d'achat = 3 questions** : 1) **acheter à l'extérieur ou produire soi-même** (faire ou faire faire) ? 2) **un ou plusieurs fournisseurs** ? 3) **quelle relation** avec les fournisseurs ?",
            "Faire ou faire faire : considérations **techniques**, **opérationnelles**, **financières et économiques**, **stratégiques**.",
            "**Un fournisseur** : coût le plus faible, développement conjoint d'innovations. **Plusieurs fournisseurs** : minimiser le risque de **rupture**, maintenir la **concurrence** en amont, privilégier les fournisseurs qui sont aussi clients. Question aussi de **centraliser ou décentraliser** l'achat.",
            "Relation : strictement commerciale, **partenariat** de production, participation financière (aucune, unidirectionnelle, croisée → filiation à terme).",
            "**Problèmes clés** : que, combien, quand, à qui et où, comment acheter ?",
            "**Processus** : définition des besoins → étude du marché amont → étude comparative des fournisseurs → négociation et choix → passation de commande → suivi et contrôle.",
            "**Organisation** : suivi administratif + gestion physique ; par **projets** ou par **technologies**.",
        ],
        [
            qcm("Choisir plusieurs fournisseurs pour un même composant permet surtout de :", ["Minimiser le risque de rupture", "Obtenir le coût le plus faible", "Développer des innovations conjointes", "Supprimer les stocks"], 0, "Plusieurs fournisseurs : moins de risque de rupture et maintien de la concurrence."),
            qcm("Choisir un fournisseur unique permet plutôt de :", ["Obtenir le coût le plus faible et développer des innovations conjointes", "Réduire le risque de rupture", "Maintenir la concurrence en amont", "Éviter toute dépendance"], 0, "Volumes concentrés → meilleur prix ; relation étroite → innovation commune."),
            qcm("Quelle est la première phase du processus d'approvisionnement ?", ["La définition des besoins à satisfaire", "La passation de commande", "La négociation", "Le suivi et le contrôle"], 0, "Puis : marché amont, comparaison, négociation et choix, commande, suivi."),
            qcm("Quelles sont les trois questions d'une politique d'achat ?", ["Faire ou faire faire ?", "Un ou plusieurs fournisseurs ?", "Quelle relation avec les fournisseurs ?", "Quel prix de vente fixer ?"], [0, 1, 2], "Le prix de vente relève de la politique commerciale.", niveau=2),
            vf("La fonction approvisionnement est autonome par rapport aux autres fonctions de l'entreprise.", False, "Le cours précise qu'elle **n'est pas autonome** (liée à la production, la finance, le commercial…)."),
            qcm("Une participation financière croisée entre une entreprise et son fournisseur peut mener à terme à :", ["Une filiation", "Une rupture de stock", "Une baisse de qualité", "Une sous-traitance"], 0, "Selon le cours : participation croisée → **filiation à terme**.", niveau=2),
            courte("Donne la définition de la fonction approvisionnement vue en cours.",
                   "L'obligation de fournir matières premières et composants en quantité et qualité suffisantes, au moment voulu et au coût le plus bas possible.", niveau=1),
            courte("Cite deux considérations qui peuvent pousser une entreprise à « faire faire » plutôt qu'à produire elle-même.",
                   "Par exemple : considérations économiques (le sous-traitant produit moins cher grâce à ses volumes), techniques (il maîtrise une technologie que l'entreprise n'a pas), opérationnelles (manque de capacité) ou stratégiques (se recentrer sur son cœur de métier).", niveau=3),
        ])

    n43 = notion(
        'stocks', 'La gestion des stocks',
        "Selon le PCG, le **stock** est « l'ensemble des biens qui interviennent dans le **cycle d'exploitation** de l'entreprise pour être soit **vendus** en l'état ou au terme d'un processus de production, soit **consommés** ». La gestion des stocks concilie deux objectifs **contradictoires** : **minimiser les ruptures** et **maximiser la rentabilité** (ni trop, ni trop peu).",
        [
            "Le stock regroupe : **approvisionnements**, **produits**, **marchandises**. On distingue un **flux d'entrée**, un **flux de sortie** et un **niveau** de stock.",
            "**Rôle de régulation** : demande aléatoire, aléas de transport et de production. **Rôle économique** : grosses commandes (coûts de transport), quantités minimales imposées, production excédentaire.",
            "**Rôle financier** (spéculation, délais de paiement/escompte), **technique** (bois, alcool : la qualité s'améliore), **commercial** (délais de livraison réduits, remises/ristournes sur quantités).",
            "**Types** : stock **actif** (consommé pendant la période) ; stock de **sécurité** (face aux aléas) ; stock de **réapprovisionnement** (niveau qui déclenche la commande) ; stock **tampon** (entre deux postes de travail).",
            "**Gestion par exception — méthode 20/80** : 20 % des articles représentent 80 % de la valeur du stock. **Méthode ABC** : trois groupes d'articles à gérer avec plus ou moins de soin.",
            "**Modèle de Wilson** : minimiser le **coût total** = coût d'**obtention (passation)** des commandes + coût de **possession** des stocks. Hypothèses : consommation régulière, pas d'aléas fournisseur, tarif unique.",
        ],
        [
            qcm("Le stock qui protège l'entreprise contre les aléas de consommation et de livraison est le stock :", ["De sécurité", "Actif", "Tampon", "De réapprovisionnement"], 0, "Définition du cours."),
            qcm("Le niveau de stock qui déclenche une nouvelle commande est le stock :", ["De réapprovisionnement", "De sécurité", "Tampon", "Actif"], 0, "Point de commande."),
            qcm("Un stock entre deux postes de travail est un stock :", ["Tampon", "Actif", "De sécurité", "Spéculatif"], 0, "Il découple deux postes successifs."),
            qcm("Selon la méthode 20/80 :", ["20 % des articles représentent 80 % de la valeur du stock", "80 % des articles représentent 80 % de la valeur", "20 % du stock est périmé", "80 % des commandes sont livrées en retard"], 0, "On concentre donc les efforts de gestion sur les 20 % d'articles les plus coûteux."),
            qcm("Le modèle de Wilson cherche à minimiser la somme :", ["Du coût de passation des commandes et du coût de possession des stocks", "Du prix d'achat et du prix de vente", "Des salaires et des loyers", "Du coût de rupture et du coût de transport"], 0, "Commander souvent coûte en passation ; commander peu souvent coûte en possession : Wilson trouve l'équilibre.", niveau=2),
            qcm("Quelles sont les hypothèses du modèle de Wilson ?", ["Consommation régulière", "Pas d'aléas liés au fournisseur", "Tarif unique du fournisseur", "Demande aléatoire"], [0, 1, 2], "Une demande aléatoire contredit l'hypothèse de consommation régulière.", niveau=3),
            qcm("Laisser vieillir du vin ou sécher du bois en stock relève du rôle :", ["Technique", "Commercial", "Financier", "De régulation"], 0, "La qualité du produit s'améliore avec le stockage."),
            vf("Un stock important présente uniquement des avantages pour l'entreprise.", False, "Il immobilise de l'argent, coûte en stockage et en assurance, risque l'obsolescence : il faut **ni trop, ni trop peu**."),
            courte("Pourquoi les deux objectifs de la gestion des stocks sont-ils contradictoires ?",
                   "Éviter les ruptures pousse à avoir beaucoup de stock, alors que maximiser la rentabilité pousse à en avoir peu (le stock immobilise des fonds et coûte cher à conserver).", niveau=2),
        ])

    n44 = notion(
        'logistique', 'La logistique',
        "La **logistique** regroupe toutes les actions ou procédures visant à **approvisionner de l'amont à l'aval** toutes les étapes de la chaîne de transformation (**chaîne logistique**) : fournisseur → magasin de stockage → poste d'assemblage → entrepôt → client.",
        [
            "**Logistique amont (de production)** : achat des matières premières, transport des MP, circulation interne entre les postes de travail, stockage des en-cours et des produits finis.",
            "**Logistique aval (de distribution)** : transport des produits finis chez les clients et distributeurs, stockage chez les distributeurs, opérations physiques de distribution.",
            "Elle influence **toute l'activité** de l'entreprise, même sans service logistique dédié.",
            "Selon la nature de l'entreprise, les **coûts logistiques** représentent **5 % à 30 % du chiffre d'affaires**.",
            "Importance pour la **production**, la fonction **commerciale** et le **système d'information**.",
        ],
        [
            qcm("Le transport des matières premières vers l'usine relève de la logistique :", ["Amont (de production)", "Aval (de distribution)", "Commerciale", "Financière"], 0, "Avant et pendant la production : **amont**."),
            qcm("Le stockage des produits chez les distributeurs relève de la logistique :", ["Aval (de distribution)", "Amont (de production)", "Interne", "Financière"], 0, "Après la production, vers le client : **aval**."),
            qcm("Selon le cours, les coûts logistiques représentent :", ["Entre 5 % et 30 % du chiffre d'affaires", "Moins de 1 % du CA", "Plus de 50 % du CA", "Exactement 10 % du CA"], 0, "Cela dépend de la nature de l'entreprise."),
            qcm("Lesquelles relèvent de la logistique amont ?", ["Circulation interne des matières entre les postes de travail", "Stockage des en-cours", "Achat des matières premières", "Transport des produits finis chez les clients"], [0, 1, 2], "Le transport vers les clients est de la logistique **aval**.", niveau=2),
            vf("Une entreprise sans service logistique n'a aucune activité logistique.", False, "La logistique influence toute l'activité, même sans fonction dédiée."),
            calc("Une entreprise réalise 2 400 000 € de chiffre d'affaires et ses coûts logistiques représentent 12 % du CA. Montant des coûts logistiques ?", 288000, "2 400 000 × 12 % = **288 000 €**.", niveau=1),
            qcm("Dans la chaîne logistique, quelle étape se situe entre le magasin de stockage et l'entrepôt de stockage ?", ["Le poste d'assemblage", "Le client", "Le fournisseur", "La banque"], 0, "Fournisseur → magasin → **poste d'assemblage** → entrepôt → client.", niveau=2),
            courte("Explique pourquoi la logistique est importante pour la fonction commerciale.",
                   "Parce qu'elle conditionne les délais de livraison, la disponibilité des produits chez les distributeurs et donc la satisfaction des clients ; une bonne logistique est un argument commercial.", niveau=2),
            courte("Donne la définition de la logistique vue en cours.",
                   "Toutes les actions ou procédures visant à approvisionner de l'amont à l'aval toutes les étapes de la chaîne de transformation (chaîne logistique).", niveau=1),
        ])
    return chapitre('ch-appro', 'Chapitre 3 — Approvisionnement et logistique', [n42, n43, n44])
