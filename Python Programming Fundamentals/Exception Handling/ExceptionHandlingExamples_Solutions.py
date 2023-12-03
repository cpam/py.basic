
# Python Exception Handling Examples

# 1. Handling ZeroDivisionError
# This function demonstrates how to handle division by zero using try-except blocks.
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

# Test case for safe_divide
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    print("Result:", safe_divide(numerator, denominator))
except ValueError:
    print("Invalid input! Please enter integers.")


# 2. Handling ValueError
# This function calculates the square root of a number and handles ValueError for invalid inputs.
import math

def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print("Result:", result)
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")

# Test case for perform_calculation
try:
    number1 = float(input("Enter a number for square root calculation: "))
    perform_calculation(number1)
except ValueError:
    print("Invalid input! Please enter a valid number.")


# 3. Handling Generic Exceptions
# This function performs a complex calculation and handles any exceptions that occur.
def complex_calculation(num):
    try:
        result = num / (num - 5)
        return result
    except Exception as e:
        print("An error occurred during calculation:", e)
        return None

# Test case for complex_calculation
try:
    num = float(input("Enter a number for complex calculation: "))
    calculation_result = complex_calculation(num)
    if calculation_result is not None:
        print("Result of the calculation:", calculation_result)
except ValueError:
    print("Invalid input! Please enter a valid number.")
