from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        for segment_index in range(3):
            self.add_segment(INITIAL_POSITIONS[segment_index])
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(*position)
        self.segments.append(new_segment)

    def extend(self):
        new_position = self.segments[-1].position()
        self.add_segment(new_position)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[segment_index - 1].position()
            self.segments[segment_index].goto(*new_position)
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
