filename = "languages.txt"
file = open(filename, "r")

""" number_lines = len(file.readlines())
print(f'There are {number_lines} lines in this file') """

""" list = file.readlines()
print(list[320]) """

""" for line in range(5):
    print(file.readline(), end='') """

line_number = 1
for line in file:
    print(f'{line_number} ' + file.readline())
    line_number += 1

file.close()