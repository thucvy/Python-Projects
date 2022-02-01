import turtle as t
import random



screen = t.Screen()
screen.setup(width=500, height=400)

colors = ["red","blue","purple","yellow","green","brown"]
all_turtles = []

is_cont = False
y = -100
for i in range(6):
    tim = t.Turtle(shape="turtle")
    tim.color(colors[i])
    tim.pu()
    tim.goto(x = -240, y = y)
    y += 50
    all_turtles.append(tim)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color \n(red/ blue/ purple/ yellow/ green/ brown): ")
print(all_turtles)
if user_bet:
    is_cont = True

while is_cont:
    for turtle_object in all_turtles:
        turtle_object.fd(random.randint(0,10))
        if turtle_object.xcor() > 230:
            answer = turtle_object.pencolor()
            is_cont = False
# screen.clear()
if user_bet == answer:
    print(f"You win 😍! The {answer} turtle wins the race.")
else:
    print(f"You lose 😭! The {answer} turtle wins the race.")

screen.exitonclick()
