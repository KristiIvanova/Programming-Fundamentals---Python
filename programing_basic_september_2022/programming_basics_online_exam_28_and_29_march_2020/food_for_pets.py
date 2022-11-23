import math
cnt_days = int(input())
total_food = float(input())

total_food_dog = 0
total_food_cat = 0
cookies = 0
total_eaten_food = 0
for i in range(1, cnt_days + 1):
    cnt_food_dog = int(input())
    cnt_food_cat = int(input())
    total_food_dog += cnt_food_dog
    total_food_cat += cnt_food_cat
    if i % 3 == 0:
        cookies += (cnt_food_dog + cnt_food_cat) * 0.1
    total_eaten_food = total_food_dog + total_food_cat

print(f"Total eaten biscuits: {round(cookies)}gr.")
print(f"{(total_eaten_food/total_food)*100:.2f}% of the food has been eaten.")
print(f"{(total_food_dog/total_eaten_food)*100:.2f}% eaten from the dog.")
print(f"{(total_food_cat/total_eaten_food)*100:.2f}% eaten from the cat.")



