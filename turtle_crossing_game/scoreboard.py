from turtle import Turtle

INT_LEVEL = 1

FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = INT_LEVEL
        self.hideturtle()
        self.penup()
        self.goto(-280,280)
        self.refresh()
        
    def level_up(self):
        self.level += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)
