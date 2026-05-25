from typing import Any, Optional

from src.models.tree_node import TreeNode


def build_heap_tree(heap_values: list[Any]) -> Optional[TreeNode]:
    """Converts an array-based binary heap into a binary tree structure."""
    if not heap_values:
        return None

    nodes = [TreeNode(value=val) for val in heap_values]

    for i, node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]

    return nodes[0]
