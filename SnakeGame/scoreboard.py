from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shapesize(50)
        self.hideturtle()
        self.pu()
        self.goto(0,270)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        # self.high_score = 0
        self.write(f"Score: {self.score}. High score: {self.high_score}", align=ALIGNMENT,font=FONT)


    def score_updt(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}. High score: {self.high_score}", align=ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
