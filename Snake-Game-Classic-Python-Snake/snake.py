# notes
"""
in the [init] function of the class---> you can define the attributes of the class and call any of the class methods and
this class method will be executed when you call the class in the main file. Instead, you can call this method in its
position in the main file
"""
"""
Turtle(shape="square") or typing only "square" as an input
"""
""" 
[ snake.turtlesize(1, 1) ]---> it is the default size of the turtle equaling a square
, these are positional arguments-->(height, width) and you can use --> turtle.shapesize() instead
"""
"""
you can set an attribute whose value equals any of values inside a list even the list is empty 
"""
"""
[turtle.heading()] --> is an attribute -- [turtle.setheading()] --> is a method  
Also
[turtle.position()] --> is an attribute -- [turtle.goto()] --> is a method  
Also 
[turtle.xcor or ycor()] --> is attributes
"""
"""
the last item in a list has an index -1
"""

from turtle import Turtle
class Snake:

    def __init__ (self):
        self.segments = []
        self.snake_body()   # note 1
        self.head = self.segments[0]  # note 4

    def snake_body(self):
        for i in range(3):
            self.add_segment((-20*i, 0))


    def add_segment(self, position):
        snake = Turtle(shape="square")  # note 2
        snake.color("white")
        snake.penup()
        snake.turtlesize(1, 1)  # note 3
        snake.goto(position)
        self.segments.append(snake)

    def longer(self):
        self.add_segment(self.segments[-1].position())   # note 6


    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

    def up(self):
        if self.head.heading() != 270:  # note 5
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear() # to clear all the items in the list
        self.snake_body()
        self.head = self.segments[0]











