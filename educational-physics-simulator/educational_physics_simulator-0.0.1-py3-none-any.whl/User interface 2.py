#This program is to add labels to the window
from pickle import APPEND
from tkinter import *
from turtle import fillcolor
import pygame
import math
root = Tk()
root.geometry("400x300+400+0")

#Reads the values already in the file
"""PresetValue = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "r")
PresetUsername = (PresetValue.readline()).strip()
PresetYearGroup = (PresetValue.readline()).strip()
PresetKnowledge = (PresetValue.readline()).strip()
PresetValue.close()"""
PresetUsername = "ExampleUser"
PresetYearGroup="Year 9"
PresetKnowledge=6
TitleLabel =Label(root, text="Ed's physics simulator", fg='red', font=("Helvetica 18 underline"))
TitleLabel.pack()

Label1 = Label(root, text="Profile", font=("bankgothic 12 underline"))
Label1.place(x=10, y=60)

#Profile section
UsernameLabel = Label(root, text="Username:").place(x=10, y=87)
UsernameEntry = Entry(root, text="Username")
UsernameEntry.place(x=75,y=90)
YearGroupLabel = Label(root, text = "Year Group:").place(x=10, y=120)
YearGroups = [ #Written like this as easier to read
    "Year 7",
    "Year 8",
    "Year 9",
    "Year 10",
    "Year 11",
    "Year 12",
    "Year 13",
]

clicked = StringVar()
clicked.set(PresetYearGroup) #Sets the default value from the first value in the Options list
drop = OptionMenu(root, clicked, *YearGroups) #Creates the menu
drop.place(x=80, y=115)

LevelLabel = Label(root, text="Coding knowledge:").place(x=10, y=167)
LevelSlider = Scale(root, from_=1, to=10, orient=HORIZONTAL, length = 145) #you can add on the end , command = blah
LevelSlider.place(x=130.5, y=150)
LevelSlider.set(PresetKnowledge)
LevelText = Label(root, text="1 = None    10 = Very skilled").place(x=130, y=190)

def GetInputs():
    global Username
    global YearGroupValue #global so we can use them in the Save function
    global SliderValue
    Username = str(UsernameEntry.get())
    YearGroupValue = str(clicked.get())
    SliderValue = str(LevelSlider.get())

    if Username.strip() == "":
        Username = "No Name"

def Save():
    GetInputs()
    Profile = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "w")
    Profile.write(Username + "\n")
    Profile.write(YearGroupValue + "\n")
    Profile.write(SliderValue + "\n")
    Profile.close()

SaveButton = Button(root, text="Save", command = Save, width=5, bg="aqua").place(x=10, y=220)

def proifle_window():
    top = Toplevel()
    top.geometry("500x350+350+0")
    #build this after testing

    top.mainloop()
def get_username():
    Profile = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "r")
    Username = Profile.readline()
    Profile.close()
    Username=Username.strip()
    return Username

def get_yeargroup():
    Profile = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "r")
    UselessVariable = Profile.readline()
    YearGroup = Profile.readline()
    Profile.close()
    YearGroup=YearGroup.strip()
    print(YearGroup)
    return YearGroup   

def Gamemode_window():
    top = Toplevel()
    top.geometry("500x500+350+0")
    global TitleLabel
    global LearningMenu
    global GravityHeading
    TitleLabel = Label(top, text="Ed's physics simulator", fg='red', font=("Helvetica 18 underline"))
    TitleLabel.pack()

    LearnQuestion = Label(top, text="What would you like to learn?", font="bankgothic 12 underline").place(x=10,y=200)
    """
    Options=["Gravity", "Planets", "Galton Board"]
    clicked1 = StringVar()
    clicked1.set(Options[0]) #Sets the default value from the first value in the Options list
    LearningMenu = OptionMenu(top, clicked1, *Options) #Creates the menu
    LearningMenu.place(x=10, y=300)
    LearningMenu.config(bg = "red")
    LearningMenu["menu"].config(bg="green")
    """

    def planet_simulation():
        import gamemodes.planet_simulation_planets
    Username = get_username()
    YearGroup = get_yeargroup()
    HelloLabel = Label(top, text="Hello " + Username + ",", font = "Cornerstone 15", width=7,fg = "Blue").place(x=10,y=42)
    YearGroupDisplay = Label(top, text="Year Group: " + YearGroup, font = "Cornerstone 13" ).place(x=10,y=70) 
    #Description
    #Planets
    planetsHeading = Label(top,text="Planets", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=120)
    planetsDescription = Label(top,text="- Learn about the motion of the celestial bodies in our Solar System", font="Helvetica 11").place(x=40, y=155)
    planetsDescription = Label(top,text="- See how distance from the Sun affects the speed of a planet", font = "Helvetica 11").place(x=40, y=180)
    planetsLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = planet_simulation).place(x=60,y=210)

    #Gravity
    gravityHeading = Label(top,text="Gravity", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=265)






#Learning section
StartLearning = Button(root, text="Start Learning -->", command=Gamemode_window, bg="lime", padx=1, pady=1, bd=10).place(x=130, y=240)
root.mainloop()
