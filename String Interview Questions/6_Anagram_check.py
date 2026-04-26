# Check if two strings are anagrams

s1 = "silent"
s2 = "listen"

if len(s1) != len(s2):
    print("Not a Anagram")

else:
    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch,0) + 1

    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            print("Not a Anagram")
            break

        freq[ch] -= 1

    else:
        print("Anagram")
