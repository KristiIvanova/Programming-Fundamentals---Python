n = int(input())
even_num = 0
odd_num = 0

for i in range (n):
    current_number = int(input())
    if i % 2 == 0:
        even_num += current_number
    else:
        odd_num += current_number

diff = abs(even_num - odd_num)
if even_num == odd_num:
    print("Yes")
    print(f"Sum = {even_num}")
else:
    print("No")
    print(f"Diff = {diff}")