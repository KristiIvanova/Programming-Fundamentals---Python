cnt_pages = int(input())
pages_per_hour = int(input())
total_days = int(input())

whole_time_reading = cnt_pages // pages_per_hour
hours_per_day = whole_time_reading // total_days

print(hours_per_day)