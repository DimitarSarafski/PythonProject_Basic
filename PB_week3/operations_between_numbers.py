number1 = int(input())
number2 = int(input())
operator_for_calculate = input()
sum = ""

if operator_for_calculate == "+":
    sum = f"{number1} + {number2} = {number1 + number2}" + (" - even" if (number1 + number2) % 2 == 0 else " - odd")
elif operator_for_calculate == "-":
    sum = f"{number1} - {number2} = {number1 - number2}" + (" - even" if (number1 - number2) % 2 == 0 else " - odd")
elif operator_for_calculate == "*":
    sum = f"{number1} * {number2} = {number1 * number2}" + (" - even" if (number1 * number2) % 2 == 0 else " - odd")
elif number2 == 0:
    print(f"Cannot divide {number1} by zero")
elif operator_for_calculate == "/":
    sum = f"{number1} / {number2} = {number1 /number2:.2f}"
elif operator_for_calculate == "%":
    sum = f"{number1} % {number2} = {number1 % number2}"

print(sum)