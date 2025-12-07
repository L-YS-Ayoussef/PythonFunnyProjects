from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.speed(0)
        self.penup()
        self.setposition(0, -280)
        self.left(90)
        self.shapesize(1, 1)

    def Up(self):
        self.setheading(90)
        self.forward(20)

    def Down(self):
        self.setheading(270)
        self.forward(20)

    def Right(self):
        self.setheading(0)
        self.forward(20)

    def Left(self):
        self.setheading(180)
        self.forward(20)

