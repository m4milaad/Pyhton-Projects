from setup import Scr
from board import Board
from ball import Ball
from scoreboard import ScoreBoard

screen = Scr()
right_board = Board(380)
left_board = Board(-380)
ball = Ball()
score_board = ScoreBoard()
screen.register_keys_r(right_board)
screen.register_keys_l(left_board)
game = True

while game:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_board) < 50 and ball.xcor() > 350 or ball.distance(left_board) < 50 and ball.xcor() < -350:
        ball.bounce_x()
    if ball.xcor() > 380 or ball.xcor() < -380:
        score_board.score_update(ball.xcor())
        ball.reset_position()
    ball.move_ball()

    screen.screen_update(ball.move_speed)
screen.exit()
