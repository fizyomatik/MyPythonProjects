import random
from turtle import Turtle

COLORS = ["red","green","black", "white", "brown","brown4","AliceBlue","aquamarine", "DeepPink","cyan","coral", "chartreuse", "chocolate","DarkGrey", "DarkSlateGray1"]
STARTING_MOVE_DISTANCE =5
MOVE_INCREMENT = 10

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_change = random.randint(1,6)
        if random_change == 1:
            new_car =Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y =random.randint(-200,200)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)



    def level_up(self):
        self.car_speed +=  MOVE_INCREMENT