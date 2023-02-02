import tkinter as tk
from tkinter.constants import *


class HintedText(tk.Text):
    def __init__(self, parent, hint, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.hint = hint
        self.insert("1.0", hint)
        self.bind("<FocusIn>", self.clear_hint)
        self.bind("<FocusOut>", self.add_hint)

    def clear_hint(self, *args):
        if self.get("1.0", END).strip() == self.hint:
            self.delete("1.0", "end")
        
    def add_hint(self, *args):
        if not self.get("1.0", END).strip():
            self.insert("1.0", self.hint)
