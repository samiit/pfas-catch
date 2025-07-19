"""Utilities for the PFAS catch/match application"""

from src.constants import pfoa_molecule
from src.llm import molecule_module, smiles_module  # , smiles_compare_module


def get_molecules(text: str) -> list:
    """Uses LLM to get the molecule name out of a given text description"""
    molecule_names_response = molecule_module(text=text)
    molecule_names = molecule_names_response.molecule_names
    print("Predicted mols", molecule_names_response.molecule_names)
    # molecule_name = [pfoa_molecule.name]  # !!!
    if not molecule_names:
        return []
    return molecule_names


def get_smiles(molecule_name: str) -> str:
    """
    Uses LLM to match to the right SMILES representation of the molecule name
    """
    # smiles_name = pfoa_molecule.smiles  # !!!
    smiles_name_response = smiles_module(molecule_name=molecule_name)
    smiles_name = smiles_name_response.smiles
    # Compare smiles_name with existing ones
    smiles_name = smiles_name.strip()
    print("SMILES name", smiles_name)
    if not smiles_name:
        return ""
    return smiles_name


def get_filename(smiles: str):
    """Get the filename from a dictionary"""
    return pfoa_molecule.image
