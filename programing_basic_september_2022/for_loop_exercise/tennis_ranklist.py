import math

cnt_turnir = int(input())
entry_points = int(input())

additional_points_w = 0
additional_points_f = 0
additional_points_sf = 0
total_points = 0
win_count = 0
for i in range (1, cnt_turnir + 1):
    finish_turnir = input()
    if finish_turnir == 'W':
        additional_points_w += 2000
        win_count +=1
    elif finish_turnir == 'F':
        additional_points_f += 1200
    elif finish_turnir == 'SF':
        additional_points_sf += 720
    total_points = additional_points_w + additional_points_f + additional_points_sf + entry_points

perc_win = (win_count / cnt_turnir) * 100
average_points = math.floor((additional_points_sf + additional_points_f + additional_points_w) / cnt_turnir)
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{perc_win:.2f}%")