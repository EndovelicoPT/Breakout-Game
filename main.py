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

        if self.distance(paddle) < 31:
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
    
    def create_walls(self, xcor, ycor):
        for num in range(1, 8):
            new_wall = Turtle('square')
            new_wall.shapesize(stretch_wid=1, stretch_len=4)
            new_wall.penup()
            new_wall.color(random.choice(COLORS))
            new_wall.goto(xcor, ycor)
            self.all_walls.append(new_wall)

    def delete_wall(self, wall):
        wall.goto(-20, -800)
        #for walls in self.all_walls:
         #   walls.goto(xcor, ycor)



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

ycor = 240
xcor = range(-585, 585, 92)

for x in xcor:
    wall_manager.create_walls(xcor=x, ycor=ycor)
    wall_manager.create_walls(xcor=x+25, ycor=200)
    wall_manager.create_walls(xcor=x, ycor=160)
    wall_manager.create_walls(xcor=x+25, ycor=120)
    wall_manager.create_walls(xcor=x, ycor=80)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(paddle)

    if ball.ycor() < -320:
        ball.reset()

    for wall in wall_manager.all_walls:
        if wall.distance(ball) < 31:
            ball.bounce_y_wall()
            wall_manager.delete_wall(wall)

    


screen.exitonclick()