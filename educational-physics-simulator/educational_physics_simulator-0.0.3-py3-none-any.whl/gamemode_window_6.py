#gamemode list window
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os
my_directory=os.path.dirname(__file__)+"\pictures"
print(my_directory)
top = Toplevel()
top.geometry("800x550+250+0")
global BG
BG = "#303030"
top.config(bg=BG)
global TitleLabel
global LearningMenu
TitleLabel = Label(top, text="Educational physics simulator", fg='red', font=("Helvetica 18 underline italic"))
TitleLabel.pack()

#functions
def planet_simulation():
    import gamemodes.planet_simulation

def planet_questions():
    import gamemodes.planet_questions

def gravity_simulation():
    import gamemodes.gravity_window_2

def gravity_questions():
    import gamemodes.gravity_questions

def galton_window():
    import gamemodes.galton_window

def galton_questions():
    import gamemodes.galton_questions

LearnQuestion = Label(top, text="What would you like to learn?", font="bankgothic 15 underline", bg=BG, fg="white").place(x=10,y=60)
#Separators/Borders
LineSeparator = "---------------"
LineSeparatorLabel1 = Label(top, text=LineSeparator*20, font="Cornerstone 13", bg=BG).place(x=-10,y=220)
LineSeparatorLabel2 = Label(top, text=LineSeparator*20, font="Cornerstone 13", bg=BG).place(x=-10,y=395)


#Description
#Planets
planetsHeading = Label(top,text="Planets", font="Cornerstone 15 underline", width=7, bg="black",fg="aqua").place(x=40,y=100)
planetsDescription = Label(top,text="- Learn about the motion of the celestial bodies in our Solar System", font="Helvetica 11", bg=BG, fg="white").place(x=40, y=135)
planetsDescription = Label(top,text="- See how distance from the Sun affects the speed of a planet", font = "Helvetica 11", bg=BG, fg="white").place(x=40, y=160)
planetsLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = planet_simulation).place(x=60,y=190)
planetsQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=planet_questions).place(x=130,y=190)
planet_img = ImageTk.PhotoImage(file=my_directory+"\solar_system_2.jpg")
planetLabel = Label(top, image=planet_img)
planetLabel.place(x=500,y=80)
#Gravity
gravityHeading = Label(top,text="Gravity", font="Cornerstone 15 underline", width=7, bg="black",fg="aqua").place(x=40,y=250)
gravityDescription1 = Label(top, text="- Learn all about how gravity varies Vertically and Horizontally!", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=285)
gravityDescription2 = Label(top, text="- See how objects act under immense gravitational strength!", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=310)
gravityDescription3 = Label(top, text="- Understand negative values in Coding.", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=335)
gravityLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = gravity_simulation).place(x=60,y=365)
gravityQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=gravity_questions).place(x=130,y=365)
gravity_img = ImageTk.PhotoImage(file=my_directory+"\gravity_2.jpg")
gravityLabel = Label(top, image=gravity_img)
gravityLabel.place(x=500,y=280)
#Galton
galtonHeading = Label(top,text="Galton Board", font="Cornerstone 15 underline", width=12, bg="black",fg="aqua").place(x=40,y=420)
galtonDescription2 = Label(top, text="- Learn about how objects logically and mathematically distribute", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=455)
galtonDescription3 = Label(top, text="- Watch objects fall down like in a PinBall machine!", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=480)
galtonLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = galton_window).place(x=60,y=510)
galtonQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=galton_questions).place(x=130,y=510)
galton_img = ImageTk.PhotoImage(file=my_directory+"\galton_2.png")
galtonLabel = Label(top, image=galton_img)
galtonLabel.place(x=500,y=425)

top.mainloop()