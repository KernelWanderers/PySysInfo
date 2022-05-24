from abc import abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")

class BaseManager(Generic[T]):
    @abstractmethod
    def _osx(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def _win(self) -> list[T]:
        raise NotImplementedError
    
    @abstractmethod
    def _linux(self) -> list[T]:
        raise NotImplementedError