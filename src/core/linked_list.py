from typing import Any, Optional

from src.models.linked_list_node import LinkedListNode


def build_linked_list(values: list[Any]) -> Optional[LinkedListNode]:
    """Builds a singly linked list from a python list."""
    if not values:
        return None
    head = LinkedListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = LinkedListNode(value)
        current = current.next
    return head


def linked_list_to_list(head: Optional[LinkedListNode]) -> list[Any]:
    """Converts a singly linked list to a python list."""
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


def reverse_linked_list(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    """Reverses a singly linked list by changing node references."""
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sorted_lists(
    left: Optional[LinkedListNode], right: Optional[LinkedListNode]
) -> Optional[LinkedListNode]:
    """Merges two sorted singly linked lists into a single sorted list."""
    if left is None:
        return right
    if right is None:
        return left

    dummy = LinkedListNode(0)
    tail = dummy

    while left is not None and right is not None:
        if left.value <= right.value:
            assert left is not None
            tail.next = left
            left = left.next
        else:
            assert right is not None
            tail.next = right
            right = right.next
        tail = tail.next

    if left is not None:
        tail.next = left
    else:
        tail.next = right

    return dummy.next


def get_middle(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    """Finds the middle node of a linked list."""
    if head is None:
        return None
    slow: Optional[LinkedListNode] = head
    fast: Optional[LinkedListNode] = head
    while fast is not None and fast.next is not None and fast.next.next is not None:
        if slow is not None:
            slow = slow.next
        fast = fast.next.next
    return slow


def sort_linked_list(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    """Sorts a singly linked list using merge sort."""
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    assert middle is not None
    next_to_middle = middle.next
    middle.next = None

    left = sort_linked_list(head)
    right = sort_linked_list(next_to_middle)

    return merge_sorted_lists(left, right)
