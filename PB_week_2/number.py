# Да се напише програма, която чете цяло число, въведено
# от потребителя и проверява
# дали е под 100, между 100 и 200 или над 200. Ако числото е:

numbers = int(input())

if numbers < 100:
    print("Less than 100")
elif 100 <= numbers <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")