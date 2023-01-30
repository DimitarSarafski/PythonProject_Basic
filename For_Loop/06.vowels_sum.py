text = input()
sum = 0

for ch in text:
    if ch == "a":
        sum = sum + 1
    if ch == "e":
        sum = sum + 2
    if ch == "i":
        sum = sum + 3
    if ch == "o":
        sum = sum + 4
    if ch == "u":
        sum = sum + 5
print(sum)
