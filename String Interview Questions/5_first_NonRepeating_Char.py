s = "Automation"
s = s.lower()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(f"first Non-repeating character: {ch}")
        break
else:
    print("No Non-repeating characters")