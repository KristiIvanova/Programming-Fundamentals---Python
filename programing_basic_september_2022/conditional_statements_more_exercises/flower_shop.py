import math
cnt_magnolias = int(input())
cnt_hyacinth = int(input())
cnt_roses = int(input())
cnt_cactus = int(input())
price_gift = float (input())

price_magnolias = cnt_magnolias * 3.25
price_hyacinth = cnt_hyacinth * 4
price_roses = cnt_roses * 3.5
price_cactus = cnt_cactus * 8

total_price = (price_magnolias + price_hyacinth + price_roses + price_cactus) * 0.95
diff = abs (price_gift - total_price)

if total_price >= price_gift:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")