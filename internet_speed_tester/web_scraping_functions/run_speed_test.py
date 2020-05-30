from internet_speed_tester.web_scraping_functions.initialize_ie_session \
    import start_ie_session


def run_speed_test(args, log_name):

    session = start_ie_session(args, log_name)


if __name__ == '__main__':

    run_speed_test()
