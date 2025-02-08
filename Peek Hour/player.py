from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("p_back.gif")
        self.penup()
        self.go_to_start()
        self.left(90)

    def go_up(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.fd(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -270:
            self.bk(MOVE_DISTANCE)

    def at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
