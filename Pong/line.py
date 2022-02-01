from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color("white")
        self.goto(0,450)
        self.setheading(270)
        self.pensize(5)
        while self.ycor() >= -400:
            self.pd()
            self.fd(50)
            self.pu()
            self.fd(50)
