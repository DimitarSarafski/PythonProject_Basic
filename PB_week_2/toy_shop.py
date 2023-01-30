PUZZEL = 2.60
TALKING_DOLL = 3
TEDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

trip = float(input())
puzzel_amount = int(input())
talking_doll_amount = int(input())
teddy_bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())

total = puzzel_amount + talking_doll_amount + teddy_bear_amount + minion_amount + truck_amount
total_cost = (puzzel_amount * PUZZEL) + (talking_doll_amount * TALKING_DOLL) + (teddy_bear_amount * TEDY_BEAR) + (minion_amount * MINION) + (truck_amount * TRUCK)

if total >= 50:
    total_cost = total_cost - (total_cost * 0.25)

rent = total_cost - (total_cost * 0.10)

if total_cost >= trip:
    money_left = rent - trip
    print(f"Yes! {money_left:.2f} lv left.")
elif total_cost <= trip:
    money_left = trip - rent
    print(f"Not enough money! {money_left:.2f} lv needed.")
