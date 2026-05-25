import uuid
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class TreeNode:
    """A node in a binary tree."""

    value: Any
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None
    color: str = "skyblue"  # Default color for visualization
