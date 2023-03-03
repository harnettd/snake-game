from time import sleep
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

the_scoreboard = Scoreboard()
the_snake = Snake()
the_food = Food()

screen.listen()
screen.onkey(fun=the_snake.up, key="Up")
screen.onkey(fun=the_snake.down, key="Down")
screen.onkey(fun=the_snake.left, key="Left")
screen.onkey(fun=the_snake.right, key="Right")

is_game_running = True
while is_game_running:
    screen.update()
    sleep(0.1)
    the_snake.move()

    if the_snake.head.distance(the_food) < 15:
        the_scoreboard.increase_score()
        the_food.refresh()

screen.exitonclick()
