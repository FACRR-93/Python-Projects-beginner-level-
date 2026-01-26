import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
iteration = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:

    cars.create_cars()
    cars.move_cars()

    time.sleep(0.1)
    screen.update()

    for i in range(0, len(cars.all_cars) -1):
        if cars.all_cars[i].distance(player) < 25:
            score.gameover()
            screen.exitonclick()

    if player.ycor() > 280:
        score.count()
        player.reset()
        cars.level_up()

