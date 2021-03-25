import tkinter as tk
import tkinter.colorchooser
import tkinter.ttk as ttk
from shape import Shape
from shapes.ellipse import Ellipse
from shapes.rectangle import Rectangle
from typing import List, Optional


class DrawingApplication:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Ellipse drawer | Perminov A.I.")
        self.app.geometry("900x500")

        self.init_components()
        self.init_events()

        self.shapes = []
        self.active_shape = None

        self.is_resize = False
        self.is_pressed = False
        self.prevX = -1
        self.prevY = -1

    def init_text_components(self):
        self.text = tk.Text(self.app, width=30)
        self.text.grid(row=0, column=0, sticky='news')

        self.text.tag_configure("error", background="#f44336", foreground="#fff")
        self.text.tag_configure("valid", background="#fff", foreground="#000")

        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)

    def init_graph_components(self):
        graph_frame = tk.Frame(self.app, width=200, bg='#aaa')
        graph_frame.grid(row=0, column=1, sticky='news')
        graph_frame.columnconfigure(0, weight=1)
        graph_frame.rowconfigure(1, weight=1)

        control_frame = tk.Frame(graph_frame)
        control_frame.grid(row=0, column=0, sticky='ew')

        self.width_box = tk.Spinbox(control_frame, width=5, from_=1, to=10)
        self.width_box.grid(row=0, column=0)

        self.color_btn = tk.Button(control_frame, text="Border", bg="#000", fg="#fff",
                                   command=lambda: self.select_color(self.color_btn))
        self.color_btn.grid(row=0, column=1)

        self.background_btn = tk.Button(control_frame, text="     Fill     ", bg="#ff0", fg="#000",
                                        command=lambda: self.select_color(self.background_btn))
        self.background_btn.grid(row=0, column=2)

        self.type_box = ttk.Combobox(control_frame, values=["Ellipse", "Rectangle"], state="readonly", width=10)
        self.type_box.grid(row=0, column=3)
        self.type_box.current(0)

        self.canvas = tk.Canvas(graph_frame, bg='#fff')
        self.canvas.grid(row=1, column=0, sticky='news')
        self.app.columnconfigure(1, weight=1)

    def init_components(self):
        self.init_text_components()
        self.init_graph_components()

    def init_events(self):
        self.canvas.bind("<Button>", self.mouse_down)
        self.canvas.bind("<ButtonRelease>", self.mouse_up)
        self.canvas.bind("<Motion>", self.mouse_move)
        self.canvas.bind("<MouseWheel>", self.mouse_wheel_vertically)
        self.canvas.bind("<Shift-MouseWheel>", self.mouse_wheel_horizontally)

        self.text.bind("<KeyRelease>", self.text_changed)

    def select_color(self, button: tk.Button):
        color = tk.colorchooser.askcolor()
        r, g, b = color[0]
        brightness = 0.299 * r + 0.587 * g + 0.114 * b
        button["bg"] = color[1]
        button["fg"] = "#fff" if brightness < 128 else "#000"

    def update_text_description(self):
        self.text.delete('1.0', tk.END)

        for shape in self.shapes:
            self.text.insert(tk.END, shape.to_str() + "\n")

    def add_shape(self, x: int, y: int) -> Shape:
        width = self.width_box.get()
        color = self.color_btn["bg"]
        background = self.background_btn["bg"]

        shape_type = self.type_box.get()

        if shape_type == "Ellipse":
            r1 = 20
            r2 = 20

            return Ellipse(x - r1, y - r2, r1, r2, width, color, background)

        if shape_type == "Rectangle":
            w = 20
            h = 20

            return Rectangle(x - w, y - h, w, h, width, color, background)

    def get_shape_at(self, x: int, y: int) -> int:
        for i, shape in enumerate(self.shapes):
            if shape.is_mouse_hover(x, y):
                return i

        return -1

    def draw(self, update_description=True):
        self.canvas.delete("all")

        if update_description:
            self.update_text_description()

        for shape in self.shapes:
            shape.to_canvas(self.canvas)

    def mouse_down(self, e):
        shape_index = self.get_shape_at(e.x, e.y)

        if e.num == 1:
            if shape_index == -1:
                self.active_shape = self.add_shape(e.x, e.y)
                self.shapes.append(self.active_shape)
                self.is_resize = True
            else:
                self.active_shape = self.shapes[shape_index]
                self.is_resize = False

            self.is_pressed = True
            self.prevX = e.x
            self.prevY = e.y
        elif e.num == 3 and shape_index != -1:
            del self.shapes[shape_index]

        self.draw()

    def mouse_up(self, e):
        self.is_pressed = False
        self.is_resize = False
        self.draw()

    def mouse_move(self, e):
        if not self.is_pressed:
            return

        if self.active_shape is None:
            return

        dx = e.x - self.prevX
        dy = e.y - self.prevY

        if self.is_resize:
            self.active_shape.resize(dx, dy)
        else:
            self.active_shape.move(dx, dy)

        self.draw()
        self.prevX = e.x
        self.prevY = e.y

    def mouse_wheel_vertically(self, e):
        for shape in self.shapes:
            shape.move(0, 15 if e.delta > 0 else -15)

        self.draw()

    def mouse_wheel_horizontally(self, e):
        for shape in self.shapes:
            shape.move(15 if e.delta > 0 else -15, 0)

        self.draw()

    def line_to_shape(self, line: str) -> Optional[Shape]:
        if Ellipse.is_valid_description(line):
            return Ellipse.parse_from_line(line)

        if Rectangle.is_valid_description(line):
            return Rectangle.parse_from_line(line)

        return None

    def parse_lines(self, lines: List[str]):
        is_valid = True

        for i, line in enumerate(lines):
            if not line.strip():
                continue

            shape = self.line_to_shape(line)

            if shape is None:
                is_valid = False
                self.text.tag_add("error", "%s.0" % (i + 1), "%s.0" % (i + 2))
            else:
                self.shapes.append(shape)
                self.text.tag_add("valid", "%s.0" % (i + 1), "%s.0" % (i + 2))

        return is_valid

    def text_changed(self, e):
        self.shapes = []
        self.text.tag_remove("valid", "1.0", "end")
        self.text.tag_remove("error", "1.0", "end")

        description = self.text.get("1.0", tk.END)
        lines = description.splitlines()

        if self.parse_lines(lines):
            self.draw(False)

    def run(self):
        self.app.mainloop()
