junior_bikers = int(input())
seniors_bikers = int(input())
trace = input()

junior_tax = 0
seniors_tax = 0
money_earned = 0
if trace =="trail":
    junior_tax = 5.50
    seniors_tax = 7
elif trace == "cross-country":
    junior_tax = 8
    seniors_tax = 9.50
elif trace == "downhill":
    junior_tax = 12.25
    seniors_tax = 13.75
else:
    junior_tax = 20
    seniors_tax = 21.50

money_earned = (junior_bikers * junior_tax) + (seniors_tax * seniors_bikers)

bikers_combine = junior_bikers + seniors_bikers
if bikers_combine >= 50 and trace == "cross-country":

    money_earned = money_earned - (money_earned * 0.25)

money_earned = money_earned - (money_earned * 0.05)

print(f"{money_earned:.2f}")
