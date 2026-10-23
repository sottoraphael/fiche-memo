---
name: "fiche-memo-maths"
description: "Transforme la leçon d'un chapitre de mathématiques de collège (6e à 3e), quel que soit son intitulé (À connaître, leçon, cours, je retiens), en fiche mémo de rappel actif, en LaTeX compilable : un tableau continu de questions atomiques avec réponse courte, conseil de processus et cases d'auto-évaluation, organisé par objectif d'apprentissage si l'enseignant le souhaite. À utiliser dès que l'enseignant demande une fiche mémo, une fiche de mémorisation, des questions de rappel, un support de révision, veut transformer un cours en questions, ou parle de rappel actif, d'auto-évaluation ou de mémorisation sur une notion de maths. Le support de cours relève de support-eleve-maths, le document enseignant de doc-enseignant-maths, l'évaluation sommative de evaluation-maths."
---

# Fiche mémo — maths collège

Fonctionne seule, à partir du cours fourni par l'enseignant. Elle peut aussi suivre d'autres
skills (support élève → fiche mémo → document enseignant → évaluation), non fournies ici.
La fiche porte uniquement sur les **essentiels du chapitre** : ce que l'élève doit restituer
sans son cours et qu'il apprend dans ce chapitre. Source méthodologique : fiche « La fiche
Mémo » (collection *Apprendre et former avec les sciences cognitives*). La fiche n'est pas
fournie ; ses règles sont reprises ci-dessous.

Exemple complet validé par l'enseignant, à imiter : `assets/exemple-fiche-memo-3e.tex`
(Calcul littéral partie 2, six objectifs, deux pages). Il montre la répartition des types de
questions, la ligne d'exemple de chaque objectif et des conseils qui ne livrent pas la
réponse.

## Sources et rigueur

S'appuyer sur des sources qui font autorité (programme officiel du niveau, documents
d'accompagnement), citées par extrait littéral ; écrire « Non rapporté » quand la source ne dit
rien, et contrôler chaque définition. Si l'enseignant n'a pas fourni le programme, lui demander
d'abord les extraits utiles. Si les instructions de son projet contiennent d'autres règles de
rigueur, elles s'appliquent aussi.

Propre à ce document : chaque réponse sera apprise par cœur, donc une approximation s'y fixe
plus durablement qu'ailleurs. Borner le domaine jusque dans la réponse courte : « pour des
quantités positives, l'écart se calcule en partant de la plus grande », plutôt que « l'écart
se calcule en partant de la plus grande quantité », qui deviendra faux avec les nombres
relatifs. La même exigence vaut pour la colonne de conseils.

## Déroulé

Entrée : le cours du chapitre fourni par l'enseignant. Si elle est fournie, la progression
annuelle sert à situer ce qui a déjà été enseigné.

0. **Repérer la leçon et les objectifs.**
   - *La leçon* : la partie du cours qui dit ce que l'élève doit savoir, quel que soit son nom
     (« À connaître », « Leçon », « Cours », « Je retiens », « L'essentiel », encadrés
     « Définition », « Propriété »…), à distinguer des activités, exemples et exercices. En cas
     de doute, demander à l'enseignant quelle partie utiliser.
   - *Les objectifs* : si le cours les énonce, les reprendre mot pour mot. Sinon, signaler le manque à
     l'enseignant et lui demander s'il veut des bandeaux d'objectif. S'il en veut, lui demander
     ses objectifs ou lui en proposer, sous la forme « Je suis capable de… », un par partie de
     la leçon. **Arrêt : attendre sa réponse.** Sans bandeaux, la fiche garde un seul tableau,
     lignes dans l'ordre de la leçon.
1. **Relever les essentiels.** Un essentiel = un point de la leçon validée **qui est nouveau
   dans ce chapitre** ; si la leçon comporte des mots à trous, ils désignent ce que l'élève
   doit produire.
   Garder ce que le chapitre introduit : un mot, une définition, une condition, une procédure,
   une extension (aux millièmes, aux nombres relatifs). Laisser à la leçon ce qu'elle rappelle
   comme outil : une lecture, une propriété ou un automatisme d'un niveau antérieur ou d'un
   chapitre déjà traité, vérifié dans le programme du niveau précédent (et ses automatismes) et
   dans la progression. La fiche reste ainsi courte et fait réviser le nouveau. *Exemple
   (6e, écritures d'un décimal) :* garder « Qu'est-ce qu'un nombre mixte ? » (mot et condition
   introduits en 6e) ; laisser « Comment se lit $\frac{a}{100}$ ? » (lecture des fractions
   décimales, CM). Quand le chapitre complète une notion déjà vue, garder seulement le
   complément.
