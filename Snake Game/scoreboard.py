from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(x=0, y=280)
        self.update()

    def update(self):
        self.write(arg=f"Score:  {self.score}", move=False, align="center", font=('Arial', 12, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game over! Total Score:  {self.score}", move=False, align="center",
                   font=('Arial', 20, 'normal'))
