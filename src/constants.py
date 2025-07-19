"""Constants for the repository"""

from pydantic import BaseModel


class Molecule(BaseModel):
    name: str
    smiles: str
    image: str


pfoa_molecule = Molecule(
    name="per-fluoro butanoic acid",
    smiles="O=C(O)C(F)(F)C(F)(F)C(C(F)(F)C(F)(F)C(C(F)(F)F)(F)F)(F)F",
    image="PFOA",
)
