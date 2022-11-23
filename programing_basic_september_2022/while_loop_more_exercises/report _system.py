needed_money = int(input())

product_count = 0
card_payment = 0
card_cnt = 0
cash_payment = 0
cash_cnt = 0

while True:

    if card_payment + cash_payment >= needed_money:
        print(f"Average CS: {card_payment / card_cnt:.2f}")
        print(f"Average CC: {cash_payment / cash_cnt:.2f}")
        break

    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    money_products = int(command)

    product_count += 1
    is_cash_payment = product_count % 2 == 1

    if money_products <= 100 and is_cash_payment:
        card_payment += money_products
        card_cnt += 1

    elif money_products >= 10 and not is_cash_payment:

        cash_payment += money_products
        cash_cnt += 1
    else:
        print("Error in transaction!")
        continue
    print("Product sold!")


