import subprocess
from abc import ABC, abstractmethod

from src.commands.command_input import command_input


def command(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        return self.run()

    return wrapper


class CommandInterface(ABC):
    """Permit defining multiple types of command."""

    @abstractmethod
    def run(self):
        pass


class SubprocessCommand(CommandInterface):
    """Implement CommandInterface for a subprocess."""

    def __init__(self, name, command_input=None):
        self.name = name
        self._arg_list = [name]
        self.arg_list = []
        self.command_input = command_input

    @property
    def command(self):
        return [self.name, *self.arg_list]

    @property
    def command_input(self):
        return self._command_input

    @command_input.setter
    def command_input(self, value):
        self._command_input = command_input.get_command_input(value)

    def add_arg(self, arg_name, arg_value=None):
        self.arg_list.append(arg_name)
        if arg_value:
            self.arg_list.append(arg_value)

    def run(self):
        return subprocess.run(
            self.command,
            input=self.command_input,
            text=True,
            stdout=subprocess.PIPE,
            check=True,
        ).stdout.strip()
