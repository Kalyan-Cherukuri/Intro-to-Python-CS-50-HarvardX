def main():
    str1 = input("How long do you want? ")
    time1 = (convert(str1))
    if (time1>=7) and (time1<=8):
        print("breakfast time")
    elif (time1>=12) and (time1<=13):
        print("Lunch time")
    elif (time1>=18) and (time1<=19):
        print("Dinner time")
    else:
        print(" ")
def convert(time):
    hrs, min = time.split(":")
    return(((float(hrs)*60)+float(min))/60)

if __name__ == "__main__":
    main()