2. **Présenter la liste à l'enseignant** : une ligne par essentiel, groupée par objectif s'il y en a, avec
   pour chacun la ligne d'exemple prévue ou non, et, pour tout point de la leçon écarté, la
   source qui montre qu'il est déjà enseigné. Un essentiel de vocabulaire sans cas à montrer
   est signalé : l'enseignant tranche. **Arrêt : attendre la validation**, il retire ou ajoute
   des essentiels.
3. **Rédiger** les questions, réponses et conseils des essentiels validés.
4. **Injecter** dans `assets/gabarit-memo.tex`, puis vérifier (voir plus bas).

Copier et suivre :

```
- [ ] Leçon repérée, objectifs repris, proposés ou écartés avec l'enseignant
- [ ] Essentiels relevés, points déjà enseignés laissés à la leçon avec leur source
- [ ] Liste validée par l'enseignant
- [ ] Questions, réponses et conseils rédigés
- [ ] Script sans erreur, compilation, contrôle visuel, relecture finale
```

## Règles de rédaction

- **Une ligne = une notion**, réponse lisible et vérifiable en moins de 15 à 20 mots.
- **Volume** : viser 5 à 6 lignes par objectif (par partie de la leçon, sans bandeaux), lignes
  d'exemple comprises, et au moins une ligne par essentiel ; chaque question porte sur un essentiel validé. Au-delà de 6 lignes
  pour un objectif, le signaler à l'enseignant avec la raison : une fiche trop longue n'est
  pas relue.
- **Une ligne, un apport** : chaque ligne demande ce qu'aucune autre ne demande. Quand une
  ligne de méthode et la ligne d'exemple qui l'applique font restituer la même chose, garder
  la ligne d'exemple (*exemple :* « Écris $0{,}6$ en pourcentage » rend inutile « Par quelle
  écriture passe-t-on pour aller d'un pourcentage à une écriture décimale ? »).
- **Ligne d'exemple** après l'essentiel quand il s'applique à un cas concret (nombre, calcul,
  figure, situation) : la question demande de traiter le cas, la réponse donne le résultat.
  Les nombres des exemples sont absents des exercices du cours fourni : un nombre déjà traité
  donne une réponse que l'élève a vue, au lieu de lui faire retrouver la méthode.
- **Faire produire.** Sur un principe, la question demande de citer, de donner ou d'écrire :
  l'élève restitue, au lieu de répondre oui ou non avec une chance sur deux. « Cite trois
  écritures possibles d'un nombre décimal », plutôt que « Une écriture décimale, une fraction
  et un pourcentage peuvent-ils désigner le même nombre ? ». La question fermée reste admise
  en discrimination sur un cas concret, avec la justification dans la réponse
  (« $1 + \frac{13}{10}$ est-il un nombre mixte ? » → « Non : $\frac{13}{10}$ est supérieure
  à 1. »).
- **Définition d'une notion nouvelle** : la question donne le terme, la réponse donne la
  définition (« Qu'est-ce qu'un nombre mixte ? » → « La somme d'un nombre entier et d'une
  fraction inférieure à 1. »). Le sens inverse (« Comment appelle-t-on… ? ») est réservé au mot
  de vocabulaire, quand c'est le mot lui-même qu'il faut retenir (« abscisse »).
- **Égalité de définition** : faire produire l'objet plutôt que réciter (« Donne une fraction
  décimale égale à $a\,\%$ » plutôt que « Par définition, à quoi est égal $a\,\%$ ? »).
