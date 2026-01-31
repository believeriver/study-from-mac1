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


class Employee(Entry):
    def __init__(self, _code: str, _name:str):
        super().__init__(_code, _name)

    def get_children(self) -> List[Entry]:
        return []

    def accept(self, visitor: Visitor):
        visitor.visit(self)


class Visitor(ABC):
    @abstractmethod
    def visit(self, entry: Entry):
        pass


class ListVisitor(Visitor):
    def visit(self, entry: Entry):
        if type(entry) == Group:
            print(f"{entry.code}: {entry.name}")
        else:
            print(f"  {entry.code}: {entry.name}")
        for child in entry.get_children():
            child.accept(self)


class CountVisitor(Visitor):
    def __init__(self):
        self.__group_count = 0
        self.__employee_count = 0

    @property
    def group_count(self) -> int:
        return self.__group_count

    @property
    def employee_count(self) -> int:
        return self.__employee_count

    def visit(self, entry: Entry):
        if type(entry) == Group:
            self.__group_count += 1
        else:
            self.__employee_count += 1
        for child in entry.get_children():
            child.accept(self)


if __name__ == "__main__":
    root_entry = Group("01", "Head Office")
    root_entry.add(Employee("001", "CE0"))
    root_entry.add(Employee("002", "CF0"))

    group1 = Group("10", "Japan")
    group1.add(Employee("1001", "A1"))

    group2 = Group("11", "Canada")
    group2.add(Employee("1101", "C1"))
    group2.add(Employee("1102", "C2"))
    group2.add(Employee("1103", "C3"))

    group1.add(group2)
    root_entry.add(group1)

    list_visitor = ListVisitor()
    count_visitor = CountVisitor()

    print(f"Group: {count_visitor.group_count}")
    print(f"Employee: {count_visitor.employee_count}")

    root_entry.accept(list_visitor)
    root_entry.accept(count_visitor)

    print('-'*10)

    print(f"Group: {count_visitor.group_count}")
    print(f"Employee: {count_visitor.employee_count}")
