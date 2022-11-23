import math
record_sec = float(input())
record_metre = float(input())
time_sec_1m = float(input())

time_seconds = record_metre * time_sec_1m
add_sec = math.floor(record_metre / 15) * 12.5
total_time = time_seconds + add_sec

if total_time >= record_sec:
    diff = abs(total_time - record_sec)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")