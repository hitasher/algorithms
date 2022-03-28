from typing import MutableSequence

from local_typing import Comparable
from .abstract_sorting_algorithm import AbstractSortingAlgorithm


class SelectionSort(AbstractSortingAlgorithm):
    def sort(self, sequence: MutableSequence[Comparable]) -> None:
        for i in range(len(sequence)):
            index_of_minimum_element: int = min(range(i, len(sequence)), key=sequence.__getitem__)
            sequence[i], sequence[index_of_minimum_element] = sequence[index_of_minimum_element], sequence[i]
