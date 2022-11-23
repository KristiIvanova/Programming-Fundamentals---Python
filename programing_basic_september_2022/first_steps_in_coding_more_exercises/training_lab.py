import  math

length_meters = float(input())
width_meters = float(input())

length_centimetre = length_meters * 100
width_centimetre = width_meters * 100

corridor_centimetre = 100

desk_per_row = (width_centimetre - corridor_centimetre)//70
rows = length_centimetre // 120

cnt_rows = int ((rows * desk_per_row) - 3)

print(cnt_rows)
