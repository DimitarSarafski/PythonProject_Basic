fuel = input()
fuel_litres = float(input())
discount_card = input()

GASOLINE = 2.22
GAS = 0.93
DIESEL = 2.33
if discount_card == "Yes":
    GASOLINE -= 0.18
    GAS -= 0.08
    DIESEL -= 0.12

if fuel == "Diesel":
    sum = fuel_litres * DIESEL
elif fuel == "Gas":
    sum = fuel_litres * GAS
elif fuel == "Gasoline":
    sum = fuel_litres * GASOLINE

if  20 <= fuel_litres <= 25:
     sum = sum * 0.92
elif fuel_litres > 25:
    sum = sum * 0.90

print(f"{sum:.2f}lv.")

# if fuel not in ["Diesel", "Gasoline", "Gas"]:
#     print("Invalid fuel!")
# elif fuel_litres >= 25:
#     print(f"You have enough {(fuel).lower()}. ")
#
# else:
#     print(f"Fill your tank with {(fuel).lower()}!")
