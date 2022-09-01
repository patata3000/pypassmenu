#!/usr/bin/env python3
import os
import subprocess
from abc import ABC, abstractmethod
from functools import reduce
from pathlib import Path





import click
from command import CommandInterface, DmenuCommand, PassCommand

from configs import USERNAME_PREFIX, dmenu_cmd, pass_insert_cmd, pass_show_cmd


def pipe(output, cmd2):
    cmd2.command_input = output
    return cmd2.run()


class Program:
    def __init__(self):
        self.command_list = []

    def pipe_commands(self):
        return reduce(pipe, self.command_list, self.command_list.pop(0).run())

    def add_command(self, cmd: CommandInterface):
        self.command_list.append(cmd)


class PassMenu(Program):
    # command_list = [DmenuCommand, PassCommand]

    def __init__(self, config_file=None):
        super().__init__()
        pass_command = PassCommand()
        self.add_command(pass_command)

    def dmenu_which_pass(self):
        cmd = DmenuCommand()
        cmd.vertical_results(nb_line=10)
        cmd.command_input =

    # def retrieve_pass(self):
    #     pass
    #     pass_selected = ask_filename()
    #     pass_show_cmd.append(pass_selected)
    #     subprocess.run(pass_show_cmd)

    # def insert_pass(self):
    #     pass_file = ask_filename()
    #     pass_insert_cmd.extend([pass_file, "-m"])
    #     pass_username = f"{USERNAME_PREFIX}{ask_username()}"
    #     pass_password = ask_password()
    #     pass_insert_input = make_pass_insert_input(
    #         pass_password, pass_username)
    #     subprocess.run(
    #         pass_insert_cmd,
    #         input=pass_insert_input,
    #         text=True,
    #         encoding="utf-8",
    #     )

    def run(self):
        return self.pipe_commands()


# @click.command("passmenu")
# @click.option("--insert/--no-insert", default=False)
# def passmenu(insert):
#     if insert:
#         insert_pass()
#     else:
#         retrieve_pass()





def test_main():
    PassMenu().run()


if __name__ == "__main__":
    test_main()
