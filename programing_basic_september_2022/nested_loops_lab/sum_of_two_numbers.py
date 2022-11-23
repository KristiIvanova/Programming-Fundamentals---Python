start_interval = int(input())
final_interval = int(input())
magic_number = int(input())

flag = False
counter_combination = 0
for a in range (start_interval, final_interval +1):
    for b in range (start_interval, final_interval + 1):
        counter_combination += 1
        if a + b == magic_number:
            print (f"Combination N:{counter_combination} ({a} + {b} = {magic_number})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{counter_combination} combinations - neither equals {magic_number}")