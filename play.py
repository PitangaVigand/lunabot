
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
        screen = myscreen()        
        mouse_scroll(screen,team)
        
        time.sleep(1)
        screen= myscreen() 
        coord = select_person(screen,team)

        fight_complete(screen,energy) 
        screen= myscreen()              
        mouse_scroll(screen,team) 
        deselect_person(coord)
     
play_by_time((4,5),1)


def play_by_vision():
    while True:


        
        #using class
        return "ok"

