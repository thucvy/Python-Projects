from turtle import Turtle

class Map(Turtle):
    def __init__(self,img):
        super().__init__()
        self.shape(img)

