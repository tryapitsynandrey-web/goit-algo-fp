def validate_positive_number(value: float, name: str) -> None:
    """Validates that a number is strictly positive."""
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0.")


def validate_non_negative_number(value: float, name: str) -> None:
    """Validates that a number is non-negative (>= 0)."""
    if value < 0:
        raise ValueError(f"{name} cannot be negative.")


def validate_integer(value: float, name: str) -> None:
    """Validates that a number is an integer."""
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer.")
