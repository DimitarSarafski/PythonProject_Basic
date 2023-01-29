vegetable_price = float(input())
fruit_price = float(input())
vegetable = int(input())
fruit = int(input())
EUR = 1.94
vegetable_cost = vegetable * vegetable_price
fruit_cost = fruit * fruit_price
total_cost = vegetable_cost + fruit_cost
total_cost_EUR = total_cost / EUR
print(f"{total_cost_EUR:.2f}")