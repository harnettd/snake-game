from time import sleep
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

the_snake = Snake()

steps_taken = 0
is_game_running = True
while is_game_running and steps_taken <= 10:
    screen.update()
    sleep(1)
    the_snake.move()
    steps_taken += 1

screen.exitonclick()
