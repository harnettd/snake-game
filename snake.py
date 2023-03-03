from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        for segment_index in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(*INITIAL_POSITIONS[segment_index])
            self.segments.append(new_segment)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[segment_index - 1].position()
            self.segments[segment_index].goto(*new_position)
        self.segments[0].forward(MOVE_DISTANCE)
