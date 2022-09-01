from abc import abstractmethod
from typing import Callable


class CommandInputInterface:
    def __init__(self, raw_input):
        self.raw_input = raw_input

    @abstractmethod
    def get_input_str(self):
        """Return input as an str."""


class CommandInputStr(CommandInputInterface):
    def get_input_str(self):
        return self.raw_input


class CommandInputList(CommandInputInterface):
    def get_input_str(self, command):
        return "/n".join(self.raw_input)


class CommandInputFactory:
    def __init__(self):
        self.command_inputs = {}

    def add_command_input(
        self,
        input_type: type,
        command_input_class: Callable[..., CommandInputInterface],
    ):
        self.command_inputs[input_type] = command_input_class

    def get_command_input(self, raw_input):
        if raw_input is None:
            return None
        raw_input_type = type(raw_input)
        try:
            return self.command_inputs[raw_input_type](
                raw_input
            ).get_input_str()
        except KeyError:
            raise KeyError(
                "CommandInputInterface is not defined for type: "
                f"{raw_input_type}"
            )


command_input = CommandInputFactory()

command_input.add_command_input(str, CommandInputStr)
command_input.add_command_input(list, CommandInputList)
