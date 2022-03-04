    

import time
from tools.tools import *
import pyautogui as pg


def select_person(screen,turn):
    first = 0+3*turn
    last = first+3
    time_coords = []
    for i in range(first, last):
        
        #print(coord)
        try:
            coord = find_coord_to_click(screen, "imgs\caracters\{0}.jpg".format(i))
            pg.moveTo(coord)
            print("Select: {0}".format(i))
            pg.click()
            time_coords.append(coord)        
            time.sleep(2)
        except Exception as e:
            print(e)
    return time_coords


def disselect_person(time_coords):
    for coord in time_coords:
        pg.moveTo(coord)
        pg.click()
        time.sleep(2)
