# === Import required functions / libraries ===

# Built-in

from datetime import datetime

# Built for project

from internet_speed_tester import set_logname


def test_set_logname():

    # === Form filename to compare against
    # internet_speedtest_log-dd-mm-yyyy-hh-mm.txt is the expected name

    date = datetime.now()
    date = date.strftime("%d-%m-%Y-%H-%M")
    expected_log_name = 'internet_speedtest_log-' + date + '.txt'

    # === Call funciton and compare this to the expected value

    check = set_logname()
    assert check == expected_log_name
