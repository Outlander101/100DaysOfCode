from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
CLOSURE_POSITION = (-1000,1000)

class Snake:

    def __init__(self):
        self.full_body = []
        self.create_snake()
        self.head = self.full_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_body(position) 
        
    def add_body(self, position):
        snake_body = Turtle("square")
        snake_body.hideturtle()
        snake_body.color("white")
        snake_body.penup()
        snake_body.pensize(5)
        snake_body.goto(position)
        snake_body.showturtle()
        self.full_body.append(snake_body)

    def extend_body(self):
        self.add_body(self.full_body[-1].position())

    def move(self):
        for body in range(len(self.full_body) - 1, 0, -1):
            new_x = self.full_body[body - 1].xcor()
            new_y = self.full_body[body - 1].ycor()
            self.full_body[body].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for body in self.full_body:
            body.goto(CLOSURE_POSITION)
        self.full_body.clear()
        self.create_snake()
        self.head = self.full_body[0]