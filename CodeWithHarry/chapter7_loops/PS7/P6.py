# n = int(input("Enter the number: "))
#
# for i in range(1, n + 1):
#     print(" "* (n -i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

n = int(input("Enter the number: "))
for i in range(1, n + 1):
    space = " "* (n-i)
    star = "*"*(2*i-1)
    print(space+star)
