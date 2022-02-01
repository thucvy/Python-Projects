ALIGN = "center"
FONT = "Verdana"
from turtle import Turtle

class Coordinate(Turtle):
    def __init__(self, position, state):
        super().__init__()
        self.pu()
        self.ht()
        self.goto(position)
        # self.color("wheat")
        self.write(state, align=ALIGN, font=FONT)