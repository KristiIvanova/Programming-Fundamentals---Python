food_for_dog_kg = int(input())
command = input()

total_food = 0
while command != "Adopted":
    food_for_dog_gr = int(command)
    total_food += food_for_dog_gr
    command = input()

diff = abs(total_food - (food_for_dog_kg * 1000))
if food_for_dog_kg * 1000 >= total_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")

