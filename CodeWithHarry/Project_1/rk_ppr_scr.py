"""
1 = rock
0 = paper
-1 = scissors
"""
import random

computer = random.choice([-1,0,1])
you_str = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()

you_dict = {"r":1,"p":0,"s":-1}
reverse_dict = {1:"Rock",0:"Paper",-1:"Scissors"}

you = you_dict[you_str]

print(f"You chose: {reverse_dict[you]}")
print(f"Computer chose: {reverse_dict[computer]}")

if (you == computer):
    print("Its a Draw!")

else:
    if(you == 1 and computer == 0):
        print("You Lost!")
    elif(you == 1 and computer == -1):
        print("You Won!")
    elif (you == 0 and computer == -1):
        print("You Lost")
    elif (you == 0 and computer == 1):
        print("You Won!")
    elif (you == -1 and computer == 0):
        print("You Won!")
    elif (you ==-1 and computer == 1):
        print("You Lost")
    else:
        print("Something went wrong")