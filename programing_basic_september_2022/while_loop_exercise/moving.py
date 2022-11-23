width_free = int(input())
lenght_free = int(input())
height_free = int(input())

free_space = width_free * lenght_free * height_free

input_line = input()
total_cartons = 0
no_more_space = False
while input_line != "Done":
    cnt_carton = int(input_line)
    total_cartons += cnt_carton
    diff = abs(total_cartons - free_space)

    if free_space < total_cartons:
        no_more_space = True
        break


    input_line = input()

if no_more_space:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")