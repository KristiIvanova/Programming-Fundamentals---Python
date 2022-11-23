price_excursion = float(input())
cnt_puzzle = int(input())
cnt_dolls = int(input())
cnt_bears = int(input())
cnt_minions = int(input())
cnt_trucks = int(input())

total_sum = (cnt_puzzle * 2.6) + (cnt_dolls * 3) + (cnt_bears * 4.1) + (cnt_minions * 8.2) + (cnt_trucks * 2)
cnt_toys = cnt_puzzle + cnt_dolls + cnt_bears + cnt_minions + cnt_trucks

if cnt_toys >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.1)
diff = abs(price_excursion - total_sum)

if price_excursion <= total_sum:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
