
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Take user input
number = int(input("Enter a number: "))

# Calculate and print the factorial
print(f"The factorial of {number} is {factorial(number)}.")
