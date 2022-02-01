STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.pu()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move_fd(self):
        self.fd(MOVE_DISTANCE)

    def move_right(self):
        self.setx(self.xcor()+MOVE_DISTANCE)

    def move_left(self):
        self.setx(self.xcor()-MOVE_DISTANCE)





