from pathlib import Path

import matplotlib.pyplot as plt

from src.core.fractal import LineSegment


def plot_fractal(segments: list[LineSegment], output_path: Path) -> None:
    """Plots and saves the Pythagoras tree fractal using matplotlib."""
    if not segments:
        return

    fig, ax = plt.subplots(figsize=(8, 8))

    max_level = max(s["level"] for s in segments) if segments else 1

    # Generate colors using a colormap
    cmap = plt.get_cmap("viridis")

    for segment in segments:
        color = cmap(segment["level"] / max_level if max_level > 0 else 0)
        # line width decreases with level
        lw = max(1.0, 5.0 - segment["level"] * 0.5)
        ax.plot([segment["x1"], segment["x2"]], [segment["y1"], segment["y2"]], color=color, lw=lw)

    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    # ensure parent dir exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight", pad_inches=0)
    plt.close()
