from turtle import Turtle

STARTING_POSITION= (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("brown4")
        self.penup()
        self.setheading(90)
        self.goto_start()

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE ,self.ycor())

    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE ,self.ycor())

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False