import tkinter as tk
from LabelEdit import InputLabel


class LabelEditApplication:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("InputLabel | Perminov A.I.")
        self.app.geometry("200x60")
        self.init_form()

    def init_form(self):
        menu_frame = tk.Frame(self.app)
        menu_frame.grid(row=0, sticky='wens')
        menu_frame.columnconfigure(0, weight=1)
        menu_frame.rowconfigure(0, weight=1)

        label = InputLabel(menu_frame)
        label.grid(row=0, column=0, sticky='wens')

        quit_btn = tk.Button(menu_frame, text='  Quit  ', command=self.app.quit)
        quit_btn.grid(row=1, column=0, sticky='es')

        self.app.rowconfigure(0, weight=1)
        self.app.columnconfigure(0, weight=1)

    def run(self):
        self.app.mainloop()
