from turtle import Turtle

SCORE_X_CORD = 0
SCORE_Y_CORD = 270
FONT_ALIGNMENT = "center"
FONT = ("Arial", 22, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_X_CORD, SCORE_Y_CORD)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=FONT_ALIGNMENT, font=(FONT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("Game Over", align=FONT_ALIGNMENT, font=FONT)
    

