def calculate_grade(marks):
    # percentage calculate karo
    total = sum(marks)
    percentage = (total / 5)
    # grade assign karo (A, B, C, D, F)
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B" 
    elif percentage >= 70:
        grade = "C" 
    elif percentage >= 60:
        grade = "D" 
    else:
        grade = "F" 
    print(f"Your Percentage: {percentage}%")
    print(f"Your Grade: {grade}")

    if percentage >= 60:
        print("You are Pass brother")
    else:
        print("You are fail Keep tryingg!!")


marks = []
for i in range(5):
    m = int(input(f"Subject {i+1} marks: "))
    marks.append(m)

calculate_grade(marks)