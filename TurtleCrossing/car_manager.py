COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = random.randint(-250, 251)
        self.cars = []
        self.create_cars()

    def create_cars(self):
        self.pu()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.goto(self.x, self.y)


    def move(self,speed):
        self.fd(STARTING_MOVE_DISTANCE + speed*MOVE_INCREMENT)


