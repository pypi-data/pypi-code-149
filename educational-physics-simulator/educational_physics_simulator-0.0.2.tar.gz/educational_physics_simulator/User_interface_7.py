from tkinter import *
from tkinter import messagebox
import webbrowser
root = Tk()
root.geometry("400x420+400+0")
root.title("Educational Physics Simulator")

#Functions to get input values
def GetInputs():
    global Username
    global YearGroupValue #global so we can use them in the Save function
    global SliderValue
    Username = str(UsernameEntry.get()) #Gets the inputs from the Entry widgets
    YearGroupValue = str(clicked.get())
    SliderValue = str(LevelSlider.get())

    if Username.strip() == "": #If no username is entered
        Username = "No Name"

def Save():
    GetInputs()
    Profile = open((""+Username+".txt"), "w")
    Profile.write(Username + "\n")
    Profile.write(YearGroupValue + "\n") #Saves the inputs into a text file for later
    Profile.write(SliderValue + "\n")
    Profile.close()
    #(Below) Saves the inputs for when the code is loaded next time
    NextPresetValue = open(("LastUser.txt"), "w")
    NextPresetValue.write(Username + "\n")
    NextPresetValue.write(YearGroupValue + "\n")
    NextPresetValue.write(SliderValue + "\n")
    NextPresetValue.close()
    
def check_inputs(): #Returns True the username has been entered. False if they have not.
    #If False then a error message box will appear
    if Username == "No Name":
        return False
    else:
        return True

def callback(url):
   webbrowser.open_new_tab(url)
   #for the image referencing

#Create a file storing the last used username
#Reads the values already in the file
try:
    PresetValue = open(("LastUser.txt"), "r")
    PresetUsername = (PresetValue.readline()).strip()
    PresetYearGroup = (PresetValue.readline()).strip()
    PresetKnowledge = (PresetValue.readline()).strip()
    PresetValue.close()
except:
    #If there is no old data to load, use this example data
    PresetUsername = "No Name"
    PresetYearGroup = "Year 7"
    PresetKnowledge = 1

###################################################################################################################
#Main window
TitleLabel = Label(root, text="Educational Physics Simulator", fg='red', font=("Helvetica 18 underline"))
TitleLabel.pack()

SubHeading = Label(root, text="Where you can learn Coding + Physics", fg="blue", font=("Courier 11")).place(x=40,y=40)

#Profile section
ProfileText = Label(root, text="Profile", font=("bankgothic 12 underline")).place(x=10, y=70)
UsernameLabel = Label(root, text="Username:").place(x=10, y=97)
UsernameEntry = Entry(root)
UsernameEntry.insert(END,PresetUsername) #Automatically loads the previous username into the input widget
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
clicked.set(PresetYearGroup) #Automatically sets it to the last Year Group entered.
drop = OptionMenu(root, clicked, *YearGroups) #Creates the menu
drop.place(x=80, y=125)

LevelLabel = Label(root, text="Coding/Physics knowledge:").place(x=10, y=177)
LevelSlider = Scale(root, from_=1, to=10, orient=HORIZONTAL, length = 155) #you can add on the end , command = blah
LevelSlider.place(x=170.5, y=160)
LevelSlider.set(PresetKnowledge)
LevelText = Label(root, text="1 = None       10 = Very skilled").place(x=170, y=200)

def Run():
    Save()
    if check_inputs() == False:
        message = "Please enter a username"
        messagebox.showerror("Profile issue", message) #If no username was entered
    else:
        PassingUsername = open(("PassingUsername.txt"),"w")
        PassingUsername.write(Username)
        PassingUsername.close()
        import profile_window

StartLearning = Button(root, text="Start Learning -->", command=Run, bg="lime", padx=1, pady=1, bd=10).place(x=130, y=250)

###########################################################################################################################
LineSeparator = "---------------" #splits the window into sections
LineSeparatorLabel1 = Label(root, text=LineSeparator*20, font="Helvetica 13").place(x=-10,y=300)

CopyrightHeading = Label(root, text="Copyright", font="Helvetica 16 underline italic").place(x=10,y=320)
CopyrightDescription = Label(root, text="This platform uses images designed by freepik.com", font="Helvetica 12 italic").place(x=10,y=360)
#Create a Label to display the link
link = Label(root, text="www.freepik.com", font=("Helvetica 13 italic"), fg="blue", cursor="hand2")
link.place(x=10,y=390)
link.bind("<Button-1>", lambda e:
callback("https://www.freepik.com/free-vector/set-fantastic-planets-asteroids-cosmic-objects_20576153.htm#query=cartoon%20satellites%20orbiting%20earth&position=1&from_view=search&track=sph>Image by upklyak"))

root.mainloop()