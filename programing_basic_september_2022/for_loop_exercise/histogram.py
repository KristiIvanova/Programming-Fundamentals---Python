num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, num + 1):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num <= 399:
        p2 += 1
    elif current_num <= 599:
        p3 += 1
    elif current_num <= 799:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

perc_p1 = p1 / num * 100
print(f"{perc_p1:.2f}%")
perc_p2 = p2 / num * 100
print(f"{perc_p2:.2f}%")
perc_p3 = p3 / num * 100
print(f"{perc_p3:.2f}%")
perc_p4 = p4 / num * 100
print(f"{perc_p4:.2f}%")
perc_p5 = p5 / num * 100
print(f"{perc_p5:.2f}%")