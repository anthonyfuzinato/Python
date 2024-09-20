N = int(input())
L = []
R= []
for x in range (1,N+1):
    L.append(x)
    
while len(L) != 1:
    print (L)
    for i in range (len(L)):
        if i % 2 == 0:
            R.append(L[i])
    for i in R:
        L.remove(i)
    R.clear()

print (L[0])