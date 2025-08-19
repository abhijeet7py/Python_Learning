# f = open("file.txt")
# print(f.read())
# f.close()

# With this approch dont hve to explicitly close the file
with open("file.txt") as f:
    print(f.read())