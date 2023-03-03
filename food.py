from numpy.random import randint
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.speed(speed="fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        rand_pos = (randint(-280, 280), randint(-280, 280))
        self.goto(*rand_pos)
