natletas= int(input().split())

lançamentos= [0] * natletas

for i in range (natletas):
    lançamentos[i]= int(input()) 
    print (f"{max(lançamentos:.2f)} foi o maior lançamento em metros")
    print (f"{lançamentos.index(max(lançamentos))+1}")
    lançamentos.sort()
    lançamentos.reverse()
    print (lançamentos[:3])