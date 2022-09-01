import os
from abc import abstractmethod

from src.commands import SubprocessCommand, command


class Pass:
    def __init__(self, password_store=None):
        self.password_store = password_store
        self._subprocess_command = SubprocessCommand("pass")

    @command
    def show(self):
        self._subprocess_command.add_arg("show")
