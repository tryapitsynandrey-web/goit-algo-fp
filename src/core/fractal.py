import math
from typing import TypedDict


class LineSegment(TypedDict):
    """Represents a line segment for drawing."""

    x1: float
    y1: float
    x2: float
    y2: float
    level: int


def generate_pythagoras_tree(
    x: float, y: float, angle: float, length: float, depth: int, current_depth: int = 0
) -> list[LineSegment]:
    """Recursively generates segments for a Pythagoras tree fractal."""
    if current_depth >= depth:
        return []

    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)

    segment = LineSegment(x1=x, y1=y, x2=x2, y2=y2, level=current_depth)
    segments = [segment]

    # Left branch
    segments.extend(
        generate_pythagoras_tree(
            x2, y2, angle + math.pi / 4, length * math.cos(math.pi / 4), depth, current_depth + 1
        )
    )

    # Right branch
    segments.extend(
        generate_pythagoras_tree(
            x2, y2, angle - math.pi / 4, length * math.sin(math.pi / 4), depth, current_depth + 1
        )
    )

    return segments
