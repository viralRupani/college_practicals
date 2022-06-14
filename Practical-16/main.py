#Write a python program to demonstrate exception handling.

integer = True
while integer:
    try:
        num1 = int(input('num1: '))
        num2 = int(input('num2: '))
        print(num1 + num2)
        integer = False
    except:
        print("Please enter Integer value")


