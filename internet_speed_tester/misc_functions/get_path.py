def get_path(file_relative_path):

    # ============================== Import Built-in Dependencies ============================== #

    import os # Needed for referencing relative paths of images used in GUI
    import sys # Used for referencing sys.MEIPASS (Temp directory PyInstaller creates for executable version of program in Production)


    # ============================== Begin Function ============================== #

    try:
    
        # MEIPASS is an an attribute which stores the location of the tmp dir PyInstaller creates when a Python program is compiled to exe

        root_path = sys._MEIPASS

    # If MEIPASS doesn't exist, the program is not being executed from a compiled exe, return the file path of the file relative to the project
    # root dir instead of looking at the MEIPASS directory at all

    except Exception:
    
        root_path = os.path.abspath('.')

    return os.path.join(root_path, file_relative_path)