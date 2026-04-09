import turtle as t
import random

if __name__ == "__main__":
    tim = t.Turtle()
    screen = t.Screen()
    t.colormode(255)
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    tim.speed("fastest")

    for _ in range(150):
        tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tim.forward(50)
        tim.setheading(random.choice(directions))
    