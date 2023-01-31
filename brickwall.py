from turtle import Turtle
import random

COLORS = ["yellow", "green", "purple", "orange", "blue", "red"]

class Walls:
    def __init__(self):
        self.all_walls = []
    
    def create_walls(self, xcor, ycor):
            new_wall = Turtle('square')
            new_wall.shapesize(stretch_wid=1, stretch_len=4)
            new_wall.penup()
            new_wall.color(random.choice(COLORS))
            new_wall.goto(xcor, ycor)
            self.all_walls.append(new_wall)

    def delete_wall(self, wall):
        wall.goto(-20, -800)