# File handling examples
# Package/Method	Description	Syntax and Code Example

# File opening modes: Different modes to open files for specific operations
# Syntax: r (reading) w (writing) a (appending) + (updating: read/write) b (binary, otherwise text)

# Example 1: Reading a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Example 2: Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, world!")

# Example 3: Appending to a file
with open("log.txt", "a") as file:
    file.write("Log entry: Something happened.")

# Example 4: Reading and updating a file
with open("data.txt", "r+") as file:
    content = file.read()
    file.write("Updated content: " + content)

# File reading methods: Different methods to read file content in various ways
# Syntax:
# 1. file.readlines() # reads all lines as a list
# 2. readline() # reads the next line as a string
# 3. file.read() # reads the entire file content as a string

# Example:
with open("data.txt", "r") as file:
    lines = file.readlines()
    next_line = file.readline()
    content = file.read()

# File writing methods: Different write methods to write content to a file
# Syntax:
# 1. file.write(content) # writes a string to the file
# 2. file.writelines(lines) # writes a list of strings to the file

# Example:
lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Iterating over lines: Iterates through each line in the file using a loop
# Syntax:
# 1. for line in file: # Code to process each line

# Example:
with open("data.txt", "r") as file:
    for line in file:
        print(line)

# Open() and close(): Opens a file, performs operations, and explicitly closes the file using the close() method
# Syntax:
# 1. file = open(filename, mode) # Code that uses the file
# 2. file.close()

# Example:
file = open("data.txt", "r")
content = file.read()
file.close()

# with open(): Opens a file using a with block, ensuring automatic file closure after usage
# Syntax:
# 1. with open(filename, mode) as file: # Code that uses the file

# Example:
with open("data.txt", "r") as file:
    content = file.read()
