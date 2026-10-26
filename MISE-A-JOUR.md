# Publier une nouvelle version

Ce dossier est la version **publiée** de la skill. Raphaël garde sa propre version sur son
compte Claude ; les deux diffèrent volontairement sur quelques passages. Une amélioration de
sa version ne se recopie donc pas telle quelle.

## Les passages propres à la version publiée (à ne jamais écraser)

Dans `fiche-memo/SKILL.md` :
1. La `description` : leçon « quel que soit son intitulé », objectifs « si l'enseignant le
   souhaite », sans « Étape 2 du workflow ».
2. Le premier paragraphe : « Fonctionne seule… », et « La fiche n'est pas fournie ».
3. « Sources et rigueur », premier paragraphe : règles écrites en entier, sans renvoi aux
   « instructions du projet ».
4. « Déroulé » : l'entrée (« le cours du chapitre fourni par l'enseignant ») et l'étape 0
   (repérer la leçon quel que soit son nom ; objectifs repris, proposés ou écartés).
5. Les renvois au « cours fourni » au lieu du « support élève » (ligne d'exemple, relecture).
6. Bandeaux facultatifs : règle « Bandeau d'objectif », section LaTeX (« Sans bandeaux,
   supprimer le bloc »), vérification n° 1.
7. **Toutes matières du collège et du lycée, sans aucun élément de mathématiques** (version
   1.1, décision de Raphaël du 2026-10-23) : `name: "fiche-memo"`, titre « Fiche mémo »,
   description « collège ou lycée, dans toute matière » ; tous les exemples pris dans d'autres
   matières (anglais, histoire, SVT, géographie, français, physique-chimie) ; plus de règle
   « Sens des opérations » ni « Égalité de définition » ; « Mot juste » à la place de
   « Comparaisons » ; déjà-vu repéré par les rappels du cours à défaut de progression ;
   objectifs repris sans leur numéro ni le mot « Objectif » ; type de question « factuelle » ;
   figures étendues aux schémas légendés, cartes et graphiques ; **plus de fiche modèle
   complète** (l'exemple de 3e de Raphaël est retiré). Une amélioration venue de la version
   de Raphaël, qui est en mathématiques, se reporte donc en règle générale avec un exemple
   d'une autre matière.

Dans `fiche-memo/scripts/verifier_memo.py` : bandeau absent ou hors forme signalé en
ATTENTION, pas en ERREUR ; élision « Je suis capable d' » acceptée.

8. Programme cherché par Claude si l'enseignant ne l'a pas ou ne veut pas le fournir
   (version 1.3, décision de Raphaël du 2026-10-25) : texte officiel, adresse de chaque
   extrait, sources de seconde main signalées, jamais de citation de mémoire ; questions de
   l'étape 0 numérotées, une réponse par question.

9. « La leçon fait foi » (version 1.4, après le retour d'une enseignante de SVT, 2026-10-25) :
   réponses dans les termes de la leçon, jamais de correction de la leçon, aucun critère ni
   lien hors leçon ; détails des cas concrets ; « Conseil fidèle à la leçon » (critère tiré des
   définitions, essayé sur chaque exemple) ; validation de la liste par quelqu'un de la
   matière ; relecture finale étendue.

10. Questions utiles et conseils (version 1.5, après deux essais en histoire, 2026-10-25) :
   une liste de la leçon = une ligne d'énumération ; 6 lignes au plus par objectif et 20
   environ pour la fiche ; « Ce qui mérite une ligne » (pas d'élément manquant à retrouver ni
   d'adjectif isolé) ; énumération « parmi » avec la liste entière ; « Test du conseil » ;
   colonne Conseil dans l'ordre méthode de la leçon, erreur fréquente donnée par l'enseignant
   (demandée en option à l'étape 2), indice de rappel, case vide en dernier recours (décision
   de Raphaël) ;
   relecture finale étendue.

11. Une seule skill, aussi pour les cours de maths de Raphaël (version 1.6, décision du
   2026-10-26) : icônes de sa version de maths redessinées en TikZ dans le gabarit (livre, croix
   et coche, question, cible, ampoule), jamais `fontawesome5` ; police `lmodern` imposée.

12. Colonne Conseil facultative, absente par défaut (version 1.7, décision de Raphaël du
   2026-10-26, après l'avis de la collègue de SVT et son essai en maths) : question à l'étape 0,
   erreurs fréquentes demandées seulement si la colonne est retenue, tableau à trois colonnes
   sinon.

## Marche à suivre (à demander à Claude en une fois)

1. Comparer la version de Raphaël et ce dossier ; reporter ses améliorations en gardant les
   passages ci-dessus.
2. Faire produire une fiche par la skill sur un cours d'essai, puis lancer
   `python fiche-memo/scripts/verifier_memo.py <fiche.tex>` : aucune ERREUR attendue.
3. Lancer `python fabriquer_zip.py` : le zip `dist/fiche-memo.zip` ne doit contenir que des
   chemins commençant par `fiche-memo/`.
4. Sauvegarde git, envoi sur GitHub, puis nouvelle version publiée (« release ») avec le zip
   en pièce jointe et une ligne qui dit ce qui a changé.
