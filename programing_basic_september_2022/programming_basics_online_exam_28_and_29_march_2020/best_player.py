import sys
max_score = - sys.maxsize
name_player = input()



hat_trick = False

best_player = ""
current_name = ""

while name_player != "END":
    cnt_goal = int(input())
    current_name = name_player
    if cnt_goal > max_score:
        max_score = cnt_goal
        best_player = current_name
#   if cnt_goal >=3:
#        hat_trick += cnt_goal
    if cnt_goal >= 10:
        break
    name_player = input()

print(f"{best_player} is the best player!")
if max_score >=3:
   print(f"He has scored {max_score} goals and made a hat-trick !!!")
elif max_score < 3:
   print(f"He has scored {max_score} goals.")