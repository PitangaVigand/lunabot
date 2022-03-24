import os
import subprocess
import time
from datetime import date, datetime

import cv2
import numpy
import pyautogui as pg
from dotenv import load_dotenv

load_dotenv(override=True)
password = os.environ["PASSWORD"]


def coords_of_target(target: str, threshold: float = 0.80) -> tuple:
    """Search for a target image and returns
    the coordinates of the image's center

    target: Name of file
    threshold: float number between 0-1

    """

    img_all = myscreen()
    try:
        part = cv2.imread("imgs\{0}.jpg".format(target), 1)
        result = cv2.matchTemplate(img_all, part, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        img_w, img_h = part.shape[1], part.shape[0]
        if max_val < threshold:
            return False

        return max_loc[0] + img_w / 2, max_loc[1] + img_h / 2
    except:
        print("{} not found".format(target))
        return False


def mouse_scroll(team: int) -> None:
    """Scroll up or down based on
    team: Intiger between 0-5
    """

    # Corretion to scroll in the right place
    coord = coords_of_target("obj_warrior_to_mouse")
    looking("obj_warrior_to_mouse")
    pg.moveTo(coord[0], coord[1] + 200)
    time.sleep(1)

    occulted_team = 3  # The number of occulted team
    if int(team) == occulted_team:
        pg.scroll(-2000)
        pg.scroll(-2000)
        pg.scroll(-2000)

    else:
        pg.scroll(2000)
        pg.scroll(2000)


def screen_log() -> None:
    """Take the screenshot of the current amount of coins"""

    name = "screenshots day/{0}_{1}hs.jpg".format(
        date.today(), datetime.now().strftime("%H")
    )
    screen = myscreen()
    coord = [int(x) for x in coords_of_target("obj_coin")]
    cropped_image = screen[coord[1] - 15 : coord[1] + 15, coord[0] : coord[0] + 100]
    cv2.imwrite(name, cropped_image)


def click(target=None, t: float = 0.5) -> bool:
    """Click on a target. The target can be
    a coordinate or a file name"""
    for i in range(5):
        try:
            if isinstance(target, str):
                coord = coords_of_target(target)
                print("Click: {}".format(target))
            else:
                print("...")
                coord = target

            time.sleep(t)
            pg.moveTo(coord)
            time.sleep(1)
            pg.click()
            return True
        except:
            continue
    return False


def myscreen() -> numpy.ndarray:
    """Takes the screenshot, save and return this file opened"""
    # This logic will be deprecated in the next realease
    screen_path = "imgs\screen.jpg"
    pg.screenshot(screen_path)
    screen = cv2.imread(screen_path, 1)
    return screen


def expand_area() -> None:
    """Try 5 times to click on white arrow to
    increase the characters area"""

    for i in range(5):
        try:
            if coords_of_target("obj_warrior_to_mouse"):
                return True
            else:
                time.sleep(1)
                click("button_arrow")
                continue
        except:
            time.sleep(5)
            print("  Trying open...")
            continue


def looking(target: str, t: float = 0.5, threshold: float = 0.7) -> bool:
    """Search a target image name 10 times
    target: Name of file
    t: Secods between loops

    """

    for i in range(10):
        time.sleep(t)
        obj = coords_of_target(target, threshold)
        if obj:
            click(target)
            return True
        else:
            if i % 3 == 0:
                print("Looking for: {0} ...".format(target))
            continue
    return False


def login_wallet() -> None:
    """Navegate and type the password
    to make a login on the metamask account"""

    time.sleep(1)
    looking("button_metamask", threshold=0.7)
    time.sleep(2)
    if coords_of_target("screen_senha", 0.6):
        looking("screen_senha")
        time.sleep(1)
        pg.typewrite(password)
        time.sleep(1)
        looking("button_desbloquear")
        pg.click(360, 500)
    elif coords_of_target("screen_logged_wallet"):
        print("Already Logged...")
        pg.click(360, 500)


def upload_git(commit_messege: str, file: str) -> bool:
    """
    Push and commit changes to
    repository
    """
    etl_push = [
        "pwd",
        "git checkout main",
        "git add {0}".format(file),  ################################################
        "git commit -m '{0}'".format(commit_messege),
        "git push",
    ]

    for command in etl_push:
        git_cli_etl = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            cwd=".",
        )

        output, errors = git_cli_etl.communicate()
        if errors:
            print(f"command: {command} \noutput: {output} \nERROR: {errors}")
        else:
            print(f"command: {command} \noutput: {output}")
    return True
