# Create a package named DemoPackage which contains two
# modules named mathematics and greets. The mathematics
# module contains sum, average, power functions, and the greets
# module contains the sayHello function.
# a) import the module from a package to another program.
# b) import a specific function from a module

from DemoPackage import mathematics, greet

# Mathematics
print(f'sum of the value is: {mathematics.sum_function(2, 2, 2)}')
print(f'average of the value is: {mathematics.average(2, 2, 2):.2f}')
print(f'power of the value is: {mathematics.power(3, 3)}')

# Greet
print(greet.say_hello("Viral Rupani"))
