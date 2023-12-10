
# AND operation example
def check_qualification(marks, attendance_percentage):
    if marks >= 80 and attendance_percentage >= 85:
        return "Qualify for honors"
    else:
        return "Not qualified for honors"

# Class definition example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Define function example
def greet(name):
    return f"Hello, {name}"

# Equal (==) operation example
def check_equality(a, b):
    return a == b

# For loop example
def print_numbers():
    for num in range(1, 10):
        print(num)

def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)

# Function call
greeting = greet("Alice")

# Greater Than or Equal To (>=) operation example
def check_greater_equal(a, b):
    return a >= b

# Greater Than (>) operation example
def check_greater(a, b):
    return a > b

# If statement example
def check_temperature(temperature):
    if temperature > 30:
        return "It's a hot day!"

# If-Elif-Else statement example
def grade_evaluation(score):
    if score >= 90:
        return "You got an A!"
    elif score >= 80:
        return "You got a B."
    else:
        return "You need to work harder."

# If-Else statement example
def check_adult(age):
    if age >= 18:
        return "You're an adult."
    else:
        return "You're not an adult yet."

# Less Than or Equal To (<=) operation example
def check_less_equal(a, b):
    return a <= b

# Less Than (<) operation example
def check_less(a, b):
    return a < b

# Loop controls (break and continue) example
def loop_control_example():
    for num in range(1, 6):
        if num == 3:
            break
        print(num)

def loop_continue_example():
    for num in range(1, 6):
        if num == 3:
            continue
        print(num)

# NOT operation example
def check_locked(isLocked):
    return not isLocked

# Not Equal (!=) operation example
def check_not_equal(a, b):
    return a != b

# Object creation example
person1 = Person("Alice", 25)

# OR operation example
def check_grade(grade):
    return grade == 11 or grade == 12

# Range function example
def range_example():
    return list(range(1, 11, 2))

# Return statement example
def add(a, b):
    return a + b

# Try-Except block example
def input_number():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        return "Invalid input. Please enter a valid number."

# Try-Except with Else block example
def input_number_with_else():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        return "Invalid input. Please enter a valid number"
    else:
        return f"You entered: {num}"

# Try-Except with Finally block example
def file_read_example():
    try:
        file = open("data.txt", "r")
        data = file.read()
        return data
    except FileNotFoundError:
        return "File not found."
    finally:
        file.close()

# While loop example
def while_loop_example():
    count = 0
    while count < 5:
        print(count)
        count += 1

# Let's demonstrate some of the functions
if __name__ == "__main__":
    qualification_result = check_qualification(90, 87)
    print(qualification_result)

    numbers_list = range_example()
    print(numbers_list)

    addition_result = add(3, 5)
    print(addition_result)

    temperature_message = check_temperature(35)
    print(temperature_message)

    grade_message = grade_evaluation(85)
    print(grade_message)

    age_message = check_adult(21)
    print(age_message)
