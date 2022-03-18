from abc import abstractmethod
from typing import Protocol, TypeVar, Any, MutableSequence


class ComparableProtocol(Protocol):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...


Comparable = TypeVar('Comparable', bound=ComparableProtocol)


def selection_sort(sequence: MutableSequence[Comparable]) -> None:
    for i in range(len(sequence)):
        index_of_minimum_element: int = min(range(i, len(sequence)), key=sequence.__getitem__)
        sequence[i], sequence[index_of_minimum_element] = sequence[index_of_minimum_element], sequence[i]
