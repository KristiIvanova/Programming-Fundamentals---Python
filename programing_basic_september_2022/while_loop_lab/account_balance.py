available_sum = 0

while True:
    current_num = input()

    if current_num == "NoMoreMoney":
        break

    current_num = float(current_num)

    if current_num >= 0:
        available_sum += current_num
        print(f"Increase: {current_num:.2f}")

    else:
        print("Invalid operation!")
        break

print(f'Total: {available_sum:.2f}')