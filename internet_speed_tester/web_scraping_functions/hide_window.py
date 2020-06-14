# Import dependencies

# 3rd party modules installed as part of this project

# Used for hiding console for --silent option
# (installed with pip install pywin32)
import win32gui

# --- Built for project ---

from internet_speed_tester.misc_functions import output_progress


window_name = 'WebDriver - Internet Explorer'


def window_enum_handler(hwnd, all_windows):

    window_text = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)

    if window_text.find(window_name) >= 0:

        all_windows.append((hwnd, window_text, class_name))


def hide_ie_window(args, log_name):

    try:
        
        message = 'Attempting to hide IE window...'
        output_progress(args, message, log_name)

        all_windows = []
        win32gui.EnumWindows(window_enum_handler, all_windows)

        for hwnd, text, class_name in all_windows:

            win32gui.ShowWindow(hwnd, False)

        return True

    except Exception as e:

        message = 'Unable to hide IE window. Proceeeding with test. Error message: ' + str(e)
        output_progress(args, message, log_name)

        return False
