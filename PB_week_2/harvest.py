from math import floor
#inputs
x_loze = int(input())
y_grozde = float(input())
z_litri_vino = int(input())
rabotnici = int(input())

#logic and outputs
otdeleno = x_loze * y_grozde
otdeleno = otdeleno * 0.40

proizvedeno = otdeleno / 2.5

if proizvedeno >= z_litri_vino:

    print(f"Good harvest this year! Total wine: {floor(proizvedeno)} liters.")
    print(f"{floor(proizvedeno - z_litri_vino)} liters left -> {floor((proizvedeno - z_litri_vino)/rabotnici)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(z_litri_vino - proizvedeno)} liters wine needed.")

