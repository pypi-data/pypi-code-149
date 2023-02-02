#This program is to add labels to the window
from tkinter import *
root = Tk()

def click():
    myLabel = Label(root, text="Look")
    myLabel.pack()

myButton = Button(root, text="Click me!", command = click)
myButton.pack()
root.mainloop()