- **Énumération : des noms seuls.** « Quels sont les termes d'une division euclidienne ? » →
  dividende, diviseur, quotient, reste. Le rôle de chaque élément fait sa propre ligne
  (« Comment appelle-t-on le nombre que l'on partage ? » → le dividende). *Cas à écarter :* une
  réponse qui associe chaque élément à sa propriété.
- **Types de questions** : sémantique (« Qu'est-ce qu'un… ? », « Comment appelle-t-on… ? »),
  procédurale (« Comment écrit-on… ? », « Par quelle étape commence-t-on pour… ? »),
  discrimination (« Dans cette figure : cosinus ou sinus ? »), complétion (formule à trous).
- **Réponse procédurale** : reprendre mot pour mot la procédure de la leçon validée.
- **Situation nommée** : la question dit sur quoi l'élève est interrogé. « Dans quelle
  situation-problème utilise-t-on l'addition ? », plutôt que « Que cherche-t-on quand on
  utilise une addition ? », qui fait deviner le registre de la réponse.
- **Sens des opérations** : « Dans quelle situation-problème utilise-t-on … ? », réponse en
  « Quand … », forme qui reprend le programme (« Connaitre le sens et les situations d'emploi
  de ces opérations »). Une opération à plusieurs sens : une ligne par sens, distinguées par une
  mention en italique (« premier sens ») qui garde la réponse cachée.
- **Colonne « Stratégie / Conseil »** : la méthode, la stratégie mentale ou l'erreur fréquente
  (« L'erreur classique est d'oublier le carré. »), jamais la réponse. *Cas à écarter :* « Le
  plus grand diviseur commun de 35 et 15 est 5 », « Ici $a = x$ et $b = 5$ », ou le calcul
  déroulé pas à pas — l'élève n'a plus rien à rappeler. Écrire le geste à faire : « Cherche le
  plus grand diviseur commun aux deux coefficients. » Ton neutre, centré sur le geste, à la
  place des jugements (« Bravo », « Facile »). Terminer souvent par une question de contrôle
  (« As-tu vérifié que… ? »).
- **Conseil concret, au niveau de l'élève** : un geste qu'un élève du niveau visé peut faire
  tout de suite, avec ses mots. *Exemple (6e) :* « Fais des paquets d'autant de parts que le
  dénominateur : chaque paquet vaut 1. As-tu vérifié que ce qui reste est plus petit que le
  dénominateur ? », plutôt que « Cherche le plus grand multiple du dénominateur qui ne dépasse
  pas le numérateur », trop abstrait pour un élève de 6e.
- **Comparaisons** : le vocabulaire mathématique (plus grand que, plus petit que, égal à,
  supérieur, inférieur), à la place de « dépasse », et le cas limite quand il compte (« si la
  fraction est plus grande que 1, ou égale à 1 »).
- **Bandeau d'objectif** (si l'enseignant en veut) : le début de la phrase d'objectif retenue
  à l'étape 0, mot pour mot, arrêté avant la condition et le critère (« Je suis capable de
  comparer deux nombres décimaux »). L'élève reconnaît l'objectif de son cours, et le bandeau
  reste court. L'élision est conservée (« Je suis capable d'associer… »). Un objectif du cours
  écrit sous une autre forme garde la forme de l'enseignant.
- **Figures** : pour une notion géométrique, un schéma TikZ compact dans la cellule
  « Question », à l'échelle 0,5 à 0,7, avec le codage (angle droit, longueurs) et des lettres
  pour chaque point et angle à nommer.
