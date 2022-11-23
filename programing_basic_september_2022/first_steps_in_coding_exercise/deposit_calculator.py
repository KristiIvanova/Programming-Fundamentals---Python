deposit_amount = float(input())
month = int(input())
annual_rate_percent = float(input())

whole_rates = deposit_amount * annual_rate_percent / 100
rate_per_month = whole_rates / 12
total_amount = deposit_amount + month * rate_per_month

print(total_amount)
