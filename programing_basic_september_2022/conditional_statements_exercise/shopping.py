budget = float(input())
cnt_video_card = int(input())
cnt_processor = int(input())
cnt_ram = int(input())

price_video_card = cnt_video_card * 250
price_processor = price_video_card * 0.35
total_price_processor = cnt_processor * price_processor

price_ram = price_video_card * 0.1
total_price_ram = cnt_ram * price_ram

total_price = price_video_card + total_price_processor + total_price_ram

if cnt_video_card > cnt_processor:
    total_price = total_price - (total_price * 0.15)

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")