
# Dictionary methods and usage
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing Values
name = person["name"]
age = person["age"]

# Add or modify
person["Country"] = "USA"  # A new entry will be created
person["city"] = "Chicago"  # Update the existing value for the same key

# clear()
grades = {'Math': 90, 'Science': 85}
grades.clear()

# copy()
new_person = person.copy()

# Creating a Dictionary
dict_name = {}  # Creates an empty dictionary

# del
del person["Country"]

# items()
info = list(person.items())

# key existence
if "name" in person:
    print("Name exists in the dictionary.")

# keys()
keys_list = list(person.keys())

# update()
person.update({"Profession": "Doctor"})

# values()
person_values = list(person.values())

# List methods and usage
fruits = ["apple", "banana", "orange"]

# append()
fruits.append("mango")

# copy()
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()

# count()
count = my_list.count(2)

# Creating a list
# already created above

# del
del my_list[2]

# extend()
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)

# insert()
my_list.insert(2, 6)

# Modifying a list
my_list[1] = 25

# pop()
removed_element = my_list.pop()
removed_element_at_index = my_list.pop(2)

# remove()
my_list.remove(30)

# reverse()
my_list.reverse()

# Slicing
sliced_list = my_list[1:4]

# sort()
my_list.sort()
my_list.sort(reverse=True)

# Sets methods and usage
colors = {"red", "green", "blue"}

# add()
colors.add("yellow")

# clear()
colors.clear()

# copy()
new_colors = colors.copy()

# Defining Sets
empty_set = set()  # Creating an Empty Set

# discard()
colors.discard("red")

# issubset()
is_subset = colors.issubset(fruits)

# issuperset()
is_superset = colors.issuperset(fruits)

# pop()
removed_color = colors.pop()

# remove()
colors.remove("green")

# Set Operations
combined = colors.union(fruits)
common = colors.intersection(fruits)
unique_to_colors = colors.difference(fruits)
sym_diff = colors.symmetric_difference(fruits)

# update()
colors.update(["cyan", "magenta"])
