from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

INITIAL_POS = 350
WALL_CORD = 280
MIN_BALL_PADDLE_DISTANCE = 50
PADDLE_CORD_LIMIT = 320
MAX_BALL_LIMIT = 380

def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((INITIAL_POS, 0))
    l_paddle = Paddle((-1 * INITIAL_POS, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')

    is_game_on = True
    while is_game_on:
        time.sleep(ball.ballspeed)
        screen.update()
        ball.move()

        # Detect Collision between ball and upper/lower walls
        if ball.ycor() > WALL_CORD or ball.ycor() < -1 * WALL_CORD:
            ball.bounce_y()
        
        # Detect Collision between ball and left/right paddles
        if ball.distance(r_paddle) < MIN_BALL_PADDLE_DISTANCE and ball.xcor() > PADDLE_CORD_LIMIT or ball.distance(l_paddle) < MIN_BALL_PADDLE_DISTANCE and ball.xcor() < -1 * PADDLE_CORD_LIMIT:
            ball.bounce_x()

        # Detect when paddle misses the ball on right
        if ball.xcor() > MAX_BALL_LIMIT:
            ball.change_balldir()
            scoreboard.increase_lscore()

        # Detect when paddle misses the ball on left
        if ball.xcor() < -1 * MAX_BALL_LIMIT:
            ball.change_balldir()
            scoreboard.increase_rscore()

    screen.exitonclick()

if __name__ == "__main__":
    main()