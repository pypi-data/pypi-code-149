#This program is to add labels to the window
from pickle import APPEND
from tkinter import *
from turtle import fillcolor
from tkinter import messagebox
import pygame
pygame.init()
#import math
root = Tk()
root.geometry("400x300+400+0")
root.title("Ed's Physics Simulator")

#Functions to get input values
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

#SaveButton = Button(root, text="Save", command = Save, width=5, bg="aqua").place(x=10, y=220)

def get_username():
    Profile = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "r")
    Username = Profile.readline()
    Profile.close()
    Username=Username.strip()
    return Username

def get_yeargroup():
    Profile = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "r")
    Profile.readline()
    YearGroup = Profile.readline()
    Profile.close()
    return YearGroup[5:] #Gets the number in "Year 12" for example. 

def get_codeskills():
    Profile = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "r")
    Profile.readline()
    Profile.readline()
    CodeSkills = Profile.readline()
    Profile.close()
    return CodeSkills.strip()

def check_inputs(): #Returns True the username has been entered. False if they have not.
    if Username == "No Name":
        return False
    else:
        return True

def get_avgscore():
    AverageScore = "N / A"
    return AverageScore

def planet_simulation():
    import gamemodes.planet_simulation

def planet_questions():
    import gamemodes.planet_questions

#Reads the values already in the file
PresetValue = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "r")
PresetUsername = (PresetValue.readline()).strip()
PresetYearGroup = (PresetValue.readline()).strip()
PresetKnowledge = (PresetValue.readline()).strip()
PresetValue.close()
###################################################################################################################
TitleLabel = Label(root, text="Ed's physics simulator", fg='red', font=("Helvetica 20 underline"))
TitleLabel.pack()

SubHeading = Label(root, text="Where you can learn Coding + Physics", fg="blue", font=("Courier 11")).place(x=40,y=44)

#Profile section
ProfileText = Label(root, text="Profile", font=("bankgothic 12 underline"))
ProfileText.place(x=10, y=70)
UsernameLabel = Label(root, text="Username:").place(x=10, y=97)
UsernameEntry = Entry(root, text="Username")
UsernameEntry.place(x=75,y=100)
YearGroupLabel = Label(root, text = "Year Group:").place(x=10, y=130)
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
drop.place(x=80, y=125)

LevelLabel = Label(root, text="Coding knowledge:").place(x=10, y=177)
LevelSlider = Scale(root, from_=1, to=10, orient=HORIZONTAL, length = 155) #you can add on the end , command = blah
LevelSlider.place(x=130.5, y=160)
LevelSlider.set(PresetKnowledge)
LevelText = Label(root, text="1 = None    10 = Very skilled").place(x=130, y=200)

def Run():
    Save()
    if check_inputs() == False:
        message = "Please enter a username"
        messagebox.showerror("Profile issue", message)
        #Label(root, text=response).pack() 

    else:
        Gamemode_window()

StartLearning = Button(root, text="Start Learning -->", command=Run, bg="lime", padx=1, pady=1, bd=10).place(x=130, y=250)

###########################################################################################################################

def Gamemode_window():
    top = Toplevel()
    top.geometry("500x500+350+0")
    global TitleLabel
    global LearningMenu
    global GravityHeading
    TitleLabel = Label(top, text="Ed's physics simulator", fg='red', font=("Helvetica 18 underline"))
    TitleLabel.pack()

    """
    Options=["Gravity", "Planets", "Galton Board"]
    clicked1 = StringVar()
    clicked1.set(Options[0]) #Sets the default value from the first value in the Options list
    LearningMenu = OptionMenu(top, clicked1, *Options) #Creates the menu
    LearningMenu.place(x=10, y=300)
    LearningMenu.config(bg = "red")
    LearningMenu["menu"].config(bg="green")
    """
    #maybe i could have easy, medium, hard mode for each subset of questions
    Username = get_username()
    YearGroup = get_yeargroup()
    CodingSkills = get_codeskills()
    HelloLabel = Label(top, text="Hello " + Username + ",", font = "Cornerstone 15",fg = "Blue").place(x=10,y=42)
    YearGroupDisplay = Label(top, text="Year Group: " + YearGroup, font = "Cornerstone 11" ).place(x=10,y=80) 
    CodingSkillsLabel = Label(top, text="Coding knowledge: " + CodingSkills + "/10", font="Cornerstone 11").place(x=10, y=100)
    AvgScoreLabel = Label(top, text="Average Score: " + get_avgscore(), font = "Cornerstone 11").place(x=10,y=120)
    LineSeparatorMsg = "-------------------------------------------------------"
    LineSeparator = Label(top, text=LineSeparatorMsg*5, font = "Cornerstone 11").place(x=-10, y=145)
    LearnQuestion = Label(top, text="What would you like to learn?", font="bankgothic 12 underline").place(x=10,y=170)
    #Description
    #Planets
    planetsHeading = Label(top,text="Planets", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=205)
    planetsDescription = Label(top,text="- Learn about the motion of the celestial bodies in our Solar System", font="Helvetica 11").place(x=40, y=240)
    planetsDescription = Label(top,text="- See how distance from the Sun affects the speed of a planet", font = "Helvetica 11").place(x=40, y=260)
    planetsLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = planet_simulation).place(x=60,y=290)
    planetsQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=planet_questions).place(x=130,y=290)
    #Gravity
    gravityHeading = Label(top,text="Gravity", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=340)

    def destroy():
        root.destroy()
        top.destroy()
    KillButton = Button(top, text="Kill", command = destroy, width=40, bg="red", fg="blue").place(x=100,y=450)

#Learning section
root.mainloop()




