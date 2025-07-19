"""All utilities for the LLM module."""

import os
from typing import Literal
import dspy
from dotenv import load_dotenv
from src.constants import MoleculeConstants


load_dotenv()  # This loads variables from .env into os.environ

open_ai_key = os.getenv("open_ai_key")
lm = dspy.LM("openai/gpt-4o", api_key=open_ai_key, cache=False)
dspy.configure(lm=lm, temperature=0.1)

mol_names = (mol.value.name for mol in MoleculeConstants)
mol_names = tuple(mol_names)
mol_smiles = (mol.value.smiles for mol in MoleculeConstants)
mol_smiles = tuple(mol_smiles)


# Define the LLM modules for molecule and SMILES processing
class MoleculeModule(dspy.Signature):
    """Module to extract molecule names from text."""

    text: str = dspy.InputField(
        description="Text description of the molecule and its requirements"
    )

    molecule_names: list[Literal[*mol_names]] | None = dspy.OutputField(
        description="Predicted molecule names. Should be one of those provided!"
    )


molecule_module = dspy.Predict(MoleculeModule)


class SmilesModule(dspy.Signature):
    """Module to get SMILES representation from molecule name."""

    molecule_name: str = dspy.InputField(
        description="Name of the molecule to get its SMILES representation"
    )

    smiles: Literal[*mol_smiles] = dspy.OutputField(
        description="SMILES representation of the molecule"
    )


smiles_module = dspy.Predict(SmilesModule)
