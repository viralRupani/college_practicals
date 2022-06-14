# Write a program to define a module to find the area and circumference of a circle.
# a) import the module to another program.
# b) import a specific function from a module to another program

from circle import find_area, find_circumference

print(f'The area of the circle is {find_area(2):.2f}')
print(f'The Circumference of the circle is {find_circumference(2)}')
