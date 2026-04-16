from turtle import Turtle

PACE = 10
BALL_SPEED = 0.1
DELTA_SPEED = 0.5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("white")
        self.xmove = PACE
        self.ymove = PACE
        self.ballspeed = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.ballspeed *= DELTA_SPEED
    
    def change_balldir(self):
        self.home()
        self.ballspeed = BALL_SPEED
        self.bounce_x()
