from snake import Snake

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
UPDATE_DELAY = 0.1

from turtle import Screen
import time


class Scr:
    def __init__(self):
        self.screen = Screen()
        self.initialize_screen()

    def initialize_screen(self):
        self.screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.title("Snake")

    def screen_update(self):
        self.screen.update()
        time.sleep(UPDATE_DELAY)

    def register_keys(self, snake):
        self.screen.listen()
        self.screen.onkey(fun=snake.up, key="Up")
        self.screen.onkey(fun=snake.down, key="Down")
        self.screen.onkey(fun=snake.left, key="Left")
        self.screen.onkey(fun=snake.right, key="Right")

    def take_input(self):
        return self.screen.textinput(
            "Action Required", 'Press "t" to try again or "q" to quit'
        )
