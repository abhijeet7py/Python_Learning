import math

try:
    math.exp(1000)  #OverflowError: math range error
except Exception as e:
    print(e)
    print("Please choose a lower exp value")