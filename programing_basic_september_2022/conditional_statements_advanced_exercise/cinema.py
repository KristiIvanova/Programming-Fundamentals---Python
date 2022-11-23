type_of_cinema = input()
row = int(input())
column = int(input())

price = 0
if type_of_cinema == "Premiere":
    price = row * column * 12
elif type_of_cinema == "Normal":
    price = row * column * 7.5
elif type_of_cinema == "Discount":
    price = row * column * 5

print(f"{price:.2f} leva")
