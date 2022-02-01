import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = t.Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

# TODO: Create a snake body (3 squares on the screen)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# TODO: Control the snake using keyboard

screen.listen()
screen.onkey(key="Left", fun=snake.left_key)
screen.onkey(key="Right", fun=snake.right_key)
screen.onkey(key="Up", fun=snake.up_key)
screen.onkey(key="Down", fun=snake.down_key)


is_on = True
while is_on:
    screen.update()
    time.sleep(0.08)
    # TODO: Move the snake
    snake.move()

    # TODO: Detect collision with food (once hit food, snake becomes longer)
    if snake.head.distance(food) < 15:
        food.refresh()
        # TODO: Create a scoreboard (score + 1 everytime hit the food)
        scoreboard.score_updt()
        snake.extend_snake()

    # TODO: Detect collision with wall (game over)
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.reset()
        snake.reset()
        # is_on = False

    # TODO: Detect collision with tail (game over)
    print(snake.snake_body)
    for snake_part in snake.snake_body[1:]:
        if snake.head.distance(snake_part) < 9.9:
            print(snake_part)
            print(snake.head.position())
            print(snake_part.position())
            scoreboard.reset()
            snake.reset()
            # is_on = False

screen.exitonclick()
