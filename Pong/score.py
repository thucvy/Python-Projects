from turtle import Turtle
FONT = ('Arial', 80, 'normal')
ALIGN = "center"

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.pu()
        self.ht()
        self.goto(position)
        self.color("white")
        self.pensize(5)
        self.write(f"{self.score}", True, align=ALIGN, font =FONT)

    def score_update(self,position):
        self.clear()
        self.score += 1
        self.goto(position)
        self.write(f"{self.score}", True, align=ALIGN, font=FONT)


    def gameover(self,winner):
        self.goto((0, 0))
        self.write(f"GAME OVER! \n{winner} wins!",True,align=ALIGN,font = FONT)
