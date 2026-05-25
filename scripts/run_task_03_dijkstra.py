import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.core.dijkstra import dijkstra, reconstruct_path
from src.models.graph_types import WeightedGraph
from src.utils.logging_config import get_logger

logger = get_logger("Task03")


def main() -> None:
    logger.info("Running Task 3: Dijkstra Algorithm")

    graph: WeightedGraph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "Z": 6},
        "E": {"C": 10, "D": 2, "Z": 3},
        "Z": {"D": 6, "E": 3},
    }

    start_node = "A"
    logger.info(f"Computing shortest paths from {start_node}")
    distances, previous = dijkstra(graph, start_node)

    for target in graph:
        dist = distances[target]
        path = reconstruct_path(previous, start_node, target)
        logger.info(f"Path to {target}: {path} (Cost: {dist})")


if __name__ == "__main__":
    main()
