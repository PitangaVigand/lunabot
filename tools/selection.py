    

import time
from tools.tools import *
import pyautogui as pg
import cv2 as cv2
import pyautogui as pg


def select_person(screen,turn):
    first = 0+3*turn
    last = first+3
    time_coords = []
    for i in range(first, last):
        
        #print(coord)
       
        coord = find_coord_to_click(screen, "imgs\caracters\{0}.jpg".format(i))
        pg.moveTo(coord)
        print("Select: {0}".format(i))
        pg.click()
        time_coords.append(coord)        
        time.sleep(2)
  
    return time_coords


def deselect_person(time_coords):
    for i,coord in enumerate(time_coords):        
        try:
            pg.moveTo(coord)
            print("Deselect: {0}".format(i))
            pg.click()
            time.sleep(2)
        except Exception as e:
            print(e)



def select_boss(screen):
        part= cv2.imread(r"imgs\banner_boss.jpg",1)      
        result = cv2.matchTemplate(screen, part, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        img_w,img_h = part.shape[1], part.shape[0]
        
        if max_val > .25:
            coord = find_coord_to_click(screen,r"imgs\banner_boss.jpg")
            pg.moveTo(coord)
            time.sleep(2)
            print("Click: Select boss")
            pg.click()
        return True

# screen = myscreen()
# coord = select_person(screen,3)

# time.sleep(1)
# deselect_person(coord)