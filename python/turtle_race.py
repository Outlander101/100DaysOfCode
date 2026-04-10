import turtle as t
import random

def main():
    screen = t.Screen()
    screen.setup(width=500, height=400)
    is_race_on = False
    user_bet = screen.textinput(title="Turtle bet", prompt="Enter your bet: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-80, -40, -10, 20, 50, 80]
    turtles = []

    for turtle_index in range(0, 6):
        new_turtle = t.Turtle("turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        turtles.append(new_turtle)
    
    if user_bet:
        is_race_on = True
    
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won!. The {winning_color} turtle is the winner")
                else:
                    print(f"You've lost!. The {winning_color} turtle is the winner")
            pace = random.randint(0, 10)
            turtle.forward(pace)


    screen.exitonclick()

if __name__ == "__main__":
    main()