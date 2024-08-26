# ✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Take user input
num_terms = int(input("Enter the number of terms: "))

# Generate and print the Fibonacci sequence
print(f"The first {num_terms} terms of the Fibonacci sequence are: {fibonacci_sequence(num_terms)}")

