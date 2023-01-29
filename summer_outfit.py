temperature = int(input())
day = input()
outfit = None
shoes = None
if day == "Morning":
    if 10 <= temperature <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < temperature <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temperature >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif day == "Afternoon":
    if 10 <= temperature <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temperature <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif temperature >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif day == "Evening":
    if 10 <= temperature <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temperature <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temperature >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
