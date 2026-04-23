s = "Automation is good".replace(" ", "")
s = s.lower()

occ = {}

for ch in s:
    if ch in occ:
        occ[ch] += 1
    else:
        occ[ch] = 1

print(occ)