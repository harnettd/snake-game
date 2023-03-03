from turtle import Turtle

POSITION = (0, 275)
ALIGNMENT="center"
FONT=("Monospace", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(*POSITION)
        self.color("white")
        self.score = 0
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()
