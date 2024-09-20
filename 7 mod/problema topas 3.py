M= int(input())
N= int(input())

temp= []
calor= []
frio= []

for i in range(N):
    Ti= int(input())
    if i > M:
            if i > M:
                calor.append(i)
    elif i < M:
            if i < M:
                frio.append(i)

    if len(calor) > len(frio):
            print ("FLAT")
    else:
            print ("WAVE")
