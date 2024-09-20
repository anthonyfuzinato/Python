alturas= list(map(int(input().split())))

print (f"A media dos jogadores {:.2f}".format {sum(alturas)/len(alturas)})

nposte= 0
nbase= 0
for i in range (len(alturas)):
    if i > 190:
        nposte +=1

for i in range (len(alturas)):
    if alturas[i] < 175:
        nbase +=1

print (f"A media dos jogadores {:.2f}".format {sum(alturas)/len(alturas)})
print (f"O numero de bases é de {nbase}" \n "O numero de pontes {nposte}")