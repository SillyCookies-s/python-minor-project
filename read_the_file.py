filename = input("Filename: ")
file = open(filename, 'r')
print(file.read())
file.close()