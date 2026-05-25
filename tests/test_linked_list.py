from src.core.linked_list import (
    build_linked_list,
    linked_list_to_list,
    merge_sorted_lists,
    reverse_linked_list,
    sort_linked_list,
)


def test_build_and_convert():
    """Tests building and converting linked lists."""
    assert linked_list_to_list(build_linked_list([])) == []
    assert linked_list_to_list(build_linked_list([1])) == [1]
    assert linked_list_to_list(build_linked_list([1, 2, 3])) == [1, 2, 3]


def test_reverse_empty_list():
    """Tests reversing an empty list."""
    assert reverse_linked_list(None) is None


def test_reverse_single_node():
    """Tests reversing a single-node list."""
    head = build_linked_list([1])
    rev = reverse_linked_list(head)
    assert linked_list_to_list(rev) == [1]


def test_reverse_many_nodes():
    """Tests reversing a list with multiple nodes."""
    head = build_linked_list([1, 2, 3])
    rev = reverse_linked_list(head)
    assert linked_list_to_list(rev) == [3, 2, 1]


def test_sort_unsorted_list():
    """Tests sorting an unsorted list."""
    head = build_linked_list([3, 1, 4, 1, 5, 9, 2, 6, 5])
    sorted_head = sort_linked_list(head)
    assert linked_list_to_list(sorted_head) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_sort_with_duplicates():
    """Tests sorting a list with duplicate elements."""
    head = build_linked_list([2, 2, 1, 1])
    sorted_head = sort_linked_list(head)
    assert linked_list_to_list(sorted_head) == [1, 1, 2, 2]


def test_merge_two_sorted_lists():
    """Tests merging two sorted lists."""
    list1 = build_linked_list([1, 3, 5])
    list2 = build_linked_list([2, 4, 6])
    merged = merge_sorted_lists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6]


def test_merge_with_empty_list():
    """Tests merging with an empty list."""
    list1 = build_linked_list([1, 2, 3])
    merged1 = merge_sorted_lists(list1, None)
    assert linked_list_to_list(merged1) == [1, 2, 3]

    list2 = build_linked_list([1, 2, 3])
    merged2 = merge_sorted_lists(None, list2)
    assert linked_list_to_list(merged2) == [1, 2, 3]
