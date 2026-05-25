import heapq
from typing import Optional

from src.models.graph_types import Node, WeightedGraph


def dijkstra(
    graph: WeightedGraph, start: Node
) -> tuple[dict[Node, float], dict[Node, Optional[Node]]]:
    """Computes shortest paths from start node to all reachable nodes using a binary heap."""
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph.")

    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            if weight < 0:
                raise ValueError("Graph contains negative edge weights.")

    distances: dict[Node, float] = {node: float("inf") for node in graph}
    previous: dict[Node, Optional[Node]] = {node: None for node in graph}
    distances[start] = 0.0

    # Priority queue stores tuples of (distance, node)
    pq: list[tuple[float, Node]] = [(0.0, start)]
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        # In case there are multiple entries for the same node, we only process the best one
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            if neighbor not in graph:
                # Graph might have edges pointing to nodes not explicitly in graph keys
                continue

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous: dict[Node, Optional[Node]], start: Node, target: Node) -> list[Node]:
    """Reconstructs the shortest path from start to target."""
    path = []
    current: Optional[Node] = target

    while current is not None:
        path.append(current)
        if current == start:
            break
        current = previous.get(current)

    if not path or path[-1] != start:
        return []  # Path not found

    path.reverse()
    return path
