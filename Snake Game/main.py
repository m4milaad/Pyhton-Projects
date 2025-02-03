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
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        game_on = False
        score.game_over()
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exit()
