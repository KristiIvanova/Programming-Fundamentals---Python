cnt_nylon = int(input())
cnt_paint_littre = int(input())
cnt_thinner_littre = int(input())
hours = int(input())

price_nylon = (cnt_nylon+2) * 1.50
price_paint = (cnt_paint_littre + (cnt_paint_littre * 0.1)) * 14.50
price_thinner = cnt_thinner_littre * 5
price_materials = price_nylon + price_paint + price_thinner + 0.4
price_painters = (price_materials * 0.3) * hours
total_price = price_materials + price_painters

print(total_price)