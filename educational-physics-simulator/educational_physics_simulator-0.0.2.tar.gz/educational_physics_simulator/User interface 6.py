#This program is to add labels to the window
#First verison without the gamemodes window within the program
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

def check_inputs(): #Returns True the username has been entered. False if they have not.
    if Username == "No Name":
        return False
    else:
        return True

#SaveButton = Button(root, text="Save", command = Save, width=5, bg="aqua").place(x=10, y=220)



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
        import gamemode_window

StartLearning = Button(root, text="Start Learning -->", command=Run, bg="lime", padx=1, pady=1, bd=10).place(x=130, y=250)

###########################################################################################################################


#Learning section
root.mainloop()




