# try, except and finally , else

try:
    num1 = int(input("Enter the Num1:"))
    num2 = int(input("Enter the Num2:"))
    result = num1 / num2

except ValueError as ve:
    print("Value error, You have entered string instead we want int.")

except ZeroDivisionError as zde:
    print("Zero div error, Don't use 0 as num2")

else:
    print(f"Result is {result}")

finally:
    print("This code will be always executed")