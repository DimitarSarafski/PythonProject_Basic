season = input()
kilometres_per_mount = float(input())

price_for_kilometer = 0

if kilometres_per_mount <= 5000:
    if season == "Spring" or season == "Autumn":
        price_for_kilometer = 0.75
    elif season == "Summer":
        price_for_kilometer = 0.90
    else:
        price_for_kilometer = 1.05
elif 5000 < kilometres_per_mount <= 10000:
    if season == "Spring" or season == "Autumn":
        price_for_kilometer = 0.95
    elif season == "Summer":
        price_for_kilometer = 1.10
    else:
        price_for_kilometer = 1.25
else:
    price_for_kilometer = 1.45

total_money_earned = (kilometres_per_mount * price_for_kilometer)*4
total_money_earned = total_money_earned - (total_money_earned * 0.10)
print(f"{total_money_earned:.2f}")