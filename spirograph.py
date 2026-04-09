import turtle as t
import random

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(gap_between_circle):
    tim = t.Turtle()
    screen = t.Screen()
    t.colormode(255)
    tim.speed("fastest")
    for _ in range(int(360/gap_between_circle)):
        tim.color(change_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_between_circle)
    screen.exitonclick()

if __name__ == "__main__":
    gap_bt_circle = 5 # input(int("Enter the expected gap between circles in Spirograph: "))
    draw_spirograph(gap_bt_circle)