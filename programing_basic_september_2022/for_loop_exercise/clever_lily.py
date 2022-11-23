age = int(input())
price_washer = float(input())
price_toy = int(input())

cnt_toy = 0
price_birday = 0
price = 0
brother_count = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        cnt_toy += 1
    else:
        brother_count += 1
        price = price + 10
        price_birday = price_birday + price

total_money = (cnt_toy * price_toy) + price_birday - brother_count
diff = abs(total_money - price_washer)
if total_money >= price_washer:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")