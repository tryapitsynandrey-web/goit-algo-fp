import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import argparse

from config.settings import DEFAULT_MONTE_CARLO_TRIALS, DEFAULT_RANDOM_SEED, OUTPUT_DIR
from src.core.monte_carlo import (
    analytical_probabilities,
    compare_probabilities,
    simulate_dice_rolls,
)
from src.utils.logging_config import get_logger
from src.visualization.probability_plotter import plot_probabilities

logger = get_logger("Task07")


def main() -> None:
    parser = argparse.ArgumentParser(description="Monte Carlo Dice Simulation")
    parser.add_argument(
        "--trials", type=int, default=DEFAULT_MONTE_CARLO_TRIALS, help="Number of simulation trials"
    )
    parser.add_argument(
        "--seed", type=int, default=DEFAULT_RANDOM_SEED, help="Random seed for determinism"
    )
    args = parser.parse_args()

    logger.info(f"Running Task 7: Monte Carlo Simulation ({args.trials} trials)")

    ana = analytical_probabilities()
    sim = simulate_dice_rolls(args.trials, seed=args.seed)
    diff = compare_probabilities(sim, ana)

    logger.info("Sum | Analytical | Simulated | Diff")
    for s in ana:
        logger.info(f"{s:3} | {ana[s] * 100:9.2f}% | {sim[s] * 100:8.2f}% | {diff[s] * 100:4.2f}%")

    output_path = OUTPUT_DIR / "monte_carlo_probabilities.png"
    plot_probabilities(sim, ana, output_path)
    logger.info(f"Chart saved to {output_path}")


if __name__ == "__main__":
    main()
