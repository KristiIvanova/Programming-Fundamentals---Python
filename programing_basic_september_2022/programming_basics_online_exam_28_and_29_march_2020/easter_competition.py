import sys

cnt_cake = int(input())

max_grade = -sys.maxsize
total_grade = 0
for i in range (cnt_cake):
    baker = input()

    while baker != "Stop":
        grade = int(input())
        if baker == "Stop":
            print(f"{baker} has {max_grade} points.")
            continue

        if grade > max_grade:
            max_grade = grade
            current_name = baker

    total_grade += grade



