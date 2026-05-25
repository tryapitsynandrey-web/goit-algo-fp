from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_probabilities(
    simulated: dict[int, float], analytical: dict[int, float], output_path: Path
) -> None:
    """Plots a comparison bar chart of simulated vs analytical probabilities."""
    sums = list(analytical.keys())
    sim_vals = [simulated[s] * 100 for s in sums]
    ana_vals = [analytical[s] * 100 for s in sums]

    x = np.arange(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width / 2, sim_vals, width, label="Simulated", color="skyblue")
    ax.bar(x + width / 2, ana_vals, width, label="Analytical", color="salmon")

    ax.set_ylabel("Probability (%)")
    ax.set_title("Monte Carlo Simulation vs Analytical Probabilities")
    ax.set_xticks(x)
    ax.set_xticklabels([str(s) for s in sums])
    ax.legend()

    for i, v in enumerate(sim_vals):
        ax.text(
            i - width / 2, v + 0.5, f"{v:.1f}%", ha="center", va="bottom", fontsize=8, rotation=90
        )
    for i, v in enumerate(ana_vals):
        ax.text(
            i + width / 2, v + 0.5, f"{v:.1f}%", ha="center", va="bottom", fontsize=8, rotation=90
        )

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
