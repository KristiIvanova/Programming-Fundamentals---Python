first_num = int(input())
second_num = int(input())

f_thousands = first_num // 1000 % 10
f_hundreds = first_num // 100 % 10
f_tens = first_num // 10 % 10
f_units = first_num % 10

s_thousands = second_num // 1000 % 10
s_hundreds = second_num // 100 % 10
s_tens = second_num // 10 % 10
s_units = second_num % 10



for i1 in range (f_thousands, s_thousands + 1):
     for i2 in range(f_hundreds, s_hundreds + 1):
          for i3 in range(f_tens, s_tens + 1):
               for i4 in range(f_units, s_units + 1):
                 if i1 % 2 != 0 and i2 % 2 != 0 and i3 % 2 != 0 and i4 % 2 != 0:
                    print(f"{i1}{i2}{i3}{i4}", end=" ")
