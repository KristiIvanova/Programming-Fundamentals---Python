import math

cnt_days = int(input())
left_food_kg = int(input())
food_dog_kg = float(input())
food_cat_kg = float(input())
food_turtle_gr = float(input())

needed_food_dog = cnt_days * food_dog_kg
needed_food_cat = cnt_days * food_cat_kg
needed_food_turtle = (cnt_days * food_turtle_gr) / 1000
total_needed_food = needed_food_turtle + needed_food_dog + needed_food_cat

diff = abs(left_food_kg - total_needed_food)
if total_needed_food <= left_food_kg:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")

