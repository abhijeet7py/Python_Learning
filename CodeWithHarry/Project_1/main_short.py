'''
1 for Gun
0 for snake
-1 for water
'''
import random

computer = random.choice([-1,0,1])
you_str = input("Enter you Choice: ").lower()
you_dict = {"g": 1,"s": 0,"w":-1}
reverse_dict = {1: "Gun",0:"Snake",-1:"Water"}

you = you_dict[you_str]

print(f"You Chose: {reverse_dict[you]}\nComputer choice: {reverse_dict[computer]}")
if (computer == you):
    print("Its a Draw!")
elif ((computer + you == 2) or (computer + you == -1)):
    print("You Win!")
else:
    print("You loose")