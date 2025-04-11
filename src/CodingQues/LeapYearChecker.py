def leap_year_check(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter the year: "))

if leap_year_check(year):
    print(f"{year} is a Leap year.")

else:
    print(f"{year} is not a leap year.")