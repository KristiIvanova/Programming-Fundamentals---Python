cnt_pen = int(input())
cnt_marker = int(input())
littre_detergent = int(input())
discount_percent = int(input())

price_pen = cnt_pen * 5.8
price_markers = cnt_marker * 7.2
price_detergent = littre_detergent * 1.2

all_price = price_pen + price_markers + price_detergent
discount_price = all_price * (discount_percent /100)
total_amount = all_price - discount_price

print(total_amount)

