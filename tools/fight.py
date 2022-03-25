import time
from xmlrpc.client import Boolean

import pyautogui as pg

from selection import *
from tools import *


def fight(energy: int) -> bool:
    """Tap boss-hunt Button, wait until fight is
    over and back to selection warrior screen

    energy: Integer between 1-3;The amount of energy the team will play.

    """

    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )
    time.sleep(1)

    # fight "energy" times with the same team
    for i in range(0, energy):
        looking("button_boss_hunt")
        print("----Starting energy:  {0}".format(i + 1))

        # cheking screen for 45 secs
        result = None
        for j in range(90):  # range try screen:
            time.sleep(0.5)
            boss_hunt = coords_of_target("button_boss_hunt")
            banner_boss = coords_of_target("banner_boss")
            derrota = coords_of_target("banner_defeat")
            vitoria = coords_of_target("banner_vitoria")
            tap_to_watch = coords_of_target("button_tap_to_watch", threshold=0.6)

            # finish fight triggers
            try:
                if tap_to_watch:
                    looking("button_tap_to_watch", threshold=0.6)

                if derrota:
                    print("Defeat!")
                    time.sleep(2)
                    looking("button_tap_to_continue", threshold=0.6)
                    result = True

                if vitoria:
                    print("Victory")
                    time.sleep(1.5)
                    looking("button_tap_to_open")
                    time.sleep(2)
                    looking("button_tap_to_continue", threshold=0.6)
                    result = True

                if boss_hunt and result:
                    break

                if banner_boss and result:
                    boss = select_boss()
                    if boss:
                        break

            except Exception as e:
                print(e)

        print("---Finishing: energy {0}".format(i + 1))
    return True


def old_fight():
    """Deprecated"""
    time.sleep(2)
    button = coords_of_target("button_boss_hunt")

    # play 3 times
    for i in range(0, 3):
        # hunt
        print("Click:1")
        pg.moveTo(button)
        pg.click()
        time.sleep(3)  # try

        # move to midle
        print("Click:2")
        pg.moveTo(button[0] - 350, button[1])
        pg.click()

        # clik in the midle
        for i in range(45):  # range try screen:
            time.sleep(1)
            pg.click()

    return True
