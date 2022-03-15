from cProfile import run
from schedule import *
from tools import *
import schedule
import time
from play import *


def run_bot():
    run = complete_play()
    time.sleep(1)
    if run:
        screen_day()
        looking("button_voltar")
    print(
        "---------{0} complete!-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )


# run_bot()
# play(*args)
play((1, 5), 3)
# schedule.every(.03).minutes.do(run_bot)
schedule.every(4.5).hours.do(run_bot)

while True:
    try:
        n = schedule.idle_seconds()
        print(int(int(n) / 60), "minuts last")
    except Exception as e:
        print(e, "  in print status of bot")
        time.sleep(3)  # try

    try:
        schedule.run_pending()
        time.sleep(10)
    except Exception as e:
        print(e, "  in run shcedule")
        time.sleep(3)  # try
        continue

# complete_play()
