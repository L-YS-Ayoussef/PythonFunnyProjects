from turtle import Turtle
class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5)
        self.setposition(x_pos, 0)
        self.right(90)
        self.color("white")
        self.penup()
        self.speed(0)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)



















