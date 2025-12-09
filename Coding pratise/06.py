# Check whether number is odd or even

# 1. using If and else:

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# 2. Using Ternery expression

num1 = int(input("Enter a number: "))
result = "Even" if num1 % 2 == 0 else "Odd"
print(f"{num1} is {result}.")

# 3. Function based Program

def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(f"{number} is {check_odd_even(number)} number.")

# 4. Handling Exception:

def check_odd_even(num):
    try:
        if num % 2 == 0:
            return "Even"
        else: return "Odd"

    except ValueError:
        print(f"{num} is not a valid input!")

number = int(input("Enter a number: "))
print(f"{number} is {check_odd_even(number)} number.")