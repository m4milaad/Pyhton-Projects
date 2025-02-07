from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.high_score = 0
        self.read_highscore()
        self.score = 0
        self.color("white")
        self.goto(x=0, y=280)
        self.update()

    def read_highscore(self):
        try:
            with open("highscore.txt", "r") as highscore:
                content = highscore.read()
                if content:
                    self.high_score = int(content)
                else:
                    self.high_score = 0
        except FileNotFoundError:
            self.high_score = 0

    def write_highscore(self):
        with open("highscore.txt", "w+") as highscore:
            highscore.write(str(self.high_score))

    def update(self):
        self.clear()
        self.write(arg=f"Score:  {self.score}           High Score: {self.high_score}", move=False, align="center",
                   font=('Arial', 12, 'normal'))

    def add_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game over! Total Score:  {self.score}", move=False, align="center",
                   font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore()
        self.score = 0
        self.update()
