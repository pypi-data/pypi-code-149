#gamemode list window
from tkinter import *
from turtle import fillcolor
from tkinter import messagebox

top = Toplevel()
top.geometry("500x800+350+0")
global TitleLabel
global LearningMenu
TitleLabel = Label(top, text="Educational physics simulator", fg='red', font=("Helvetica 18 underline"))
TitleLabel.pack()
global Username
PassingUsername = open(("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profiles/PassingUsername.txt"),"r")
Username = PassingUsername.readline()
PassingUsername.close()
#functions
def get_yeargroup():
    Profile = open(("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profiles/"+Username+".txt"), "r")
    Profile.readline()
    YearGroup = Profile.readline()
    Profile.close()
    return YearGroup[5:] #Gets the number in "Year 12" for example. 

def get_codeskills():
    Profile = open(("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profiles/"+Username+".txt"), "r")
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

    try:
        PointsRead = open(("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profiles/"+Username+"points.txt"), "r")
    except:
        MakePointsFile = open(("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profiles/"+Username+"points.txt"), "w")
        MakePointsFile.close()
    try:
        PointsRead = open(("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profiles/"+Username+"points.txt"), "r")
        AverageScore = (PointsRead.readline())[0] # gets the first character just in case the user spammed the submit button - we wantt the user to see their success if not then we'd just .distroy() the window
        PointsRead.close()
    except:
        AverageScore = "N / A"
    if AverageScore == "":
        AverageScore = "N / A"
    PointsRead = open(("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profiles/"+Username+"points.txt"), "w")
    PointsRead.write("")
    PointsRead.close()
    return AverageScore

def planet_simulation():
    messagebox.showinfo("Planet Simulation", "Remember to look at the motion and distance!")
    import gamemodes.planet_simulation

def planet_questions():
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
YearGroup = get_yeargroup()
CodingSkills = get_codeskills()
HelloLabel = Label(top, text="Hello " + Username + ",", font = "Cornerstone 15",fg = "Blue").place(x=10,y=42)
YearGroupDisplay = Label(top, text="Year Group: " + YearGroup, font = "Cornerstone 11" ).place(x=10,y=80) 
CodingSkillsLabel = Label(top, text="Coding knowledge: " + CodingSkills + "/10", font="Cornerstone 11").place(x=10, y=100)
AvgScoreLabel = Label(top, text="Average Score: " + get_avgscore(), font = "Cornerstone 11").place(x=10,y=120)
InstructionsLabel = Label(top, text="Instructions: - Press 'Play' to explore a simulation.", font="Cornerstone 11", fg="red").place(x=10,y=145)
InstructionsLabel2 = Label(top, text=" - Complete questions by pressing 'Gain Points'.", font="Cornerstone 11", fg="red").place(x=89,y=165)
LineSeparatorMsg = "-------------------------------------------------------"
LineSeparator = Label(top, text=LineSeparatorMsg*5, font = "Cornerstone 11").place(x=-10, y=185)
LearnQuestion = Label(top, text="What would you like to learn?", font="bankgothic 12 underline").place(x=10,y=210)
#Description
#Planets
planetsHeading = Label(top,text="Planets", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=245)
planetsDescription = Label(top,text="- Learn about the motion of the celestial bodies in our Solar System", font="Helvetica 11").place(x=40, y=280)
planetsDescription = Label(top,text="- See how distance from the Sun affects the speed of a planet", font = "Helvetica 11").place(x=40, y=300)
planetsLaunch = Button(top, text="- Play", width = 6, bg="lime", borderwidth=3, command = planet_simulation).place(x=60,y=330)
planetsQuestions = Button(top, text="Gain points", width = 9, bg="yellow", borderwidth=3, command=planet_questions).place(x=130,y=330)
#Gravity
gravityHeading = Label(top,text="Gravity", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=380)

def destroy():
    top.destroy()
KillButton = Button(top, text="Kill", command = destroy, width=40, bg="red", fg="blue").place(x=100,y=490)

top.mainloop()

#maybe insert images in places to make it cooler