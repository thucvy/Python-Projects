import turtle
import pandas
from map import Map
from coordinate import Coordinate
from score import Score

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
turtle.addshape(img)

map = Map(img)
score = Score()

data = pandas.read_csv("50_states.csv")
all_states_list = data.state.to_list()
correct_answer = []
is_cont = True
while is_cont:
    answer_input = turtle.textinput("Guess the State", "What's another state's name? Type 'exit' if you want to quit the game")
    row = data[data.state == answer_input.title()]
    if row.empty:
        score.incorrect()
    elif answer_input.title() in correct_answer:
        pass
    else:
        x = int(row.x)
        y = int(row.y)
        coordinate = Coordinate((x, y), answer_input.title())
        score.correct()
        correct_answer.append(answer_input.title())
    if score.score == 50 or answer_input.lower() == "exit":
        missing_states = [state for state in all_states_list if state not in correct_answer]
        # for state in all_states_list:
        #     if state not in correct_answer:
        #         missing_states.append(state)
        missing_states_df = pandas.DataFrame(missing_states, columns = ['state'])
        missing_states_df.to_csv("states_to_learns.csv")
        is_cont = False

screen.exitonclick()
