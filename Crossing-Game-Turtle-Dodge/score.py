from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setposition(-300, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over!", align="center", font=("Arial", 60, "normal"))











