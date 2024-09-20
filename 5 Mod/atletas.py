natletas= int(input())
nomes= []
tempo= []
atletas=int(input('Quantos atletas são? '))
dic=[(nome:atleta)*atletas]
for i in range(natletas):
    nome, atleta= input(f"O atleta nº{i+1}").split()
    nome.append(nomes)
    tempo.append(atleta)

for x in tempo:
    menor= tempo.index(min(tempo))
    sla= nomes[menor]

print ()