from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-200, 280)
        self.write(f"Score: {self.left_score}", False, "Center")
        self.goto(200, 280)
        self.write(f"Score: {self.right_score}", False, "Center")

    def score_update(self, cor):
        if cor > 0:
            self.left_score += 1
        elif cor < 0:
            self.right_score += 1
        self.clear()
        self.write_score()
