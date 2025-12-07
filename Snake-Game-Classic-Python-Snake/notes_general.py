# general notes concerning for OOP

# 1 ---> Class Inheritance
"""
# inheritance includes the appearance (attributes) and behaviour (methods)
"""
# for example--->
"""
class Animal:  # the mother class which will inherit (give) its contents to the fish class (daughter)
    def __init__(self):  # defining the attributes of the Animal class
        self.num_eyes = 2
    def breathe(self):  # defining the method breathe of the Animal class
        print("Inhale, exhale.")
class Fish(Animal):   # the class Animal inside the parentheses referring to that the class fish will take the class Animal contents
    def __init__(self):
        super().__init__()   # super(). ---> referring to the class Animal
    def breathe(self):
        super().breathe()   # to call the method breathe in the Animal class
        print("doing this underwater.")
    def swim(self):        # an independent method inside the Fish class
        print("moving in water.")
nemo = Fish()
animal = Animal()
print(nemo.num_eyes)
print(animal.num_eyes)
nemo.swim()
nemo.breathe()
animal.breathe()

### the code above will print--->
'''
2
2
moving in water.
Inhale, exhale.
doing this underwater.
Inhale, exhale.
'''
"""

# ---------------------------------------------------------------------------------------------------------------------

# 2 ---> Slicing
"""
this concept in python means that you can take some of the variables of a list and work with them solo 
slicing can act with lists, tuples. 
"""
# for example -->
"""
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
slice = piano_keys[0:4]
print(slice)

### the code will print ---> ['a', 'b', 'c', 'd']
"""

# [2:] ---> from position 2 to the end of the list
#[2:5:2] ---> indexes -> (2, 4)

# piano_list--> 7 items
# [::2] ---> indexes -> (0, 2, 4, 6)
# [::-1] ---> it will reverse the order of the list items





