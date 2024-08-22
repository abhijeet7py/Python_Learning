# Create a program that takes two numbers as input and prints
# whether the first number is greater than,
# less than, or equal to the second number.

### Task #5
#Create a program that takes two numbers as input and prints whether the first number
# is greater than, less than, or equal to the second number.
num1=int(input("enter the number1: "))
num2=int(input("enter the number2: "))
print("Number1 is greater than number2:",num1>num2)
print("Number1 is less than number2:",num1<num2)
print("Number1 is equal than number2:",num1==num2)




def compare_numbers():
    # Take two numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Compare the two numbers
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num1} is less than {num2}.")
    else:
        print(f"{num1} is equal to {num2}.")

# Call the function to execute the comparison
compare_numbers()
