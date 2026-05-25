from src.core.heap_tree import build_heap_tree


def test_empty_heap():
    """Tests that an empty heap returns None."""
    assert build_heap_tree([]) is None


def test_single_value_heap():
    """Tests converting a heap with a single value."""
    root = build_heap_tree([42])
    assert root is not None
    assert root is not None
    assert root.value == 42
    assert root.left is None
    assert root.right is None


def test_complete_heap_mapping():
    """Tests child mapping for a complete heap."""
    root = build_heap_tree([0, 1, 2, 3, 4, 5, 6])
    # array mapping:
    # 0 -> left: 1, right: 2
    # 1 -> left: 3, right: 4
    # 2 -> left: 5, right: 6
    assert root is not None
    assert root.value == 0
    assert root.left is not None
    assert root.left.value == 1
    assert root.right is not None
    assert root.right.value == 2
    assert root.left.left is not None
    assert root.left.left.value == 3
    assert root.left.right is not None
    assert root.left.right.value == 4
    assert root.right.left is not None
    assert root.right.left.value == 5
    assert root.right.right is not None
    assert root.right.right.value == 6


def test_incomplete_heap_mapping():
    """Tests child mapping for an incomplete heap."""
    root = build_heap_tree([0, 1, 2, 3, 4])
    # array mapping:
    # 0 -> left: 1, right: 2
    # 1 -> left: 3, right: 4
    # 2 -> left: None, right: None
    assert root is not None
    assert root.value == 0
    assert root.left is not None
    assert root.left.value == 1
    assert root.right is not None
    assert root.right.value == 2
    assert root.left.left is not None
    assert root.left.left.value == 3
    assert root.left.right is not None
    assert root.left.right.value == 4
    assert root.right is not None
    assert root.right.left is None
    assert root.right is not None
    assert root.right.right is None
