
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
     
play_by_time((0,5),1)


def play_by_vision():
    view = True
    while view:
        #start
        #print
        play = True   
        #count energy 
        energy = 1
        while play:                   
            end_teams = fight_complete(screen,energy)
            if end_teams:
                play = False
            return
        view = False

