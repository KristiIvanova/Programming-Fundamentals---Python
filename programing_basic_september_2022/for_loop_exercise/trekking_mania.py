cnt_people = int(input())
sum_Mussala = 0
sum_Monblan = 0
sum_Kilimandjaro = 0
sum_K2 = 0
sum_Everest = 0

total_people =0
for i in range (1, cnt_people + 1):
    counter_people = int(input())
    if counter_people <= 5:
        sum_Mussala += counter_people
    elif counter_people <= 12:
        sum_Monblan += counter_people
    elif counter_people <= 25:
        sum_Kilimandjaro += counter_people
    elif counter_people <= 40:
        sum_K2 += counter_people
    elif counter_people >= 41:
        sum_Everest += counter_people
    total_people = total_people + counter_people

perc_Mussala = (sum_Mussala / total_people) * 100
print(f"{perc_Mussala:.2f}%")
perc_Monblan = (sum_Monblan / total_people) * 100
print(f"{perc_Monblan:.2f}%")
perc_Kilimandjaro = (sum_Kilimandjaro / total_people) * 100
print(f"{perc_Kilimandjaro:.2f}%")
perc_K2 = (sum_K2 / total_people) * 100
print(f"{perc_K2:.2f}%")
perc_Everest = (sum_Everest / total_people) * 100
print(f"{perc_Everest:.2f}%")