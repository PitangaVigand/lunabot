import os
import time
import webbrowser

import cv2
import numpy
import pyautogui as pg

link = "https://app.lunarush.io/"
seg = 2

scream_path = "imgs\scream.jpg"

def find_coord_to_click(img_all, img_part):            
    part= cv2.imread(img_part,1)      
    result = cv2.matchTemplate(img_all, part, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    img_w,img_h = part.shape[1], part.shape[0] 
    return max_loc[0]+ img_w/2, max_loc[1]+img_h/2

def select_person(scream,turn):
    first = 0+3*turn
    last = first+3
    time_coords = []
    for i in range(first, last):
        coord = find_coord_to_click(scream, "imgs\caracters\{0}.jpg".format(i))
        print(coord)
        pg.moveTo(coord)
        pg.click()
        time_coords.append(coord)        
        time.sleep(2)
    return time_coords



def disselect_person(time_coords):
    for coord in time_coords:
        pg.moveTo(coord)
        pg.click()
        time.sleep(2)    


def fight(turn):
    pg.screenshot(scream_path)
    scream = tela = cv2.imread(scream_path,1) 
    time_coords = select_person(scream,turn)
    time.sleep(2)
    button = find_coord_to_click(scream, r"imgs\b_cacar_chefe.jpg" )

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
            #pg.screenshot(scream_path)
            # out = find_coord_to_click(scream, r"imgs\toque para continuar.jpg" )
            # toque_para = find_coord_to_click(scream, r"imgs\toque_para_abrir.jpg" )
            # if out:
            #     print("click")   
            #     pg.moveTo(out)
            #     pg.click()
            #     break
            # elif toque_para:
            #     print("click")   
    #         #     pg.moveTo(toque_para)
    #         #     pg.click()
    #         #     break
    #         # else:
    #         #     continue

            
        # time.sleep(3)
        # print("click3")
        # pg.moveTo(button)
        # pg.click()
    return time_coords


def play():
    for i in range(3,5):
        time_coords = fight(i)
        time.sleep(5)
        disselect_person(time_coords)

# pg.screenshot(scream_path)
# scream = tela = cv2.imread(scream_path,1)
# select_person(scream)
    
# pg.print_function()
# # start_boss()
# # select_person()
# # navegador = webbrowser.open(link)
#coor = play()
fight(0)
# play()
