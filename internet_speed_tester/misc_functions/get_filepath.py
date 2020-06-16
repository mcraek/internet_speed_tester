# === Import dependencies ===

# Built-in

import os
import sys


def get_path(file_relative_path):

    try:

        # MEIPASS is an an attribute which stores the location of the tmp dir PyInstaller creates
        # when a Python program is compiled to exe

        root_path = sys._MEIPASS

    # If MEIPASS doesn't exist, the program is not being executed
    # from a compiled exe, return the file path of the file relative
    # to the project root dir instead of looking at the MEIPASS
    # directory at all

    except Exception:

        root_path = os.path.abspath('.')

    return os.path.join(root_path, file_relative_path)
