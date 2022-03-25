from cProfile import run
from schedule import *
from tools import *
import schedule
import time
from play import *


def run_bot(function_to_run, energy: int, play_now: bool = False) -> None:
    """
    Run a specific function for
    """
    print("------{0}-------------------".format(inspect.currentframe().f_code.co_name))
    if play_now:
        function_to_run(energy)

    # mark the schedule
    schedule.every(energy * 1.5).hours.do(function_to_run, energy)

    while True:
        # Calculate point of time of next run
        try:
            n = schedule.idle_seconds()
            if int(n / 60) % 60 == 0:
                print(schedule.next_run().strftime("--------Next run %H:%M --------"))

        except Exception as e:
            print(e)
            time.sleep(3)

        # the call
        try:
            schedule.run_pending()
            time.sleep(5)
        except Exception as e:
            print(e, "  in run schedule")
            time.sleep(3)  # try
            continue


run_bot(complete_play, 3, False)
