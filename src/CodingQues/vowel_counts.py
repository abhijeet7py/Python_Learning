# def count_vowels(s):
#     vowels = 0
#     consonants = 0
#
#     s = s.lower()
#     for ch in s:
#         if ch in "aeiou":
#             vowels += 1
#
#         elif ch.isalpha():
#             consonants += 1
#
#     return vowels,consonants
#
# string = input("Enter a string: ")
#
# vowel, consonant = count_vowels(string)
# print("Vowel: ",vowel)
# print("Consonants: ",consonant)

def count_vowel(s):
    vowel = 0
    consonants = 0

    s = s.lower()

    for ch in s:
        if ch in "aeiou":
            vowel += 1

        elif ch.isalpha():
            consonants += 1

    return vowel,consonants

string = input("Enter a string: ")
vowels,consonants = count_vowel(string)
print("Vowels: ",vowels)
print("Consonants: ",consonants)











