from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 200)
        self.color("white")
        self.write(f"{self.l_score}   :   {self.r_score}", align="center", font=("Arial", 50, "normal"))


    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}   :   {self.r_score}", align="center", font=("Arial", 50, "normal"))

    def winner(self):
        if self.l_score == 5:
            self.goto(0, 0)
            self.write(f"Congratulations!   Left", align="center", font=("Arial", 40, "bold"))
            return True
        elif self.r_score == 5:
            self.goto(0, 0)
            self.write(f"Congratulations!   Right", align="center", font=("Arial", 40, "bold"))
            return True

