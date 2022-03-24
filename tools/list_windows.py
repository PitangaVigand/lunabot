import win32gui


def list_windows_names() -> None:
    """
    Search for all opened windowns and print
    the memory code with their respective names

    """

    def winEnumHandler(hwnd, cxt):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))

    win32gui.EnumWindows(winEnumHandler, None)
