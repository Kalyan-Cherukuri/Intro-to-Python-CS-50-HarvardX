def main():
    #name, house = get_student()
    #student = get_student()
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    return {"name": name, "house": house}

if __name__ == '__main__':
    main()