s = "Hello123automation23god45s"

num = ""
sum = 0

for ch in s:
    if ch.isdigit():
        num += ch

    else:
        if num:
            sum += int(num)
            num = ""

if num:
    sum += int(num)

print(sum)
