# turtle.home() + turtle.clear() =  turtle.reset()
from turtle import Turtle, Screen
import random


def turtle_init(name, color):
    name.shape("turtle")
    name.color(color)
    name.penup()


turtle_colors = ["red", "green", "blue", "yellow", "orange", "purple"]
turtle_names = ["Shellby", "Speedy", "Turtlenecks", "Squirt", "Carapace", "Leafy"]
scr = Screen()
scr.title("Turtle Race Bet")
scr.setup(500, 400)
race = False
user_bet = scr.textinput("Place your bets!", "Which turtle would win the race?\n'red', 'green', 'blue', 'yellow', 'orange', 'purple'")
if user_bet:
    race = True
pos = -130
for i in range(6):
    turtle_names[i] = Turtle()
    turtle_init(turtle_names[i], turtle_colors[i])
    turtle_names[i].goto(-230, pos)
    pos += 60

while race:
    for t in turtle_names:
        if t.xcor() > 230:
            winner = t.fillcolor()
            if user_bet.lower() == winner.lower():
                print("You won the bet")
            else:
                print(f"You lost the Bet! {winner.title()} won the race")
            race = False
            break
        t.fd(random.randint(1, 10))
scr.exitonclick()
