film = float(input())
statist = int(input())
statist_clothes = float(input())

decor = film * 0.10
statist_clothes_combine = statist_clothes * statist

if statist < 150:
    statist_clothes_combine = statist_clothes_combine
else:
    statist_clothes_combine = statist_clothes_combine - (statist_clothes_combine * 0.10)

total_cost = statist_clothes_combine + decor
if film > total_cost:
    money_left = film - total_cost
    print(f"Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    money_need = total_cost - film
    print(f"Not enough money!")
    print(f"Wingard needs {money_need:.2f} leva more.")

