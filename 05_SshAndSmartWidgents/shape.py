from abc import abstractmethod
from tkinter import Canvas


STYLE_REGEXP = r"\d+ #[0-9a-f]{3}([0-9a-f]{3})? #[0-9a-f]{3}([0-9a-f]{3})?"


class Shape:
    def __init__(self, x0: int, y0: int, width: int, color: str, background: str):
        self.x0 = x0
        self.y0 = y0

        self.width = width
        self.color = color
        self.background = background

    @abstractmethod
    def is_mouse_hover(self, x: int, y: int) -> bool:
        pass

    def move(self, dx: int, dy: int):
        self.x0 += dx
        self.y0 += dy

    @abstractmethod
    def resize(self, dx: int, dy: int):
        pass

    @abstractmethod
    def to_str(self) -> str:
        pass

    @abstractmethod
    def to_canvas(self, canvas: Canvas):
        pass

    @staticmethod
    @abstractmethod
    def parse_from_line(line: str):
        pass
