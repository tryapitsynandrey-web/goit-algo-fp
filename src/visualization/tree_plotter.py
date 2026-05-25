from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import networkx as nx

from src.models.tree_node import TreeNode


def add_edges(
    graph: nx.DiGraph,
    node: Optional[TreeNode],
    pos: dict,
    x: float = 0,
    y: float = 0,
    layer: int = 1,
) -> None:
    """Recursively adds nodes and edges to the NetworkX graph for plotting."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.value)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            x_left = x - 1 / 2**layer
            pos[node.left.id] = (x_left, y - 1)
            add_edges(graph, node.left, pos, x=x_left, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)


def plot_tree(root: Optional[TreeNode], output_path: Path) -> None:
    """Plots a binary tree using NetworkX and Matplotlib."""
    if root is None:
        return

    tree: nx.DiGraph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, node_size=2500, node_color=colors)

    # ensure parent dir exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
