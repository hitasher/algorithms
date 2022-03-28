from abc import ABC, abstractmethod
from typing import MutableSequence

from local_typing import Comparable


class AbstractSortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, sequence: MutableSequence[Comparable]) -> None:
        pass
