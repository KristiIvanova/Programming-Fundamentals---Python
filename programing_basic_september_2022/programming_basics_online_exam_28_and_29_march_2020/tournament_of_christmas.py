cnt_days = int(input())
command = input()

total_money = 0
total_counter_win = 0
total_counter_lose = 0

for i in range (1, cnt_days + 1):
    command = input()
    money = 0
    counter_win = 0
    counter_lose = 0
    while command != "Finish":
        if command == "win":
            money += 20
            counter_win += 1
        elif command == "lose":
            counter_lose += 1
        command = input()

    if counter_win > counter_lose:
        total_money += money + (money * 0.1)
    else:
        total_money += money

    total_counter_win += counter_win
    total_counter_lose += counter_lose

if total_counter_win > total_counter_lose:
    total_money = total_money + (total_money * 0.2)
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
