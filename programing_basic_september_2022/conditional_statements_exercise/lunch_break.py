from math import ceil

name_of_serial = input()
duration_of_episod = int(input())
duration_break = int(input())

duration_rest = duration_break / 4
duration_lunch = duration_break / 8

total_time = duration_break - duration_lunch - duration_rest

diff = abs(total_time - duration_of_episod)
rounded_diff = ceil(diff)
if total_time >= duration_of_episod:
    print(f"You have enough time to watch {name_of_serial} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {rounded_diff} more minutes.")