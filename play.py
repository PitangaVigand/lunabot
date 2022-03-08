
import os
import time

from tools.fight import *
from tools.tools import *
from tools.selection import *
from start import *



def play_by_time(range_team, energy):
    screen = myscreen()
    select_boss(screen)

    if not os.path.exists("screenshots day/{}.jpg".format(date.today())):
        screen_day()
    else:
        print("Screenshot already taken")
    
    for team in range(*range_team):
        screen = myscreen()
        time.sleep(1)        
        mouse_scroll(screen,team)
        
        time.sleep(1)
        screen= myscreen() 
        coord = select_person(screen,team)

        fight_complete(screen,energy) 
        screen= myscreen()              
        mouse_scroll(screen,team) 
        deselect_person(coord)
        time.sleep(1)
        
    click(screen,"button_voltar")
    print("The End")

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

def complete_play_by_time():
    start()
    play_by_time((0,5),1)


#complete_play_by_time()
#play_by_time((3,5),1)