from collections import deque
from typing import Optional

from src.models.tree_node import TreeNode
from src.utils.colors import generate_hex_gradient


def dfs_iterative(root: Optional[TreeNode]) -> list[TreeNode]:
    """Performs an iterative Depth-First Search using a stack."""
    if root is None:
        return []

    visited_nodes = []
    stack = [root]
    visited_ids = set()

    while stack:
        node = stack.pop()

        if node.id not in visited_ids:
            visited_ids.add(node.id)
            visited_nodes.append(node)

            # To process left first in DFS, we push right then left to the stack
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return visited_nodes


def bfs_iterative(root: Optional[TreeNode]) -> list[TreeNode]:
    """Performs an iterative Breadth-First Search using a queue."""
    if root is None:
        return []

    visited_nodes = []
    queue = deque([root])
    visited_ids = set()

    while queue:
        node = queue.popleft()

        if node.id not in visited_ids:
            visited_ids.add(node.id)
            visited_nodes.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return visited_nodes


def apply_traversal_colors(order: list[TreeNode]) -> None:
    """Assigns unique gradient colors to nodes based on their position in the traversal order."""
    if not order:
        return

    colors = generate_hex_gradient(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]
