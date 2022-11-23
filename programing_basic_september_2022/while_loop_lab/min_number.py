import sys

min_num = sys.maxsize

while True:
    current_num = input()

    if current_num == 'Stop':
        break

    current_num = int (current_num)

    if current_num < min_num:
        min_num = current_num
print(min_num)