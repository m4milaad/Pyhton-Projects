from setup import Scr
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Scr()
score = ScoreBoard()
snake = Snake()
food = Food()
screen.register_keys(snake)


def action():
    choice = screen.take_input()
    if choice == "t":
        screen.register_keys(snake)
        snake.reset()
        score.reset()
    elif choice == "q":
        score.reset()
        screen.screen.bye()

    else:
        print("Invalid choice")
        score.reset()
        screen.screen.bye()


game_on = True
while game_on:
    screen.screen_update()
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()
    if snake.out_of_boundaries():
        action()
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            action()
