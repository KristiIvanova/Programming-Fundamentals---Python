N1 = int(input())
N2 = int(input())
operation = input()

result = 0
zero_flag = False
if operation == '+':
    result = N1 + N2
elif operation == '-':
    result = N1 - N2
elif operation == '*':
    result = N1 * N2
elif operation == '/':
    if N2 == 0:
        zero_flag = True
    else:
        result = N1 / N2
elif operation == '%':
    if N2 == 0:
        zero_flag = True
    else:
        result = N1 % N2

if result % 2 == 0 and zero_flag == False and operation in ['+','-','*']:
    print(f"{N1} {operation} {N2} = {result} - even")
elif result % 2 != 0 and zero_flag == False and operation in ['+','-','*']:
    print(f"{N1} {operation} {N2} = {result} - odd")
elif operation == '/' and zero_flag == False :
    print(f"{N1} {operation} {N2} = {result:.2f}")
elif operation == '%' and zero_flag == False :
    print(f"{N1} {operation} {N2} = {result}")
elif operation in ['/','%'] and zero_flag == True:
    print (f"Cannot divide {N1} by zero")



