s = "Automation is good"

seen = set()
result= ""

for ch in s.lower():
    if ch != " " and ch not in seen:
        seen.add(ch)
        result += ch

print(result)

# Optimised with list
s1 = "Automation is good"
seens = set()
results = []
for ch in s1.lower():
    if ch != " " and ch not in seens:
        seens.add(ch)
        results.append(ch)

print("".join(results))
