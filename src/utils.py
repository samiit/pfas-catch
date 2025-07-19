"""Utilities for the PFAS catch/match application"""

from src.constants import pfoa_molecule


def get_molecules(text: str) -> list:
    """Uses LLM to get the molecule name out of a given text description"""
    molecule_name = [pfoa_molecule.name]  # !!!
    return molecule_name


def get_smiles(molecule_name: str) -> str:
    """
    Uses LLM to match to the right SMILES representation of the molecule name
    """
    smiles_name = pfoa_molecule.smiles  # !!!
    return smiles_name


def get_filename(smiles: str):
    """Get the filename from a dictionary"""
    return pfoa_molecule.image
