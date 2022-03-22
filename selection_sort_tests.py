import unittest
from random import sample

from selection_sort import selection_sort


def generate_random_list(n: int) -> list[int]:
    return sample(range(-2 * n, 2 * n), n)


class TestSelectionSort(unittest.TestCase):
    def test_list_is_sorted_after_sorting(self):
        for _ in range(10):
            lst: list[int] = generate_random_list(100)
            selection_sort(lst)
            self.assertEqual(sorted(lst), lst)
