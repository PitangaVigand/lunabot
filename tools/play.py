from msvcrt import locking
import os
import time

from fight import *
from tools import *
from selection import *
from start import *


def play(range_team, energy):
    print("------{0}-------------------".format(inspect.currentframe().f_code.co_name))

    for i in range(0, 3):
        try:
            for team in range(*range_team):
                screen = myscreen()
                time.sleep(1)
                coord = 0

                for i in range(0, 5):
                    try:
                        mouse_scroll(screen, team)
                        screen = myscreen()
                        coord = select_person(screen, team)
                        break
                    except Exception as e:
                        time.sleep(3)  # try
                        print(e, "  Trying to select person...")
                        continue

                fight_status = fight(screen, energy, coord)

                if not fight_status:
                    print("No fight in play!")
                    time.sleep(3)  # try
                    return False

                screen = myscreen()
                mouse_scroll(screen, team)
                deselect_person(coord)
                time.sleep(1)

            print(
                "------Finish {0}-------------------".format(
                    inspect.currentframe().f_code.co_name
                )
            )
            time.sleep(1)
            return True
        except Exception as e:
            time.sleep(3)  # try
            print(e, "  Trying put team to fight....")
            continue


def complete_play():
    for i in range(0, 3):

        # Open to boss
        start_try = start()
        if start:

            # select boss
            for i in range(0, 3):

                screen = myscreen()
                boss = select_boss(screen)
                if boss:

                    #####play####
                    play_turn = play((0, 5), 3)
                    if play_turn:
                        return True
                    else:
                        print("  Trying play....")
                        time.sleep(3)  # try
                        continue
                else:
                    time.sleep(3)  # try
                    print("  Trying pick up boss")
                continue
