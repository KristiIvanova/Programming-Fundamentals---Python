budget = float(input())
cnt_statists = int(input())
price_clothes = float(input())

decor_price = budget * 0.1
all_clothes_sum = cnt_statists * price_clothes

if cnt_statists > 150:
    all_clothes_sum = all_clothes_sum * 0.9

diff = abs(budget - (all_clothes_sum+decor_price))
if decor_price + all_clothes_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")