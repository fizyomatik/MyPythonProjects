from turtle import Turtle

class Player(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y= self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def go_forward(self):
        new_x= self.xcor() - 20
        self.goto(new_x,self.ycor())
    def go_backward(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

