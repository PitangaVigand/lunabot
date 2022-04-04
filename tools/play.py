import time

from fight import *
from selection import *
from start import *
from tools import *


def play(range_team: tuple, energy: int) -> bool:
    """
    The complete process of choose a team, select characters, fight,
    desselect characters and start again until all the teams will have played

    """
    print("------{0}-------------------".format(inspect.currentframe().f_code.co_name))

    for team in range(*range_team):
        screen = myscreen()
        time.sleep(1)
        coord = 0

        for i in range(0, 5):
            try:
                mouse_scroll(team)
                screen = myscreen()
                coord = select_characters(team)
                break
            except Exception as e:
                time.sleep(3)
                print(e, "  Trying to select person...")
                continue

        # fight_status = fight(energy)

        # if not fight_status:
        #     print("No fight in play!")
        #     time.sleep(3)
        #     return False

        screen = myscreen()
        mouse_scroll(team)
        deselect_characters(coord, team)
        time.sleep(1)

    print(
        "------Finish {0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )
    time.sleep(1)
    return True


def complete_play(energy: int) -> None:
    """
    The whole process of:
        .open lunarush website,
        .start game,
        .play all teams,
        .Storage screenshot amount of coins
    """

    start_try = start()
    if start_try:
        # try make the cycle 3 times
        for i in range(0, 3):
            boss = select_boss()
            if boss:
                play_turn = play((3, 5), energy)
                time.sleep(1)
                if play_turn:
                    screen_log()
                    looking("button_back")
                    start_try = None
                    break
    print("------------Finish!-------------------")
