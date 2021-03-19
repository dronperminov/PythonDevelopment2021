import tkinter as tk
from tkinter import font


class TextField:
    def __init__(self, text: str, position: int = 0):
        self.text = text
        self.position = position

    def add_char(self, c: str):
        self.text = self.text[:self.position] + c + self.text[self.position:]
        self.position += 1

    def backspace(self):
        if self.position == 0:
            return

        self.text = self.text[:self.position - 1] + self.text[self.position:]
        self.position -= 1

    def delete(self):
        if self.position < len(self.text):
            self.text = self.text[:self.position] + self.text[self.position + 1:]

    def move_cursor(self, dx: int):
        self.position = min(len(self.text), max(0, self.position + dx))

    def home(self):
        self.position = 0

    def end(self):
        self.position = len(self.text)

    def set_by_click(self, x: int, font: tk.font.Font):
        self.position = 0

        if not self.text or x < font.measure(self.text[0]):
            return

        while self.position < len(self.text) and x > font.measure(self.text[:self.position + 1]):
            self.position += 1

    def to_str(self) -> str:
        return self.text[:self.position] + 'ⵊ' + self.text[self.position:]
