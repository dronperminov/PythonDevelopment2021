import tkinter as tk
from tkinter import font

from text_field import TextField


class InputLabel(tk.Label):
    def __init__(self, master, **kwargs):
        self.font = font.Font(size=15, weight="normal")
        super().__init__(master, takefocus=True, highlightthickness=1, anchor="nw", font=self.font, **kwargs)
        self.field = TextField("")

        self.bind("<Left>", lambda event: self.process_key("<Left>"))
        self.bind("<Right>", lambda event: self.process_key("<Right>"))
        self.bind("<Home>", lambda event: self.process_key("<Home>"))
        self.bind("<End>", lambda event: self.process_key("<End>"))
        self.bind("<Delete>", lambda event: self.process_key("<Delete>"))
        self.bind("<BackSpace>", lambda event: self.process_key("<BackSpace>"))
        self.bind("<Any-KeyPress>", self.add_char)
        self.bind("<Button-1>", self.click)

        self.update_text()
        self.focus_set()

    def update_text(self):
        self.config(text=self.field.to_str())

    def process_key(self, key: str):
        if key == '<Delete>':
            self.field.delete()
        elif key == '<BackSpace>':
            self.field.backspace()
        elif key == '<Left>':
            self.field.move_cursor(-1)
        elif key == '<Right>':
            self.field.move_cursor(1)
        elif key == '<Home>':
            self.field.home()
        elif key == '<End>':
            self.field.end()

        self.update_text()

    def add_char(self, event):
        if str.isprintable(event.char):
            self.field.add_char(event.char)
            self.update_text()

    def click(self, arg):
        self.field.set_by_click(arg.x, self.font)
        self.update_text()
        self.focus_set()
