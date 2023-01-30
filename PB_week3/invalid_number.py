numbers = int(input())

valid = 100 <= numbers <= 200 or numbers == 0
if not valid:
    print("invalid")