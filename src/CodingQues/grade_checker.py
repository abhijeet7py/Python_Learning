def determine_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 90:
        return "B"
    elif 70 <= score <= 80:
        return "C"
    elif 60 <= score <= 70:
        return "D"
    elif 0 <= score <= 60:
        return "F"
    else:
        return "Invalid score"

def main():
    try:
        score = float(input("Enter a valid score between 0 to 100: "))

        grade = determine_grade(score)

        if grade == "Invalid score":
            print("Please enter a valid score between 0 to 100.")

        else:
            print(f"The grade for score {score} is : {grade}")

    except ValueError:
        print("Invalid input! please enter a numerical value.")

if __name__ == "__main__":
    main()



