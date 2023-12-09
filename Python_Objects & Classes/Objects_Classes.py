# Introduction to Classes and Objects in Python

# Python is an object-oriented programming (OOP) language, which means it uses a paradigm centered around objects and classes.

# Classes:
# A class is a blueprint or template for creating objects. It defines the structure and behavior that its objects will have.
# Think of a class as a cookie cutter, and objects as the cookies cut from that template.
# In Python, classes are created using the class keyword.

# Creating Classes:
# When you create a class, you specify the attributes (data) and methods (functions) that objects of that class will have.
# Attributes are defined as variables within the class, and methods are defined as functions.

# Example: Designing a "Car" class with attributes such as "color" and "speed," along with methods like "accelerate."

# Class Declaration
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h

    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0

    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed

# Objects:
# An object is a fundamental unit in Python that represents a real-world entity or concept.
# Objects can be tangible (like a car) or abstract (like a student's grade).

# Every object has two main characteristics:
# State: The attributes or data that describe the object.
# Behavior: The actions or methods that the object can perform.

# Instantiating Objects:
# Once you've defined a class, you can create individual objects (instances) based on that class.
# Each object is independent and has its own set of attributes and methods.

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Interacting with Objects:
# You interact with objects by calling their methods or accessing their attributes using dot notation.

# Accelerate the cars
car1.accelerate(30)
car2.accelerate(20)

# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")
