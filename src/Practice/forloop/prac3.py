text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"number of vowels is {count}")


for i in range(1,6):
    print("*" * i)

sqaures = []

for i in range(1,201,5):
    sqaures.append(i * i)


print(sqaures)