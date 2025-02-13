import turtle
from turtle import Turtle

import pandas

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_answers_count = 0
correct_answers_list = []
screen = turtle.Screen()
tim = Turtle()
tim.pu()
tim.ht()

screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
screen.bgpic("blank_states_img.gif")

while correct_answers_count != 50:
    answer = screen.textinput(f"{correct_answers_count}/50 states guessed", "Guess any state?").title()

    if answer in states and answer not in correct_answers_list:
        correct_answers_count += 1
        correct_answers_list.append(answer)
        x_to_go = data[data.state == answer].x.item()
        y_to_go = data[data.state == answer].y.item()
        tim.goto(x_to_go, y_to_go)
        tim.write(answer, False, "center")
    elif answer == "Exit":
        missed_states = [state for state in states if state not in correct_answers_list]
        break

if correct_answers_count != 50:
    print(
        f"You guessed {50 - correct_answers_count} states right! I'm creating missed_states.csv for the states you missed")
    export_data = pandas.DataFrame(missed_states)
    export_data.to_csv("Missed_states.csv")
