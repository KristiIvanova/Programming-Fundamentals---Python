pool_volume_liters = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

fill_p1 = p1 * hours
fill_p2 = p2 * hours
total_fill = fill_p2 + fill_p1
total_fill_percent = total_fill / pool_volume_liters * 100
fill_p1_percent = fill_p1 / total_fill * 100
fill_p2_percent = fill_p2 / total_fill * 100

if total_fill <= pool_volume_liters:
    print(f"The pool is {total_fill_percent:.2f}% full. " \
            f"Pipe 1: {fill_p1_percent:.2f}%. Pipe 2: {fill_p2_percent:.2f}%.")
else:
    diff = abs(total_fill - pool_volume_liters)
    print(f"For {hours} hours the pool overflows with {diff:.2f} liters.")
