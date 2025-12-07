import random
import turtle
from turtle import Turtle
turtle.colormode(255)

class Cars(Turtle):
    def __init__(self, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        r = random.randint(1, 230)
        g = random.randint(1, 230)
        b = random.randint(1, 230)
        self.color((r, g, b))
        self.penup()
        x_pos = random.randint(-8, 8) * 40
        self.setposition(x_pos, y_pos)
        self.setheading(180)






