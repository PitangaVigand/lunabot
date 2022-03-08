from tkinter import Button
from tkinter.tix import Select
import webbrowser
import pyautogui as pg
from tools.tools import *
from tools.selection import *
import time



def  open_link(link):
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
	webbrowser.open_new(link)

def start():	
    #open chrome on luna link
    #open_link(link)
	open_link("https://lunarush.io/")
	looking("button_play_now") 

    #login
	for i in range(25):	
		print(i)		
		time.sleep(1)
		screen = myscreen()
		if find_coord_to_click(screen, r"imgs\button_entrar_com_meta.jpg"):
			click(screen,"button_entrar_com_meta")
			break

		looking("button_entrar_com_meta")
		looking("button_assinar")
		over = looking("banner_cacar_chefe")
		time.sleep(1)
		if over == True:
    			break


