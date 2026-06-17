class Car:
   def __init__(self, color):
       self.color = color

   def drive(self):
       print("The car is driving!")

car1 = Car("red")
car2 = Car("blue")

print(car1.color)  # red
print(car2.color)  # blue

car1.drive()       # The car is driving!


"""
class Car: creates a blueprint called Car.
__init__ runs when a new object is created.
self refers to the specific object being created or used.
self.color stores data on that object.
drive() is a method (a function that belongs to the class).


Think of a cookie cutter:

The cookie cutter = class
Each cookie made from it = object


"""