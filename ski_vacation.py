days = int(input())
type_room = input()
review = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35
total_cost = 0
days = days -1
if days < 10:
    if type_room == "apartment":
        total_cost = days * apartment
        total_cost = total_cost - (total_cost * 0.30)
    elif type_room == "president apartment":
        total_cost = days * president_apartment
        total_cost = total_cost - (total_cost - 0.10)
    else:
        total_cost = days * room_for_one_person
elif 10 <= days < 15:
    if type_room == "apartment":
        total_cost = days * apartment
        total_cost = total_cost - (total_cost * 0.35)
    elif type_room == "president apartment":
        total_cost = days * president_apartment
        total_cost = total_cost - (total_cost - 0.15)
    else:
        total_cost = days * room_for_one_person
elif days > 15:
    if type_room == "apartment":
        total_cost = days * apartment
        total_cost = total_cost - (total_cost * 0.50)
    elif type_room == "president apartment":
        total_cost = days * president_apartment
        total_cost = total_cost - (total_cost * 0.20)
    else:
        total_cost = days * room_for_one_person

if review =="positive":
    total_cost = total_cost + (total_cost *0.25)
elif review =="negative":
    total_cost = total_cost - (total_cost * 0.10)

print(f"{total_cost:.2f}")