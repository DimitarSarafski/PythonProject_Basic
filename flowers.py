bought_hrisatem = int(input())
bought_rose = int(input())
bought_lale = int(input())
season = input()
holiday = input()
combine = bought_hrisatem + bought_rose + bought_lale

if season == "Spring" or season == "Summer":
    HRISATEM_PRICE = 2.00
    ROSE_PRICE = 4.10
    LALE_PRICE = 2.50
else:
    HRISATEM_PRICE = 3.75
    ROSE_PRICE = 4.50
    LALE_PRICE = 4.15

total_price = (bought_hrisatem * HRISATEM_PRICE) + (bought_rose * ROSE_PRICE) + (LALE_PRICE * bought_lale)

if holiday == "Y":
    total_price = total_price + (total_price * 0.15)

if season == "Spring" and bought_lale > 7:
    total_price = total_price - (total_price * 0.05)
if season == "Winter" and bought_rose >= 10:
    total_price = total_price - (total_price * 0.10)

if combine > 20:
    total_price = total_price - (total_price * 0.20)

print(f"{total_price + 2:.2f}")