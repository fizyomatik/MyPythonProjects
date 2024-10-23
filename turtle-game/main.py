from turtle import Screen
from player import Player
from car import Car
from level import Level
import time

screen = Screen()
screen.bgcolor("bisque")
screen.setup(800,600)
screen.title("Turtle Cross")
screen.listen()
screen.tracer(0)

player = Player()
car = Car()
level =Level()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


game_is_on =True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            level.game_over()


    if player.is_at_finish_line():
        player.goto_start()
        car.level_up()
        level.level_up()




screen.exitonclick()