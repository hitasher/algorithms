from typing import MutableSequence

from local_typing import Comparable


def selection_sort(sequence: MutableSequence[Comparable]) -> None:
    for i in range(len(sequence)):
        index_of_minimum_element: int = min(range(i, len(sequence)), key=sequence.__getitem__)
        sequence[i], sequence[index_of_minimum_element] = sequence[index_of_minimum_element], sequence[i]
