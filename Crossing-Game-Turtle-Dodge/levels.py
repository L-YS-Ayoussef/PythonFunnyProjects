from turtle import Turtle
from cars import Cars
import random


class Levels(Turtle):

    def __init__(self):
        super().__init__()
        self.level_num = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setposition(300, 260)
        self.write(f"Level: {self.level_num}", align="center", font=("Arial", 20, "normal"))
        self.sp = 0.1


    def level(self, level_columns, num_cars_row):
        car = []
        for y in range(-220, 240, level_columns):
            num = random.randint(num_cars_row, 10)
            for x in range(num):
                cars = Cars(y)
                car.append(cars)
        return car

    def increase_level(self):
        self.level_num += 1
        self.clear()
        self.write(f"Level: {self.level_num}", align="center", font=("Arial", 20, "normal"))

    def difficult(self):
        self.sp -= 0.02
        return self.sp











