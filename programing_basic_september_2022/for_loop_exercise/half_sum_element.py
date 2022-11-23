import sys
n = int(input())

max_num = - sys.maxsize
total_sum = 0
for i in range(0, n):
    sum_num = int(input())
    if sum_num > max_num:
         max_num = sum_num
    total_sum += sum_num
all_num_sum = total_sum - max_num
diff = abs (all_num_sum - max_num)
if all_num_sum == max_num:
    print("Yes")
    print(f"Sum = {all_num_sum}")
else:
    print("No")
    print(f"Diff = {diff:}")