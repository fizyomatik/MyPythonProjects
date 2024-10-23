from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update()


    def update(self):
        self.clear()
        self.goto(-300, 200)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 40, "normal"))


    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 40, "normal"))
