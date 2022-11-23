year_price = int(input())
basketball_shoes = year_price - (year_price * 0.4)
basketball_equipe = basketball_shoes - (basketball_shoes  * 0.2)
basketball_ball = basketball_equipe/4
basketball_accessories = basketball_ball/5
total_amount = basketball_accessories + basketball_ball + basketball_shoes + basketball_equipe + year_price

print(total_amount)
