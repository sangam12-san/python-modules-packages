"""
Custom module providing mathematical utility functions.
"""

from typing import List, Union

Number = Union[int, float]

def calculate_mean(numbers: List[Number]) -> float:
    """Calculates the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty.")
    return sum(numbers) / len(numbers)

def filter_above_threshold(numbers: List[Number], threshold: Number) -> List[Number]:
    """Filters and returns numbers greater than the specified threshold."""
    return [num for num in numbers if num > threshold]