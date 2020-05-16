def check_arguments(argv=None):

    # === Import required functions / libraries ===

    import argparse

    # === Define valid arguments ===

    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--log', help='outputs verbose logs including errors to same directory as program',
                        action="store_true")

    parser.add_argument('-o', '--outfile', help='determines whether download / upload speeds are output to files within same directory as program for parsing',
                        action="store_true")

    parser.add_argument('-s', '--silent', help='if set to true, hides console and outputs results to text file in same directory as program. debug is not set to true automatially',
                        action="store_true")

    parser.add_argument('-v', '--verbose', help='increases verbosity of console output',
                        action='store_true')

    # === Store / return arguments ===

    parsed_args = parser.parse_args()


    return parsed_args
