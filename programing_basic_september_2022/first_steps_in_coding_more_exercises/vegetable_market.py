price_veg_kg = float(input())
price_fruit_kg = float(input())
total_kg_veg = int(input())
total_kg_fruit = int(input())

veg_sum = price_veg_kg * total_kg_veg
fruit_sum = price_fruit_kg * total_kg_fruit

total_sum = (veg_sum+fruit_sum)/1.94

print(f"{total_sum:.2f}")