from tkinter import *
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
 time.sleep(0.01)
 win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# window setup
window = Tk()
window.geometry('500x500')

# canvas
canvas = Canvas(window, width=500, height=500, bg='green')
canvas.pack()

square = canvas.create_rectangle(5, 5, 30, 30, fill='grey', width = 0)

def left(event):
 x = -10
 y = 0
 canvas.move(square, x, y)

def right(event):
 x = 10
 y = 0
 canvas.move(square, x, y)

def up(event):
 x = 0
 y = -10
 canvas.move(square, x, y)

def down(event):
 x = 0
 y = 10
 canvas.move(square, x, y)


window.bind("a", left)
window.bind("d", right)
window.bind("w", up)
window.bind("s", down)
 
window.mainloop()