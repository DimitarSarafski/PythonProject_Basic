from math import  floor, ceil
magnolia = int(input())
zumbil = int(input())
rose = int(input())
cactus = int(input())
gift = float(input())

MAGNOLIA = 3.25
ZUMBIL = 4
ROSE = 3.50
CACTUS = 8

sum_combine = (magnolia * MAGNOLIA) + \
              (zumbil * ZUMBIL) +\
              (rose * ROSE) +\
              (cactus * CACTUS)
sum = sum_combine * 0.95

if gift <= sum:
    print(f"She is left with {floor(sum - gift)} leva.")
else:
    print(f"She will have to borrow {ceil(gift - sum)} leva.")
