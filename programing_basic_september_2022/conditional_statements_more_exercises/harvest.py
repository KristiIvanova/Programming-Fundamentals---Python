import math

vineyard_metre = int(input())
grapes_metre = float(input())
needed_litre_wine = int(input())
cnt_workers = int(input())

total_grapes = vineyard_metre * grapes_metre
wine = (total_grapes * 0.4) / 2.5
diff = abs(needed_litre_wine - wine)
litre_per_person = diff / cnt_workers

if needed_litre_wine <= wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(litre_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")