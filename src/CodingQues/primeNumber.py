# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#
#     i = 5
#
#     while i * i <= num:
#         if num % i == 0 or num % (i +2) == 0:
#             return False
#
#         i += 6
#
#     return True
#
# try:
#     number = int(input("Enter a no: "))
#     if is_prime(number):
#         print(f"{number} is a prime number")
#
#     else:
#         print(f"{number} is not a prime number")
#
# except ValueError as e:
#     print(e)


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False

        i += 6
    return True


start = int(input("Enter a start no: "))
end = int(input("Enter a end no: "))
print(f"\nPrime numbers between {start} and {end} are:")
for num in range(start,end + 1):

    if is_prime(num):
        print(num , end= " ")

    # else:
    #     print(f"{num} is not a prime no")







