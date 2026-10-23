# Publier une nouvelle version

Ce dossier est la version **publiée** de la skill. Raphaël garde sa propre version sur son
compte Claude ; les deux diffèrent volontairement sur quelques passages. Une amélioration de
sa version ne se recopie donc pas telle quelle.

## Les passages propres à la version publiée (à ne jamais écraser)

Dans `fiche-memo-maths/SKILL.md` :
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

Dans `fiche-memo-maths/scripts/verifier_memo.py` : bandeau absent ou hors forme signalé en
ATTENTION, pas en ERREUR ; élision « Je suis capable d' » acceptée.

## Marche à suivre (à demander à Claude en une fois)

1. Comparer la version de Raphaël et ce dossier ; reporter ses améliorations en gardant les
   passages ci-dessus.
2. Lancer `python scripts/verifier_memo.py assets/exemple-fiche-memo-3e.tex` : « OK » attendu.
3. Lancer `python fabriquer_zip.py` : le zip dans `dist/` ne doit contenir que des chemins
   commençant par `fiche-memo-maths/`.
4. Sauvegarde git, envoi sur GitHub, puis nouvelle version publiée (« release ») avec le zip
   en pièce jointe et une ligne qui dit ce qui a changé.
