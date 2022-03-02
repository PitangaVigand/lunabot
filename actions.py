from calendar import c
import os
import time
import webbrowser

import cv2
import numpy
import pyautogui as pg

link = "https://app.lunarush.io/"
seg = 2

screen_path = "imgs\screen.jpg"

def find_coord_to_click(img_all, img_part):            
    part= cv2.imread(img_part,1)      
    result = cv2.matchTemplate(img_all, part, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    img_w,img_h = part.shape[1], part.shape[0] 
    return max_loc[0]+ img_w/2, max_loc[1]+img_h/2

def select_person(screen,turn):
    first = 0+3*turn
    last = first+3
    time_coords = []
    for i in range(first, last):
        coord = find_coord_to_click(screen, "imgs\caracters\{0}.jpg".format(i))
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

def mouse_scroll():
    screen = tela = cv2.imread(screen_path,1)
    coord = find_coord_to_click(screen,r"imgs\guerreiro_para_mouse.jpg")
    pg.click(coord)
    pg.moveTo(coord[0],coord[1]+200)
    time.sleep(2)
    pg.scroll(-200)

def fight(turn):
    mouse_scroll()
    pg.screenshot(screen_path)
    screen = tela = cv2.imread(screen_path,1) 
    time_coords = select_person(screen,turn)
    time.sleep(2)
    button = find_coord_to_click(screen, r"imgs\b_cacar_chefe.jpg" )

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

    return time_coords

def change_boss(screen):
        part= cv2.imread(r"imgs\boss.jpg",1)      
        result = cv2.matchTemplate(screen, part, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        img_w,img_h = part.shape[1], part.shape[0]
        
        if max_val > .25:
            co = find_coord_to_click(screen,r"imgs\boss.jpg")
            pg.moveTo(co)
            print("ok")

    

        # if find_coord_to_click() 
        #     print("Boss")


def play():
    for i in range(0,6):
        time_coords = fight(i)
        time.sleep(5)
        disselect_person(time_coords)


# mouse_scroll()
screen = tela = cv2.imread(screen_path,1) 
# coor =select_person(screen,3)
# disselect_person(coor)
#fight(4)
# play()
change_boss(screen)
