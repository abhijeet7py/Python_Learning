# sub1 = float(input("Enter marks: "))
# sub2 = float(input("Enter marks: "))
# sub3 = float(input("Enter marks: "))
#
# total = sub1 + sub2 + sub3
# percentage = (total/300)*100
#
# if (sub1 >= 33) and (sub2 >= 33) and (sub3 >= 33) and (percentage >= 40):
#     print(f"Student has passed with percentage {percentage}")
#
# else:
#     print(f"Student has failed with percentage {percentage}")


# Take all 3 subject marks in one line
sub1, sub2, sub3 = map(float, input("Enter marks of 3 subjects separated by space: ").split())

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

if (sub1 >= 33) and (sub2 >= 33) and (sub3 >= 33) and (percentage >= 40):
    print(f"✅ Student has passed with percentage {percentage:.2f}")
else:
    print(f"❌ Student has failed with percentage {percentage:.2f}")
