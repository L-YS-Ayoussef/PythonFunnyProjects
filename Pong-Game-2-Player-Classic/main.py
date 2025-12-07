# Notes --->
"""
you can use [ screen.setup(width= , height=) ] instead of--> [screen.screensize(800, 600) its parameters-->
(canvwidth= , canvheight=) ]
--->but they are different--->
[ screen.setup(width= , height=) ] ---> display the screen without scroll bar. Unlike -->[ screen.screensize(800, 600) ]
"""
"""
you can create many paddles that are different in the x_position by making the x_position be an input 
"""
"""
you can control the animation of any game by using--> [screen.tracer(0)] && [screen.update()] to watch the change on the 
screen and you have to put this change inside the loop with [screen.update()] and set the time so that you can watch it
"""
"""
you can't use keyboard in the game if you used--> [screen.textinput(title=, prompt=)] 
because --> the keyboard here is dealing with the windows of the textinput not the game
"""


from turtle import Screen
from paddle import Paddle
from ball import Ball
from edge import Edge
from score import Score
import time
import tkinter as tk

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)  # note 1
screen.title("Pong Game")
screen.tracer(0)
screen.listen()
# r_player = screen.textinput(title="Right Player", prompt="Enter your name! ")   # note 4
# l_player = screen.textinput(title="Left Players", prompt="Enter your name! ")

root = screen.getcanvas().winfo_toplevel()
root.resizable(False, False)

icon_img = tk.PhotoImage(file="pingpong.png")
root.iconphoto(False, icon_img)
root._icon_img = icon_img

edge_top = Edge(290)
edge_bottom = Edge(-290)

r_paddle = Paddle(x_pos=350)  # note 2
l_paddle = Paddle(x_pos=-350)

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball(45)
score = Score()


game_on = True
while game_on:
    screen.update()  # note 3
    time.sleep(0.1)
    ball.forward(20)
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce(270, 270, 90, 90)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce(90, 0, 0, 270)
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce(0, 90, 270, 0)
    if ball.xcor() > 380:
        score.l_score += 1
        score.update_score()
        ball.hideturtle()
        ball.spe()
        if score.winner():
            break
        else:
            ball = Ball(225)
            ball.speed()
    elif ball.xcor() < -380:
        score.r_score += 1
        score.update_score()
        ball.hideturtle()
        ball.spe()
        if score.winner():
            break
        else:
            ball = Ball(45)


screen.exitonclick()
