type_of_gorivo = input()
littre = int(input())
word = type_of_gorivo.lower ()

if type_of_gorivo == "Diesel" and littre >= 25:
    print(f"You have enough {word}.")
elif type_of_gorivo == "Gasoline" and littre >= 25:
    print(f"You have enough {word}.")
elif type_of_gorivo == "Gas" and littre >= 25:
    print(f"You have enough {word}.")
elif type_of_gorivo == "Diesel" and littre < 25:
    print(f"Fill your tank with {word}!")
elif type_of_gorivo == "Gasoline" and littre < 25:
    print(f"Fill your tank with {word}!")
elif type_of_gorivo == "Gas" and littre < 25:
    print(f"Fill your tank with {word}!")
elif type_of_gorivo not in ["diesel", "gasoline", "gas"]:
    print("Invalid fuel!")