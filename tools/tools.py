
import time
from datetime import date

import cv2
import numpy as np
import pyautogui as pg
import win32gui
import win32ui

#glabal varibles
today = date.today()
link = "https://app.lunarush.io/"
seg = 2
screen_path = "imgs\screen.jpg"
screen = cv2.imread(screen_path,1)


#functions
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


def fight():
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
        for i in range(36):
            print(i)
            time.sleep(1)            
            pg.click()

    return True


def select_boss(screen):
        part= cv2.imread(r"imgs\boss.jpg",1)      
        result = cv2.matchTemplate(screen, part, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        img_w,img_h = part.shape[1], part.shape[0]
        
        if max_val > .25:
            co = find_coord_to_click(screen,r"imgs\boss.jpg")
            pg.moveTo(co)
            print("ok")


def screen_day():
    name = "screenshots day/{}.jpg".format(date.today())
    pg.screenshot(screen_path)
    screen = cv2.imread(screen_path,1)
    coord = [int(x) for x in find_coord_to_click(screen,r"imgs\coin.jpg")]
    print(coord)
    cropped_image = screen[coord[1]-15:coord[1]+15, coord[0]:coord[0]+100]
    cv2.imwrite(name, cropped_image)


def get_screen():
    w= 1920
    h=1080
    hwnd =  win32gui.FindWindow(None, "LunaRush - Google Chrome" )

    #get the window image data
    wDC = win32gui.GetWindow(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateC

    screenshot =  np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screen

def start():
    #open chrome on luna
    #press play button
    #login e senha
    #caçar_chefe_bunner
    

    
    
