import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

MIN_DISTANCE_FOOD_SNAKE = 15
WALL_CORD = 270
RES = 600
SLEEP = 0.05
CORD_CLOSENESS = 10

def main():
    screen = turtle.Screen()
    screen.setup(width=RES, height=RES)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.tracer()
    is_game_on = True
    snake_g = Snake()
    food_g = Food()
    scoreboard_g = Scoreboard()

    screen.listen()
    screen.onkey(fun=snake_g.up, key="Up")
    screen.onkey(fun=snake_g.down, key="Down")
    screen.onkey(fun=snake_g.left, key="Left")
    screen.onkey(fun=snake_g.right, key="Right")

    while is_game_on:
        screen.update()
        time.sleep(SLEEP)
        snake_g.move()
        
        # Detect collision between Snake and Food
        if snake_g.head.distance(food_g) < MIN_DISTANCE_FOOD_SNAKE:
            scoreboard_g.increase_score()
            snake_g.extend_body()
            food_g.refresh()

        # Detect collisions between Snake and Walls
        if abs(snake_g.head.xcor()) >= WALL_CORD or abs(snake_g.head.ycor()) >= WALL_CORD:
            scoreboard_g.reset()
            snake_g.reset()
            is_game_on = False
            scoreboard_g.game_over()
        
        # Detect collisions between Snake head and tail
        for body in snake_g.full_body[1:]:            
            if snake_g.head.distance(body) < CORD_CLOSENESS:
                scoreboard_g.reset()
                snake_g.reset()
                is_game_on = False
                scoreboard_g.game_over()

    screen.exitonclick()

if __name__ == "__main__":
    main()