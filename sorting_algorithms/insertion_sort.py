from typing import MutableSequence

from local_typing import Comparable
from .abstract_sorting_algorithm import AbstractSortingAlgorithm


class InsertionSort(AbstractSortingAlgorithm):
    def sort(self, sequence: MutableSequence[Comparable]) -> None:
        for i in range(1, len(sequence)):
            j = i - 1
            while j >= 0 and sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
                j -= 1
