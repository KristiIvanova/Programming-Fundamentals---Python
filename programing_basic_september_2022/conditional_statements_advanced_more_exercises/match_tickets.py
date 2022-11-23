budget = float (input())
category = input()
cnt_people = int(input())

expenses = 0
ticket = 0
if 1 <= cnt_people <= 4:
    expenses = budget * 0.75
elif 5 <= cnt_people <= 9:
    expenses = budget * 0.60
elif 10 <= cnt_people <= 24:
    expenses = budget * 0.50
elif 25 <= cnt_people <= 49:
    expenses = budget * 0.40
else:
    expenses = budget * 0.25

if category == "VIP":
    ticket = cnt_people * 499.99
elif category == "Normal":
    ticket = cnt_people * 249.99

needed_money = budget - expenses
diff = abs (needed_money - ticket)

if needed_money >= ticket:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
