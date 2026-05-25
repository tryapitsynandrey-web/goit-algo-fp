import re

from src.core.heap_tree import build_heap_tree
from src.core.tree_traversal import apply_traversal_colors, bfs_iterative, dfs_iterative


def test_dfs_order():
    """Tests the exact iteration order for DFS."""
    root = build_heap_tree([1, 2, 3, 4, 5, 6, 7])
    # array mapping:
    # 1 -> L:2, R:3
    # 2 -> L:4, R:5
    # 3 -> L:6, R:7
    # DFS (left-first) should be: 1, 2, 4, 5, 3, 6, 7
    order = dfs_iterative(root)
    values = [node.value for node in order]
    assert values == [1, 2, 4, 5, 3, 6, 7]


def test_bfs_order():
    """Tests the exact iteration order for BFS."""
    root = build_heap_tree([1, 2, 3, 4, 5, 6, 7])
    # BFS should match level-order / array order
    order = bfs_iterative(root)
    values = [node.value for node in order]
    assert values == [1, 2, 3, 4, 5, 6, 7]


def test_no_duplicate_visited_nodes():
    """Tests that nodes are visited exactly once."""
    root = build_heap_tree([1, 2, 3])
    order = dfs_iterative(root)
    assert len(order) == 3
    assert len(set(node.id for node in order)) == 3


def test_generated_colors_unique_and_valid():
    """Tests that generated colors are unique, correct count, and valid hex."""
    root = build_heap_tree([1, 2, 3, 4, 5])
    order = bfs_iterative(root)
    apply_traversal_colors(order)

    colors = [node.color for node in order]
    assert len(colors) == 5
    assert len(set(colors)) == 5

    # Valid hex check
    hex_pattern = re.compile(r"^#[0-9a-fA-F]{6}$")
    for color in colors:
        assert hex_pattern.match(color) is not None
