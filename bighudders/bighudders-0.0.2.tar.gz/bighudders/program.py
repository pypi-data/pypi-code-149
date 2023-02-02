from tkinter import *
from PIL import ImageTk,Image
import os
my_directory=os.path.dirname(__file__)+"\\pictures\\mylespic.jpg"

img = Image.open(my_directory)
img.show()
