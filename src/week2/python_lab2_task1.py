
"""
Lab 2.2 – Comprehensions and Transformations
Practice list, set and dictionary comprehensions.
"""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    """Return the square of each number."""
    return [n ** 2 for n in numbers]


def positives(numbers: list[int]) -> list[int]:
    """Return only numbers greater than zero."""
    return [n for n in numbers if n > 0]


def even_squares(numbers: list[int]) -> set[int]:
    """Return squares of even numbers as a set."""
    return {n ** 2 for n in numbers if n % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:
    """Map each number to its cube."""
    return {n: n ** 3 for n in numbers}


if __name__ == "__main__":
    print(f"Squares: {squares(NUMBERS)}")
    print(f"Positives: {positives(NUMBERS)}")
    print(f"Even squares: {even_squares(NUMBERS)}")
    print(f"Cubes: {cubes(NUMBERS)}")
