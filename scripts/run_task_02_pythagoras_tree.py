import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import argparse
import math

from config.settings import DEFAULT_RECURSION_DEPTH, MAX_RECURSION_DEPTH, OUTPUT_DIR
from src.core.fractal import generate_pythagoras_tree
from src.utils.logging_config import get_logger
from src.visualization.fractal_plotter import plot_fractal

logger = get_logger("Task02")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Pythagoras Tree Fractal")
    parser.add_argument(
        "--depth",
        type=int,
        default=DEFAULT_RECURSION_DEPTH,
        help=f"Recursion depth (default: {DEFAULT_RECURSION_DEPTH}, max: {MAX_RECURSION_DEPTH})",
    )
    args = parser.parse_args()

    depth = args.depth
    if depth < 1 or depth > MAX_RECURSION_DEPTH:
        raise ValueError(f"Depth must be between 1 and {MAX_RECURSION_DEPTH}")

    logger.info(f"Running Task 2: Pythagoras Tree Fractal with depth {depth}")

    # Initial parameters
    x = 0.0
    y = 0.0
    angle = math.pi / 2  # Pointing upwards
    length = 100.0

    segments = generate_pythagoras_tree(x, y, angle, length, depth)

    output_path = OUTPUT_DIR / "pythagoras_tree.png"
    plot_fractal(segments, output_path)

    logger.info(f"Fractal generated with {len(segments)} segments.")
    logger.info(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
