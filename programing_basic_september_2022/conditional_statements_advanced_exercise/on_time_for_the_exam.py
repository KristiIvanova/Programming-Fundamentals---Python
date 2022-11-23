hour_of_exam = int(input())
min_of_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())

all_hour_min_exam = (hour_of_exam * 60) + min_of_exam
all_hour_min_arrival = (hour_arrival * 60) + min_arrival
diff_min = abs(all_hour_min_arrival-all_hour_min_exam)
if all_hour_min_arrival > all_hour_min_exam:
    print('Late')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")
elif all_hour_min_arrival == all_hour_min_exam or diff_min <= 30:
    print('On time')
    if  diff_min > 0:
        print(f"{diff_min} minutes before the start")
elif diff_min > 30:
    print('Early')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")