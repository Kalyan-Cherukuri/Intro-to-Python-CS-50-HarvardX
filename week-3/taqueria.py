dict1= {
"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
Total = 0
while True:
    try:
        item = input("Item: ")
        if item in dict1.keys():
            Total = Total + dict1[item]
            print(f"Total: ${Total}")
    except EOFError:
        break
