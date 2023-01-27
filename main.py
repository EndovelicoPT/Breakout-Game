from turtle import Screen
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


screen = Screen()
screen.setup(1300, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player = Paddle((0, -280))
screen.listen()
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_left, "Left")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()