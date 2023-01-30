budget = float(input())
videocadrs = int(input())
procesors = int(input())
ram = int(input())

videocadrs_price = 250
videocadrs_total = videocadrs * 250
procesors_price =  videocadrs_total * 0.35
procesors_total = procesors * procesors_price
ram_cost = videocadrs_total * 0.10
ram_total = ram * ram_cost
cost_total = videocadrs_total + procesors_total + ram_total
if videocadrs > procesors:
    discount = cost_total * 0.15
    cost_total = cost_total - discount
if budget >= cost_total:
    money_left = budget - cost_total
    print(f"You have {money_left:.2f} leva left!")
else:
    money_need = cost_total -budget
    print(f"Not enough money! You need {money_need:.2f} leva more!")