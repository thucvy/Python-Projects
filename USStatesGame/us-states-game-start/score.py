from turtle import Turtle

ALIGN = "center"
FONT = ("Verdana", 35, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.ht()
        self.goto(0, 250)
        self.write(f"{self.score}/50 US States", align=ALIGN, font=FONT)

    def correct(self):
        self.clear()
        self.score += 1
        self.write(f"Correct! You got: {self.score}/50 US States", align=ALIGN, font=FONT)

    def incorrect(self):
        self.clear()
        self.write(f"Wrong! You got: {self.score}/50 US States", align=ALIGN, font=FONT)
