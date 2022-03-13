
from select import select
import time
from datetime import date , datetime

import cv2
import pyautogui as pg
import inspect



#glabal varibles
today = date.today()
screen_path = "imgs\screen.jpg"
screen = cv2.imread(screen_path,1)


#functions
def find_coord_to_click(img_all, img_part, threshold = .85):
    img_all = myscreen()
    try:             
        part= cv2.imread(img_part,1)      
        result = cv2.matchTemplate(img_all, part, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        img_w,img_h = part.shape[1], part.shape[0] 
        if max_val < threshold :
            return False

        return max_loc[0]+ img_w/2, max_loc[1]+img_h/2 
    except:
        print("{} not found".format(img_part))
        return False


def mouse_scroll(screen, team):    
    time.sleep(1) 
    coord = find_coord_to_click(screen,r"imgs\obj_guerreiro_para_mouse.jpg")
    pg.moveTo(coord)
    time.sleep(1)
    pg.click()
    pg.moveTo(coord[0],coord[1]+200)
    time.sleep(1)

    if int(team) == 3:
        pg.scroll(-2000)
        time.sleep(1)
        pg.scroll(-2000)
        time.sleep(1)
        pg.scroll(-2000)
        
    else:
        pg.scroll(2000)
        time.sleep(1)
        pg.scroll(2000)


def screen_day():   
    name = "screenshots day/{0}_{1}hs.jpg".format(date.today(),datetime.now().strftime("%H"))
    screen = myscreen()
    coord = [int(x) for x in find_coord_to_click(screen,r"imgs\obj_coin.jpg")]
    cropped_image = screen[coord[1]-15:coord[1]+15, coord[0]:coord[0]+100]
    cv2.imwrite(name, cropped_image)


def click(screen=screen,target=1):
    if isinstance(target, str):
        print("Click: {}".format(target))
        coord = find_coord_to_click(screen,r"imgs\{0}.jpg".format(target))
    else:
        print("Click: Toque para...")
        coord = target

    pg.moveTo(coord)
    time.sleep(1)   
    pg.click()
    return True


def myscreen():
    pg.screenshot(screen_path)
    screen = cv2.imread(screen_path,1)
    return screen


def open_warrios():    
    for i in range(0,5):
        screen = myscreen()
        try:        
            if find_coord_to_click(screen,r"imgs\obj_guerreiro_para_mouse.jpg"):
                return True
            else:
                time.sleep(1)
                screen = myscreen()
                click(screen,"button_seta")
                continue
        except:
            time.sleep(5)
            print("  Trying open...")
            continue
     


def looking(target, t = .25):     
    for i in range(8):
        time.sleep(t)
        if i % 5 == 0:
            print("Loking for: {0} ...".format(target))       		
        
        screen = myscreen()
        obj = find_coord_to_click(screen, r"imgs\{0}.jpg".format(target),.7)        
        if obj:
            click(screen,target)
            return True 
        else:
            continue
    return False
            
    
