# === Import required functions / libraries ===

from datetime import datetime


def set_logname():

    # === Form / return log filename

    date = datetime.now()
    date = date.strftime("%d-%m-%Y-%H-%M")
    log_name = 'internet_speedtest_log-' + date + '.txt'

    return log_name


if __name__ != "__main__":

    set_logname()

else:

    pass
