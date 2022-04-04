import time

import schedule
from schedule import *

from play import *
from tools import *
import cv2 as cv


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
            time.sleep(1)
        except Exception as e:
            print(e, "  in run schedule")
            time.sleep(3)  # try
            continue

        # Interations with external commands
        key = cv.waitKey(1) & 0xFF
        if key == ord("t") or key == ord("T"):
            print(schedule.next_run().strftime("--------Next run %H:%M --------"))
        elif key == ord("r"):
            function_to_run(energy)
        elif key == ord("s"):
            break


run_bot(complete_play, 1, True)
