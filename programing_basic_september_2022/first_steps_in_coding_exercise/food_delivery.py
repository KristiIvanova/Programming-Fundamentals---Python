cnt_chicken = int(input())
cnt_fish = int(input())
cnt_vegeterian = int(input())

price_chicken = cnt_chicken * 10.35
price_fish = cnt_fish * 12.40
price_vegeterian = cnt_vegeterian * 8.15
all_price = price_chicken + price_fish + price_vegeterian
price_dessert = all_price * 0.20
total_amount = all_price + price_dessert +2.5

print(f"{total_amount:.2f}")