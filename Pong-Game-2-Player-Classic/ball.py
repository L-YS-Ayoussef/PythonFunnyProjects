# Notes-->
"""
you can change the heading of the turtle by-->
1) dealing with the angle --> change the angle then forward
2) dealing with the xy position --> change xy position direct
"""

from turtle import Turtle


class Ball(Turtle):
    def __init__(self, start):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.setposition(0, 0)
        self.setheading(start)
        self.penup()

    def move(self, turn):
        self.left(turn)
        self.forward(20)

    def bounce(self, ff, ttf, otf, tof):
        if self.heading() == 45:
            self.move(ff)
        elif self.heading() == 225:
            self.move(ttf)
        elif self.heading() == 135:
            self.move(otf)
        elif self.heading() == 315:
            self.move(tof)

    def spe(self):
        if self.speed() < 10:
            sp = self.speed() + 1
            self.speed(sp)
        else:
            self.speed(0)
