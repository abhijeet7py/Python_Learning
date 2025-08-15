'''
1 for Gun
0 for snake
-1 for water
'''

import random

computer = random.choice([0,1,-1])

you_str = input("Enter your Choice: ").lower()
you_dict = {"w": -1,"g": 1,"s": 0}
reverse_dic = {-1: "Water", 0: "Snake", 1: "Gun"}
you = you_dict[you_str]

print(f"You Chose: {reverse_dic[you]}\nComputer choice: {reverse_dic[computer]}")

'''
1 for Gun
0 for snake
-1 for water
'''

if (computer == you):
    print("Its a draw!")

else:
    #G vs W
    if (computer == 1 and you == -1): #2
        print("You Win!")
    #G vs S
    elif(computer == 1 and you == 0): #1
        print("You Loose!")
    #W vs S
    elif(computer == -1 and you == 0): #-1
        print("You Win!")
    #W vs G
    elif (computer == -1 and you == 1): #0
        print("You Loose!")
    #S vs W
    elif (computer == 0 and you == -1): #1
        print("You Loose!")
    #S vs G
    elif (computer == 0 and you == 1): #-1
        print("You Win!")
    else:
        print("Something went wrong!")