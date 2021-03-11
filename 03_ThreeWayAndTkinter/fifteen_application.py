import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from typing import List
from fifteen import Fifteen


class FifteenApplication:
    def __init__(self, size: int):
        self.app = tk.Tk()

        self.size = size
        self.fifteen = Fifteen(size)

        self.app.title("Fifteen | Perminov A.I.")
        self.app.geometry("320x300")
        self.menu_frame = self.init_menu_frame()
        self.game_frame = self.init_game_frame()
        self.buttons = self.init_buttons()

    def restart(self):
        self.fifteen.shuffle()
        self.update_buttons()

    def update_buttons(self):
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j].config(text=str(self.fifteen.get_value_at(j, i)))

    def move(self, x: int, y: int):
        self.fifteen.move(x, y)
        self.update_buttons()

        if self.fifteen.is_win():
            messagebox.showinfo("Game over", "You win!")
            self.restart()

    def init_menu_frame(self) -> tk.Frame:
        menu_frame = tk.Frame(self.app)
        menu_frame.grid(row=0, sticky='wen')
        menu_frame.columnconfigure(0, weight=1)
        menu_frame.columnconfigure(1, weight=1)

        menu_font = font.Font(family='Helvetica', size=14)

        new_game_btn = tk.Button(menu_frame, text='New', font=menu_font, command=self.restart)
        new_game_btn.grid(row=0, column=0)

        quit_btn = tk.Button(menu_frame, text='Quit', font=menu_font, command=self.app.quit)
        quit_btn.grid(row=0, column=1)

        self.app.columnconfigure(0, weight=1)
        return menu_frame

    def init_game_frame(self) -> tk.Frame:
        game_frame = tk.Frame(self.app)
        game_frame.grid(row=1, sticky='wesn')
        self.app.rowconfigure(1, weight=1)

        for i in range(self.size):
            game_frame.columnconfigure(i, weight=1)
            game_frame.rowconfigure(i, weight=1)

        return game_frame

    def init_buttons(self) -> List[List[tk.Button]]:
        buttons = []
        btn_font = font.Font(family='Helvetica', size=15)

        for i in range(self.size):
            buttons_row = []

            for j in range(self.size):
                btn_text = self.fifteen.get_value_at(j, i)
                btn_command = lambda i=i, j=j: self.move(j, i)
                btn = tk.Button(self.game_frame, text=btn_text, font=btn_font, command=btn_command)
                btn.grid(row=i, column=j, sticky='wens')
                buttons_row.append(btn)

            buttons.append(buttons_row)

        return buttons

    def run(self):
        self.app.mainloop()
