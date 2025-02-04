from time import sleep
from turtle import Screen

HEIGHT = 600
WIDTH = 800


class Scr:
    def __init__(self):
        self.scr = Screen()
        self.initialize_screen()

    def initialize_screen(self):
        self.scr.title("Pong")
        self.scr.bgcolor("black")
        self.scr.setup(width=WIDTH, height=HEIGHT)
        self.scr.tracer(0)

    def screen_update(self, speed):
        self.scr.update()
        sleep(speed)

    def register_keys_r(self, board):
        self.scr.listen()
        self.scr.onkey(board.go_up, "Up")
        self.scr.onkey(board.go_down, "Down")

    def register_keys_l(self, board):
        self.scr.listen()
        self.scr.onkey(board.go_up, "w")
        self.scr.onkey(board.go_down, "s")

    def exit(self):
        self.scr.exitonclick()
