# ============================== Import Dependencies ============================== #

# 3rd party modules installed as part of this project

import      win32gui		# Used for hiding console for --silent option (installed with pip install pywin32)
import subprocess

window_name = 'WebDriver - Internet Explorer'

def window_enum_handler(hwnd, all_windows):

    window_text = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)

    if window_text.find(window_name) >= 0:

        all_windows.append((hwnd, window_text, class_name))


def hide_window():

    all_windows = []
    win32gui.EnumWindows(window_enum_handler, all_windows)

    for hwnd, text, class_name in all_windows:

        win32gui.ShowWindow(hwnd, False)