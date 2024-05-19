from pyautogui import *
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
 time.sleep(0.1)
 win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

wait(3)

while keyboard.is_pressed("q") == False:
 click(719,845) #click on bridge
 wait(0.5)
 click(700,221) #click on fireball
 wait(9)
 click(700,221) #click on fireball
 wait(6)
 click(966,190) #exit from quest
 wait(0.5)