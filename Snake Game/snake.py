from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def add_segment(self, pos):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].xcor(), self.segments[seg - 1].ycor())
        self.segments[0].fd(MOVE_DIST)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)
