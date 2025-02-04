from turtle import Turtle


class Board(Turtle):
    def __init__(self, xcord):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(xcord, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def collision(self):
        pass