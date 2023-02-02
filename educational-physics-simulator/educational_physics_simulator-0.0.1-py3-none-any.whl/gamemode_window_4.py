#gamemode list window
from tkinter import *
from turtle import fillcolor
from tkinter import messagebox

top = Toplevel()
top.geometry("500x800+350+0")
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

#maybe i could have easy, medium, hard mode for each subset of questions
"""
Options=["Gravity", "Planets", "Galton Board"]
clicked1 = StringVar()
clicked1.set(Options[0]) #Sets the default value from the first value in the Options list
LearningMenu = OptionMenu(top, clicked1, *Options) #Creates the menu
LearningMenu.place(x=10, y=300)
LearningMenu.config(bg = "red")
LearningMenu["menu"].config(bg="green")
"""




LearnQuestion = Label(top, text="What would you like to learn?", font="bankgothic 12 underline").place(x=10,y=60)
#Description
#Planets
planetsHeading = Label(top,text="Planets", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=100)
planetsDescription = Label(top,text="- Learn about the motion of the celestial bodies in our Solar System", font="Helvetica 11").place(x=40, y=135)
planetsDescription = Label(top,text="- See how distance from the Sun affects the speed of a planet", font = "Helvetica 11").place(x=40, y=160)
planetsLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = planet_simulation).place(x=60,y=190)
planetsQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=planet_questions).place(x=130,y=190)
#Gravity
gravityHeading = Label(top,text="Gravity", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=240)

def destroy():
    top.destroy()
KillButton = Button(top, text="Kill", command = destroy, width=40, bg="red", fg="blue").place(x=100,y=490)

top.mainloop()

#maybe insert images in places to make it cooler