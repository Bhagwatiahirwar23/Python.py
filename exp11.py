#python program to read character by character from a file
file = open('file.text','r')
print(file)
a = []
for line in file:
    #a.append(line.split())
#print(a[0][1])
    for word in line:
        print(word)
        """for character in word:
            print(character)"""