# fruits = []
#
# f1= input("Enter a fruit: ")
# fruits.append(f1)
# f2= input("Enter a fruit: ")
# fruits.append(f2)
# f3= input("Enter a fruit: ")
# fruits.append(f3)
#
# print(fruits)

marks = []

for i in range(6):
    mark = int(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

# Sort the marks
marks.sort()

print("\nMarks in sorted order:", marks)