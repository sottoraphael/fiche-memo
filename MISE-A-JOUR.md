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

## Marche à suivre (à demander à Claude en une fois)

1. Comparer la version de Raphaël et ce dossier ; reporter ses améliorations en gardant les
   passages ci-dessus.
2. Faire produire une fiche par la skill sur un cours d'essai, puis lancer
   `python fiche-memo/scripts/verifier_memo.py <fiche.tex>` : aucune ERREUR attendue.
3. Lancer `python fabriquer_zip.py` : le zip `dist/fiche-memo.zip` ne doit contenir que des
   chemins commençant par `fiche-memo/`.
4. Sauvegarde git, envoi sur GitHub, puis nouvelle version publiée (« release ») avec le zip
   en pièce jointe et une ligne qui dit ce qui a changé.
