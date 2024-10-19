# Python Coding Challenge Cheatsheet

## Data Structures

### Lists
```python
# Create a list
my_list = [1, 2, 3, 4, 5]

# Access elements
first_element = my_list[0]
last_element = my_list[-1]

# Slicing
subset = my_list[1:4]  # [2, 3, 4]

# Common operations
my_list.append(6)  # Add to end
my_list.insert(0, 0)  # Insert at index
my_list.pop()  # Remove and return last element
my_list.remove(3)  # Remove first occurrence of value
```

### Dictionaries
```python
# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Access elements
value = my_dict['a']

# Add or modify
my_dict['d'] = 4

# Check if key exists
if 'e' in my_dict:
    print("Key exists")

# Iterate over keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

### Sets
```python
# Create a set
my_set = {1, 2, 3, 4, 5}

# Add and remove elements
my_set.add(6)
my_set.remove(1)

# Set operations
other_set = {4, 5, 6, 7, 8}
union = my_set | other_set
intersection = my_set & other_set
difference = my_set - other_set
```

## Control Flow

### Conditional Statements
```python
if condition:
    # do something
elif other_condition:
    # do something else
else:
    # do another thing
```

### Loops
```python
# For loop
for item in iterable:
    # do something

# While loop
while condition:
    # do something

# Break and continue
for item in iterable:
    if condition:
        break  # Exit loop
    if other_condition:
        continue  # Skip to next iteration
```

## Functions

```python
def function_name(param1, param2=default_value):
    # function body
    return result

# Lambda functions
square = lambda x: x**2
```

## List Comprehensions

```python
# Basic syntax
new_list = [expression for item in iterable if condition]

# Example
squares = [x**2 for x in range(10) if x % 2 == 0]
```

## Error Handling

```python
try:
    # code that might raise an exception
except ExceptionType as e:
    # handle the exception
else:
    # code to run if no exception occurred
finally:
    # code that will always run
```

## Useful Built-in Functions

- `len(sequence)`: Returns the length of a sequence
- `range(start, stop, step)`: Generates a sequence of numbers
- `enumerate(iterable)`: Returns an iterator of tuples containing indices and values
- `zip(*iterables)`: Creates an iterator of tuples where each tuple contains the i-th element from each of the input iterables
- `map(function, iterable)`: Applies a function to every item of an iterable
- `filter(function, iterable)`: Constructs an iterator from elements of an iterable for which a function returns true

## Sorting

```python
# Sort a list in-place
my_list.sort()

# Sort a list and return a new sorted list
sorted_list = sorted(my_list)

# Custom sort with key function
sorted_list = sorted(my_list, key=lambda x: len(x))
```

## File I/O

```python
# Read from a file
with open('filename.txt', 'r') as file:
    content = file.read()

# Write to a file
with open('filename.txt', 'w') as file:
    file.write('Hello, World!')
```

Import necessary modules (e.g., `import math`, `from collections import defaultdict`) when using more advanced features or algorithms.
