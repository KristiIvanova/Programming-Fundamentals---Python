number = int(input())

cnt_numbers = 0
sum_numbers = 0
for n in range (0,number):
    numbers = int(input())
    sum_numbers += numbers
    cnt_numbers +=1


print(f"{sum_numbers/cnt_numbers:.2f}")

