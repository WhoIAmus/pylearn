from tkinter import *
import random
import easygui
tk = Tk()
canvas = Canvas(tk, width=100, height=100)
canvas.pack()
kolory=["black","red","blue","green","pink","yellow"]

game=True
while game:
    k=random.choice(kolory)
    b=random.choice(kolory)
    
    canvas.delete("all")
    canvas.create_text(50,50,text=b,fill=k,font="Times 25")
    
    user = easygui.buttonbox("Який колір тексту?", choices = kolory )
    
    if user != k:
        game = False

easygui.msgbox("GAME OVER!")