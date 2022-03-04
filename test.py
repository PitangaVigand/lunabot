import cv2 as cv2
import pyautogui as pg


screen_path = "imgs\screen.jpg"
pg.screenshot(screen_path)
screen = cv2.imread(screen_path,1)
def find_coord_to_click(img_all, img_part):            
    part= cv2.imread(img_part,1)      
    result = cv2.matchTemplate(img_all, part, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    img_w,img_h = part.shape[1], part.shape[0] 
    if max_val < .85 :
        return False

    return max_loc[0]+ img_w/2, max_loc[1]+img_h/2 
coord = find_coord_to_click(screen, r"imgs\obj_guerreiro_para_mouse.jpg" )
pg.moveTo(coord)
print(coord)