- **Noir et blanc** : la fiche est imprimée en noir et blanc ; chaque information passe par le
  texte, les lettres ou un codage (« l'angle $\widehat{ABC}$ », un angle codé), à la place de la
  couleur (« l'angle en bleu »). Listes éventuelles : puces pleines puis vides, le tiret se
  confondant avec un signe moins.

Exemple de ligne :

```latex
\caseseval & \centering \begin{tikzpicture}[scale=0.5]
    \draw[thick] (0,0) node[below left]{$C$} -- (3,0) node[below right]{$B$} -- (0,2) node[above left]{$A$} -- cycle;
    \draw (0,0) ++(0.3,0) -- ++(0,0.3) -- ++(-0.3,0);
\end{tikzpicture} \\ \vspace{1mm} \small Dans le triangle $ABC$ rectangle en $C$, donne l'égalité de Pythagore. & $AB^2 = AC^2 + BC^2$ & \footnotesize \textit{L'hypoténuse $[AB]$ est le côté opposé à l'angle droit en $C$ : elle figure seule d'un côté de l'égalité.} \\ \hline
```

## LaTeX

Partir de `assets/gabarit-memo.tex`, qui fait foi : remplacer les marqueurs `{{...}}`, répéter
le bandeau d'objectif et la ligne de tableau autant que nécessaire. Sans bandeaux, supprimer
le bloc du bandeau. Le fichier contient
uniquement le LaTeX ; les commentaires à l'enseignant restent dans le chat.
- **Un seul tableau `xltabular` pour tout le chapitre**, bandeaux inclus : il se coupe entre
  les pages et répète l'en-tête grâce à `\endhead`. `tabularx` basculerait entier sur la page
  suivante, et un tableau par objectif avec `\clearpage` coûterait une page par objectif.
- **Largeurs du gabarit** à garder : tableau sur `\dimexpr\textwidth-5pt\relax`, `\parbox` du
  bandeau sur `\dimexpr\textwidth-20pt\relax`. Avec `1\textwidth` ou `-10pt`, le tableau dépasse
  d'environ un millimètre dans la marge, sans erreur.
- **Interligne** : `\arraystretch` à 2.2 par défaut ; 1.8 seulement si cela évite une page
  presque vide. Après toute suppression de lignes, revenir à 2.2 si la fiche garde le même
  nombre de pages.
- **Virgule décimale** : dans les formules, écrire `0{,}25` (sinon une espace parasite suit la
  virgule).
- **Guillemets** en notation ASCII (deux apostrophes inversées, deux apostrophes droites) : les
  caractères « » et `\og{}`/`\fg{}` rendent des glyphes parasites sans erreur de compilation.
- **Euro** : `\texteuro{}`, jamais `\euro{}` ni `eurosym`. Échapper `\%`, `\_`, `\&`. Toute
  expression mathématique entre `$...$`.

## Vérification

1. Lancer `python scripts/verifier_memo.py chemin/fichier.tex`, corriger, relancer jusqu'à ce
   qu'il ne signale plus d'erreur. Il contrôle guillemets, euro, marqueurs restants, tableau
   `xltabular` unique avec `\endhead`, largeurs, absence de `\clearpage`, réglage des puces,
   mentions de couleur. Il signale aussi, sans bloquer, un bandeau qui ne commence pas par
   « Je suis capable de » ou l'absence de bandeau : attendu quand l'enseignant a gardé sa forme
   d'objectif ou n'a pas voulu de bandeaux, à vérifier sinon. Toute erreur se corrige avant de
   passer à la compilation.
2. Compiler : `pdflatex -interaction=nonstopmode fichier.tex`. L'environnement repart de zéro à
   chaque session : installer une fois, avant la première compilation, avec
   `apt-get update && apt-get install -y texlive-lang-french texlive-fonts-extra texlive-latex-extra`
   (sans le `apt-get update`, l'installation échoue sur un environnement neuf). Si l'installation
   échoue, le dire et préciser que la compilation n'a pas été testée. Compter les pages
   (`pdfinfo`) et signaler tout débordement.
3. Regarder le PDF : `pdftoppm -png -r 60`, puis ouvrir les images. Une compilation sans erreur ne
   prouve pas que le rendu est juste — des lignes de tableau qui se chevauchent ne déclenchent
   aucun avertissement. Après une modification par script, vérifier objectif par objectif et
   non sur le fichier entier.
4. Relire ce que le script ne voit pas : chaque essentiel validé a sa question et sa ligne
   d'exemple prévue ; chaque ligne porte sur ce que le chapitre introduit ; 6 lignes par
   objectif au plus, ou un dépassement signalé ; une notion et un apport par ligne ; des
   questions qui font produire ; énumérations de noms seuls ; conseil qui donne le chemin,
   concret, au vocabulaire du niveau ; comparaisons précises avec leur cas limite ; exemples
   sur des nombres neufs par rapport au cours ; bandeaux mot pour mot ; notations du
   niveau.

Dire à l'enseignant si la compilation a réussi et combien de pages compte la fiche.