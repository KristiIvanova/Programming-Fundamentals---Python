degree = float(input())
weather = ""

if 26.00 <= degree <= 35.00:
    weather = "Hot"
elif 20.01 <= degree <= 25.9:
    weather = "Warm"
elif 15.00 <= degree <= 20.00:
    weather = "Mild"
elif 12.00 <= degree <= 14.9:
    weather = "Cool"
elif 5.00 <= degree <= 11.9:
    weather = "Cold"
else:
   print("unknown")

print(weather)