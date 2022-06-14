# Write a program to read the content of file line by line and write it

def list_to_str(the_list):
    str = ""
    for _ in the_list:
        str += _
    return str


# for reading the file
print('The file content:')
with open('text.txt', 'r') as file:
    lines = file.readlines()
    for _ in range(len(lines)):
        print(f'line {_ + 1}. {lines[_]}')
    # for writing file
    with open('text2.txt', 'a') as file:
        file.write(list_to_str(lines))
