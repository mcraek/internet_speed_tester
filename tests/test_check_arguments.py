# === Import main program to test ===

from    internet_speed_tester       import      check_arguments

def test_parser():

    check = vars(check_arguments('v'))
    assert check['verbose'] == True