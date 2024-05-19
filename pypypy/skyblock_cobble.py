import pyautogui
import time
import keyboard
import numpy as np
import random
import win32.lib.win32con as win32con
from win32 import win32api

def wait(x):
 time.sleep(x)

def click (x, y) :
 win32api.SetCursorPos((x,y))
 win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
 time.sleep(0.01)
 win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

wait(5)

pyautogui.mouseDown()
pyautogui.keyDown('w')

while not keyboard.is_pressed('e'):
   wait(0.2)

pyautogui.keyUp('w')
pyautogui.mouseUp()
