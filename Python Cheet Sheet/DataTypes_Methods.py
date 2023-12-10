
# Common Data Types examples
boolean_value = True  # bool
complex_number = 1.2j  # complex
dictionary = {'x': 2, 'y': 5}  # dict
floating_point = 3.0  # float
integer = 3  # int
mutable_list = [2, 'x', 3.1]  # list
character_sequence = "Python"  # str
immutable_tuple = (2, 4, 7)  # tuple

# Common Dictionary Methods examples
dictionary.clear()  # clear
default_value = dictionary.get('k', 'default')  # get
has_key_result = 'k' in dictionary  # has_key (Note: has_key() is deprecated in Python 3.x)
items_list = list(dictionary.items())  # items
keys_list = list(dictionary.keys())  # keys
popped_value = dictionary.pop('k', 'default')  # pop
values_list = list(dictionary.values())  # values

# Common File Methods examples (Note: File operations require an actual file to work on)
with open('example.txt', 'w+') as file:
    file.write('Example content')
    file.seek(0)
    read_content = file.read()  # read
    file.seek(0)
    readline_content = file.readline()  # readline
    file.seek(0)
    readlines_content = file.readlines()  # readlines
    file.seek(0)
    file.writelines(['Line 1', 'Line 2'])  # writelines
    file.close()  # close

# Common List Methods examples
mutable_list.append('new_obj')  # append
count_of_obj = mutable_list.count('x')  # count
index_of_obj = mutable_list.index(3.1)  # index
popped_item = mutable_list.pop()  # pop
mutable_list.remove('x')  # remove
mutable_list.reverse()  # reverse
mutable_list.sort()  # sort

# Common String Methods examples
capitalized_string = character_sequence.capitalize()  # capitalize
centered_string = character_sequence.center(10)  # center
count_of_sub = character_sequence.count('o')  # count
find_result = character_sequence.find('Py')  # find
is_digit = character_sequence.isdigit()  # isdigit
is_lower = character_sequence.islower()  # islower
joined_string = ','.join(['a', 'b', 'c'])  # join
lowercased_string = character_sequence.lower()  # lower
stripped_string = '  whitespace  '.strip()  # strip
split_string = character_sequence.split('t')  # split

# Common Tuple Methods examples
immutable_tuple.count(2)  # count
tuple_index = immutable_tuple.index(4)  # index
