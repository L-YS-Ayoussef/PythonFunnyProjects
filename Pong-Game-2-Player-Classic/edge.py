from turtle import Turtle

class Edge(Turtle):
    def __init__(self, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 40)
        self.setposition(0, y_pos)
        self.penup()






