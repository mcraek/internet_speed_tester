# === Import Dependencies ===

# Built-in

import os
import glob


def test_functionality_with_logging():

    # Execute program with verbose and logging options, validate program completes and contains
    # speed results in log file

    os.system('python ../internet_speed_tester/main.py -vl')

    # Import results of test from log file by importing newest .txt file from tests directory

    file_list = glob.glob('./*.txt')
    newest_txt_file = max(file_list, key=os.path.getctime)
    log_contents = open(newest_txt_file, 'r').read()

    # Verify speed test completed and contains download and upload speed results

    down_speed_results = 'Download speed (MB / s):'
    up_speed_results = 'Upload speed (MB / s):'

    assert down_speed_results in log_contents and up_speed_results in log_contents

    # Remove log file containing speed test results

    os.remove(newest_txt_file)
