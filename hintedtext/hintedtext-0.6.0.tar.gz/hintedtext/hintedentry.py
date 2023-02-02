import tkinter as tk

class HintedEntry(tk.Entry):
    def __init__(self, parent, hint, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.hint = hint
        self.insert("0", hint)
        self.bind("<FocusIn>", self.clear_hint)
        self.bind("<FocusOut>", self.add_hint)

    def clear_hint(self, *args):
        if self.get() == self.hint:
            self.delete("0", "end")
        
    def add_hint(self, *args):
        if not self.get():
            self.insert("0", self.hint)

