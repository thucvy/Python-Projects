# https://pypi.org/project/colorgram.py/


import colorgram
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()
colors = colorgram.extract('hirst_dot_painting.jpg', 400)
color_list = []

# first_color = colors[0]
# rgb = first_color.rgb
# hsl = first_color.hsl
# proportion = first_color.proportion
tim.pu()
tim.setheading(225)
tim.fd(300)
tim.setheading(360)


for color in colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    rgb_color = (r, g, b)
    color_list.append(rgb_color)

print(color_list)
for _ in range(2):
    color_list.remove(color_list[0])

print(color_list)


for _ in range(9):
    tim.pu()
    for _ in range(19):
        tim.dot(10, random.choice(color_list))
        tim.fd(20)
    tim.dot(10, random.choice(color_list))
    tim.lt(90)
    tim.dot(10, random.choice(color_list))
    tim.fd(20)
    tim.lt(90)
    for _ in range(19):
        tim.dot(10, random.choice(color_list))
        tim.fd(20)
    tim.dot(10, random.choice(color_list))
    tim.rt(90)
    tim.dot(10, random.choice(color_list))
    tim.fd(20)
    tim.rt(90)


screen = t.Screen()
screen.exitonclick()
