
import time
from datetime import date

import cv2
import pyautogui as pg

from tools.tools import *
from tools.selection import *


#glabal varibles
screen_path = "imgs\screen.jpg"


def fight():
    time.sleep(2)
    button = find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg" )

    #play 3 times
    for i in range(0,3):
        #caçar       
        print("Click:1")
        pg.moveTo(button)
        pg.click()
        time.sleep(5)

        #move to midle
        print("Click:2")
        pg.moveTo(button[0]-350, button[1])
        pg.click()       
       
        #clik in the midle
        for i in range(45):
            print(i)
            time.sleep(1)            
            pg.click()

    return True


def fight_complete(screen,energy):
    time.sleep(1)
    button = find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg" )

    #play 3 times
    for i in range(0,energy):
        #caçar 
        try:      
            print("Click: Caçar")
            pg.moveTo(button)
            pg.click()            
        except Exception as e:
            print(e)
            break

        #move to midle
        time.sleep(5)
        print("Click: Midle")
        pg.moveTo(button[0]-350, button[1]-25)
        pg.click()       
       
        #clik in the midle
        for i in range(45):            
            print(i)
            time.sleep(1) 
            screen = myscreen()
            toque_para = find_coord_to_click(screen, r"imgs\button_toque_para.jpg")
            caçar_chefe = find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg")
            banner_boss = find_coord_to_click(screen, r"imgs\banner_boss.jpg")
            toque_para_continuar = find_coord_to_click(screen, r"imgs\button_toque_para_continuar.jpg",)
            toque_para_abrir = find_coord_to_click(screen, r"imgs\button_toque_para_abrir.jpg")
            toque_para_assistir = find_coord_to_click(screen, r"imgs\button_toque_para_assistir.jpg")          

            #make time stops       
            
            if toque_para:                
                click(toque_para)
            
            if toque_para_abrir:                
                click(toque_para_abrir)
            
            if toque_para_continuar:                
                click(toque_para_continuar)

            if caçar_chefe:
                print("breack caçar chefe")
                break  

            if banner_boss:
                boss = select_boss(screen)
                if boss:
                    print("Break boss")
                    break 
            
                        
            #pg.click()

    return True

# screen = cv2.imread(screen_path,1)
