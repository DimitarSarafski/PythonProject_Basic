from math import ceil, floor
#inputs
days = int(input())
food_left = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_turtle = float(input())
#outputs
dog_eat = days * food_for_dog
cat_eat = days * food_for_cat
turtle_eat = (days * food_for_turtle) / 1000
food_combine= dog_eat + cat_eat + turtle_eat

if food_combine >= food_left:
    print(f"{ceil(food_combine - food_left)} more kilos of food are needed.")
else:

    print(f"{floor(food_left - food_combine)} kilos of food left.")

