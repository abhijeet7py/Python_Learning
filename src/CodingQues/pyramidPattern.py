n = int(input("Enter a no: "))

for i in range(1 , n +1):
    print(" " * (n - i),end="")
    # print(f"{i}"*(2*i - 1))
    for j in range(1, 2 * i):
        print(j, end="")

    print()