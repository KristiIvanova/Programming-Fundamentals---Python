n = int(input())
left_side = 0
right_side = 0

for i in range(n):
     current_num = int(input())
     left_side += current_num
#print(left_side)


for i in range(n):
     current_num_2 = int(input())
     right_side += current_num_2
#print(right_side)

diff = abs(left_side - right_side)
if left_side == right_side:
     print(f"Yes, sum = {left_side}")
else:
     print(f"No, diff = {diff}")