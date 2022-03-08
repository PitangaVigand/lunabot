
from schedule import * 
import schedule
import time
from play import complete_play_by_time


def run_bot():
    print("Bot is running...")


schedule.every(.5).minutes.do(run_bot)
schedule.every(.75).hours.do(complete_play_by_time)

while True: 
    try:   
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(e)

