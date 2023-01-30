product = input()
day_of_the_week = input()
amount = float(input())
price = 0



if day_of_the_week == "Monday" or  day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday" \
        or day_of_the_week == "Thursday" or day_of_the_week == "Friday":
    if product == "banana":
        price = 2.50
        total = amount * price
        print(f"{total:.2f}")
    elif product == "apple":
        price = 1.20
        total = amount * price
        print(f"{total:.2f}")
    elif product == "orange":
        price = 0.85
        total = amount * price
        print(f"{total:.2f}")
    elif product == "grapefruit":
        price = 1.45
        total = amount * price
        print(f"{total:.2f}")
    elif product == "kiwi":
        price = 2.70
        total = amount * price
        print(f"{total:.2f}")
    elif product == "pineapple":
        price = 5.50
        total = amount * price
        print(f"{total:.2f}")
    elif product == "grapes":
        price = 3.85
        total = amount * price
        print(f"{total:.2f}")
    else:
        print("error")
elif day_of_the_week == "Saturday" or  day_of_the_week == "Sunday":
    if product == "banana":
        price = 2.70
        total = amount * price
        print(f"{total:.2f}")
    elif product == "apple":
        price = 1.25
        total = amount * price
        print(f"{total:.2f}")
    elif product == "orange":
        price = 0.90
        total = amount * price
        print(f"{total:.2f}")
    elif product == "grapefruit":
        price = 1.60
        total = amount * price
        print(f"{total:.2f}")
    elif product == "kiwi":
        price = 3.00
        total = amount * price
        print(f"{total:.2f}")
    elif product == "pineapple":
        price = 5.60
        total = amount * price
        print(f"{total:.2f}")
    elif product == "grapes":
        price = 4.20
        total = amount * price
        print(f"{total:.2f}")
    else:
        print("error")
else:
    print("error")
