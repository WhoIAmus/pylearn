from tkinter import *
root = Tk()
root.title('Calculator')
root.geometry('500x500')
root.resizable(False,False)
root.config(background='steelblue')

text = Entry(root)

def calc():
    global gettext
    label['text'] = int(eval(gettext))

btn1 = Button(root,text = "calculate",command = calc)

gettext = text.get()

def calc():
    return eval(gettext)

label = Label(root)

btn1.pack(side ="top")
text.pack(side ="top")
label.pack(side = 'bottom')

root.mainloop()