from turtle import Turtle
import random

CARS = ["car.gif", "car2.gif", "car3.gif", "car4.gif", "car5.gif"]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) in (1, 5):
            new_car = Turtle(random.choice(CARS))
            new_car.penup()
            # new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(320, random.randint(-6, 6) * 40)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                car.ht()
                self.all_cars.remove(car)
                del car
            else:
                car.bk(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
