cnt_holiday = int(input())

rest_days = cnt_holiday * 127
working_days = (365 - cnt_holiday) * 63
time_for_play = rest_days + working_days

diff = abs(30000 - time_for_play)
hours = diff // 60
minutes = diff % 60
if time_for_play > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")