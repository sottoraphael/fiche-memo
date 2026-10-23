# Fiche mémo de mathématiques (collège) : une skill pour Claude

Cette skill transforme la leçon d'un chapitre de mathématiques de collège (6e à 3e) en fiche
mémo : un tableau de questions courtes, avec pour chacune la réponse, un conseil de méthode et
six cases où l'élève note s'il a su répondre. La fiche sort en PDF, prête à imprimer en noir
et blanc.

Une skill est un ensemble de consignes écrites une fois, que Claude suit ensuite à chaque
demande. Celle-ci est celle que j'utilise pour mes classes, adaptée pour fonctionner hors de
mon propre espace de travail.

## 1. Ce qu'il vous faut

- Un compte Claude, même gratuit (je ne l'ai utilisée qu'avec un abonnement payant).
- L'option « Exécution de code et création de fichiers », activée par défaut. Si la skill
  apparaît grisée, vérifiez cette option dans les paramètres : sans elle, Claude ne peut pas
  fabriquer le PDF.

Vous n'avez rien à installer sur votre ordinateur. Claude met en page la fiche avec LaTeX (un
logiciel de mise en page), qu'il installe lui-même dans son propre espace de travail.

## 2. Installer la skill

1. Téléchargez le fichier `fiche-memo-maths.zip` dans la rubrique
   [Releases](https://github.com/sottoraphael/fiche-memo-maths/releases/latest) de cette
   page. Ne le décompressez pas.
2. Dans Claude (site ou application), ouvrez Personnaliser, puis Skills.
3. Téléversez le zip.
4. Activez la skill dans la liste.

## 3. Faire une fiche

Ouvrez une conversation, joignez ou collez le cours du chapitre, puis demandez par exemple :
« Fais la fiche mémo de ce chapitre de 5e. »

Claude procède alors en plusieurs temps, et s'arrête pour vous demander votre avis :

- il repère la leçon dans votre cours, quel que soit son nom (« À connaître », « Leçon »,
  « Je retiens »…) ;
- si le cours n'énonce pas d'objectifs, il vous demande si vous voulez des bandeaux
  d'objectif, et lesquels ;
- il vous présente la liste des notions qu'il compte interroger : vous en retirez ou en
  ajoutez ;
- il rédige les questions, fabrique le PDF et le vérifie.

Relisez toujours la fiche. Claude a tendance à poser trop de questions : il faut parfois
recentrer et en supprimer.

## 4. Si le PDF ne sort pas

Claude vous donne alors le fichier `.tex` de la fiche (le texte source de la mise en page).
Vous pouvez le transformer en PDF sans rien installer avec [Overleaf](https://www.overleaf.com),
un site de mise en page LaTeX (compte gratuit) : créez un projet vide, remplacez son contenu
par celui du fichier, puis cliquez sur « Recompile ».

## 5. D'où vient la méthode

Le format de la fiche reprend celui de la fiche « La fiche Mémo » de l'association Apprendre
et Former avec les Sciences Cognitives ([AFSC](https://www.sciences-cognitives.fr/)). Cette fiche n'est pas fournie
ici : j'en ai repris les règles avec mes propres mots.

## 6. Contenu du dossier

- `fiche-memo-maths/SKILL.md` : les consignes que suit Claude.
- `fiche-memo-maths/assets/` : le modèle de la fiche et un exemple complet (3e, calcul
  littéral).
- `fiche-memo-maths/scripts/` : le contrôle que Claude lance sur chaque fiche avant de la
  mettre en page.

## 7. Licence

Raphaël Sotto, 2026. Je publie cette skill sous licence
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr) : vous pouvez
l'utiliser, la partager et l'adapter, en citant l'auteur, sans usage commercial, et en
publiant vos versions modifiées sous la même licence.

Raphaël Sotto, enseignant de mathématiques : [synactive.fr](https://synactive.fr)
