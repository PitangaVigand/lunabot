
import os
import time

from tools.fight import *
from tools.tools import *
from tools.selection import *


def play_by_time(range_team, energy):
    if not os.path.exists("screenshots day/{}.jpg".format(date.today())):
        screen_day()
    else:
        print("Screenshot already taken")
    
    for team in range(*range_team):
        pg.screenshot(screen_path)
        screen = cv2.imread(screen_path,1)
        mouse_scroll(screen,team)
        time.sleep(2)
        coor = select_person(screen,team)

        fight_complete(screen,energy)               
        mouse_scroll(screen,team) 
        disselect_person(coor)
     
play_by_time((0,5),3)


def play_by_vision():
    while True:


        
        #using class
        return "ok"

