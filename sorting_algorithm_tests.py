import unittest
from abc import ABC, abstractmethod
from random import sample

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quicksort import Quicksort


def generate_random_list(n: int) -> list[int]:
    return sample(range(-2 * n, 2 * n), n)


class TestAbstractSortingAlgorithm(unittest.TestCase, ABC):
    @abstractmethod
    def sorting_function(self, sequence) -> None:
        pass

    def test_list_is_sorted_after_sorting(self):
        for _ in range(10):
            lst: list[int] = generate_random_list(100)
            self.sorting_function(lst)
            self.assertEqual(sorted(lst), lst)


class TestSelectionSort(TestAbstractSortingAlgorithm):
    def sorting_function(self, sequence) -> None:
        selection_sort(sequence)


class TestQuicksort(TestAbstractSortingAlgorithm):
    def sorting_function(self, sequence) -> None:
        Quicksort.sort(sequence)


class TestBubbleSort(TestAbstractSortingAlgorithm):
    def sorting_function(self, sequence) -> None:
        bubble_sort(sequence)


del TestAbstractSortingAlgorithm
