import subprocess
from abc import ABC, abstractmethod

from src.commands import SubprocessCommand


class DmenuCommand(SubprocessCommand):
    @property
    def name(self):
        return "dmenu"

    def vertical_results(self, nb_line: int = 8):
        self.add_arg("-l", nb_line)
