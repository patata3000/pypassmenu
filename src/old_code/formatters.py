"""Utilities to format list input."""


def format_pass_filename(root_path, filepath):
    return str(filepath.relative_to(str(root_path)).with_suffix(""))


def get_formatted_filename_list(root_path, gpg_files):
    return [format_pass_filename(root_path, filepath) for filepath in gpg_files]


def make_dmenu_input(filename_list):
    return "\n".join(filename_list)


def make_pass_insert_input(*args):
    return "\n".join(args)


def make_username_input(username_list):
    return "\n".join(username_list)


def make_username_list(username_input: str):
    return username_input.split("\n")
