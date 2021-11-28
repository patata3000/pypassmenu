#!/usr/bin/env python3
import os
from pathlib import Path
import subprocess

import click

from configs import dmenu_cmd, pass_insert_cmd, pass_show_cmd, USERNAME_PREFIX
from dmenu_asker import (
    ask_filename,
    ask_password,
    ask_username,
)
from formatters import make_pass_insert_input


def retrieve_pass():
    pass_selected = ask_filename()
    pass_show_cmd.append(pass_selected)
    subprocess.run(pass_show_cmd)


def insert_pass():
    pass_file = ask_filename()
    pass_insert_cmd.extend([pass_file, "-m"])
    pass_username = f"{USERNAME_PREFIX}{ask_username()}"
    pass_password = ask_password()
    pass_insert_input = make_pass_insert_input(pass_password, pass_username)
    subprocess.run(
        pass_insert_cmd, input=pass_insert_input, text=True, encoding="utf-8"
    )


@click.command("passmenu")
@click.option("--insert/--no-insert", default=False)
def passmenu(insert):
    if insert:
        insert_pass()
    else:
        retrieve_pass()


if __name__ == "__main__":
    passmenu()
