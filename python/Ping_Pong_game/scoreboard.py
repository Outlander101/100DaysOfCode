from turtle import Turtle

X_POSITION = 100
Y_POSITION = 200
FONT = ("Courier",40,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    
    def increase_lscore(self):
        self.l_score += 1
        self.refresh()

    def increase_rscore(self):
        self.r_score += 1
        self.refresh

    def refresh(self):
        self.clear()
        self.goto(-1 * X_POSITION, Y_POSITION)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(X_POSITION, Y_POSITION)
        self.write(self.r_score, align="center", font=FONT)
