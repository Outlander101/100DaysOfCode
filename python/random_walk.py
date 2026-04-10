import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

if __name__ == "__main__":
    tim = t.Turtle()
    screen = t.Screen()
    t.colormode(255)
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    tim.speed("fastest")

    for _ in range(150):
        tim.color(random_color())
        tim.forward(50)
        tim.setheading(random.choice(directions))
    