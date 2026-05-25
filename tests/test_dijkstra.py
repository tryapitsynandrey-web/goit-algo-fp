import pytest

from src.core.dijkstra import dijkstra, reconstruct_path
from src.models.graph_types import WeightedGraph


def test_normal_weighted_graph() -> None:
    """Tests shortest path in a normal connected graph."""
    graph: WeightedGraph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    distances, previous = dijkstra(graph, "A")
    assert distances["A"] == 0
    assert distances["B"] == 1
    assert distances["C"] == 3
    assert distances["D"] == 4

    path = reconstruct_path(previous, "A", "D")
    assert path == ["A", "B", "C", "D"]


def test_disconnected_node() -> None:
    """Tests graph with an unreachable node."""
    graph: WeightedGraph = {"A": {"B": 1}, "B": {"A": 1}, "C": {}}
    distances, _ = dijkstra(graph, "A")
    assert distances["A"] == 0
    assert distances["B"] == 1
    assert distances["C"] == float("inf")


def test_zero_weight_edge() -> None:
    """Tests graph with a zero weight edge."""
    graph: WeightedGraph = {"A": {"B": 0}, "B": {}}
    distances, _ = dijkstra(graph, "A")
    assert distances["B"] == 0


def test_negative_weight_rejection() -> None:
    """Tests that negative edge weights are rejected."""
    graph: WeightedGraph = {"A": {"B": -1}, "B": {}}
    with pytest.raises(ValueError, match="Graph contains negative edge weights"):
        dijkstra(graph, "A")


def test_missing_start_node() -> None:
    """Tests that a missing start node raises an error."""
    graph: WeightedGraph = {"A": {"B": 1}, "B": {}}
    with pytest.raises(ValueError, match="Start node C not found"):
        dijkstra(graph, "C")
