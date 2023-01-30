budget = float(input())
category = input()
people = int(input())

VIP = 499.99
NORMAL = 249.99
tiket_prize = 0


if 1 <= people <= 4:
    budget = budget - (budget * 0.75)
elif 5 < people <= 9:
    budget = budget - (budget * 0.60)
elif 10 < people <= 24:
    budget = budget - (budget * 0.50)
elif 25 < people <= 49:
    budget = budget - (budget * 0.40)
else:
    budget = budget - (budget * 0.25)

if category == "VIP":
    tiket_prize = people * VIP
else:
    tiket_prize = people * NORMAL

if tiket_prize <= budget:
    print(f"Yes! You have {budget - tiket_prize:.2f} leva left.")
else:
    print(f"Not enough money! You need {tiket_prize - budget:.2f} leva.")