from turtle import Screen
from turtle import Turtle
import time
import random

STEPS = 20
COLORS = ["yellow", "green", "purple", "orange", "blue", "red"]


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


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self, paddle):
        new_y = self.ycor() - self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

        if self.xcor() > 605 or self.xcor() < -605:
            self.bounce_x_wall()
        
        if self.ycor() > 290:
            self.bounce_y_wall()

        if self.distance(paddle) < 10:
            self.bounce_y()

    def bounce_x(self):
        self.x_move *= -1

    def bounce_x_wall(self):
        self.x_move *= -1

    def bounce_y_wall(self):
        self.y_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1


class Walls:
    def __init__(self):
        self.all_walls = []
    
    def create_walls(self):
        new_wall = Turtle('square')
        new_wall.shapesize(stretch_wid=1, stretch_len=2)
        new_wall.penup()
        new_wall.color(random.choice(COLORS))
        new_wall.goto(595, 250)


screen = Screen()
screen.setup(1300, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((0, -280))
ball = Ball()
wall_manager = Walls()
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(paddle)

    if ball.distance(paddle) < 31:
        ball.bounce_y()

    if ball.ycor() < -320:
        ball.reset()


screen.exitonclick()