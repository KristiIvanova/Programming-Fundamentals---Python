length = int(input())
widht = int(input())
height = int(input())
percent = float(input())

volume_centimetre = length * widht * height
volume_littre = volume_centimetre / 1000
total_littre = volume_littre * (percent / 100)

result = volume_littre - total_littre

print(result)