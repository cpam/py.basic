# Python Exception Handling Overview

# This Python file summarizes the key concepts of exception handling in Python, 
# including common exceptions and the use of try-except blocks.

# ------------------------------
# Common Exceptions in Python
# ------------------------------

# 1. ZeroDivisionError
# Occurs when a number is divided by zero.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError: Cannot divide by zero.")

# 2. ValueError
# Arises when a function receives an argument with the right type but inappropriate value.
try:
    num = int("abc")
except ValueError:
    print("Caught ValueError: Invalid input for integer conversion.")

# 3. FileNotFoundError
# Encountered when trying to access a file that does not exist.
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Caught FileNotFoundError: The file does not exist.")

# 4. IndexError
# Occurs when trying to access an item at an invalid index.
my_list = [1, 2, 3]
try:
    missing = my_list[5]
except IndexError:
    print("Caught IndexError: Index out of range.")

# 5. KeyError
# Arises when a dictionary key is not found.
my_dict = {"name": "Alice", "age": 30}
try:
    missing = my_dict["city"]
except KeyError:
    print("Caught KeyError: Key not found in dictionary.")

# 6. TypeError
# Occurs when an operation is applied to an object of an inappropriate type.
try:
    result = "hello" + 5
except TypeError:
    print("Caught TypeError: Incompatible types for operation.")

# 7. AttributeError
# Happens when an attribute reference or assignment fails.
text = "example"
try:
    missing = text.some_method()
except AttributeError:
    print("Caught AttributeError: Method or attribute does not exist.")

# 8. ImportError
# Encountered when an import statement fails to find the module definition.
try:
    import non_existent_module
except ImportError:
    print("Caught ImportError: Module not found.")

# ------------------------------
# Handling Exceptions with Try and Except
# ------------------------------

# Using Try-Except to handle exceptions
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")

# This line will be executed regardless of whether an exception occurred
print("Outside of try and except block")

# The try-except block is a powerful tool for handling exceptions in Python. 
# It allows the program to continue executing even if an error occurs, 
# preventing crashes and enabling graceful error handling.
