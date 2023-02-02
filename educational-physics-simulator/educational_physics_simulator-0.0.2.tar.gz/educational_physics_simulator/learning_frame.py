from tkinter import *
root1 = Toplevel()
root1.geometry("400x350+400+0")


TitleLabel = Label(root1, text="Ed's physics simulator", fg='red', font=("Helvetica 18 underline"))
TitleLabel.pack()

LearnQuestion = Label(root1, text="What would you like to learn?", font="bankgothic 12 underline").place(x=10,y=60)

Options=["Gravity", "Planets"]

clicked1 = StringVar()
clicked1.set(Options[0]) #Sets the default value from the first value in the Options list
drop1 = OptionMenu(root1, clicked1, *Options) #Creates the menu
drop1.place(x=10, y=115)
root1.mainloop()
