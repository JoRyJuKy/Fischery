import win32con, win32api
from time import sleep
import pyautogui

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

def move(x, y, relative=False):
    x, y = int(x), int(y)
    if relative:
        x, y = [d + p for d, p in zip(win32api.GetCursorPos(), (x, y))]
    for dx in [x-1, x]: 
        win32api.mouse_event(
            win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE,
            int(dx/SCREEN_WIDTH*65535.0),
            int(y/SCREEN_HEIGHT*65535.0),
        )
def down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
def up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
def click():
    down()
    sleep(0.01)
    up()