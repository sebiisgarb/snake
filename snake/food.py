import random
from scoreboard import Scoreboard
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.food_eaten()

    def food_eaten(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
