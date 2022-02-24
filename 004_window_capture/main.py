#from curses import window
import os

from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as pg
from time import time

import win32gui, win32ui, win32con


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# def window_capture():
#     hwnd = win32gui.FindWindow(None, windowname)

#https://learncodebygaming.com/blog/fast-window-capture




def myscream():
    
    time_loop = time()
    while(True):
        screenshot =  ImageGrab.grab()
        screenshot =  np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        cv.imshow('Computer Vision',screenshot)

        print("FPS: {} ".format(1/(time()-time_loop)))
        time_loop = time()
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break



    print('done')