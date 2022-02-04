import random
import time

import keyboard
import pyautogui
import win32api
import win32con
from pyautogui import *


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the   script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):

    if pyautogui.pixel(323, 580)[0] == 0:
        click(311, 580)
    if pyautogui.pixel(411, 580)[0] == 0:
        click(411, 580)
    if pyautogui.pixel(482, 580)[0] == 0:
        click(482, 580)
    if pyautogui.pixel(574, 580)[0] == 0:
        click(574, 580)
