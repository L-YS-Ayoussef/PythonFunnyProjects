# notes -->

# part 1 ---> notes concerning for tkinter and some built functions in python
"""
when you set the grid of a widget the width of the widget will be the width of the widget, and it will affect the other
widgets in the same column, so to solve this problem---> there is a parameter of the method "grid" called ( columnspan )
--> this parameter means how many columns will the widget span for example -->
[ widget.grid(row=0, column=0, columnspan=2) ] ---> this widget will have two columns starting from the column 0
"""

"""
to make the cursor already in a textbox -->
.focus()
"""

"""
you can delete the data in a textbox --->
.delete(first index, last index)
## if you don't writs the last index, it automatically will delete a character
"""

"""
** there is something in tkinter called --> ( Standard Dialogs "popups" ) ---> [ message boxes ]
** to import a messagebox ---> [ from tkinter import messagebox ]
even there is an import for the * (everything in the module), because import * --> 
means import all the classes and constants of the tkinter not something like "messagebox"
** there are different types of the messagebox (showinfo, askyesno, askretrycancel, showerror, showwarning)
"""

"""
** there is an inbuilt function in python called [ .join() ] -- it is used in this way --->
** new_item = string.join(python sequence)   *#* python sequences ---> iterable types ---> (list, tuple, range)
---> it will give
new_item(a string of the joined items of the python sequence) separated by the string
"""

"""
to make what in a textbox be copied to the clipboard we have to import the module( pyperclip ) and it has two methods-->
1) pyperclip.copy("the text wanna be copied")
2) pyperclip.paste() to paste the copied text
"""


# part 2 ---> CATCHING ERRORS & EXCEPTIONS
"""
there are four keywords concerning this part -->
1) try: [ do something might have an error ]
2) except: [ if there is an error, do this ]
3) else: [ if there was no any error, do this ]
4) finally: [ do something whatever what happened ]
"""

"""
** you can define the type of the error after ( except )-->
--> it means that you will try to execute some codes if there is an error you define, there are codes will be executed
** for example --> 
except KeyError:   # "KeyError" is a class
"""

"""
** also you can do --> 
except KeyError as error_message: ---> here the variable (error_message) carries the name of the KeyError 
** when you use "as" after the type of the error,
the variable's value will be the value of the error found in the console
"""

"""
when you use "else" --> its codes will be executed if there is no any error and also the codes of "try" will be executed
"""

# for example <---------------->
"""
try:
    file = open("lysa.txt")
    file.write("Youssef")
    print(file.read)
except KeyError as file_error:
    print(f"no{file_error}")
else:
    print("yes")
finally:
    print("jaaa")
"""

"""
** you can raise or make you own exceptions using the condition ( raise )
** for example --> 
raise KeyError(string or something) ---> this cose will cause an error whose type is KeyError and its value is what
inside the parentheses
"""


# part 3 ---> DEALING WITH ( JSON ) DATA
"""
** dealing with "text files" for searching is complex, so we can deal with ( JSON files ) for searching
** ( JSON ) --> stands for ( Javascript Object Notation )
"""

# we can use a JSON file to read or write or update-->
"""
1) write --> first set the mode of the file to "w"
then, --> [ json.dump(what you will write, the location, parameter called [indent] ) ]
** what you will write --> you have to write a nested dictionary you create in the json file 
** this parameter [indent] --> provides the number of spaces to indent all the json data to make it easier to read 
** you can't write in the JSON file itself you must update data and rewrite it
** the mode "w" --> delete what in the file then start writing over
"""

"""
2) read ---> first set the mode of the file to "r"
then, ---> [ data = json.load(the file name) ]
** data here is a dictionary
"""

"""
3) update --> this goal needs five steps -->

1) open the file in "r" mode
2) read the old data ---> [ data_file = json.load(the file name) ]
3) update the old data ---> [ data_file.update(new_data which is a nested dictionary) ]
4) open the file in "w" mode
5) write the nem data in the file ---> [ json.dump(data_file, the file name) ]
"""


