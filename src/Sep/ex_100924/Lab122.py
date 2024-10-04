print("--- Start of the Program ---")

try:
    a = int(input("Enter the num1: "))
    b = int(input("Enter the num2: "))
    c = a / b
    print("Result of div is, ", c)

except Exception as e: # Exception is class containing multiple classes
    print(e)
    print("Please check your inputs, It shouldn't be string or zero")


print("--- End of Program ---")