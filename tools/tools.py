
import time
from datetime import date

import cv2
import pyautogui as pg


#glabal varibles
today = date.today()
screen_path = "imgs\screen.jpg"
screen = cv2.imread(screen_path,1)


#functions
def find_coord_to_click(img_all, img_part, threshold = .85):            
    part= cv2.imread(img_part,1)      
    result = cv2.matchTemplate(img_all, part, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    img_w,img_h = part.shape[1], part.shape[0] 
    if max_val < threshold :
        return False

    return max_loc[0]+ img_w/2, max_loc[1]+img_h/2 



def mouse_scroll(screen, team):    
    coord = find_coord_to_click(screen,r"imgs\obj_guerreiro_para_mouse.jpg")
    pg.moveTo(coord)
    time.sleep(1)
    pg.click()
    pg.moveTo(coord[0],coord[1]+200)
    time.sleep(1)
    print("scroll")
    if int(team) == 3:
        pg.scroll(-600)
    else:
        pg.scroll(600)




def screen_day():
    name = "screenshots day/{}.jpg".format(date.today())
    screen = myscreen()
    coord = [int(x) for x in find_coord_to_click(screen,r"imgs\obj_coin.jpg")]
    print(coord)
    cropped_image = screen[coord[1]-15:coord[1]+15, coord[0]:coord[0]+100]
    cv2.imwrite(name, cropped_image)


def click(target):
    if isinstance(target, str):
        coord = find_coord_to_click(screen,r"imgs\{0}.jpg".format(target))
    else:
        coord = target

    pg.moveTo(coord)
    time.sleep(1)
    print("Click: {}".format(target))
    pg.click()

    return True


#def push_git():
def myscreen():
    pg.screenshot(screen_path)
    screen = cv2.imread(screen_path,1)
    return screen

def count_energy():    
    return "ok"
