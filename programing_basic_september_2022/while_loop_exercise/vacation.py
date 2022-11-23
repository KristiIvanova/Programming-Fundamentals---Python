money_excursion = float(input())
init_money = float(input())

#action = ""
current_money = 0
counter_days = 0
cnt = 0
while init_money < money_excursion and cnt < 5:
    action = input()
    current_money = float(input())
    counter_days += 1

    if action == "spend":
        cnt += 1
        init_money -= current_money
        if init_money < 0:
            init_money = 0

    if action == "save":
        cnt = 0
        init_money += current_money


   # if current_money >= money_excursion:
   #     break

if init_money >= money_excursion:
    print(f"You saved the money for {counter_days} days.")
if cnt == 5:
    print("You can't save the money.")
    print(f"{counter_days}")