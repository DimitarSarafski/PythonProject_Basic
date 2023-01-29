season = input()
group_type = input()
nunber_of_students = int(input())
nights = int(input())

type_sport = None
total_price = 0
price_for_vacation = 0

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price_for_vacation = 9.6
    else:
        price_for_vacation = 10
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price_for_vacation = 7.2
    else:
        price_for_vacation = 9.5
else:
    if group_type == "boys" or group_type == "girls":
        price_for_vacation = 15
    else:
        price_for_vacation = 20

if season == "Winter":
    if group_type == "girls":
        type_sport = "Gymnastics"
    elif group_type == "boys":
        type_sport = "Judo"
    else:
        type_sport = "Ski"
elif season == "Spring":
    if group_type == "girls":
        type_sport = "Athletics"
    elif group_type == "boys":
        type_sport = "Tennis"
    else:
        type_sport = "Cycling"
else:
    if group_type == "girls":
        type_sport = "Volleyball"
    elif group_type == "boys":
        type_sport = "Football"
    else:
        type_sport = "Swimming"

total_price = (nunber_of_students * price_for_vacation) * nights

if nunber_of_students >= 50:
    total_price = total_price * 0.50
elif 20 <= nunber_of_students < 50:
    total_price = total_price * 0.85
elif 10 <= nunber_of_students < 20:
    total_price = total_price * 0.95
else:
    total_price = total_price

print(f"{type_sport} {total_price:.2f} lv.")