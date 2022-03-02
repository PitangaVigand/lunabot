import win32gui
def list_windows_names():
    def winEnumHandler(hwnd,cxt):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))

    win32gui.EnumWindows(winEnumHandler,None)

list_windows_names()

name = "LunaRush - Google Chrome"