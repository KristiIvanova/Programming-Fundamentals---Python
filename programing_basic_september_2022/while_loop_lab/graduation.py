name = input()
total_grades = 0
failed_years = 0
avg_grade = 0
years = 0

while True:
    annual_grade = float(input())
    years += 1

    if annual_grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {years} grade")
            break
        years -= 1
    else:
        total_grades += annual_grade
        if years == 12:
            avg_grade = total_grades / 12
            print(f"{name} graduated. Average grade: {avg_grade:.2f}")
            break

