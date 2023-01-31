from turtle import Screen
import time
from ball import Ball
from scoreboard import Scoreboard
from brickwall import Walls
from paddle import Paddle

screen = Screen()
screen.setup(1300, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((0, -280))
ball = Ball()
wall_manager = Walls()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

#Coordinates for the bricks
ycor = 240
xcor = range(-585, 585, 88)

for x in xcor:
    wall_manager.create_walls(xcor=x, ycor=ycor)
    wall_manager.create_walls(xcor=x, ycor=200)
    wall_manager.create_walls(xcor=x, ycor=160)
    wall_manager.create_walls(xcor=x, ycor=120)
    wall_manager.create_walls(xcor=x, ycor=80)

#Game setup
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(paddle)

    if ball.ycor() < -320:
        ball.reset()

    for wall in wall_manager.all_walls:
        if wall.distance(ball) < 30 or wall.distance(ball.xcor() - 30, ball.ycor())\
             < 30 or wall.distance(ball.xcor() + 30, ball.ycor()) < 30:
            ball.bounce_y_wall()
            wall_manager.delete_wall(wall)
            scoreboard.level_up()

screen.exitonclick()