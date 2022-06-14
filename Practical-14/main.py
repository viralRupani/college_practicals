# Write a program to catch on Divide by zero Exception with finally clause.

def div(dividend, divisor):
    try:
        return dividend / divisor
    except:
        print("Can not divide it by zero")


print(div(2, 0))
