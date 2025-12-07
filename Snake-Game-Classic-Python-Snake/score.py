# notes
"""
the default turtle color is black, so if the background is also black then [self.write()] won't appear on the screen
"""
"""
[turtle.write()] ---> like turtle draws but by writing you can select the font properties
"""


from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_score.txt") as file:
            self.high_score = int(file.read())   # when the file is empty, the string won't be converted to an integer
            # so it must at least have an integer number as a string to be converted later
        self.color("white")   # note 1
        self.hideturtle()
        self.penup()
        self.goto(0, 255)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  . High Score:{self.high_score}", align="center", font=("Arial", 24, "normal"))   # note 2

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()




 




