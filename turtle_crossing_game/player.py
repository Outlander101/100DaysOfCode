from turtle import Turtle

STARTING_POS = (0, -320)
PACE = 10
FINAL_POS = 320

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset()
        self.setheading(90)
    
    def move_up(self):
        self.forward(PACE)

    def player_won(self):
        return self.ycor() >= FINAL_POS
    
    def reset(self):
        self.goto(STARTING_POS)
    
