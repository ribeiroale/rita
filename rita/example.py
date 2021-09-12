def add(x: float, y: float) -> float:
    """Returns the sum of two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Returns the subtraction of two numbers."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Returns the multiplication of two numbers."""
    return x * y


def divide(x: float, y: float) -> float:
    """Returns the division of two numbers."""
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y
