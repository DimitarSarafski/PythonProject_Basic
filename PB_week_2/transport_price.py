kilometres = int(input())
day_or_night = input()
if kilometres >= 100:
    price = kilometres * 0.06
elif 100 > kilometres >= 20:
    price = kilometres * 0.09
else:
    if day_or_night == "day":
        price = 0.70 + (kilometres *0.79)
    else:
        price = 0.70 + (kilometres *0.90)
print(f"{price:.2f}")