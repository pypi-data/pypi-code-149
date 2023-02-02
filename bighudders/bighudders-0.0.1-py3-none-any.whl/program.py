from tkinter import *
from PIL import ImageTk,Image
import os
my_directory=os.path.dirname(__file__)+"\\mylespic.jpg"

root = Tk()
my_img = ImageTk.PhotoImage(file=my_directory)
imageLabel = Label(root, image=my_img)
imageLabel.pack()

root.mainloop()