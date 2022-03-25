import time
import webbrowser

from selection import *
from tools import *


def open_link(link: str) -> None:
    """Utility function to open chrome browser on specific link"""

    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(
            "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
        ),
    )
    webbrowser.open_new(link)
    return None


def start():
    """Open browser, check metamask login
    and select type of game"""

    if coords_of_target("banner_boss"):
        return True

    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )

    if not coords_of_target("button_play_now"):
        open_link("https://lunarush.io/")

    over = False
    while True:
        time.sleep(2)
        login_wallet()
        play = looking("button_play_now")
        time.sleep(1)
        if not play:
            time.sleep(2)
            start()

        time.sleep(3)
        try_run = 5
        while True:
            if coords_of_target("screen_loading_1", 0.9) or coords_of_target(
                "\screen_loading_2", 0.9
            ):
                print("Loading...")
                time.sleep(try_run)
                continue
            else:
                break

        for i in range(0, try_run):
            meta = looking("button_login_with_metamask")
            if meta:
                for i in range(0, try_run):
                    assinar = looking("button_assinar")
                    time.sleep(2)
                    if assinar:
                        for i in range(0, try_run):
                            over = looking("banner_boss_hunt")
                            time.sleep(1)
                            if over == True:
                                return True
                time.sleep(try_run)

            else:
                time.sleep(try_run)
                continue
