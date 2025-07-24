captcha = "captcha:6*5=?"

# Extract characters
num1 = int(captcha[8])   # '6'
num2 = int(captcha[10])  # '5'
operator = captcha[9]    # '-'

print(num1, num2)

result = 0
if operator == '-':
    result = num1 - num2
elif operator == '+':
    result = num1 + num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 // num2  # Use integer division to match Java behavior

print("Result:", result)
