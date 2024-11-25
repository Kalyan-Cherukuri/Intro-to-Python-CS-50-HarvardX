str1 = input("File name: ")

if ".gif" in str1:
    print("image/gif")
elif ".jpg" in str1 or ".jpeg" in str1:
    print("image/jpeg")
elif ".png" in str1:
    print("image/png")
elif ".pdf" in str1:
    print("application/pdf")
elif ".txt" in str1:
    print("application/text")
elif ".zip" in str1:
    print("application/zip")
else:
    print("application/octet-stream")