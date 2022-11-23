price_mackerel = float(input())
price_sprat = float(input())
price_bonito = float(input())
price_safrid = float(input())
price_midi = float(input())

sum_bonito = price_mackerel + (price_mackerel * 0.6)
total_price_bonito = price_bonito * sum_bonito
sum_safrid = price_sprat + (price_sprat * 0.8)
total_price_safrid = sum_safrid * price_safrid
total_price_midi = price_midi * 7.5

bill = total_price_midi + total_price_bonito + total_price_safrid

print(f"{bill:.2f}")