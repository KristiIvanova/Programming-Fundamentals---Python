cnt_juri = int(input())
name_presentation = input()
sum_all_grade = 0
count_grades = 0

while name_presentation != "Finish":
    sum_grade = 0
    for juri in range (1, cnt_juri +1):
        grade = float(input())
        count_grades += 1
        sum_grade += grade
        sum_all_grade += grade
    avg_grade_presentation = sum_grade / cnt_juri
    print( f"{name_presentation} - {avg_grade_presentation:.2f}.")

    name_presentation = input()

avg_all_grade_presentation = sum_all_grade / count_grades
print(f"Student's final assessment is {avg_all_grade_presentation:.2f}.")