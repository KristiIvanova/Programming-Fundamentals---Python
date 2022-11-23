days = int(input())
type_of_room = input()
opinion = input()

price = 0

if type_of_room == 'room for one person':
        price = (days - 1) * 18
elif type_of_room == 'apartment':
    if days < 10:
        price = ((days - 1) * 25) * 0.7
    elif 10 < days < 15:
        price = ((days - 1)* 25) * 0.65
    else:
        price = ((days - 1) * 25) * 0.5
elif type_of_room == 'president apartment':
    if days < 10:
        price = ((days - 1) * 35) * 0.9
    elif 10 < days < 15:
        price = ((days -1) * 35) * 0.85
    else:
        price = ((days - 1) * 35) * 0.80

if opinion == 'positive':
    price = price * 1.25
elif opinion == 'negative':
    price = price * 0.9
print(f"{price:.2f}")