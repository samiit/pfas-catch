"""All utilities for the LLM module."""

import os
import dspy

open_ai_key = os.getenv("open_ai_key")
lm = dspy.LM("openai/gpt-4o-mini", api_key=open_ai_key)
dspy.configure(lm=lm)

molecule_module = dspy.Predict(
    "text: str -> molecule_names: list[str]", name="get_all_molecule_names_from_text"
)

smiles_module = dspy.Predict(
    "molecule_name: str -> smiles: str",
    name="get_smiles_representation_from_molecule_name",
)

smiles_compare_module = dspy.Predict(
    "smiles1: str, smiles2: str -> is_equal: bool",
    name="compare_two_smiles",
)
