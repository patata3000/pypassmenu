import subprocess

from command import DmenuCommand
from file_manips import get_filename_list, get_username_list, save_username
from formatters import get_formatted_filename_list, make_dmenu_input

from configs import dmenu_cmd, password_store_dir_path





def ask_password():
    return subprocess.run(
        dmenu_cmd, input="", text=True, stdout=subprocess.PIPE
    ).stdout.strip()


def ask_save_username(usernames_list, username):
    response = (
        subprocess.run(
            dmenu_cmd, input="Yes\nNo", text=True, stdout=subprocess.PIPE
        )
        .stdout.strip()
        .lower()
    )
    if response in ["y", "yes"]:
        return True
    elif response in ["n", "no"]:
        pass
    else:
        ask_save_username(usernames_list, username)


def ask_username():
    usernames_list = get_username_list()
    pass_username = subprocess.run(
        dmenu_cmd,
        input=make_dmenu_input(get_username_list()),
        text=True,
        stdout=subprocess.PIPE,
    ).stdout.strip()
    if ask_save_username(usernames_list, pass_username):
        save_username(usernames_list, pass_username)
    return pass_username


def ask_filename():
    filename_list = get_filename_list()
    dmenu_cmd = DmenuCommand()
    formatteds_filename_list = get_formatted_filename_list(
        password_store_dir_path, filename_list
    )
    return subprocess.run(
        dmenu_cmd,
        input=make_dmenu_input(formatteds_filename_list),
        text=True,
        stdout=subprocess.PIPE,
    ).stdout.strip()
