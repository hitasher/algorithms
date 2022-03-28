from typing import MutableSequence

from local_typing import Comparable
from .abstract_sorting_algorithm import AbstractSortingAlgorithm


class Quicksort(AbstractSortingAlgorithm):
    def sort(self, sequence: MutableSequence[Comparable]) -> None:
        self.__quicksort(sequence, 0, len(sequence) - 1)

    @classmethod
    def __quicksort(cls, sequence: MutableSequence[Comparable], begin_index: int, end_index: int) -> None:
        if begin_index >= end_index:
            return
        pivot_index: int = cls.__partition(sequence, begin_index, end_index)
        cls.__quicksort(sequence, begin_index, pivot_index - 1)
        cls.__quicksort(sequence, pivot_index + 1, end_index)

    @staticmethod
    def __partition(sequence: MutableSequence[Comparable], begin_index: int, end_index: int) -> int:
        pivot_index: int = begin_index
        for i in range(begin_index + 1, end_index + 1):
            if sequence[i] <= sequence[begin_index]:
                pivot_index += 1
                sequence[i], sequence[pivot_index] = sequence[pivot_index], sequence[i]
        sequence[pivot_index], sequence[begin_index] = sequence[begin_index], sequence[pivot_index]
        return pivot_index
