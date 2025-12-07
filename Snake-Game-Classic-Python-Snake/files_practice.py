# notes --->

"""
the [read method] with files ---> return the contents of the file
"""
"""
when you open a file --> it takes up sources of your computer, do you should close it after finish
"""
"""
you can append to the file without deleting everything in the file by changing the mode to "a"
"""

"""
"/" --> forward slash refers to the root when you write the file path
fro ex.--->
[ /users/lenovo/pycharmprojects/main.py ]
"""
"""
there are two types of paths:
1) absolute file path ---> the path separated by "/"
2) relative file path ---> the path relating to a folder or another file and be written --> [ ./ ]
"""
"""
the file path in Mac separated by a forward slash "/", but in windows by a back slash '\'
but when we write the path in pycharm we use a forward slash "/" either windows or mac
"""
"""
example for using the relative file path --->

[ /Users/LondonAppBrewery/Desktop/file.txt]  the path of a file wanted to call in main.py
[ /Users/LondonAppBrewery/pycharmProjects/WindowsDemo/main.py ] the main.py path 

to call the first file relating to main.py, first ---
--> think of the path of main.py and how to come back to the common root with the file wanted to call 
---> to come back you write --> [ ../ ] for one back, so 
------> [ ../../Desktop/file.txt] this is the relative path of the file wanted to call 
"""
"""
the difference between the absolute and relative file path is that the absolute file path is always relative to 
the root folder, but the relative file path is relative to where you are and where you want to go 
"""




"""
file = open("file_for_practice")
contents = file.read()   # note 1
print(contents)
file.close()  # note 2
"""

# you can write the code above in another way for ex.--->
# with open("file_for_practice.txt", mode="a") as file:
#     # here you don't have to close the file, cause this way can control your file
#     file.write("leader Youssef")  # .write ---> write in the line
#     file.write("\nyoussef")







