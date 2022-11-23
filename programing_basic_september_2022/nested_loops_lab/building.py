cnt_floor = int(input())
cnt_room_of_floor = int(input())
floor_letter = ''

for floor in range (cnt_floor, 0, -1):
    for room in range (cnt_room_of_floor):
        if floor == cnt_floor:
            floor_letter = 'L'
        elif floor % 2 == 0:
            floor_letter = 'O'
        else:
            floor_letter = 'A'
        print(f"{floor_letter}{floor}{room}", end = " ")
    print()
