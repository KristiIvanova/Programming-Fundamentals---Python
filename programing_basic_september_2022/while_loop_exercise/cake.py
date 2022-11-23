
width = int(input())
lenght = int(input())

total_cake = width * lenght
no_more_pieces = False

cnt_pieces = input()
while cnt_pieces != "STOP":
    part_cake = int(cnt_pieces)

    total_cake -= part_cake

    if total_cake <= 0:
        no_more_pieces = True
        break

    cnt_pieces = input()

if no_more_pieces:
    print(f"No more cake left! You need {abs(total_cake)} pieces more.")
else:
    print(f"{total_cake} pieces are left.")

