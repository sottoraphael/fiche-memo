#!/usr/bin/env python3
"""Contrôle statique d'une fiche mémo (skill fiche-memo).

Usage : python scripts/verifier_memo.py chemin/fichier.tex
Sortie : une ligne par constat, préfixée ERREUR ou ATTENTION ; code de retour 1 si ERREUR.
La compilation reste à faire séparément avec pdflatex.
"""
import re
import sys
from pathlib import Path


def sans_commentaires(texte):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ligne) for ligne in texte.splitlines())


def verifier(chemin):
    brut_complet = Path(chemin).read_text(encoding="utf-8")
    t = sans_commentaires(brut_complet)
    corps = t.split(r"\begin{document}", 1)[-1]
    erreurs, alertes = [], []

    if "«" in corps or "»" in corps:
        erreurs.append("guillemets « » présents : utiliser ``...'' (notation ASCII)")
    if re.search(r"\\og\b|\\fg\b", corps):
        erreurs.append("\\og ou \\fg présent : utiliser ``...''")
    if re.search(r"\\euro\b|eurosym", t):
        erreurs.append("\\euro ou eurosym présent : utiliser \\texteuro{}")
    if "{{" in t:
        erreurs.append("marqueur {{...}} du gabarit non remplacé")
    if r"\clearpage" in corps or r"\newpage" in corps:
        erreurs.append("saut de page : les objectifs s'enchaînent dans un seul tableau")

    # Impression noir et blanc : une information portée par une couleur disparaît.
    for m in re.finditer(r"\b(en|de couleur) (bleu|rouge|vert|jaune|orange|violet|rose)s?\b", corps):
        alertes.append(f"information portée par une couleur, à remplacer (noir et blanc) : « {m.group(0)} »")
    # Puces pleines puis vides, réglées dans le préambule du gabarit.
    if r"\frenchsetup{StandardItemLabels=true}" not in brut_complet:
        erreurs.append("réglage des puces absent du préambule : recopier le préambule du gabarit")

    n_xl = len(re.findall(r"\\begin\{xltabular\}", corps))
    if n_xl != 1:
        erreurs.append(f"{n_xl} tableau(x) xltabular : il en faut un seul pour tout le chapitre")
    if re.search(r"\\begin\{tabularx\}", corps):
        erreurs.append("tabularx dans le corps : il ne se coupe pas entre les pages, utiliser xltabular")
    if r"\endhead" not in corps:
        erreurs.append("\\endhead absent : l'en-tête ne se répétera pas en haut de page")
    if n_xl and not re.search(r"\\begin\{xltabular\}\{\\dimexpr\\textwidth-5pt\\relax\}", corps):
        erreurs.append("largeur du tableau différente de \\dimexpr\\textwidth-5pt\\relax")

    bandeaux = re.findall(r"Objectif : (.*?)\}\}", corps)
    # Bandeaux facultatifs, forme de l'enseignant admise : signalés sans bloquer.
    if not bandeaux:
        alertes.append("aucun bandeau d'objectif : attendu si l'enseignant n'en veut pas")
    for b in bandeaux:
        if not re.match(r"Je suis capable d(e |')", b.strip()):
            alertes.append(f"bandeau hors forme « Je suis capable de… » : {b[:60]}")
    for m in re.finditer(r"\\parbox\{([^}]*)\}", corps):
        if m.group(1) != r"\dimexpr\textwidth-20pt\relax":
            erreurs.append(f"largeur de bandeau {m.group(1)} au lieu de \\dimexpr\\textwidth-20pt\\relax")

    n_lignes = len(re.findall(r"\\caseseval", corps))
    if n_lignes == 0:
        erreurs.append("aucune ligne de question (\\caseseval)")
    elif bandeaux and n_lignes < len(bandeaux):
        alertes.append(f"{n_lignes} ligne(s) pour {len(bandeaux)} objectif(s) : un objectif sans question ?")

    return erreurs, alertes


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    try:
        erreurs, alertes = verifier(sys.argv[1])
    except FileNotFoundError:
        print(f"ERREUR : fichier introuvable : {sys.argv[1]}")
        sys.exit(2)
    except UnicodeDecodeError:
        print(f"ERREUR : {sys.argv[1]} n'est pas encodé en UTF-8 : l'enregistrer en UTF-8.")
        sys.exit(2)
    for e in erreurs:
        print("ERREUR :", e)
    for a in alertes:
        print("ATTENTION :", a)
    if not erreurs and not alertes:
        print("OK : aucun écart détecté par le contrôle statique.")
    sys.exit(1 if erreurs else 0)
