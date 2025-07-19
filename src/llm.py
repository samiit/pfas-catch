"""All utilities for the LLM module."""

import os
from typing import Literal
import dspy
from dotenv import load_dotenv
from src.constants import pfoa_molecule, pfba_molecule, pfbs_molecule, pfos_molecule

load_dotenv()  # This loads variables from .env into os.environ

open_ai_key = os.getenv("open_ai_key")
lm = dspy.LM("openai/gpt-4o", api_key=open_ai_key, cache=False)
dspy.configure(lm=lm, temperature=0.1)


# Define the LLM modules for molecule and SMILES processing
class MoleculeModule(dspy.Signature):
    """Module to extract molecule names from text."""

    text: str = dspy.InputField(
        description="Text description of the molecule and its requirements"
    )
    molecule_names: list[
        Literal[
            pfoa_molecule.name,
            pfba_molecule.name,
            pfbs_molecule.name,
            pfos_molecule.name,
            None,
        ]
    ] = dspy.OutputField(
        description="Predicted molecule names. Should be one of those provided!"
    )


molecule_module = dspy.Predict(MoleculeModule)


class SmilesModule(dspy.Signature):
    """Module to get SMILES representation from molecule name."""

    molecule_name: str = dspy.InputField(
        description="Name of the molecule to get its SMILES representation"
    )
    smiles: Literal[
        pfoa_molecule.smiles,
        pfba_molecule.smiles,
        pfbs_molecule.smiles,
        pfos_molecule.smiles,
        None,
    ] = dspy.OutputField(description="SMILES representation of the molecule")


smiles_module = dspy.Predict(SmilesModule)


# class SmilesCompareModule(dspy.Signature):
#     """Module to compare SMILES representations."""

#     smiles1: str = dspy.InputField(description="First SMILES representation")
#     smiles2: str = dspy.InputField(description="Second SMILES representation")
#     is_equal: bool = dspy.OutputField(
#         description="True if the two SMILES representations are equal"
#     )


# smiles_compare_module = dspy.Predict(SmilesCompareModule)
