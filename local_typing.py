from abc import abstractmethod
from typing import Protocol, TypeVar, Any


class __ComparableProtocol(Protocol):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

    @abstractmethod
    def __eq__(self, other: Any) -> bool: ...

    @abstractmethod
    def __gt__(self, other: Any) -> bool: ...


Comparable = TypeVar('Comparable', bound=__ComparableProtocol)
