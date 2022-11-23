n_kilometre = int(input())
type_of_day = input()
price = 0

if n_kilometre < 20 and type_of_day == "day":
    price = 0.70 + (n_kilometre * 0.79)
elif n_kilometre < 20 and type_of_day == "night":
    price = 0.70 + (n_kilometre * 0.90)
elif n_kilometre >= 20 and n_kilometre < 100:
    price = n_kilometre * 0.09
elif n_kilometre >= 100:
    price = n_kilometre * 0.06

print(f"{price:.2f}")