import time
from tools import *
import pyautogui as pg
import cv2 as cv2
import pyautogui as pg
import inspect


def select_person(screen, turn):
    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )
    # time.sleep(1)
    first = 0 + 3 * turn
    last = first + 3
    time_coords = []
    for i in range(first, last):
        time.sleep(2.5)
        # print(coord)
        coord = find_coord_to_click("imgs\caracters\{0}.jpg".format(i))
        pg.moveTo(coord)
        print("Select: {0}".format(i))
        pg.click()
        time_coords.append(coord)
        # check is person was selected
        # if not seta:
        # back to loop

    time.sleep(1)

    return time_coords


def deselect_person(time_coords):
    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )
    time.sleep(1)
    for i, coord in enumerate(time_coords):
        try:
            time.sleep(2.5)
            pg.moveTo(coord)
            print("Deselect: {0}".format(i))
            pg.click()

        except Exception as e:
            print(e)
            time.sleep(3)  # try


def select_boss(screen):
    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )
    time.sleep(1)
    part = cv2.imread(r"imgs\banner_boss.jpg", 1)
    result = cv2.matchTemplate(screen, part, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    img_w, img_h = part.shape[1], part.shape[0]

    if max_val > 0.25:
        looking("banner_boss")

    time.sleep(3)
    if open_warrios():
        return True
    return False
