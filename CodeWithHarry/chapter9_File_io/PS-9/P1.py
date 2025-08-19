# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’

f = open("poem.txt")
content = f.read()

if ("Twinkle" in content):
    print("Present")

else:
    print("Not Present")
f.close()