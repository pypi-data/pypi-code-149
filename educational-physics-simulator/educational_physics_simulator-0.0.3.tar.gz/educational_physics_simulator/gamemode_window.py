#gamemode list window
from tkinter import *
from turtle import fillcolor
from tkinter import messagebox

top = Toplevel()
top.geometry("500x500+350+0")
global TitleLabel
global LearningMenu
TitleLabel = Label(top, text="Ed's physics simulator", fg='red', font=("Helvetica 18 underline"))
TitleLabel.pack()

#functions
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
    top.destroy()
    import gamemodes.planet_questions

#######################################################################################################
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
Username="ExampleUser"
YearGroup="9"
CodingSkills="6"
"""Username = get_username()
YearGroup = get_yeargroup()
CodingSkills = get_codeskills()"""
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
    top.destroy()
KillButton = Button(top, text="Kill", command = destroy, width=40, bg="red", fg="blue").place(x=100,y=450)

top.mainloop()
