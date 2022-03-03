from mailbox import NotEmptyError
from tools.tools import *
from tools.actions import action
from datetime import datetime
import time
import os

def play_by_time():
    if not os.path.exists("screenshots day/{}.jpg".format(date.today())):
        screen_day()
    else:
        print("Screenshot already taken")
    
    for team in range(0,6):
        if team == 3:        
            mouse_scroll()

        pg.screenshot(screen_path)
        screen = cv2.imread(screen_path,1) 
        time.sleep(2)
        coor = select_person(screen,team)
        fight()

        if team == 3:        
            mouse_scroll()

        disselect_person(coor)()
     
play_by_time()


def play_by_vision():
    
    #using class
    return "ok"

