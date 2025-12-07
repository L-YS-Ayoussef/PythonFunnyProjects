# notes
"""
[ screen.setup(width=100, height=100) ]--> you can type the values of method parameters as positional arguments
-->(width, height)
"""
"""
screen.tracer() ---> if the input=0 then the screen is off that nothing happens on the screen
---> to show what happened on the screen we can update the screen ---> screen.update() to sho the final screen after
editing without showing the steps of editing
"""
"""
you must delay disappearing the screen ---> [ time.sleep(amount of time) ] after updating it ---> [ screen.update() ] 
so that you can show what happened on the screen 
"""
"""
to make our snake which consists of three squares move in any direction as a piece we must make the last piece 
replace the one after that the snake can act as a piece
"""
"""
you can type the file main of the project which contains the flow of the whole project first, then type the project as 
(OOP)  
"""
"""
[ screen.onkey() ]--> you can use positional arguments--> (fun, key) 
"""
"""
[turtle.distance()]--> the arguments of this method are (x, y) or another turtle (body) 
"""
"""
using [> 290 or < -290] is the most accurate way to guarantee that the game will be over when the snake hit the wall
"""
"""
we can use the loop on the collision with tail in another way for ex.--> 

# for seg in snake.segments: 
#     if seg == snake.head:   
#         pass
#     elif snake.head.distance(seg) < 10:
#         score.game_over()
#         game_on = False
#         break

we can merge (slicing) into code above for ex.--> 

# for seg in snake.segments[1:]: 
#     if snake.head.distance(seg) < 10:
#         score.game_over()        
#         game_on = False
#         break

"""


import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import tkinter as tk

screen = Screen()
screen.setup(width=600, height=600)  # note 1
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # note 2
screen.listen()
root = screen.getcanvas().winfo_toplevel()
root.resizable(False, False)
icon_img = tk.PhotoImage(file="snake.png")
root.iconphoto(False, icon_img)
root._icon_img = icon_img

snake = Snake()
food = Food()
score = Score()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(snake.left, "Left")  # note 6

game_on = True
speed_second = 0.1
while game_on:
    screen.update()
    time.sleep(speed_second) # note 3
    snake.move()
    snake.segments[0].forward(20)
    if snake.head.distance(food) < 15:   # note 7
        food.circle_position()
        score.increase_score()
        snake.longer()
        speed_second -= 0.002
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:  # note 8
        score.reset()
        snake.reset()
    for i in range(len(snake.segments)-1):  # len(snake.segments)-1 ---> avoiding an index error (out of range)&& note 9
        if snake.head.distance(snake.segments[i + 1]) < 10:
            """[i + 1] ---> to make the loop start from the second segment and not the head cause the head hit
             any of the other segments, the game over---> if you start from the head the game won't start  
            """
            score.reset()
            snake.reset()

screen.exitonclick()
