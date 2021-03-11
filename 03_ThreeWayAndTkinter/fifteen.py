import random
from typing import List


LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'
DIRECTIONS = [LEFT, RIGHT, UP, DOWN]
SHUFFLE_ITERATIONS = 20


class Fifteen:
    def __init__(self, size: int = 4):
        self.size = size
        self.field = self.__init_field()

        self.empty_x = self.size - 1
        self.empty_y = self.size - 1

    def __init_field(self) -> List[List[int]]:
        field = []

        for i in range(self.size):
            field.append([i * self.size + j + 1 for j in range(self.size)])

        field[-1][-1] = 0
        return field

    def __can_move(self, direction: str) -> bool:
        if direction == RIGHT:
            return self.empty_x > 0

        if direction == LEFT:
            return self.empty_x < self.size - 1

        if direction == UP:
            return self.empty_y < self.size - 1

        if direction == DOWN:
            return self.empty_y > 0

        return False

    def __move(self, direction: str):
        x = self.empty_x
        y = self.empty_y

        if direction == RIGHT:
            x = self.empty_x - 1
        elif direction == LEFT:
            x = self.empty_x + 1
        elif direction == UP:
            y = self.empty_y + 1
        else:
            y = self.empty_y - 1

        self.field[self.empty_y][self.empty_x] = self.field[y][x]
        self.field[y][x] = 0
        self.empty_x = x
        self.empty_y = y

    def get_value_at(self, x, y) -> str:
        if x == self.empty_x and y == self.empty_y:
            return ""

        return str(self.field[y][x])

    def print(self):
        for row in self.field:
            print("|" + "".join(["%3d |" % value if value > 0 else "    |" for value in row]))

    def move(self, x, y):
        if self.empty_y == y and self.empty_x == x + 1:
            self.__move(RIGHT)
        elif self.empty_y == y and self.empty_x == x - 1:
            self.__move(LEFT)
        elif self.empty_y == y + 1 and self.empty_x == x:
            self.__move(DOWN)
        elif self.empty_y == y - 1 and self.empty_x == x:
            self.__move(UP)

    def shuffle(self, iterations=SHUFFLE_ITERATIONS):
        for i in range(iterations):
            directions = [direction for direction in DIRECTIONS if self.__can_move(direction)]
            direction = random.choice(directions)
            self.__move(direction)

    def is_win(self):
        if self.empty_x != self.size - 1 or self.empty_y != self.size - 1:
            return False

        for i in range(self.size * self.size - 1):
            if self.field[i // self.size][i % self.size] != i + 1:
                return False

        return True
