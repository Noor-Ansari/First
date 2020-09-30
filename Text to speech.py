
# First import libraries/modules that we will use

from tkinter import StringVar
import tkinter as tk
import pyttsx3


# Define the function that will convert the text into specch 
# If no text would be there it will ask for text

def func():
    txt = field.get()
    if txt == "":
        engine = pyttsx3.init()
        engine.setProperty("rate",125)
        engine.say("Please enter some text")
        engine.runAndWait()
    else:
        engine = pyttsx3.init()
        engine.setProperty("rate",125)
        engine.say(txt)
        engine.runAndWait()
  
# Define the function to reset the entered text

def reset():
    msg.set("")

# Define the function to exit the program

def exit():
    root.destroy()

# Create the root of our GUI and set some other properties

root = tk.Tk()
root.geometry("360x300")
root.title("Text to speech")
root.config(bg= "sky blue")


# Create a label for the heading

title = tk.Label(root, text = "Text to speech converter")
title.config(bg="sky blue", font="Arial, 20")
title.grid(row=0,column = 0, columnspan = 4,padx=15, pady=5)

# Create another label 

label1 = tk.Label(root, text = "Enter your message :")
label1.config(bg="sky blue",font="Arial, 12")
label1.grid(row =1, column=0)

# Create the entry field to take input from user

msg = StringVar()
field = tk.Entry(root, textvariable = msg)
field.config(font="20")
field.grid(row=1,column=1, columnspan=3, pady=20, ipady=10)

# Create the reset button

Reset = tk.Button(root, text = "Reset",command=reset)
Reset.config(font=10)
Reset.grid(row=3,column=1)

# Create the button that will convert text into speech

play = tk.Button(root, text = "Convert", command = func)
play.config(font = 10)
play.grid(row=3,column=2)

# Create the exit button

Exit = tk.Button(root, text = "Exit",command=exit)
Exit.config(font=10)
Exit.grid(row=3,column=3)

# Don't forget to miss this line 

root.mainloop()