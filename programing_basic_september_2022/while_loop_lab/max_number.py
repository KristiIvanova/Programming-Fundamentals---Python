import sys

max_num = - sys.maxsize

while True:
    current_num = input()
    if current_num == 'Stop':
        break

    current_num = int(current_num)

    if current_num > max_num:
        max_num = current_num

print(max_num)