from tkinter import *
root = Tk()
root.geometry("400x400")

frame = LabelFrame(root, padx=5,pady=5)
frame.pack(padx=10,pady=10)

button = Button(frame, text="Hello").pack()



root.mainloop()