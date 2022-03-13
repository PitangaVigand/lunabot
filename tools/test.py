
import time
from datetime import *
from turtle import screensize
from tools import *
from selection import *
from tools import find_coord_to_click, looking, myscreen


def check_selectect():
    print("--------------------{0}-------------------".format(inspect.currentframe().f_code.co_name))	
    find = find_coord_to_click(1,r"imgs\ref_deselect.jpg",.7)
    if find:
        looking("ref_deselect")
        time.sleep(2)
        check_selectect()
    else:
        print("----Nothing deselected!")
        return False
        
     
    

check_selectect()
#looking("button_voltar")
def energy_count():

    for status in range(0,4):
        img = r"imgs\energy_{0}.jpg".format(status)


    screen = myscreen()
    coord = [int(x) for x in find_coord_to_click(screen,r"imgs\obj_coin.jpg")]
    cropped_image = screen[coord[1]-15:coord[1]+15, coord[0]:coord[0]+100]
    