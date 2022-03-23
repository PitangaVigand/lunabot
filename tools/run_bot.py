from cProfile import run
from schedule import *
from tools import *
import schedule
import time
from play import *


def run_bot():
    # to avoid problems of more than ano monitors

    # start
    run = complete_play()
    time.sleep(1)
    if run:
        screen_day()
        looking("button_back")
    print(
        "---------{0} complete!-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )


run_bot()
schedule.every(4.5).hours.do(run_bot)
while True:
    try:
        n = schedule.idle_seconds()
        if int(n / 60) % 60 == 0:
            print(schedule.next_run().strftime("--------Next run %H:%M --------"))

    except Exception as e:
        print(e, "  in print status of bot")
        time.sleep(3)  # try0503pitgui

    try:
        schedule.run_pending()
        time.sleep(5)
    except Exception as e:
        print(e, "  in run shcedule")
        time.sleep(3)  # try
        continue
