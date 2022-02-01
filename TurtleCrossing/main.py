import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#TODO: CREATE AND MOVE TURTLE
player = Player()
screen.listen()
screen.onkey(fun=player.move_fd, key="Up")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")

#TODO: Create a list of random cars
cars = []

#TODO: SET LEVEL
level = Scoreboard()


#TODO: Create game loop
game_is_on = True
n = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    n += 1
    speed = level.level - 1
    loop = 6 - speed
    if n % loop == 0:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move(speed)
        #TODO: Detect collision
        if car.ycor()-30 <= player.ycor() <= car.ycor()+10 and car.xcor()-18 <= player.xcor() <= car.xcor()+18:
            level.gameover()
            game_is_on = False
    if player.ycor() >= 290:
        level.level_update()
        player.create_player()

screen.exitonclick()



