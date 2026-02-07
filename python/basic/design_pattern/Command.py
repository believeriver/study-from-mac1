from abc import ABC, abstractmethod


class File(object):
    def __init__(self, name: str):
        self.__name = name

    def open(self):
        print(f"{self.__name} is opened")

    def compress(self):
        print(f"{self.__name} is compressed")

    def close(self):
        print(f"{self.__name} is closed")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class OpenCommand(Command):
    def __init__(self, file: File):
        self.__file = file

    def execute(self):
        self.__file.open()


class CompressCommand(Command):
    def __init__(self, file: File):
        self.__file = file

    def execute(self):
        self.__file.compress()


class CloseCommand(Command):
    def __init__(self, file: File):
        self.__file = file

    def execute(self):
        self.__file.close()


class Queue(object):
    def __init__(self):
        self.__commands = []

    def add_command(self, command: Command):
        self.__commands.append(command)

    def execute_command(self):
        for command in self.__commands:
            command.execute()


if __name__ == '__main__':
    file = File("command.py")
    queue = Queue()

    queue.add_command(OpenCommand(file))
    queue.add_command(CompressCommand(file))
    queue.add_command(CloseCommand(file))

    queue.execute_command()

