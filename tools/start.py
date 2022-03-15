from tkinter import Button
from tkinter.tix import Select
from turtle import Screen
import webbrowser
import pyautogui as pg
from tools import *
from selection import *
import time


def open_link(link):
    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(
            "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
        ),
    )
    webbrowser.open_new(link)


def start():
    if find_coord_to_click(screen, r"imgs\banner_boss.jpg"):

        return True

    print(
        "--------------------{0}-------------------".format(
            inspect.currentframe().f_code.co_name
        )
    )
    # open chrome on luna link
    # open_link(link)
    open_link("https://lunarush.io/")

    # enter
    over = False
    while True:
        time.sleep(2)
        play = looking("button_play_now")

        time.sleep(1)
        if not play:

            time.sleep(2)
            start()

        try_run = 5
        while True:
            if find_coord_to_click(
                screen, r"imgs\screen_loading_1.jpg", 0.9
            ) or find_coord_to_click(screen, r"imgs\screen_loading_2.jpg", 0.9):
                print("Loading...")
                time.sleep(try_run)
                continue
            else:
                break

        for i in range(0, try_run):
            meta = looking("button_entrar_com_meta")
            if meta:
                for i in range(0, try_run):
                    assinar = looking("button_assinar")
                    time.sleep(2)
                    if assinar:
                        for i in range(0, try_run):
                            over = looking("banner_cacar_chefe")
                            time.sleep(1)
                            if over == True:
                                return True
                time.sleep(try_run)

            else:
                time.sleep(try_run)


# start()
