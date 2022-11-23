cnt_clients = int(input())

price = 0
cnt_purchase = 0
total_price = 0
bucket = 0
for clients in range (cnt_clients):
    purchase = input()

    while purchase != "Finish":
        if purchase == "basket":
            price = 1.5
        elif purchase == "wreath":
            price = 3.8
        elif purchase == "chocolate bunny":
            price = 7
        total_price += price
        cnt_purchase += 1
        purchase = input()
    if cnt_purchase % 2 == 0:
        total_price -= (total_price * 0.2)
    if purchase == "Finish":
         print(f"You purchased {cnt_purchase} items for {total_price:.2f} leva.")
         bucket += total_price
         total_price = 0
         cnt_purchase = 0
print(f"Average bill per client is: {(bucket / cnt_clients):.2f} leva.")


