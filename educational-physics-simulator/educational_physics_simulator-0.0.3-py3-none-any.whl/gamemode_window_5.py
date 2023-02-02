#gamemode list window
from tkinter import *
from turtle import fillcolor
from tkinter import messagebox

top = Toplevel()
top.geometry("500x600+350+0")
global BG
BG = "#303030"
top.config(bg=BG)
global TitleLabel
global LearningMenu
TitleLabel = Label(top, text="Ed's physics simulator", fg='red', font=("Helvetica 18 underline italic"))
TitleLabel.pack()

#functions
def planet_simulation():
    messagebox.showinfo("Planet Simulation", "Remember to look at the motion and distance!")
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
#Description
#Planets
planetsHeading = Label(top,text="Planets", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=100)
planetsDescription = Label(top,text="- Learn about the motion of the celestial bodies in our Solar System", font="Helvetica 11", bg=BG, fg="white").place(x=40, y=135)
planetsDescription = Label(top,text="- See how distance from the Sun affects the speed of a planet", font = "Helvetica 11", bg=BG, fg="white").place(x=40, y=160)
planetsLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = planet_simulation).place(x=60,y=190)
planetsQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=planet_questions).place(x=130,y=190)
#Gravity
gravityHeading = Label(top,text="Gravity", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=240)
gravityDescription1 = Label(top, text="- Learn all about how gravity varies Vertically and Horizontally!", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=275)
gravityDescription2 = Label(top, text="- See how objects act under immense gravitational srength!", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=300)
gravityDescription3 = Label(top, text="- Understand negative values in Coding.", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=325)
gravityLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = gravity_simulation).place(x=60,y=355)
gravityQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=gravity_questions).place(x=130,y=355)

galtonHeading = Label(top,text="Galton Board", font="Gothic 15 underline", width=13, bg="black",fg="aqua").place(x=40,y=400)
galtonDescription1 = Label(top, text="Learn about how objects logically and mathematically distribute")
galtonDescription2 = Label(top, text="- Learn all about how galton varies Vertically and Horizontally!", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=435)
galtonDescription3 = Label(top, text="- Watch objects fall down like in a PinBall machine!", font="Cornerstone 11", bg=BG, fg="white").place(x=40,y=460)
galtonLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = galton_window).place(x=60,y=505)
galtonQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=galton_questions).place(x=130,y=505)

top.mainloop()

