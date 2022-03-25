# from curses import window

import os
import time

import cv2 as cv
import numpy as np
import pyautogui as pg
import win32con
import win32gui
import win32ui
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# def window_capture():
#     hwnd = win32gui.FindWindow(None, windowname)

# https://learncodebygaming.com/blog/fast-window-capture


luna = "LunaRush - Google Chrome"
test = "Slack"


def get_window_app(windowname):
    # define your monitor width and height
    w, h = int(2056 / 2), 1980

    # for now we will set hwnd to None to capture the primary monitor
    hwnd = win32gui.FindWindow(None, windowname)
    hwnd = None

    # get the window image data
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

    # save the image as a bitmap file
    # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

    # convert the raw data into a format opencv can read
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype="uint8")
    img.shape = (h, w, 4)

    # free resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    # make image C_CONTIGUOUS to avoid errors with cv.rectangle()
    img = np.ascontiguousarray(img)

    return img


def get_window(windowname):
    # define your monitor width and height
    hwnd_target = 0x1107F4

    left, top, right, bot = win32gui.GetWindowRect(hwnd_target)
    w = right - left
    h = bot - top

    win32gui.SetForegroundWindow(hwnd_target)

    # for now we will set hwnd to None to capture the primary monitor
    hwnd = win32gui.FindWindow(None, windowname)
    hwnd = None

    # get the window image data
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

    # save the image as a bitmap file
    # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

    # convert the raw data into a format opencv can read
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype="uint8")
    img.shape = (h, w, 4)

    # free resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    # make image C_CONTIGUOUS to avoid errors with cv.rectangle()
    img = np.ascontiguousarray(img)

    return img


def get_window_chrome():
    hwnd_target = 0xA0778

    left, top, right, bot = win32gui.GetWindowRect(hwnd_target)
    w = right - left
    h = bot - top

    win32gui.SetForegroundWindow(hwnd_target)

    hdesktop = win32gui.GetDesktopWindow()
    hwndDC = win32gui.GetWindowDC(hdesktop)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = saveDC.BitBlt((0, 0), (w, h), mfcDC, (left, top), win32con.SRCCOPY)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        "RGB", (bmpinfo["bmWidth"], bmpinfo["bmHeight"]), bmpstr, "raw", "BGRX", 0, 1
    )

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hdesktop, hwndDC)

    return im
    # if result == None:
    #     #PrintWindow Succeeded
    #     im.save("test.png")


def capture_opencv():
    while True:
        loop = time()
        screenshot = np.array(pg.screenshot())
        # screenshot = screenshot[:,:,::-1].copy() #fix color problem
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        cv.imshow("Vision", screenshot)
        print("FPS: {}".format(1 / (time() - loop)))
        if cv.waitKey(1) == ord("q"):
            cv.destroyAllWindows()
            break
    print("Done")


def capture_win_api():
    while True:
        loop = time.time()
        screenshot = np.array(get_window_chrome())
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        cv.imshow("Vision", screenshot)
        print("FPS: {}".format(1 / (time.time() - loop)))
        if cv.waitKey(1) == ord("q"):
            cv.destroyAllWindows()
            break
    print("Done")


capture_win_api()
