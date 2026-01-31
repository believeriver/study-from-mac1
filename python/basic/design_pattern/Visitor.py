from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Entry(ABC):
    def __init__(self, _code: str, _name: str):
        self.__code = _code
        self.__name = _name

    @property
    def code(self) -> str:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_children(self) -> List[Entry]:
        pass

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Group(Entry):
    def __init__(self, _code: str, _name:str):
        super().__init__(_code, _name)
        self.__entries: List[Entry] = []

    def add(self, entry: Entry):
        self.__entries.append(entry)

    def get_children(self) -> List[Entry]:
        return self.__entries

    def accept(self, visitor: Visitor):
        visitor.visit(self)





