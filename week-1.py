"""
1.Indoor Voice

str1 = input("Enter a string: ")
str2 = str1.lower()
print(str2)
"""


"""
2.Playback Speed

str1 = input("Enter a string: ")
str2 = str1.replace(" ","...")
print(str2)
"""


"""
3.Making faces

str1 = input("Enter a string: ")
str2 = str1.replace(":(","🙁").replace(":)","🙂")
print(str2)
"""


"""
4.Einstein
m = int(input("Enter a number: "))
c = 300000000

E = m*c**2
print(E)
"""


"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars * percent)/100
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d[1:5]
    print(d)
    return float(d)


def percent_to_float(p):
    p = p[0:2]
    return float(p)

main()
"""

