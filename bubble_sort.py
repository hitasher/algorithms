from typing import MutableSequence

from local_typing import Comparable


def bubble_sort(sequence: MutableSequence[Comparable]):
    start_index = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(len(sequence) - start_index - 1):
            if sequence[j + 1] < sequence[j]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
                is_sorted = False
        start_index += 1
