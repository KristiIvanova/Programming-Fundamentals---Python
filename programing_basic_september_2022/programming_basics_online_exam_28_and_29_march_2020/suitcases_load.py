trunk_capacity = float(input())
counter = 0
while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    suitcase_volume = float(command)
    if (counter + 1) % 3 == 0:
        suitcase_volume = suitcase_volume + (suitcase_volume * 0.1)
    if suitcase_volume > trunk_capacity:
        print("No more space!")
        break
    counter += 1
    trunk_capacity -= suitcase_volume
print(f"Statistic: {counter} suitcases loaded.")






