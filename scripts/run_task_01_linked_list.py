import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.core.linked_list import (
    build_linked_list,
    linked_list_to_list,
    merge_sorted_lists,
    reverse_linked_list,
    sort_linked_list,
)
from src.utils.logging_config import get_logger

logger = get_logger("Task01")


def main() -> None:
    logger.info("Running Task 1: Linked List Operations")

    # Reverse
    initial_values = [10, 20, 30, 40, 50]
    ll = build_linked_list(initial_values)
    logger.info(f"Original list: {linked_list_to_list(ll)}")
    reversed_ll = reverse_linked_list(ll)
    logger.info(f"Reversed list: {linked_list_to_list(reversed_ll)}")

    # Sort
    unsorted_values = [5, 2, 9, 1, 5, 6]
    ll2 = build_linked_list(unsorted_values)
    logger.info(f"Unsorted list: {linked_list_to_list(ll2)}")
    sorted_ll = sort_linked_list(ll2)
    logger.info(f"Sorted list: {linked_list_to_list(sorted_ll)}")

    # Merge
    l1 = build_linked_list([1, 3, 5, 7])
    l2 = build_linked_list([2, 4, 6, 8])
    logger.info(f"List 1 (sorted): {linked_list_to_list(l1)}")
    logger.info(f"List 2 (sorted): {linked_list_to_list(l2)}")
    merged = merge_sorted_lists(l1, l2)
    logger.info(f"Merged sorted list: {linked_list_to_list(merged)}")


if __name__ == "__main__":
    main()
