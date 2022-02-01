FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(-280,270)
        self.ht()
        self.level = 1
        self.write(f"Level: {self.level}", font=FONT)


    def level_update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def gameover(self):
        self.goto((0,0))
        self.write(f"GAME OVER!", align = "center", font = FONT)