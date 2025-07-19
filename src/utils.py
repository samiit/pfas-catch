"""Utilities for the PFAS catch/match application"""

from src.constants import images_dict


def get_molecules(text: str) -> list:
    """Uses LLM to get the molecule name out of a given text description"""
    molecule_name = ["per-fluoro butanoic acid"]  # !!!
    return molecule_name


def get_smiles(molecule_name: str) -> str:
    """
    Uses LLM to match to the right SMILES representation of the molecule name
    """
    smiles_name = "O=C(O)C(F)(F)C(F)(F)C(C(F)(F)C(F)(F)C(C(F)(F)F)(F)F)(F)F"  # !!!
    return smiles_name


def get_filename(smiles: str):
    """Get the filename from a dictionary"""
    return images_dict.get(smiles, "default_image")
