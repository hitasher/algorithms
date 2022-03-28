from typing import MutableSequence

from local_typing import Comparable
from .abstract_sorting_algorithm import AbstractSortingAlgorithm


class BubbleSort(AbstractSortingAlgorithm):
    def sort(self, sequence: MutableSequence[Comparable]) -> None:
        end_index: int = len(sequence) - 1
        is_sorted: bool = False
        while not is_sorted:
            is_sorted = True
            for j in range(end_index):
                if sequence[j + 1] < sequence[j]:
                    sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
                    is_sorted = False
            end_index -= 1
