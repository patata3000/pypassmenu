import os
from pathlib import Path

from formatters import make_dmenu_input

dmenu_cmd = ["dmenu", "-c", "-l", "8", "-g", "4"]
XDG_DATA_HOME = os.environ.get("XDG_DATA_HOME", "~/.local/share")
xdg_data_home_path = Path(XDG_DATA_HOME)

PASSWORD_STORE_DIR = os.environ.get(
    "PASSWORD_STORE_DIR", str(xdg_data_home_path.joinpath("pass"))
)
PASSMENU_DATA_DIR = os.environ.get(
    "PASSMENU_DATA_DIR", str(xdg_data_home_path.joinpath("passmenu"))
)

pass_show_cmd = ["pass", "show"]
pass_insert_cmd = ["pass", "insert"]
password_store_dir_path = Path(PASSWORD_STORE_DIR)
passmenu_data_dir_path = Path(PASSMENU_DATA_DIR)
os.makedirs(str(passmenu_data_dir_path), exist_ok=True)
USERNAME_PREFIX = "username: "
