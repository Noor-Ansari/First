# First import the libraries/modules that we will use

import tkinter as tk
import numpy as np
from tkinter import END


# Define different functions to perform different task

def press(num):
        current = txt.get()
        txt.delete(0,END)
        txt.insert(0,str(current) + str(num))
    
def button_add():
     global first
     global match
     first = txt.get()
     txt.delete(0,END)
     match = "+"
     

def button_sub():
     global first
     global match
     first = txt.get()
     txt.delete(0,END)
     match = "-"


def button_multi():
     global first
     global match
     first = txt.get()
     txt.delete(0,END)
     match = "*"
     

def button_divide():
     global first
     global match
     first = txt.get()
     txt.delete(0,END)
     match = "/"

def button_equal():
    second = txt.get()
    txt.delete(0, END)
    if match=="+":
        txt.insert(0,int(first)+int(second))
    elif match=="-":
        txt.insert(0,int(first)-int(second))
    elif match=="*":
        txt.insert(0,int(first)*int(second))
    elif match == "/":
        txt.insert(0,int(first)/int(second))

def button_delete():
    txt.delete(0,END)        


def button_clean():
    value = txt.get()
    txt.delete(0,END)
    ind = len(value) - 1
    to_clear = value[ind]
    new = value.rstrip(to_clear)
    txt.insert(0,new)

def button_sqrt():
    value = txt.get()
    txt.delete(0,END)
    new = np.sqrt(int(value))
    txt.insert(0,new)

def button_square():
    value = txt.get()
    txt.delete(0,END)
    new = int(value)*int(value)
    txt.insert(0,new)
    
def button_decimal():
    value = txt.get()
    txt.delete(0,END)
    new = 1/int(value)
    txt.insert(0,new)

# Create the root window for our calculator

window = tk.Tk()
window.title("Calculator")
window.config(bg="sky blue",bd=5)

# Create the entry field 

txt = tk.Entry(window,width=25,borderwidth=5,font=("Arial",15))
txt.grid(row=0,column=0,columnspan=4,ipady=15)


# Create different types of buttons

button_0 = tk.Button(window,text="0",padx=25, pady=20, bg="Sky blue",command = lambda : press(0))
button_0.grid(row=5,column=1)

button_1 = tk.Button(window,text="1",padx=25, pady=20, bg="Sky blue",command = lambda : press(1))
button_1.grid(row=4,column=0)

button_2 = tk.Button(window,text="2",padx=25, pady=20, bg="Sky blue",command = lambda : press(2))
button_2.grid(row=4,column=1)

button_3 = tk.Button(window,text="3",padx=25, pady=20, bg="Sky blue",command = lambda : press(3))
button_3.grid(row=4,column=2)

button_4 = tk.Button(window,text="4",padx=25, pady=20, bg="Sky blue",command = lambda : press(4))
button_4.grid(row=3,column=0)

button_5 = tk.Button(window,text="5",padx=25, pady=20, bg="Sky blue",command = lambda : press(5))
button_5.grid(row=3,column=1)

button_6 = tk.Button(window,text="6",padx=25, pady=20, bg="Sky blue",command = lambda : press(6))
button_6.grid(row=3,column=2)

button_7 = tk.Button(window,text="7",padx=25, pady=20, bg="Sky blue",command = lambda : press(7))
button_7.grid(row=2,column=0)

button_8 = tk.Button(window,text="8",padx=25, pady=20, bg="Sky blue",command = lambda : press(8))
button_8.grid(row=2,column=1)

button_9 = tk.Button(window,text="9",padx=25, pady=20, bg="Sky blue",command = lambda : press(9))
button_9.grid(row=2,column=2)

button_add = tk.Button(window,text="+",padx=22, pady=20, bg="Sky blue",command = button_add)
button_add.grid(row=4,column=3)

button_sub = tk.Button(window,text="-",padx=25, pady=20, bg="Sky blue", command = button_sub)
button_sub.grid(row=3,column=3)

button_multi = tk.Button(window,text="x",padx=25, pady=20, bg="Sky blue", command = button_multi)
button_multi.grid(row=2,column=3)

button_divide = tk.Button(window,text="/",padx=25, pady=20, bg="Sky blue", command = button_divide)
button_divide.grid(row=5,column=2)

button_sqr = tk.Button(window,text="X2",padx=21, pady=20, bg="Sky blue",command = button_square)
button_sqr.grid(row=1,column=1)

button_sqrt = tk.Button(window,text="√ ",padx=22, pady=20, bg="Sky blue",command=button_sqrt)
button_sqrt.grid(row=1,column=3)

button_deci = tk.Button(window,text="1/x",padx=20, pady=20, bg="Sky blue",command = button_decimal)
button_deci.grid(row=1,column=0)

button_clean = tk.Button(window,text="C",padx=23, pady=20, bg="Sky blue", command=button_clean)
button_clean.grid(row=1,column=2)

button_clear = tk.Button(window,text="Delete",padx=15, pady=20, bg="Sky blue",command=button_delete)
button_clear.grid(row=5,column=0)

button_equal = tk.Button(window,text="=",padx=22, pady=20, bg="Green",command = button_equal)
button_equal.grid(row=5,column=3)

# Don't forget this line

window.mainloop()