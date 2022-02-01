import turtle as t
from line import Line
from paddle import Paddle
from ball import Ball
from score import Score
import time

# TODO: Create main screen
screen = t.Screen()
screen.setup(1200,900)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

line = Line()

SCORE1_POSITION = (-200,320)
SCORE2_POSITION = (200,320)
score1 = Score(SCORE1_POSITION)
score2 = Score(SCORE2_POSITION)

# TODO: Create paddles

paddle_1 = Paddle((-550,0))
paddle_2 = Paddle((550,0))

# TODO: Create ball
ball = Ball()

screen.listen()
screen.onkey(key="w", fun=paddle_1.move_up)
screen.onkey(key="s", fun=paddle_1.move_down)
screen.onkey(key="Up", fun=paddle_2.move_up)
screen.onkey(key="Down", fun=paddle_2.move_down)


is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()

    #TODO: Detect collision with wall
    if abs(ball.ycor()) < 410:
        ball.move()
        # print(ball.position())
    else:
        ball.bounce_wall()
        # print(ball.position())

    #TODO: Detect collision with paddle
    if ball.distance(paddle_1) <= 50 and ball.xcor() < -530:
        ball.bounce_paddle()
    elif ball.xcor() > 580:
        ball.refresh()
        score1.score_update(SCORE1_POSITION)
        print(score1.position())
    elif ball.distance(paddle_2) <= 50 and ball.xcor() > 530:
        ball.bounce_paddle()
    elif ball.xcor() < -580:
        ball.refresh()
        score2.score_update(SCORE2_POSITION)
        print(score2.position())
    else:
        pass
    if score1.score == 10:
        winner = "Left player"
        is_on = False
    elif score2.score == 10:
        winner = "Right player"
        is_on = False
score1.gameover(winner)




















screen.exitonclick()