import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import OUTPUT_DIR
from src.core.heap_tree import build_heap_tree
from src.core.tree_traversal import apply_traversal_colors, bfs_iterative, dfs_iterative
from src.utils.logging_config import get_logger
from src.visualization.tree_plotter import plot_tree

logger = get_logger("Task05")


def main() -> None:
    logger.info("Running Task 5: DFS and BFS Traversal Visualization")

    heap_values = [0, 4, 5, 10, 1, 3]

    # DFS
    logger.info("Plotting DFS traversal...")
    root_dfs = build_heap_tree(heap_values)
    dfs_order = dfs_iterative(root_dfs)
    apply_traversal_colors(dfs_order)

    dfs_path = OUTPUT_DIR / "dfs_traversal.png"
    plot_tree(root_dfs, dfs_path)
    logger.info(f"DFS traversal saved to {dfs_path}")

    # BFS
    logger.info("Plotting BFS traversal...")
    root_bfs = build_heap_tree(heap_values)
    bfs_order = bfs_iterative(root_bfs)
    apply_traversal_colors(bfs_order)

    bfs_path = OUTPUT_DIR / "bfs_traversal.png"
    plot_tree(root_bfs, bfs_path)
    logger.info(f"BFS traversal saved to {bfs_path}")


if __name__ == "__main__":
    main()
