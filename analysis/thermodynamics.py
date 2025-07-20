"""Evaluate the thermodynamic properties of the molecular system."""

#!/usr/bin/env python3

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def calculate_pmf_from_rdf(rdf_file, temperature=298.15, output_file="pmf.dat"):
    """
    Calculate Potential of Mean Force (PMF) from Radial Distribution Function

    Args:
        rdf_file: Path to RDF file (2 columns: r(nm), g(r))
        temperature: Temperature in Kelvin (default: 298.15 K)
        output_file: Output file for PMF data
    """

    # Constants
    kB = 8.314e-3  # Boltzmann constant in kJ/mol/K
    kT = kB * temperature

    # Read RDF data
    print(f"Reading RDF data from {rdf_file}...")
    data = pd.read_csv(rdf_file, sep=" ", header=None, names=["r(nm)", "g_r"])
    r = data["r(nm)"].values  # Distance in nm
    g_r = data["g_r"].values  # g(r)

    # Avoid log(0) by setting minimum g(r) value
    g_r_safe = np.where(g_r > 1e-10, g_r, 1e-10)

    # Calculate PMF: W(r) = -kT * ln[g(r)]
    pmf = -kT * np.log(g_r_safe)

    # Set reference (PMF at large distances should be 0)
    # Use average of last 10% of points as reference
    ref_start = int(0.9 * len(pmf))
    reference = np.mean(pmf[ref_start:])
    pmf_corrected = pmf - reference

    # Save PMF data
    print(f"Saving PMF data to {output_file}...")
    output_df = pd.DataFrame({"Distance(nm)": r, "PMF(kJ/mol)": pmf_corrected})
    output_df.to_csv(output_file, index=False, header=True)

    # Find binding free energy (minimum PMF)
    min_idx = np.argmin(pmf_corrected)
    binding_distance = r[min_idx]
    binding_energy = pmf_corrected[min_idx]

    print("\n=== BINDING ANALYSIS ===")
    print(f"Binding distance: {binding_distance:.2f} nm")
    print(f"Binding free energy: {binding_energy:.2f} kJ/mol")
    print(f"Temperature: {temperature:.1f} K")

    # Calculate dissociation constant
    # Kd = exp(ΔG / kT)
    if binding_energy < 0:
        kd = np.exp(-binding_energy / kT)
        print(f"Dissociation constant: {kd:.2e} M")

    # Create plots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plot RDF
    ax1.plot(r, g_r, "b-", linewidth=2)
    ax1.axhline(y=1, color="k", linestyle="--", alpha=0.5)
    ax1.set_xlabel("Distance (nm)")
    ax1.set_ylabel("g(r)")
    ax1.set_title("Radial Distribution Function: PFBA - DETA-cyclohexane")
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, min(3.0, r[-1]))

    # Plot PMF
    ax2.plot(r, pmf_corrected, "r-", linewidth=2)
    ax2.axhline(y=0, color="k", linestyle="--", alpha=0.5)
    ax2.axvline(
        x=binding_distance,
        color="g",
        linestyle=":",
        alpha=0.7,
        label=f"Binding distance: {binding_distance:.2f} nm",
    )
    ax2.axhline(
        y=binding_energy,
        color="g",
        linestyle=":",
        alpha=0.7,
        label=f"Binding energy: {binding_energy:.2f} kJ/mol",
    )
    ax2.set_xlabel("Distance (nm)")
    ax2.set_ylabel("PMF (kJ/mol)")
    ax2.set_title("Potential of Mean Force (Binding Free Energy)")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xlim(0, min(3.0, r[-1]))

    plt.tight_layout()
    img_path = Path("images") / f"{output_file.stem}rdf_pmf_analysis.png"
    plt.savefig(img_path, dpi=300, bbox_inches="tight")
    print(f"\nPlots saved to: {img_path}")

    return r, g_r, pmf_corrected, binding_distance, binding_energy
