type_flowers = input()
cnt_flower = int(input())
budget = int(input())

total_sum = 0
if type_flowers == "Roses":
    total_sum = cnt_flower * 5
    if cnt_flower > 80:
        total_sum = total_sum * 0.9

elif type_flowers == "Dahlias":
    total_sum = cnt_flower * 3.8
    if cnt_flower > 90:
        total_sum = total_sum * 0.85

elif type_flowers == "Tulips":
    total_sum = cnt_flower * 2.8
    if cnt_flower > 80:
        total_sum = total_sum * 0.85

elif type_flowers == "Narcissus":
    total_sum = cnt_flower * 3
    if cnt_flower < 120:
        total_sum = total_sum * 1.15

elif type_flowers == "Gladiolus":
    total_sum = cnt_flower * 2.50
    if cnt_flower < 80:
        total_sum = total_sum * 1.20

diff = abs(total_sum-budget)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {cnt_flower} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")