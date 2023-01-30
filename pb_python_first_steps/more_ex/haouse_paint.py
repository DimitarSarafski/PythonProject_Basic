height_house = float(input())
weight_house = float(input())
height_celling = float(input())

wall = weight_house * height_house
window = (1.5 * 1.5) * 2
all_walls = (wall * 2) - window
back_wall = height_house * height_house
door = 1.2 * 2
front_and_back_wall = 2 * back_wall - door
combine_house = all_walls + front_and_back_wall
green_paint = combine_house / 3.4
celling_wall = 2 * (height_house * weight_house)
celling_front_back = 2 * ((height_house * height_celling) / 2)
cell = celling_wall + celling_front_back
red_paint = cell / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
