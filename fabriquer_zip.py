"""Fabrique dist/fiche-memo.zip, la pièce jointe de chaque version publiée.

Usage : python fabriquer_zip.py
Le zip contient le dossier de la skill au premier niveau (fiche-memo/SKILL.md),
forme exigée par Claude : https://claude.com/docs/skills/how-to
"""
import zipfile
from pathlib import Path

ICI = Path(__file__).parent
SKILL = ICI / "fiche-memo"
SORTIE = ICI / "dist" / "fiche-memo.zip"

fichiers = sorted(
    f for f in SKILL.rglob("*")
    if f.is_file() and "__pycache__" not in f.parts and not f.name.startswith(".")
)
assert (SKILL / "SKILL.md") in fichiers, "SKILL.md absent"
SORTIE.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(SORTIE, "w", zipfile.ZIP_DEFLATED) as z:
    for f in fichiers:
        # as_posix : des « / » dans le zip, même fabriqué sous Windows.
        z.write(f, f.relative_to(ICI).as_posix())

with zipfile.ZipFile(SORTIE) as z:
    noms = z.namelist()
assert all(n.startswith("fiche-memo/") for n in noms), noms
for n in noms:
    print(n)
print(f"{SORTIE.name} : {len(noms)} fichiers, {SORTIE.stat().st_size // 1024} Ko")
