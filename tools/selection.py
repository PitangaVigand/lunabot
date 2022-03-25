import inspect
import time

import pyautogui as pg

from tools import *


def select_characters(team: int) -> list:
    """
    Select the 3 characters
    based on team number

    #####Logic of numbers of the teams and characters:######
    The game allow us to fight using tree characters per round. We have 15 characters
    to fight, named of from 0 to 14 regarding the order we prefer
    (search for the best character combination for you)
    team = 0 , will play [0,1,2] caracters
    team = 1 , will play [3,4,5] caracters
    ...and so on.

    """

    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )

    first = 0 + 3 * team
    last = first + 3
    team_coords = []
    for i in range(first, last):
        time.sleep(1)
        coord = coords_of_target("caracters\{0}".format(i), 0.85)
        pg.moveTo(coord)
        print("Select: {0}".format(i))
        pg.click()
        team_coords.append(coord)
        time.sleep(1.5)
    time.sleep(1)

    return team_coords


def deselect_characters(team_coords: list, team: int) -> None:
    """
    Deselect the characters based on a list of coordinates

    team_coords: list of coordinates of each previously selected character
    team: integer between 0-5

    """

    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )
    time.sleep(1)

    for i, coord in enumerate(team_coords):
        try:
            time.sleep(2.5)
            pg.moveTo(coord)
            person = i + 3 * team
            print("Deselect: {0}".format(person))
            pg.click()

        except Exception as e:
            print(e)
            time.sleep(3)  # try


def select_boss() -> bool:
    """
    Select the boss available boss

    """
    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )
    time.sleep(1)

    # screen = myscreen()
    # part = cv2.imread(r"imgs\banner_boss.jpg", 1)
    # result = cv2.matchTemplate(screen, part, cv2.TM_CCOEFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # img_w, img_h = part.shape[1], part.shape[0]

    # # filter results
    # if max_val > 0.25:
    looking("banner_boss")
    time.sleep(3)

    # open the character's area
    if expand_area():
        return True
    return False
