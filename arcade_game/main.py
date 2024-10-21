from turtle import Screen
from player import Player
from ball import Ball
import time
from scoreboard import Score

XCOR = 380
YCOR = 0



screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.listen()
screen.title("Pong")
screen.tracer(0)


player = Player((XCOR, YCOR))

enemy = Player((-XCOR,YCOR))

ball = Ball()

score_board = Score()




screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_forward, "Left")
screen.onkey(player.go_backward, "Right")



screen.onkey(enemy.go_up, "w")
screen.onkey(enemy.go_down, "s")
screen.onkey(enemy.go_forward, "a")
screen.onkey(enemy.go_backward, "d")

game_is_on= True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # detect wall's collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collison with players
    if ball.distance(player)< 30  or ball.distance(enemy)< 30 :
        ball.bounce_x()

    if ball.xcor()> XCOR:
        ball.reset_position()
        score_board.enemy_scored()
    elif ball.xcor() < -XCOR:
        ball.reset_position()
        score_board.player_scored()

screen.exitonclick()