STEP = 60

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.pu()
        self.goto(position)
        self.setheading(90)


    # TODO: Move the paddle
    def move_up(self):
        self.setheading(90)
        self.fd(STEP)

    def move_down(self):
        self.setheading(270)
        self.fd(STEP)





