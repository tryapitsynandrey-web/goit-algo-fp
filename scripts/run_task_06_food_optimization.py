import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.core.food_optimizer import REQUIRED_ITEMS, dynamic_programming, greedy_algorithm
from src.utils.logging_config import get_logger

logger = get_logger("Task06")


def main() -> None:
    logger.info("Running Task 6: Food Optimization")

    budget = 100
    logger.info(f"Budget: {budget}")

    logger.info("--- Greedy Algorithm ---")
    greedy_res = greedy_algorithm(REQUIRED_ITEMS, budget)
    logger.info(f"Selected: {greedy_res['selected_items']}")
    logger.info(f"Total Cost: {greedy_res['total_cost']}")
    logger.info(f"Total Calories: {greedy_res['total_calories']}")

    logger.info("--- Dynamic Programming ---")
    dp_res = dynamic_programming(REQUIRED_ITEMS, budget)
    logger.info(f"Selected: {dp_res['selected_items']}")
    logger.info(f"Total Cost: {dp_res['total_cost']}")
    logger.info(f"Total Calories: {dp_res['total_calories']}")


if __name__ == "__main__":
    main()
