I1,D1,I2,D2= map(int,input().split())

if I2 < 37:
    print("NORMAL")
elif I2 >= 37:
    if I2 and D2 > I1 and D1:
        print ("FEBRE SUBIU")
    elif I2 and D2 == I1 and D1:
        print ("FEBRE MANTEVE")
    else:
        print ("FEBRE BAIXOU")