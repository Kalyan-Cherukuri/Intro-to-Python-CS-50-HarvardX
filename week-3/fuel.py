while(True):
    try:
        str1 = input("Fraction: ")
        x, y = str1.split("/")
        Fuel = (int(x) / int(y)) * 100
        if (Fuel>=0) and (Fuel<20):
            print("E")
        elif (Fuel>=20) and (Fuel<40):
            print("25%")
        elif (Fuel>=40) and (Fuel<60):
            print("50%")
        elif (Fuel>=60) and (Fuel<80):
            print("75%")
        elif (Fuel>=80) and (Fuel<=100):
            print("F")
    except (ZeroDivisionError, ValueError):
        print("X is not an integer")
    else:
        break