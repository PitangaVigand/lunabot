
import time
from datetime import date

import cv2
import pyautogui as pg
from tools.tools import *



#glabal varibles
screen_path = "imgs\screen.jpg"


def fight():
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
        for i in range(45):
            print(i)
            time.sleep(1)            
            pg.click()

    return True


def fight_complete(screen,energy):
    time.sleep(2)
    button = find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg" )

    #play 3 times
    for i in range(0,energy):
        #caçar 
        try:      
            print("click caçar")
            pg.moveTo(button)
            pg.click()
            time.sleep(5)
        except Exception as e:
            print(e)
            break

        #move to midle
        print("click midle")
        pg.moveTo(button[0]-350, button[1])
        pg.click()       
       
        #clik in the midle
        for i in range(45):            
            print(i)
            time.sleep(1)

            #make time stops
            pg.screenshot(screen_path)
            screen = cv2.imread(screen_path,1)
            if find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg"):
                break  

            if find_coord_to_click(screen, r"imgs\banner_boss.jpg"):
                select_boss(screen)                 
            pg.click()

    return True

screen = cv2.imread(screen_path,1)
