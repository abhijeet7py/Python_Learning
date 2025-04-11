def triangle_classify(side1,side2,side3):
    if side1 == side2 == side3:
        return "Equilateral triangle"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isoscales triangle"
    else:
        return "Scalene triangle"

side1 = int(input("Enter length of side 1: "))
side2 = int(input("Enter length of side 2: "))
side3 = int(input("Enter length of side 3: "))

print(triangle_classify(side1,side2, side3))
