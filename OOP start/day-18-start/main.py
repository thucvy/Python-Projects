import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# colors = ["CadetBlue","DarkMagenta","cyan","chocolate","DeepPink","DarkRed","DarkGray","DarkOliveGreen4","DarkOrchid","coral"]
directions = [0, 90, 180, 270]
is_cont = True
tim.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# screen = Screen()
# screen.exitonclick()

# for _ in range(4):
#     tim.fd(100)
#     tim.left(90)

# for _ in range(15):
#     tim.fd(10)
#     tim.pd()
#     tim.fd(10)
#     tim.pu()

# #triange:
# for _ in range(3):
#     tim.fd(100)
#     tim.right(360/3)
#
# #square
# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)
#

# Drawing different shapes
# n = 3
# while n <= 10:
#     tim.color(random.choice(colors))
#     for _ in range(n):
#         tim.fd(100)
#         tim.right(360/n)
#     n += 1


#Generate random walk

# while is_cont:
#     direction = random.choice(directions)
#     tim.color(random_color())
#     tim.speed("fastest")
#     tim.pensize(15)
#     tim.fd(30)
#     tim.setheading(direction)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size_of_gap)

draw_spirograph(3)
screen = t.Screen()
screen.exitonclick()