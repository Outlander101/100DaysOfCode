from turtle import Turtle
import random

FOOD_PERC_STRETCH = 0.5
RANGE_SCREEN = 260

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=FOOD_PERC_STRETCH, stretch_wid=FOOD_PERC_STRETCH)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-1 * RANGE_SCREEN, RANGE_SCREEN)
        y_axis = random.randint(-1 * RANGE_SCREEN, RANGE_SCREEN)
        self.goto(x=x_axis, y=y_axis)