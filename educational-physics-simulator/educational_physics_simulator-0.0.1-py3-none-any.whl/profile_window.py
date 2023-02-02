#gamemode list window
from tkinter import *
from PIL import ImageTk,Image
import os
path = os.path.dirname(__file__)
my_directory= os.path.abspath(os.path.join(path, os.pardir))+"\\User interface\\profiles"

top = Toplevel()
top.geometry("410x440+350+0")
top.title("Profile Window")
global TitleLabel
global LearningMenu
global BG
BG = "#303030"
top.config(bg=BG)
TitleLabel = Label(top, text="Educational physics simulator", fg='red', bg=BG, font=("Helvetica 18 underline italic"))
TitleLabel.pack()
global Username
PassingUsername = open((my_directory+"\PassingUsername.txt"),"r")
Username = PassingUsername.readline()
PassingUsername.close()
#functions
def get_yeargroup():
    Profile = open((my_directory+"\\"+Username+".txt"), "r")
    Profile.readline()
    YearGroup = Profile.readline()
    Profile.close()
    return YearGroup[5:] #Gets the number in "Year 12" for example. 

def get_codeskills():
    Profile = open((my_directory+"\\"+Username+".txt"), "r")
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
    AverageScore="N / A"
    try:
        PointsRead = open((my_directory+"\\"+Username+"points.txt"), "r")
        PointsRead.close()
    except:
        MakePointsFile = open((my_directory+"\\"+Username+"points.txt"), "w")
        MakePointsFile.close()

    try:
        PointsRead = open((my_directory+"\\"+Username+"points.txt"), "r")
        Output = PointsRead.readline()
        AverageScore=(int(Output[0])+int(Output[1])+int(Output[2]))/3
        AverageScore=str(AverageScore)[0:3]
        PointsRead.close()
 
    except:
        AverageScore = "N / A"
    if AverageScore == "":
        AverageScore = "N / A"
    PointsRead = open((my_directory+"\\"+Username+"points.txt"), "w")
    PointsRead.write("")
    PointsRead.close()
    return str(AverageScore)

def Run():
    import gamemode_window_6

def Checked():
    if InstructionsChecked.get() == 1:
        Start = Button(top, text="Start", command = Run, bg="lime", fg="black", padx=1, pady=1, bd=6)
        Start.place(x=10,y=395)
#######################################################################################################
YearGroup = get_yeargroup()
CodingSkills = get_codeskills()
HelloLabel = Label(top, text="Hello " + Username + ",", font = "Cornerstone 18 bold underline", fg = "#0099f2", bg=BG).place(x=10,y=60)
YearGroupDisplay = Label(top, text="Year Group: " + YearGroup, font = "Cornerstone 13", fg = "White", bg=BG).place(x=10,y=110) 
CodingSkillsLabel = Label(top, text="Coding knowledge: " + CodingSkills + "/10", font="Cornerstone 13", fg = "White", bg=BG).place(x=10, y=140)
AvgScoreLabel = Label(top, text="Average Score: " + get_avgscore(), font = "Cornerstone 13", fg = "White", bg=BG).place(x=10,y=170)
LineSeparator = "---------------"
LineSeparatorLabel1 = Label(top, text=LineSeparator*20, font="Cornerstone 13", bg=BG).place(x=-10,y=200)

InstructionsLabel1 = Label(top, text="Instructions:", fg="red", bg=BG, font="Cornerstone 15 underline").place(x=10, y=220)
InstructionsLabel2 = Label(top, text="- Press 'Play' to explore a simulation.", font="Cornerstone 13", fg="white", bg=BG).place(x=20,y=255)
InstructionsLabel3 = Label(top, text="- Complete questions by pressing 'Gain Points'.", font="Cornerstone 13", fg="white", bg=BG).place(x=20,y=285)
LineSeparatorLabel2 = Label(top, text=LineSeparator*20, font="Cornerstone 13", bg=BG).place(x=-10,y=320)
InstructionsChecked = IntVar()
CheckBox = Checkbutton(top, text = "Tick here to confirm I have read the instructions", bg="black", fg="#e3225c", font="Cornerstone 12", variable = InstructionsChecked, command = Checked)
CheckBox.place(x=10,y=350)

import os
"""cwd=os.getcwd()
print(cwd)
base_folder=os.path.dirname("profile_window")
image_path=os.path.join(base_folder, "/pictures/profile_icon.jpg")
my_img = PhotoImage(file=image_path)"""
#img_dir =os.getcwd()

my_directory=os.path.dirname(__file__)+"\pictures\profile_icon.jpg"
my_img = ImageTk.PhotoImage(file=my_directory)
imageLabel = Label(top, image=my_img)
imageLabel.place(x=270,y=60)

top.mainloop()