# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}
#
#
# You need to share this via the GITHUB repo.


num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))

print(f"Maximum number is:{max(num1,num2)}")
print(f"Power of num1 to num2 is:{pow(num1,num2)}")
print(f"Substraction of num1 to num2 is:{(num1-num2)}")
print(f"Multiplication of num1 to num2 is:{(num1*num2)}")
a = print(f"Division of num1 to num2 is:{(num1/num2)}")
print(f"sum of num1 to num2 is:{(num1+num2)}")

print(type(a))