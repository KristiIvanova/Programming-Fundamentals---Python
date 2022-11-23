budget = float(input())
season = input()

destination = ""
type_of_vacation = ""

if season == "summer":
    if budget <= 100:
       destination = 'Bulgaria'
       type_of_vacation = 'Camp'
       budget = budget * 0.30
    elif budget <= 1000:
        destination = 'Balkans'
        type_of_vacation = 'Camp'
        budget = budget * 0.4
    else:
        destination = 'Europe'
        type_of_vacation = 'Hotel'
        budget = budget * 0.9

elif season == "winter":
    type_of_vacation = 'Hotel'
    if budget <= 100:
        destination = 'Bulgaria'
        budget = budget * 0.70
    elif budget <= 1000:
        destination = 'Balkans'
        budget = budget * 0.8
    else:
        destination = 'Europe'
        budget = budget * 0.9


print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {budget:.2f}")