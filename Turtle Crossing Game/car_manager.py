import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.startingx = 300
        self.create_cars()


    def create_cars(self):
        chance = random.randint(1,6)
        if chance == 1:
            cars = Turtle()
            random_c = random.randint(0, len(COLORS) - 1)
            random_y = random.randint(-250, 250)
            cars.shape("square")
            cars.shapesize(stretch_wid=1, stretch_len=2)
            cars.penup()
            cars.color(COLORS[random_c])
            cars.goto(self.startingx, random_y)
            self.all_cars.append(cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT













