hours = int(input())
min = int(input(  ))

total_hour_min = (hours * 60) + min + 15
hours = total_hour_min // 60
min = total_hour_min % 60

if hours > 23:
    hours = 0
if min < 10:
    print(f"{hours}:0{min}")
else:
    print(f"{hours}:{min}")