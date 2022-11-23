type_of_gorivo = input()
littre = float(input())
club_card = input()

if type_of_gorivo == "Gas":
    price = 0.93
    if club_card == "Yes":
        price = price - 0.08
elif type_of_gorivo == "Gasoline":
    price = 2.22
    if club_card == "Yes":
        price = price - 0.18
elif type_of_gorivo == "Diesel":
    price = 2.33
    if club_card == "Yes":
        price = price - 0.12

if 20 <= littre <= 25:
    total_price = (littre * price) * 0.92
elif littre > 25:
    total_price = (littre * price) * 0.90
else:
    total_price = littre * price

print(f"{total_price:.2f} lv.")


