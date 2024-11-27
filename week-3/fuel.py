str1 = input("Fraction: ")

x, y = str1.split("/")

Fuel = (int(x)/int(y))*100


if Fuel == 0:
    print("E")
if (Fuel > 0) and (Fuel <= 25):
    print("25%")
if (Fuel > 25) and (Fuel <= 50):
    print("50%")
if (Fuel > 50) and (Fuel <= 75):
    print("75%")
if (Fuel > 75) and (Fuel < 100):
    print("100%")
if Fuel == 100:
    print("F")
elif int(x) == 0:
    print("")
else:
    print("")