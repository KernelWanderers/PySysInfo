from abc import abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")

class BaseManager(Generic[T]):
    @abstractmethod
    def __osx(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def __win(self) -> list[T]:
        raise NotImplementedError
    
    @abstractmethod
    def __linux(self) -> list[T]:
        raise NotImplementedError