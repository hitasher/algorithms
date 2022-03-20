import unittest
from random import sample

from binary_search import binary_search


def generate_random_sorted_list(n: int) -> list[int]:
    lst: list[int] = sample(range(-2 * n, 2 * n), n)
    lst.sort()
    return lst


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_does_not_find_elements_in_sample_case(self):
        lst: list[int] = [1, 3, 5]
        for el in [0, 2, 4, 6]:
            self.assertIsNone(binary_search(lst, el))

    def test_binary_search_finds_existing_elements(self):
        lst: list[int] = generate_random_sorted_list(100)
        for el in lst:
            index: int = binary_search(lst, el)
            self.assertEqual(el, lst[index])

    def test_binary_search_does_not_find_non_existing_elements(self):
        lst: list[int] = generate_random_sorted_list(100)
        minimum_element: int = lst[0]
        maximum_element: int = lst[-1]
        self.assertIsNone(binary_search(lst, minimum_element - 1))
        self.assertIsNone(binary_search(lst, maximum_element + 1))
