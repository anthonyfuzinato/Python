nosso, deles, R= map(int,input().split())

if nosso + (R * 3)> deles + (R * 3):
    print (":-D")

elif deles < nosso:
    print (":-)")
elif nosso + (R * 3) >= deles:
    print(":-|")

elif deles > nosso:
    print(":-(")