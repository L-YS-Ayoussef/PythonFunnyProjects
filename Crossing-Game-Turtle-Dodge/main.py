from turtle import Screen
from player import Player
from score import Score
from levels import Levels
import time
import tkinter as tk

screen = Screen()
screen.setup(800, 600)
screen.title("Crossing Game")
screen.tracer(0)
screen.listen()
root = screen.getcanvas().winfo_toplevel()
root.resizable(False, False)
icon_img = tk.PhotoImage(file="turtle.png")
root.iconphoto(False, icon_img)
root._icon_img = icon_img

player = Player()

level_columns = 80
num_cars_row = 4
cars_level = Levels()
cars_list = cars_level.level(level_columns, num_cars_row)
speed_cars = 0.1

score = Score()


game_on = True
while game_on:
    screen.update()
    time.sleep(speed_cars)

    screen.onkey(player.Up, "Up")
    screen.onkey(player.Down, "Down")
    screen.onkey(player.Right, "Right")
    screen.onkey(player.Left, "Left")

    for i in cars_list:
        if i.xcor() >= -360:
            i.forward(20)
        else:
            i.setposition(350, i.ycor())
    for c in cars_list:
        if c.ycor() - player.ycor() < 20:
            if player.distance(c) < 20 or player.xcor() == c.xcor():
                game_on = False
                score.game_over()
                break

    if player.ycor() % level_columns == 0:
        score.increase_score()

    if player.ycor() > 240:
        player.hideturtle()
        player = Player()
        level_columns -= 20
        num_cars_row += 1
        cars_list = cars_level.level(level_columns, num_cars_row)
        cars_level.increase_level()
        speed_cars = cars_level.difficult()


screen.exitonclick()
