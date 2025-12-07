# notes
"""
the arguments of the method shapesize or turtlesize---> 10 pixels = 0.5
"""
"""
in this project--> we have two turtles (snake & food) so that we can make collisions between them
that we didn't use [turtle.dot(size, color)] cause it is a drawing not a body 
"""
"""
we didn't use [random.randint(-300, 300)] ---> the dot might be at the edge of the screen that it will be hard for
the snake to capture it, so we used [random.randint(-280, 280)] instead
"""

import random
from turtle import Turtle, Screen

class Food(Turtle):   # using inheritance

    def __init__(self):
        super().__init__()
        self.shape("circle")    # note 2
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)   # note 1
        self.speed(0)
        self.color("blue")
        self.circle_position()

    def circle_position(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)  # note 3












