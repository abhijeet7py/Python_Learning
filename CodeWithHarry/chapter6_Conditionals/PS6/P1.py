
num1 = int(input("Enter a Number1: "))
num2 = int(input("Enter a Number2: "))
num3 = int(input("Enter a Number3: "))
num4 = int(input("Enter a Number4: "))

if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    print("Greatest number : ", num1)

elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    print("Greatest number : ", num2)

elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    print("Greatest number : ", num3)

else:
    print("Greatest number: ",num4)