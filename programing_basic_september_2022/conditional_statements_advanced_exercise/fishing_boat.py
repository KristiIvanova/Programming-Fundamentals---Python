budget = int(input())
season = input()
cnt_fisher = int(input())

rent = 0
if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if cnt_fisher <= 6:
    rent = rent * 0.9
elif 6 < cnt_fisher <= 11:
    rent = rent * 0.85
elif cnt_fisher > 11:
    rent = rent * 0.75

if cnt_fisher % 2 == 0 and season != 'Autumn':
    rent = rent * 0.95

diff = abs(rent - budget)
if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")