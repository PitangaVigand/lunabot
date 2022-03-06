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
	time.sleep(5) 
	  		
  	#press play button
	screen = myscreen()
	click("button_play_now")

    #login e senha
	for i in range(25):	
		print(i)		
		time.sleep(1)
		screen = myscreen()
		if find_coord_to_click(screen, r"imgs\button_entrar_com_meta.jpg"):
			click("button_entrar_com_meta")
			break
	
	#caçar_chefe_bunner
	select_boss()
	play = True
	return play
# pg.moveTo(button)
# time.sleep(1)
# print("Click:Play")
# pg.click() 
