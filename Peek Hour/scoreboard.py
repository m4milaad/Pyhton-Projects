from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.level = 1
        self.penup()
        self.ht()
        self.goto(-290, 270)
        self.write_score()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        self.level = 1
        self.clear()
        self.write_score()
