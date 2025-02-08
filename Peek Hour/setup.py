from turtle import Screen

SHAPES = ["car.gif", "car2.gif", "car3.gif", "car4.gif", "car5.gif", "p_back.gif", "road.gif"]


class Setup:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgpic("road.gif")
        self.screen.tracer(0)
        for shape in SHAPES:
            self.screen.register_shape(shape)

    def register_keys(self, player):
        self.screen.listen()
        self.screen.onkey(player.go_up, "Up")
        self.screen.onkey(player.go_down, "Down")

    def update_screen(self):
        self.screen.update()
