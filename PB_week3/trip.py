budget = float(input())
season = input()
destination =""
type = ""
cost = 0

if budget <= 100:
    destination = "Bulgaria"
    if season =="summer":
        type = "Camp"
        cost = budget * 0.30
    else:
        type = "Hotel"
        cost = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type = "Camp"
        cost = budget * 0.40
    else:
        type = "Hotel"
        cost = budget * 0.80
else:
    destination = "Europe"
    type = "Hotel"
    cost = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type} - {cost:.2f}")
