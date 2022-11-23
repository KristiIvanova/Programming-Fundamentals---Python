juniors_cyclist = int(input())
seniors_cyclist = int(input())
type_road = input()

tax = 0
if juniors_cyclist and type_road == "trail":
    tax += 5.5 * juniors_cyclist
elif juniors_cyclist and type_road == "cross-country":
    tax += 8 * juniors_cyclist
elif juniors_cyclist and type_road == "downhill":
    tax += 12.25 * juniors_cyclist
elif juniors_cyclist and type_road == "road":
    tax += 20 * juniors_cyclist
if seniors_cyclist and type_road == "trail":
    tax += 7 * seniors_cyclist
elif seniors_cyclist and type_road == "cross-country":
    tax += 9.5 * seniors_cyclist
elif seniors_cyclist and type_road == "downhill":
    tax += 13.75 * seniors_cyclist
elif seniors_cyclist and type_road == " road":
    tax += 21.50 * seniors_cyclist

if (juniors_cyclist + seniors_cyclist) >= 50 and type_road == "cross-country":
        tax = tax * 0.75

left_money = tax - (tax * 0.05)
print(f"{left_money:.2f}")
