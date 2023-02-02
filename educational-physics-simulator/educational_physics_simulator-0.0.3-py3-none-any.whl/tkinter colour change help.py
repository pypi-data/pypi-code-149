import tkinter as tk


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x300+200+400")
        self.input_a = tk.StringVar()
        self.label = tk.Label(self, text="Enter Value")
        self.label.grid(row=0, column=0)
        tk.Entry(self, textvariable=self.input_a).grid(row=0, column=1)
        tk.Button(self, text="Run", command=self.color_changer).grid(row=1, column=1)

    def color_changer(self):
        input_b = self.input_a.get()
        print(input_b)
        if input_b == "r":
            self["bg"] = "red"
            self.label["bg"] = "red"
        if input_b == "y":
            self["bg"] = "yellow"
        if input_b == "g":
            self["bg"] = "green"



if __name__ == '__main__':
    Main().mainloop()