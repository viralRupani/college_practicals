# Write a user-defined exception that could be raised when the text
# entered by a user consists of less than 10 characters.


user_input = input("Enter a String: ")

if len(user_input) < 10:
    raise Exception("The string length is less than 10")


