from tkinter import *
from math import *

def set_text(text):
    e1.insert(END,text)
    return   
 
def evaluate():
    s = e1.get()
    x = str(eval(s))
    e1.delete(0,END)
    e1.insert(END,x)
    
def fn_c():
    c = e1.get()
    e1.delete(END,0)
    
def fn_ac():
    ac = e1.get()
    e1.delete(0,END)
     
root=Tk()
root.title('Calculator')

e1_var = StringVar()
e1 = Entry(root,textvariable=e1_var)
e1.grid(columnspan = 6)

b1 = Button(root,text = '7',height=2,width=4,command = lambda: set_text("7"))
b1.grid(row=1,column=0)
b2 = Button(root,text = '8',height=2,width=4,command = lambda: set_text("8"))
b2.grid(row=1,column=1)
b3 = Button(root,text = '9',height=2,width=4,command = lambda: set_text("9"))
b3.grid(row=1,column=2)
b4 = Button(root,text = '/',height=2,width=4,command = lambda: set_text("/"))
b4.grid(row=1,column=3)
b5 = Button(root,text = 'AC',height=2,width=4,command = fn_ac)
b5.grid(row=1,column=4)
b6 = Button(root,text = 'C',height=2,width=4,command = fn_c)
b6.grid(row=1,column=5)
b7 = Button(root,text = '4',height=2,width=4,command = lambda: set_text("4"))
b7.grid(row=2,column=0)
b8 = Button(root,text = '5',height=2,width=4,command = lambda: set_text("5"))
b8.grid(row=2,column=1)
b9 = Button(root,text = '6',height=2,width=4,command = lambda: set_text("6"))
b9.grid(row=2,column=2)
b10 = Button(root,text = 'x',height=2,width=4,command = lambda: set_text("*"))
b10.grid(row=2,column=3)
b11 = Button(root,text = '(',height=2,width=4,command = lambda: set_text("("))
b11.grid(row=2,column=4)
b12 = Button(root,text = ')',height=2,width=4,command = lambda: set_text(")"))
b12.grid(row=2,column=5)
b13 = Button(root,text = '1',height=2,width=4,command = lambda: set_text("1"))
b13.grid(row=3,column=0)
b14 = Button(root,text = '2',height=2,width=4,command = lambda: set_text("2"))
b14.grid(row=3,column=1)
b15 = Button(root,text = '3',height=2,width=4,command = lambda: set_text("3"))
b15.grid(row=3,column=2)
b16 = Button(root,text = '-',height=2,width=4,command = lambda: set_text("-"))
b16.grid(row=3,column=3)
b17 = Button(root,text = 'rt',height=2,width=4,command = lambda: set_text("sqrt"))
b17.grid(row=3,column=4)
b18 = Button(root,text = 'x2',height=2,width=4,command = lambda: set_text("^2"))
b18.grid(row=3,column=5)
b19 = Button(root,text = '0',height=2,width=4,command = lambda: set_text("0"))
b19.grid(row=4,column=0)
b20 = Button(root,text = '.',height=2,width=4,command = lambda: set_text("."))
b20.grid(row=4,column=1)
b21 = Button(root,text = '%',height=2,width=4,command = lambda: set_text("%"))
b21.grid(row=4,column=2)
b22 = Button(root,text = '+',height=2,width=4,command = lambda: set_text("+"))
b22.grid(row=4,column=3)
b23 = Button(root,text = '=',height=2,width=10,command = evaluate)
b23.grid(row=4,column =4,columnspan=6)

root.mainloop()
