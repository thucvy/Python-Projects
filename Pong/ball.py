from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_step = 20
        self.y_step = 20
        self.move_speed = 0.1

    def move(self):
        x = self.xcor()
        y = self.ycor()
        x += self.x_step
        y += self.y_step
        self.goto((x,y))

    def bounce_wall(self):
        self.y_step *= -1
        self.move()

    def bounce_paddle(self):
        self.x_step *= -1
        self.move_speed *= 0.9
        self.move()

    def refresh(self):
        self.goto((0,0))
        self.move_speed = 0.1
        self.bounce_paddle()

