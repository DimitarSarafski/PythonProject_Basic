flower = input()
number_of_flowers = int(input())
budget = int(input())
total_amount = 0
ROSES = 5
DAHLIAS = 3.80
TULIPS = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

if flower == "Roses":
    total_amount = number_of_flowers * ROSES
    if number_of_flowers > 80:
        total_amount = total_amount - (total_amount * 0.1)
elif flower == "Dahlias":
    total_amount = number_of_flowers * DAHLIAS
    if number_of_flowers > 90:
        total_amount = total_amount - (total_amount * 0.15)
elif flower == "Tulips":
    total_amount = number_of_flowers * TULIPS
    if number_of_flowers > 80:
        total_amount = total_amount - (total_amount * 0.15)
elif flower == "Narcissus":
    total_amount = number_of_flowers * NARCISSUS
    if number_of_flowers < 120:
        total_amount = total_amount + (total_amount * 0.15)
elif flower == "Gladiolus":
    total_amount = number_of_flowers * GLADIOLUS
    if number_of_flowers < 80:
        total_amount = total_amount + (total_amount * 0.20)

if total_amount <= budget:
    money_left = budget - total_amount
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_amount - budget:.2f} leva more. ")