# Continue statement
# continue statement skips the current iteration of loop and
# moves to the next iteration.

# for number in range(10):
#     if number % 2 == 0:
#         continue
#     print(number)

# | i | condition | o/p |
# | 0 | 0%2 == 0| -> True | continue skip No o/p
# | 1 | 1%2 == 0| -> False | 1
# | 2 | 2%2 == 0| -> True |  continue skip No o/p
# | 3 | 3%2 == 0| -> False | 3


for number in range(10):
    if number % 2 == 0:
        pass
    print(number)