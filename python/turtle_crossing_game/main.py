import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

RESOLUTION = 700
REFRESH_SPEED = 0.1

def main():
    screen = Screen()
    screen.setup(width=RESOLUTION, height=RESOLUTION)
    screen.tracer(0)

    player = Player()
    cars = CarManager()
    score = ScoreBoard()

    screen.listen()
    screen.onkey(player.move_up, "Up")

    is_game_on = True
    while is_game_on:
        time.sleep(REFRESH_SPEED)
        screen.update()
        
        cars.create_car()
        cars.move()

        # Detect Collisions between Turtle and Cars.
        for car in cars.all_cars:
            if car.distance(player) < 30:
                is_game_on = False
                score.game_over()

        # Detect if player won the round
        if player.player_won():
            cars.level_up()
            score.level_up()
            player.reset()

    screen.exitonclick()

if __name__ == "__main__":
    main()
