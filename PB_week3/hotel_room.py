mount = input()
nights = int(input())
studio = 0
apartment = 0

if mount == "May" or mount == "October":
    studio = 50
    apartment = 65
elif mount == "June" or mount == "September":
    studio = 75.20
    apartment = 68.70
elif mount == "July" or mount == "August":
    studio = 76
    apartment = 77

if mount == "May" or mount == "October":
        if 7 >= nights < 13:
            studio = studio - (studio * 0.05)
        elif(mount == "May" or mount == "October") and nights >= 14:
            studio = studio - (studio * 0.3)
if (mount == "June" or mount == "September")and nights > 14:
    studio = studio - (studio * 0.20)

if nights > 14 :
    apartment = apartment -(apartment * 0.10)

print(f"Apartment: { nights * apartment:.2f} lv.")
print(f"Studio: {nights * studio:.2f} lv.")