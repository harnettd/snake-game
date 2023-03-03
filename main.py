from time import sleep
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segments = []
for segment in range(3):
    segments.append(Turtle(shape="square"))
    segments[-1].color("white")
    segments[-1].penup()
    segments[-1].speed(speed="fastest")
    segments[-1].setx(x=segment * (-20))

steps_taken = 0
is_game_running = True
while is_game_running and steps_taken <= 10:
    screen.update()
    sleep(0.2)
    for segment_index in range(len(segments) - 1, 0, -1):
        new_position = segments[segment_index - 1].position()
        segments[segment_index].goto(*new_position)
    steps_taken += 1
    segments[0].left(90)
    segments[0].forward(20)

screen.exitonclick()
