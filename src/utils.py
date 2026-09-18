# Build: 40fe5fe87915faf43837455cdd2cddf0

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
