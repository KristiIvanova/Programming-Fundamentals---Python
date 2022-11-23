text = input()
num = 0
for ch in range(len(text)):
    if text[ch] == "a":
        num += 1
    if text[ch] == "e":
        num += 2
    if text[ch] == "i":
        num += 3
    if text[ch] == "o":
        num += 4
    if text[ch] == "u":
        num += 5
print(num)