# Write a program to demonstrate the dictionaries functions and operations.


# Dictionary
fruits = {
    1: "Mango",
    2: "Orange",
    3: "Apple",
    4: "Banana"
}


# copy()
# copies the dictionary and assign it into new one.
copied_fruits = fruits.copy()
print(copied_fruits)

# pop()
# returns the value that key is containing
print(copied_fruits.pop(2))

# values()
# returns the list of dictionary
print(copied_fruits.values())

# items()
# Return the list with all dictionary keys with values
print(copied_fruits.items())