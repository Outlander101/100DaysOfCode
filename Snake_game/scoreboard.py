import os
from turtle import Turtle

SCORE_X_CORD = 0
SCORE_Y_CORD = 270
FONT_ALIGNMENT = "center"
FONT = ("Arial", 22, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.valid_file("high_score.txt")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_X_CORD, SCORE_Y_CORD)
        self.update_scoreboard()

    def valid_file(self, s_file):
        if os.path.exists(s_file):
            with open(s_file) as file:
                try:
                    self.high_score = int(file.read())
                except ValueError:
                    self.high_score = 0
        else:
            self.high_score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=FONT_ALIGNMENT, font=(FONT))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("Game Over", align=FONT_ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.update_file()

    def update_file(self):
        with open("high_score.txt", mode='w') as file:
           # file.write(str(self.high_score))
           file.write(f"{self.high_score}")
    

