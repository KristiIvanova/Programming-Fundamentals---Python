cnt_failed_grade = int(input())

failed_times = 0
solved_problem_counts = 0
grades_sum = 0
last_problem = ""
has_failed = True
while failed_times < cnt_failed_grade:
    name_init = input()

    if name_init == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1

    grades_sum += grade
    solved_problem_counts += 1
    avg_grade = grades_sum / solved_problem_counts
    last_problem = name_init

if has_failed:
    print(f"You need a break, {failed_times} poor grades.")
else:
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {solved_problem_counts}")
    print(f"Last problem: {last_problem}")
