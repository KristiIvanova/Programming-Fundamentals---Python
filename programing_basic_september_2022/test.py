cnt_excursion_sea = int(input())
cnt_excursion_mountain = int(input())

profit = 0
current_counter_sea = 0
current_counter_mountain = 0


while cnt_excursion_sea + cnt_excursion_mountain != 0:
    name_excursion = input()
    ##total_counter_sea += current_counter_sea
    ##total_counter_mountain += current_counter_mountain
    ##if cnt_excursion_sea == 0:
    ##    break
    if name_excursion == "Stop":
        break
    if name_excursion == "sea":
        if cnt_excursion_sea <= 0:
            current_price = 0
        else:
            current_price = 680
            cnt_excursion_sea -= 1
        profit += current_price

    elif name_excursion == "mountain":
        if cnt_excursion_mountain <= 0:
            current_price = 0
        else:
            current_price = 499
            cnt_excursion_mountain -= 1
        profit += current_price

if cnt_excursion_sea + cnt_excursion_mountain != 0:
    print(f"Profit: {profit} leva.")
else:
    print("Good job! Everything is sold.")
    print(f"Profit: {profit} leva.")


