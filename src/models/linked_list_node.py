from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class LinkedListNode:
    """A node in a singly linked list."""

    value: Any
    next: Optional["LinkedListNode"] = None
