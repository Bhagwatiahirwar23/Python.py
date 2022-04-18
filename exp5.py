# Write a program to display the number of lines in the file and size of a file in bytes..
file = open('Hello.text')
row_count = 0
size_count = 0
for row in file:
    row_count += 1
    for charater in row:
        size_count += 1
        print(charater)
print(row_count)
print(size_count)
file.close()

import os
 
"""file_size = os.path.getsize('C:\\Users\\HP\\Desktop\\Program Files\\Python Lab Experiments\\Hello.text')
print("file size is:",file_size,"bytes")
print()"""
