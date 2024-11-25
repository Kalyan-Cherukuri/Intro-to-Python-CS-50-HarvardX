str1 = input("Expressions: ")

x,y,z = str1.split(" ")

if y == "+":
    print(float(x)+float(z))

if y == "-":
    print(float(x)-float(z))

if y == "*":
    print(float(x)*float(z))

if y == "/":
    if int(z)==0:
        print("Not divisible by zero")
    else:
        print(float(x)/float(z))