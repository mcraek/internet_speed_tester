# === Import required functions / libraries ===

# Built-in

import os
import pytest
import shutil

# Create fixture which sets a temporary working directory for tests / files
# generatedduring testing. After tests are complete, remove the temp directory
# To see the path of the tempdir:
# add a print('tempdir located at: ' + str(tempdir)) below, and run pytest -s


@pytest.fixture
def temp_dir(tmpdir):

    # Create the temporary directory
    tempdir = tmpdir.mkdir("internet_speed_tester_workingdir")

    # Store current directory to return to after test
    original_wd = os.getcwd()

    # Change to temporary directory
    os.chdir(tempdir)

    # After tests are complete, return to original working_dir
    # and remove the temp directory

    yield temp_dir
    os.chdir(original_wd)
    shutil.rmtree(str(tempdir))
