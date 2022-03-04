import time

import cv2
import pyautogui as pg
from tools.tools import *

class action():
    def select_person(screen,turn, self):
        first = 0+3*turn
        last = first+3
        coords = []
        for i in range(first, last):
            coord = find_coord_to_click(screen, "imgs\caracters\{0}.jpg".format(i))
            print(coord)
            pg.moveTo(coord)
            pg.click()
            coords.append(coord)        
            time.sleep(2)
        return coords

        
    def hunt_boss(self):
        time.sleep(2)
        button = find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg" )

        #play 3 times
        for i in range(0,3):
            #caçar       
            print("click1")
            pg.moveTo(button)
            pg.click()
            time.sleep(5)

            #move to midle
            print("click2")
            pg.moveTo(button[0]-350, button[1])
            pg.click()       
        
            #clik in the midle
            for i in range(31):
                print(i)
                time.sleep(1)            
                pg.click()

        return True
    
    
    def select_boss(screen,self):
        part= cv2.imread(r"imgs\boss.jpg",1)      
        result = cv2.matchTemplate(screen, part, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        img_w,img_h = part.shape[1], part.shape[0]

        if max_val > .25:
            result = cv2.matchTemplate(screen, part, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where( result >= threshold)
            co = find_coord_to_click(screen,r"imgs\boss.jpg")
            pg.moveTo(co)
            print("ok")
        return True


    def disselect_person(time_coords,self):
        for coord in time_coords:
            pg.moveTo(coord)
            pg.click()
            time.sleep(2)
        return True
