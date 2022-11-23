destination = input()

while destination != "End":
    budget = float(input())
    money_in_hand = 0
    while money_in_hand < budget:
        current_money = float(input())
        money_in_hand += current_money
    print(f"Going to {destination}!")

    destination = input()
