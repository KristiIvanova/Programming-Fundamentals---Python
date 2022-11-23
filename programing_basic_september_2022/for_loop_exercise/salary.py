cnt_open_tabs = int(input())
salary = int(input())

total_salary = salary

for i in range(1, cnt_open_tabs + 1):
    name_site = input()
    if name_site == "Facebook":
        salary = salary - 150
    elif name_site == "Instagram":
        salary = salary - 100
    elif name_site == "Reddit":
        salary = salary - 50

    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
