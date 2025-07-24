import re

captcha = "Captch:124-123=?"

match = re.search(r'(\d+)([+\-*/])(\d+)',captcha)

num1 = int(match.group(1))
operator = (match.group(2))
num2 = int(match.group(3))
3
result = 0
if operator == '-':
    result = num1 - num2
elif operator == '=':
    result = num1 + num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 // num2

print(result)