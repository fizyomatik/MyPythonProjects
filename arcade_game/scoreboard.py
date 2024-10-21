from turtle import Turtle


class Score(Turtle):
    def __init__(self):
       super().__init__()
       self.color("white")
       self.penup()
       self.hideturtle()
       self.player_score = 0
       self.enemy_score = 0
       self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.enemy_score, align="center", font = ("Courier", 80,"normal"))
        self.goto(100, 200)
        self.write(self.player_score, align="center", font=("Courier", 80, "normal"))

    def player_scored(self):
        self.player_score +=1
        self.update()

    def enemy_scored(self):
        self.enemy_score +=1
        self.update()