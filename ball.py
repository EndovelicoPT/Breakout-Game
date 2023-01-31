from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.06

    def move(self, paddle):
        new_y = self.ycor() - self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

        if self.xcor() > 605 or self.xcor() < -605:
            self.bounce_x_wall()
        
        if self.ycor() > 290:
            self.bounce_y_wall()

        if self.distance(paddle) < 30 or self.distance(paddle.xcor() - 30, paddle.ycor())\
             < 30 or self.distance(paddle.xcor() + 30, paddle.ycor()) < 30:
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
        #self.move_speed = 0.1
        self.x_move *= -1