import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from setup import Setup

scr = Setup()
player = Player()
car = CarManager()
scoreboard = Scoreboard()
scr.register_keys(player)

while True:
    time.sleep(0.05)
    car.move()
    car.create_car()
    scr.update_screen()
    for each_car in car.all_cars:
        if each_car.distance(player) < 15:
            user = scr.screen.textinput("Action Required", 'Press "t" to try again or "q" to quit').lower()
            if user == "t":
                scr.register_keys(player)
                player.go_to_start()
                scoreboard.reset()
            elif user == "q":
                scr.screen.bye()
                break
            else:
                print("Invalid Option!")
                scr.screen.bye()
                break
    if player.at_finish_line():
        player.go_to_start()
        car.increase_speed()
        scoreboard.level_up()

