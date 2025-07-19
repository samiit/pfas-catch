"""Constants for the repository"""

from pydantic import BaseModel


class Molecule(BaseModel):
    name: str
    smiles: str
    image: str


pfba_molecule = Molecule(
    name="per-fluoro butanoic acid",
    smiles="O=C(O)C(F)(F)C(F)(F)C(F)(F)F",
    image="PFOA",
)
pfbs_molecule = Molecule(
    name="per-fluoro butane sulfonic acid",
    smiles="O=S(C(F)(F)C(F)(F)C(F)(F)C(F)(F)F)(O)=O",
    image="PFBS",
)
pfoa_molecule = Molecule(
    name="per-fluoro butanoic acid",
    smiles="O=C(O)C(F)(F)C(F)(F)C(C(F)(F)C(F)(F)C(C(F)(F)F)(F)F)(F)F",
    image="PFOA",
)
pfos_molecule = Molecule(
    name="per-fluoro octane sulfonic acid",
    smiles="O=S(C(F)(F)C(F)(F)C(F)(F)C(C(F)(F)C(F)(F)C(F)(F)C(F)(F)F)(F)F)(O)=O",
    image="PFOS",
)
