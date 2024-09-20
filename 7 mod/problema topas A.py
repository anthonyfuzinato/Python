S,T,D = map(int, input().split())
 
 
if S==1:
    print ((T* 10)+(D*80)+100)
    if (T* 10)+(D*80)+100<250:
        print(250)
 
elif S==2:
    print ((T*15)+(D*120)+150)
    if (T*15)+(D*120)+150<350:
        print (350)
