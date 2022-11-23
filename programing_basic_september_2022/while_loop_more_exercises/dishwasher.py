cnt_detergent = int(input())
command = input()

total_dishes = 0
total_pots = 0
counter = 0
cnt_pots = 0
cnt_dishes = 0
while command != "End":
    cnt_dishes_pots = int(command)
    total_detergent = 0
    counter += 1
    total_detergent = cnt_detergent * 750
    if counter % 3 == 0:
        total_pots += cnt_dishes_pots * 15
        cnt_pots += cnt_dishes_pots
    else:
        total_dishes += cnt_dishes_pots * 5
        cnt_dishes += cnt_dishes_pots

    total_detergent -= total_dishes + total_pots

    if total_detergent < 0:
        break

    command = input()

if total_detergent >= 0:
    print("Detergent was enough!")
    print(f"{cnt_dishes} dishes and {cnt_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")