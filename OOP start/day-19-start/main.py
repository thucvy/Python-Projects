import turtle as t

tim = t.Turtle()
screen = t.Screen()

# def move_forward():
#     tim.fd(10)
#
# screen.listen()
# screen.onkey(move_forward,"space")
# screen.exitonclick()
#

# TODO: Make an Etch-A-Sketch App
def forwards():
    tim.fd(10)

def backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(25)
    tim.fd(10)

def clockwise():
    tim.right(25)
    tim.fd(10)

def clear_draw():
    tim.reset()


screen.listen()
screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_draw, "c")
screen.exitonclick()



