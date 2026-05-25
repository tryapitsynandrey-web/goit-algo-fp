import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import OUTPUT_DIR
from src.core.heap_tree import build_heap_tree
from src.utils.logging_config import get_logger
from src.visualization.tree_plotter import plot_tree

logger = get_logger("Task04")


def main() -> None:
    logger.info("Running Task 4: Binary Heap Visualization")

    # A max-heap example
    heap_values = [100, 19, 36, 17, 3, 25, 1, 2, 7]

    logger.info(f"Building tree from heap array: {heap_values}")
    root = build_heap_tree(heap_values)

    output_path = OUTPUT_DIR / "binary_heap.png"
    plot_tree(root, output_path)

    logger.info(f"Heap visualized and saved to {output_path}")


if __name__ == "__main__":
    main()
