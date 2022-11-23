change = float(input())
convert_change = change * 100

cnt_coins = 0
while True:
    if convert_change >= 200:
        convert_change -= 200
    elif convert_change >= 100:
        convert_change -= 100
    elif convert_change >= 50:
        convert_change -= 50
    elif convert_change >= 20:
        convert_change -= 20
    elif convert_change >= 10:
        convert_change -= 10
    elif convert_change >= 5:
        convert_change -= 5
    elif convert_change >= 2:
        convert_change -= 2
    elif convert_change >= 1:
        convert_change -= 1
    else:
        break

    cnt_coins += 1

print(cnt_coins)
