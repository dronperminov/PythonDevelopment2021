from tkinter import Canvas


class Ellipse:
    def __init__(self, x0: int, y0: int, r1: int, r2: int, width: int, color: str, background: str):
        self.x0 = x0
        self.y0 = y0
        self.r1 = r1
        self.r2 = r2

        self.width = width
        self.color = color
        self.background = background

    def is_mouse_hover(self, x: int, y: int) -> bool:
        dx = x - self.x0
        dy = y - self.y0

        return (dx / self.r1)**2 + (dy / self.r2)**2 < 1

    def move(self, dx: int, dy: int):
        self.x0 += dx
        self.y0 += dy

    def resize(self, dx: int, dy: int):
        if self.r1 + dx <= 5 or self.r2 + dy <= 5:
            return

        self.r1 += dx
        self.r2 += dy
        self.x0 += dx / 2
        self.y0 += dy / 2

    def to_str(self) -> str:
        return f"ellipse ({int(self.x0)} {int(self.y0)}) {self.r1} {self.r2}; {self.width} {self.color} {self.background}"

    def to_canvas(self, canvas: Canvas):
        x1 = self.x0 - self.r1
        y1 = self.y0 - self.r2

        x2 = self.x0 + self.r1
        y2 = self.y0 + self.r2

        canvas.create_oval(x1, y1, x2, y2, fill=self.background, outline=self.color, width=self.width)
