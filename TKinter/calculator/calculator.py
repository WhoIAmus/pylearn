from tkinter import *

field_text=""

def add_to_field(x):
    global field_text
    field_text = field_text + str(x)
    field.delete('1.0','end')
    field.insert('1.0',field_text)

def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete('1.0','end')
    field.insert('1.0',result)

def clear():
    global field_text
    field_text = ''
    field.delete('1.0','end')

window = Tk()
window.geometry('300x255')
field = Text(window, height=2, width=21, font=('Times New Roman',20))

field.grid(row=1, column=1, columnspan=4)
# numbers

btn_0 = Button(window,text='0',command= lambda: add_to_field(0),width=5,font=("Times New Roman",14))
btn_0.grid(row=5,column=1)

btn_1 = Button(window,text='1',command= lambda: add_to_field(1),width=5,font=("Times New Roman",14))
btn_1.grid(row=4,column=1)

btn_2 = Button(window,text='2',command= lambda: add_to_field(2),width=5,font=("Times New Roman",14))
btn_2.grid(row=4,column=2)

btn_3 = Button(window,text='3',command= lambda: add_to_field(3),width=5,font=("Times New Roman",14))
btn_3.grid(row=4,column=3)

btn_4 = Button(window,text='4',command= lambda: add_to_field(4),width=5,font=("Times New Roman",14))
btn_4.grid(row=3,column=1)

btn_5 = Button(window,text='5',command= lambda: add_to_field(5),width=5,font=("Times New Roman",14))
btn_5.grid(row=3,column=2)

btn_6 = Button(window,text='6',command= lambda: add_to_field(6),width=5,font=("Times New Roman",14))
btn_6.grid(row=3,column=3)

btn_7 = Button(window,text='7',command= lambda: add_to_field(7),width=5,font=("Times New Roman",14))
btn_7.grid(row=2,column=1)

btn_8 = Button(window,text='8',command= lambda: add_to_field(8),width=5,font=("Times New Roman",14))
btn_8.grid(row=2,column=2)

btn_9 = Button(window,text='9',command= lambda: add_to_field(9),width=5,font=("Times New Roman",14))
btn_9.grid(row=2,column=3)

#operation buttons

btn_equals= Button(window,text='=',command=lambda: calculate(),width=15,font=("Times New Roman",14))
btn_equals.grid(row=6,column=3,columnspan=2)

btn_leftdash= Button(window,text='(',command= lambda: add_to_field('('),width=5,font=("Times New Roman",14))
btn_leftdash.grid(row=6,column=1)

btn_rightdash= Button(window,text=')',command= lambda: add_to_field(')'),width=5,font=("Times New Roman",14))
btn_rightdash.grid(row=6,column=2)

btn_point= Button(window,text='.',command= lambda: add_to_field('.'),width=5,font=("Times New Roman",14))
btn_point.grid(row=5,column=2)

btn_clear= Button(window,text='clear',command= lambda: clear(),width=5,font=("Times New Roman",14))
btn_clear.grid(row=5,column=3)

btn_plus= Button(window,text='+',command= lambda: add_to_field('+'),width=5,font=("Times New Roman",14))
btn_plus.grid(row=4,column=4)

btn_minus= Button(window,text='-',command= lambda: add_to_field('-'),width=5,font=("Times New Roman",14))
btn_minus.grid(row=5,column=4)

btn_multiply= Button(window,text='*',command= lambda: add_to_field('*'),width=5,font=("Times New Roman",14))
btn_multiply.grid(row=2,column=4)

btn_divide= Button(window,text='/',command= lambda: add_to_field('/'),width=5,font=("Times New Roman",14))
btn_divide.grid(row=3,column=4)

window.mainloop()