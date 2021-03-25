import re
from tkinter import Canvas
from shape import Shape, STYLE_REGEXP


class Rectangle(Shape):
    def __init__(self, x0: int, y0: int, w: int, h: int, width: int, color: str, background: str):
        super(Rectangle, self).__init__(x0, y0, width, color, background)
        self.w = w
        self.h = h

    def is_mouse_hover(self, x: int, y: int) -> bool:
        dx = abs(x - self.x0)
        dy = abs(y - self.y0)

        return dx <= self.w / 2 and dy <= self.h / 2

    def resize(self, dx: int, dy: int):
        if self.w + dx <= 5 or self.h + dy <= 5:
            return

        self.w += dx
        self.h += dy
        self.x0 += dx / 2
        self.y0 += dy / 2

    def to_str(self) -> str:
        return f"rectangle ({int(self.x0)} {int(self.y0)}) {self.w} {self.h}; {self.width} {self.color} {self.background}"

    def to_canvas(self, canvas: Canvas):
        x1 = self.x0 - self.w // 2
        y1 = self.y0 - self.h // 2

        x2 = self.x0 + self.w // 2
        y2 = self.y0 + self.h // 2

        canvas.create_rectangle(x1, y1, x2, y2, fill=self.background, outline=self.color, width=self.width)

    @staticmethod
    def parse_from_line(line: str) -> "Rectangle":
        args = line.split()
        x0 = int(args[1][1:])
        y0 = int(args[2][:-1])
        w = int(args[3])
        h = int(args[4][:-1])
        width = int(args[5])
        color = args[6]
        background = args[7]

        return Rectangle(x0, y0, w, h, width, color, background)

    @staticmethod
    def is_valid_description(line: str) -> bool:
        return bool(re.fullmatch(r"rectangle \(\d+ \d+\) \d+ \d+; " + STYLE_REGEXP, line))
