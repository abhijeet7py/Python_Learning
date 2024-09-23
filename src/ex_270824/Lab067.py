# def sum_three_num(a,b,c):
#   return a + b+ c

# a = lambda a,b,c : a + b + c
# print(a(22,45,78))

def find_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")

# find_odd_even(5)

check_even_odd = lambda num: "Even" if num % 2 == 0 else "odd"
print(check_even_odd(125))