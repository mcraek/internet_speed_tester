# === Import required functions / libraries ===

# Built-in

import pytest
import sys
from unittest.mock import patch

# Built for project

from internet_speed_tester import check_arguments


# Define acceptable arguments, and values that should be set to
# True once an argument is called
# For each acceptable argument, test to make sure the expected setting
# is returned True when the argument is called


@pytest.mark.parametrize(('argument', 'expected_setting'), (

    ('-l', 'log'),
    ('--log', 'log'),
    ('-o', 'outfile'),
    ('--outfile', 'outfile'),
    ('-s', 'silent'),
    ('--silent', 'silent'),
    ('-v', 'verbose'),
    ('--verbose', 'verbose'),

))
def test_arguments(argument, expected_setting):

    with patch('sys.argv', ['internet_speed_test', argument]):

        check = vars(check_arguments(sys.argv[1:]))
        assert check[expected_setting]
