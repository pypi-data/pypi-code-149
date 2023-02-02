#This program is to add labels to the window
from pickle import APPEND
from tkinter import *
from turtle import fillcolor
root = Tk()
root.geometry("400x350+400+0")

#Reads the values already in the file
"""PresetValue = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "r")
PresetUsername = (PresetValue.readline()).strip()
PresetYearGroup = (PresetValue.readline()).strip()
PresetKnowledge = (PresetValue.readline()).strip()
PresetValue.close()
"""
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
    """ 
    GetInputs()
    Profile = open("C:/Users/hardy/OneDrive/Documents (This PC)/Ed/A Level/EPQ/User interface/profile.txt", "w")
    Profile.write(Username + "\n")
    Profile.write(YearGroupValue + "\n")
    Profile.write(SliderValue + "\n")
    Profile.close()
    """

SaveButton = Button(root, text="Save", command = Save, width=5, bg="aqua").place(x=10, y=220)

def LearningProgram():
    top = Toplevel()
    top.geometry("500x350+350+0")
    global TitleLabel
    global LearningQuestion
    global LearningMenu
    global GravityHeading
    TitleLabel = Label(top, text="Ed's physics simulator", fg='red', font=("Helvetica 18 underline"))
    TitleLabel.pack()

    LearnQuestion = Label(top, text="What would you like to learn?", font="bankgothic 12 underline").place(x=10,y=60)

    Options=["Gravity", "Planets", "Galton Board"]
    clicked1 = StringVar()
    clicked1.set(Options[0]) #Sets the default value from the first value in the Options list
    LearningMenu = OptionMenu(top, clicked1, *Options) #Creates the menu
    LearningMenu.place(x=10, y=280)
    LearningMenu.config(bg = "red")
    LearningMenu["menu"].config(bg="green")

    def Gravity():
        from typing import List
        import pygame
        import math
        pygame.init()
        gravitywindow = Toplevel()
        gravitywindow.geometry("400x400")
        sunChecked = IntVar()
        earthChecked = IntVar()
        marsChecked = IntVar()
        mercuryChecked = IntVar()
        venusChecked = IntVar()

        ListOfPlanets=[]
        sunBox = Checkbutton(gravitywindow, text = "Sun", variable = sunChecked )
        sunBox.pack()
        earthBox = Checkbutton(gravitywindow,text="Earth", variable=earthChecked)
        earthBox.pack()
        marsBox = Checkbutton(gravitywindow,text="Mars", variable=marsChecked)
        marsBox.pack()
        mercuryBox = Checkbutton(gravitywindow,text="Mercury", variable=mercuryChecked)
        mercuryBox.pack()
        venusBox = Checkbutton(gravitywindow,text="Venus", variable=venusChecked)
        venusBox.pack()

        ListOfTicks = []
        def save_me():
            ListOfTicks = [sunChecked.get(), earthChecked.get(), marsChecked.get(), mercuryChecked.get(), venusChecked.get()]
            planet_simulation(ListOfTicks)

        SaveButton = Button(gravitywindow,text="Save", command = save_me)
        SaveButton.pack()

        def planet_simulation(ListOfTicks):
            

            print(ListOfTicks)
            WIDTH, HEIGHT = 1200,650
            WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Planet Simulation")

            #List of colours defined in RGB
            WHITE = (255,255,255)
            BLACK = (0,0,0)
            YELLOW = (255,255,0) #Change these colours later
            BLUE = (0,0,255)
            RED = (255,0,0)
            DARK_GREY = (80,78,81)
            PINK = (229,38,178)
            FONT = pygame.font.SysFont("Helvetica", 16) #Initialising the font

            class Planet:
                
                #Astronmical Unit
                AU = 149.6e6*1000 #Multiply by 1000 to convert the kilometers to meters
                #Gravitational constant
                G = 6.67428e-11
                SCALE = 200 / AU #One AU = 100 pixels on the screen
                TIMESTEP = 3600*24 #Seconds in an hour * hours in a day = seconds in a day
                def __init__(self,x,y,radius,colour,mass):
                    #Parent behavours for children (planets) to inherit
                    self.x=x #meters away from the sun on the x=axis
                    self.y=y #meters away from ths sun on the y-acis
                    self.radius=radius
                    self.colour=colour
                    self.mass=mass

                    self.orbit = []
                    self.sun = False
                    self.distance_to_sun=0

                    self.x_velocity=0
                    self.y_velocity=0

                def draw(self, win):
                    x = self.x * self.SCALE + WIDTH / 2
                    y = self.y * self.SCALE + HEIGHT / 2
                    #These coordinates are to be the offset values...
                    #...from the center of the screen as the top left of the screen is (0,0) not the centre

                    if len(self.orbit) > 2:
                        updated_points = []
                        for point in self.orbit:
                            x, y = point
                            x = x*self.SCALE + WIDTH/2
                            y = y*self.SCALE + HEIGHT/2
                            updated_points.append((x,y))

                        pygame.draw.lines(win, self.colour, False, updated_points, 2)

                    pygame.draw.circle(win, self.colour, (x,y), self.radius)

                    if not self.sun: #Placing this here so that the text is in front of the circle (due to being printed afterwards)
                        distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, PINK)
                        win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
                def attraction(self,other):
                    other_x, other_y = other.x, other.y
                    distance_x = other_x - self.x
                    distance_y = other_y - self.y
                    distance = math.sqrt(distance_x**2 + distance_y**2)

                    if other.sun:
                        self.distance_to_sun = distance
                        #If it's the sun then we can store the distance here

                    force = self.G * self.mass * other.mass / distance**2 #The hypotenuse from the sun to the planet
                    theta = math.atan2(distance_y, distance_x) #atan2 is inverse tan function
                    force_x = math.cos(theta) * force #This calculates each component of force in each dimension (x,y)
                    force_y = math.sin(theta) * force
                    return force_x, force_y #If you printed these numbers, they would be massive as these are real values as it's a simulation

                def update_position(self, ListOfPlanets):
                    total_fx = total_fy = 0 #Force in x and y directions set to 0
                    for planet in ListOfPlanets:
                        if self == planet:
                            continue #Otherwise would give a 0 error as you cant give the force of yourself to yourself

                        fx, fy = self.attraction(planet)
                        total_fx +=fx
                        total_fy +=fy

                    self.x_velocity += total_fx / self.mass * self.TIMESTEP
                    self.y_velocity += total_fy / self.mass * self.TIMESTEP

                    self.x += self.x_velocity * self.TIMESTEP
                    self.y += self.y_velocity * self.TIMESTEP
                    self.orbit.append((self.x, self.y)) #adding to the list of orbit positions

            def main():
                run = True
                clock = pygame.time.Clock()

                sun = Planet(0,0,30,YELLOW,1.98892 * 10**30) #creating a planet and defining the already declared variables
                sun.sun = True

                earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
                earth.y_velocity = 29.783*1000 #as it's in m/s
                mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
                mars.y_velocity = 24.077*1000
                mercury = Planet(-0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
                mercury.y_velocity = -47.4*1000
                venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
                venus.y_velocity = -35.02*1000
                ListOfPlanets = [sun, earth, mars, mercury, venus]
                
            

                while run:
                    clock.tick(60) #Setting the frame rate
                    #WINDOW.fill(WHITE)
                    WINDOW.fill(BLACK)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    print(ListOfPlanets)
                    if ListOfTicks[0] == 1:
                        sun.update_position(ListOfPlanets)
                        sun.draw(WINDOW)
                    if ListOfTicks[1] == 1:
                        earth.update_position(ListOfPlanets)
                        earth.draw(WINDOW)
                    if ListOfTicks[2] == 1:
                        mars.update_position(ListOfPlanets)
                        mars.draw(WINDOW)
                    if ListOfTicks[3] == 1:
                        mercury.update_position(ListOfPlanets)
                        mercury.draw(WINDOW)
                    if ListOfTicks[4] == 1:
                        venus.update_position(ListOfPlanets)
                        venus.draw(WINDOW)
                    """"
                    for planet in ListOfPlanets:
                        planet.update_position(ListOfPlanets)
                        planet.draw(WINDOW)
                    """
                    pygame.display.update()

                pygame.quit()

            main()
        gravitywindow.mainloop()
        
    #Description
    GravityHeading = Label(top,text="Planets", font="Gothic 15 underline", width=8, bg="black",fg="aqua").place(x=40,y=100)
    GravityDescription = Label(top,text="- Learn about the motion of the celestial bodies in our Solar System", font="Helvetica 11").place(x=40, y=135)
    GravityDescription = Label(top,text="- See how distance from the Sun affects the speed of a planet", font = "Helvetica 11").place(x=40, y=160)
    GravityLaunch = Button(top, text="Play", width = 6, bg="lime", borderwidth=3, command = Gravity).place(x=60,y=190)

#Learning section
StartLearning = Button(root, text="Start Learning -->", command=LearningProgram, bg="lime", padx=1, pady=1, bd=10).place(x=130, y=280)
root.mainloop()