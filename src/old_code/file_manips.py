from formatters import make_username_list

from configs import passmenu_data_dir_path, password_store_dir_path


def save_username(usernames_list, username):
    if username not in usernames_list:
        usernames_list.append(username)
        formatted_usernames = "\n".join(usernames_list)
        with open(
            passmenu_data_dir_path.joinpath("usernames"),
            "w+",
            encoding="utf-8",
        ) as usernames_file:
            usernames_file.write(formatted_usernames)
            return True
    return False


def get_username_list():
    try:
        with open(
            passmenu_data_dir_path.joinpath("usernames"),
            "r",
            encoding="utf-8",
        ) as usernames_file:
            return make_username_list(usernames_file.read())
    except FileNotFoundError:
        return []


def remove_username(username):
    usernames_list = get_username_list()
    if username not in usernames_list:
        usernames_list.append(username)


def get_filename_list():
    return password_store_dir_path.rglob("*.gpg")
