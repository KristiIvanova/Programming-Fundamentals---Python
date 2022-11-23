month = input()
cnt_night_stay = int(input())

Apartment = 0
Studio = 0
if month in ['May', 'October']:
    if cnt_night_stay > 7 and cnt_night_stay < 14:
        Studio = cnt_night_stay * 50 * 0.95
        Apartment = cnt_night_stay * 65
    elif cnt_night_stay > 14:
        Studio = cnt_night_stay * 50 * 0.70
        Apartment = cnt_night_stay * 65 * 0.90
    else:
        Studio = cnt_night_stay * 50
        Apartment = cnt_night_stay * 65

elif month in ['June', 'September']:
    if cnt_night_stay > 14:
        Studio = cnt_night_stay * 75.20 * 0.80
        Apartment = cnt_night_stay * 68.70 * 0.90
    else:
        Studio = cnt_night_stay * 75.20
        Apartment = cnt_night_stay * 68.70

elif month in ['July', 'August']:
    if cnt_night_stay > 14:
        Studio = cnt_night_stay * 76
        Apartment = cnt_night_stay * 77 * 0.90
    else:
        Studio = cnt_night_stay * 76
        Apartment = cnt_night_stay * 77

print(f"Apartment: {Apartment:.2f} lv.")
print(f"Studio: {Studio:.2f} lv.")