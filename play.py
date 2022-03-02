from mailbox import NotEmptyError
from tools.tools import *
from tools.actions import action



def play():
    
    while True:
        selection_done = None
        change_boss_done = None
        disselect_person_done = None
        hunt_boss_done = None


        
        #if energia cheia 
        if first_sceen:
            selection_done = action.select_person()
        if self.select_person_done:
            hunt_boss_done = action.hunt_boss()
     
    

