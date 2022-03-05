from tkinter import Button
import webbrowser
import pyautogui as pg
from tools import *
import time

def  open_link(link):
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
	webbrowser.open_new(link)

open_link("https://lunarush.io/")
button = find_coord_to_click(screen, r"imgs\button_play_now.jpg")

pg.moveTo(button[0]-350, button[1])
time.sleep(1)
print("Click:Play")
pg.click() 
