import unittest
from abc import ABC, abstractmethod
from typing import Type
from random import sample

from .abstract_sorting_algorithm import AbstractSortingAlgorithm
from . import (
    SelectionSort,
    BubbleSort,
    InsertionSort,
    Quicksort
)


def generate_random_list(n: int) -> list[int]:
    return sample(range(-2 * n, 2 * n), n)


class TestAbstractSortingAlgorithm(unittest.TestCase, ABC):
    @property
    @abstractmethod
    def sorting_algorithm_class(self) -> Type[AbstractSortingAlgorithm]:
        pass

    def test_list_is_sorted_after_sorting(self):
        sorting_algorithm: AbstractSortingAlgorithm = self.sorting_algorithm_class()
        for _ in range(10):
            lst: list[int] = generate_random_list(100)
            sorting_algorithm.sort(lst)
            self.assertEqual(sorted(lst), lst)


class TestSelectionSort(TestAbstractSortingAlgorithm):
    sorting_algorithm_class = SelectionSort


class TestBubbleSort(TestAbstractSortingAlgorithm):
    sorting_algorithm_class = BubbleSort


class TestInsertionSort(TestAbstractSortingAlgorithm):
    sorting_algorithm_class = InsertionSort


class TestQuicksort(TestAbstractSortingAlgorithm):
    sorting_algorithm_class = Quicksort


del TestAbstractSortingAlgorithm
