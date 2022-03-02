from turtle import screensize
import cv2
import numpy as np
import pyautogui as pg
import time

scream_path = "imgs\scream.jpg"
#scream = pg.screenshot(scream_path)
tela = cv2.imread(scream_path,1)
to_find = cv2.imread(r"imgs\b_cacar_chefe.jpg", 1)
img_w,img_h = to_find.shape[1], to_find.shape[0]


result = cv2.matchTemplate(tela, to_find, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right =  (top_left[0]+ img_w, top_left[1]+img_h)


cv2.rectangle(tela, top_left, bottom_right,color=(0,255,0), thickness=2,lineType=cv2.LINE_4)
cv2.imshow('result', tela)
cv2.waitKey()


# pg.click((max_loc[0]+50, max_loc[1]+50))
# pg.click()
# time.sleep(10)
# pg.click()
# pg.screenshot("imgs/teste")