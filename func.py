# *args allows you to pass a variable number of non-keyword arguments to a function. It’s useful when you don’t know beforehand how many arguments will be passed to your function.

def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3)


# **kwargs allows you to pass a variable number of keyword arguments to a function. It’s useful when you want to handle named arguments in a flexible way.

def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="Alice", age=30)


# In this case, example_function accepts any number of named arguments, which are accessed as a dictionary inside the function.

def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Alice", age=30)

# Great to hear you have a new repository on GitHub! Let's dive into *args and **kwargs, which are important concepts in Python.


# *args allows you to pass a variable number of non-keyword arguments to a function. It’s useful when you don’t know beforehand how many arguments will be passed to your function.
# Example:


def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3)

# Output:

# 1
# 2
# 3

# Here, example_function can accept any number of arguments, which are accessed as a tuple inside the function.


# **kwargs allows you to pass a variable number of keyword arguments to a function. It’s useful when you want to handle named arguments in a flexible way.



def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="Alice", age=30)




# name: Alice
# age: 30

# In this case, example_function accepts any number of named arguments, which are accessed as a dictionary inside the function.
# Combining *args and **kwargs

# You can use both *args and **kwargs in the same function to handle both positional and keyword arguments.


def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Alice", age=30)


# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}

# This function can take any number of positional and keyword arguments, giving you a lot of flexibility in how you call it.