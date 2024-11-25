str1 = input("Greeting: ")

if("Hello" in str1) or ("hello" in str1):
    print("$0")

elif(str1[0] == "h") or (str1[0] == "H"):
    print("$20")

else:
    print("$100")