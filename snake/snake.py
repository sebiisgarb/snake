from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTNACE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("square")

    def create_snake(self):
        for positions in START_POSITION:
            self.add_segment(positions)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(DISTNACE)

    def up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return
        self.segments[0].setheading(0)