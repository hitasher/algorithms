from typing import Sequence

from local_typing import Comparable


def binary_search(sequence: Sequence[Comparable], target: Comparable) -> int | None:
    lower_bound: int = 0
    upper_bound: int = len(sequence) - 1

    while lower_bound <= upper_bound:
        middle_index: int = (lower_bound + upper_bound) // 2
        current_element: Comparable = sequence[middle_index]
        if current_element == target:
            return middle_index
        if current_element < target:
            lower_bound = middle_index + 1
        else:
            upper_bound = middle_index - 1

    return None
