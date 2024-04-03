from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x=0, y=270)
        self.color("White")

    def score_increase(self):
        self.clear()
        self.score += 1

    def show_score(self):
        self.write(f"Score: {self.score}", align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center")
