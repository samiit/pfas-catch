"""Constants for the repository"""

from enum import Enum
from pydantic import BaseModel


class Molecule(BaseModel):
    name: str
    smiles: str
    image: str
    iupac_name: str | None = None


pfba_molecule = Molecule(
    name="per-fluoro butanoic acid",
    smiles="O=C(O)C(F)(F)C(F)(F)C(F)(F)F",
    image="PFBA",
)
pfbs_molecule = Molecule(
    name="per-fluoro butane sulfonic acid",
    smiles="O=S(C(F)(F)C(F)(F)C(F)(F)C(F)(F)F)(O)=O",
    image="PFBS",
)
pfoa_molecule = Molecule(
    name="per-fluoro octanoic acid",
    smiles="O=C(O)C(F)(F)C(F)(F)C(C(F)(F)C(F)(F)C(C(F)(F)F)(F)F)(F)F",
    image="PFOA",
)
pfos_molecule = Molecule(
    name="per-fluoro octane sulfonic acid",
    smiles="O=S(C(F)(F)C(F)(F)C(F)(F)C(C(F)(F)C(F)(F)C(F)(F)C(F)(F)F)(F)F)(O)=O",
    image="PFOS",
)

deta_benzene = Molecule(
    name="DETA Benzene",
    smiles="CC[N+](CC)(C)CC[N+](CC1CCCCC1)(C)CC[N+](CC)(C)CC",
    image="DETA_benzene",
    iupac_name="N1-(cyclohexylmethyl)-N1-(2-(diethyl(methyl)ammonio)ethyl)-N2,N2-diethyl-N1,N2-dimethylethane-1,2-diaminium",
)

deta_cyclohexane = Molecule(
    name="DETA Cyclohexane",
    smiles="CC[N+](CC)(C)CC[N+](CC1=CC=CC=C1)(C)CC[N+](CC)(C)CC",
    image="DETA_cyclohexane",
    iupac_name="N1-benzyl-N1-(2-(diethyl(methyl)ammonio)ethyl)-N2,N2-diethyl-N1,N2-dimethylethane-1,2-diaminium",
)

deta_imidazole = Molecule(
    name="DETA Imidazole",
    smiles="CC[N+](CC)(C)CC[N+](CC1=NC=CN1)(C)CC[N+](CC)(C)CC",
    image="DETA_imidazole",
    iupac_name="N1-((1H-imidazol-2-yl)methyl)-N1-(2-(diethyl(methyl)ammonio)ethyl)-N2,N2-diethyl-N1,N2-dimethylethane-1,2-diaminium",
)

deta_nitrobenzene = Molecule(
    name="DETA Nitrobenzene",
    smiles="CC[N+](CC)(C)CC[N+](CC1=CC=C([N+]([O-])=O)C=C1)(C)CC[N+](CC)(C)CC",
    image="DETA_nitrobenzene",
    iupac_name="N1-(2-(diethyl(methyl)ammonio)ethyl)-N2,N2-diethyl-N1,N2-dimethyl-N1-(4-nitrobenzyl)ethane-1,2-diaminium",
)

deta_phenol = Molecule(
    name="DETA Phenol",
    smiles="CC[N+](CC)(C)CC[N+](CC1=CC=C(O)C=C1)(C)CC[N+](CC)(C)CC",
    image="DETA_phenol",
    iupac_name="N1-(2-(diethyl(methyl)ammonio)ethyl)-N2,N2-diethyl-N1-(4-hydroxybenzyl)-N1,N2-dimethylethane-1,2-diaminium",
)

deta_hexane = Molecule(
    name="DETA Hexane",
    smiles="CC[N+](CC)(C)CC[N+](CCCCCCC)(C)CC[N+](CC)(C)CC",
    image="DETA_hexane",
    iupac_name="N1-(2-(diethyl(methyl)ammonio)ethyl)-N2,N2-diethyl-N1-heptyl-N1,N2-dimethylethane-1,2-diaminium",
)

deta_isopentane = Molecule(
    name="DETA Isopentane",
    smiles="CC[N+](CC)(C)CC[N+](CCC(C)CC(C)(C)C)(C)CC[N+](CC)(C)CC",
    image="DETA_isopentane",
    iupac_name="N1-(2-(diethyl(methyl)ammonio)ethyl)-N2,N2-diethyl-N1,N2-dimethyl-N1-(3,5,5-trimethylhexyl)ethane-1,2-diaminium",
)


class MoleculeConstants(Enum):
    pfoa: Molecule = pfoa_molecule
    pfba: Molecule = pfba_molecule
    pfbs: Molecule = pfbs_molecule
    pfos: Molecule = pfos_molecule
    deta_benzene: Molecule = deta_benzene
    deta_cyclohexane: Molecule = deta_cyclohexane
    deta_imidazole: Molecule = deta_imidazole
    deta_nitrobenzene: Molecule = deta_nitrobenzene
    deta_phenol: Molecule = deta_phenol
    deta_hexane: Molecule = deta_hexane
    deta_isopentane: Molecule = deta_isopentane


best_adsorbers = {
    "per-fluoro butanoic acid": "DETA_cyclohexane",
    "per-fluoro butane sulfonic acid": "DETA_phenol",
    "per-fluoro octanoic acid": "DETA_hexane",
    "per-fluoro octane sulfonic acid": "DETA_hexane",
}
