a = int(input("Enter your age: "))

if (a >= 18):
    print("You are Eligible for vote.")

elif(a == 0):
    print("You are entering 0 which is invalid age.")

elif (a <= 0):
    print("You are entering negative age which is invalid")
else:
    print("You are not Eligible for vote.")