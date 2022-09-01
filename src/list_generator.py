from abc import ABC, abstractmethod

from path import Path


class ListGeneratorInterface(ABC):
    @abstractmethod
    def make_list(self):
        """Create a list."""


class ListFromDirectory(ListGeneratorInterface):
    def __init__(self, directory_path: str, suffix: str):
        self.directory_path = Path(directory_path)
        self.suffix = suffix

    def make_list(self):
        filename_list = self.directory_path.rglob("*.gpg")
        return [
            str(filepath.relative_to(str(self.directory_path)).with_suffix(""))
            for filepath in filename_list
        ]


class ListFromString(ListGeneratorInterface):
    def __init__(self, string, sep="\n"):
        self.string = string
        self.sep = sep

    def make_list(self):
        return [self.string.split(self.sep)]


class ListFromPythonList(ListGeneratorInterface):
    def __init__(self, list_):
        self.list = list_

    def make_list(self):
        return self.list
