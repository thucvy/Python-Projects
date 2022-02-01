from turtle import Turtle
from snake import Snake
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5)
        self.pu()
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        food_x = random.randint(-280, 290)
        food_y = random.randint(-280, 250)
        self.goto(food_x,food_y)