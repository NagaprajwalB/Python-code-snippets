# print(*values, sep=' '/str, end=str/'\n')
''' *value :Multiple values can be passed separated by commas.
    sep : it seperates the values with the given string. By default, it is a space (" ").
    end : it is appended at the end of the printed values. By default, it is a new line character (\n).'''

# print always returns None

print(10, 20, 30, 40)
print(10, 20, 30, 40, sep=" ")
print(10, 20, 30, 40, sep="---")

print ("Iron \n man")

print(100)
print(200, end = "\n")
print(300, end = "-$-")
print(400)
print(500)

print(1,2,3,4,5, sep = "$", end = "--")
print(10,20,30,40, end = "$$$")
print(100,200,300,400, sep = "##")
print("BYE")