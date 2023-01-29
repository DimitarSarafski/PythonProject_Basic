budget = int(input())
season = input()
number_of_fishers = int(input())
ship_price = 0


if season == "Spring":
    ship_price = 3000
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
elif season == "Winter":
    ship_price = 2600

if number_of_fishers <= 6:
    discount = 0.10
elif 7 < number_of_fishers <= 11:
    discount = 0.15
elif number_of_fishers >= 12:
    discount = 0.25

ship_price = ship_price - (ship_price * discount)

if number_of_fishers % 2 ==0 and season != "Autumn":
    ship_price = ship_price - (ship_price * 0.05)

if budget >= ship_price:
    print(f"Yes! You have {budget - ship_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {ship_price - budget:.2f} leva.")
