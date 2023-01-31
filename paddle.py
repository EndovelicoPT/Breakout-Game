from turtle import Turtle
STEPS = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.penup()
        self.goto(position)

    def move_right(self):
        x_cor = self.xcor() + STEPS
        if x_cor > 585:
            x_cor = 585
        self.setx(x_cor)

    def move_left(self):
        x_cor = self.xcor() - STEPS
        if x_cor < -585:
            x_cor = -585
        self.setx(x_cor)