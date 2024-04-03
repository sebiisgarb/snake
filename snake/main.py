import time
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    scoreboard.show_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.head.distance(food) < 15:
        food.food_eaten()
        scoreboard.score_increase()
        snake.extend()

    #collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #collisiont with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()