name_actor = input()
points_academy = float(input())
cnt_people = int(input())

total_points = points_academy
for i in range (1,cnt_people + 1):
    name_evaluative = input()
    point_evaluative = float(input())

    current_points = (len(name_evaluative)*point_evaluative) / 2
    total_points += current_points

    if total_points >= 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")