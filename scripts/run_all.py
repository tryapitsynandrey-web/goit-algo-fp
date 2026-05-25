import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import subprocess

from src.utils.logging_config import get_logger

logger = get_logger("RunAll")


def run_script(script_name: str) -> None:
    logger.info("=" * 50)
    logger.info(f"Executing {script_name}...")
    logger.info("=" * 50)
    try:
        subprocess.run(["python", f"scripts/{script_name}"], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error executing {script_name}: {e}")


def main() -> None:
    scripts = [
        "run_task_01_linked_list.py",
        "run_task_02_pythagoras_tree.py",
        "run_task_03_dijkstra.py",
        "run_task_04_heap_visualization.py",
        "run_task_05_tree_traversals.py",
        "run_task_06_food_optimization.py",
        "run_task_07_monte_carlo.py",
    ]

    for script in scripts:
        run_script(script)

    logger.info("All tasks completed.")


if __name__ == "__main__":
    main()
