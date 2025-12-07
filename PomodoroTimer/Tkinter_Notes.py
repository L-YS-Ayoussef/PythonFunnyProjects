# notes--->

"""
Canvas is a widget allowing you to layer things one on top of the others-->
you can draw something and draw something on the top of that
"""

"""
the parameter (image) in the class (Canvas)--> 
when you type---> [ image="tomato.png" ]--> there is an error that the parameter doesn't expect the string type
, So --->
you can use the class ---> [ photoImage(file="tomato.png") ] and assign it to an object
and this object will be the argument of the parameter (image)
"""

"""
when you use the class "Canvas" --> it is a class, so you have to set its position -->[ .pack() ]
in this canvas you can create a text or an image and they will layout according to the X & Y positions
"""

"""
there are standard attributes used for all of the widgets,
and there are specific attributes used only for a specific widget
"""

"""
there is a parameter called [ highlightthickness ]--> it is used to set the thickness of the border of the widget.
when its value = 0 ---> there won't be a border not any separator between the background of the widget and the window 
"""

"""
programs used [ window.mainloop() ] are called [ Event Driven ], that we have top loop on the window to watch what
happened
"""

"""
[ window.after() ]---> is a method executing a function after a piece of seconds 
"""

"""
if you wanna change the value of a parameter of a method of an object ---> you can 
[ object.config(parameter= new value) ], but if this object is the class Canvas and called canvas ---> you will 
[ canvas.itemconfig(itemname, parameter= new value) ]
the item above means an attribute
"""

"""
Python Dynamic Typing ---> 
it is to change the data type by changing the content of this data
--> python is flexible when dealing with data types unlike the other languages like C, Java that data type is constant
through the program
"""

"""
you can assign the timer in [note 7] to a variable and -->
[ window.after_cancel(the timer) ]--> it will stop the timer 
and you can assign none value to the timer in the main script as a global scope and globalize it inside the function 
and use it
"""





