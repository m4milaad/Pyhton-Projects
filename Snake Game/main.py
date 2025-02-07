from setup import Scr
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Scr()
score = ScoreBoard()
snake = Snake()
food = Food()
screen.register_keys(snake)

game_on = True
while game_on:
    screen.screen_update()
    snake.move()
    if snake.segments[0].distance(food) < 15:
        # this loop detects collision with food and increments the scoreboard by 1
        food.refresh()
        score.add_score()
        snake.extend()
    if snake.out_of_boundaries():
        # game_on = False
        choice = screen.take_input()
        if choice == "t":
            snake.reset()
            score.reset()
        elif choice == "q":
            game_on = False
        else:
            print("Invalid choice")
            game_on = False
        snake.reset()
        score.reset()
        # score.game_over()
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            # game_is_on = False
            score.reset()
            snake.reset()
            # score.game_over()

screen.exit()
