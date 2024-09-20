N_atletas= int(input())

tempos= []
nomes= []

for i in range (N_atletas):
    nomes.append[input("qual o nome do atleta nº? "+i)]
    tempos.append[float(input("qual o tempo do atleta nº? "+i))]

tempos_ordenados= tempos.copy()
tempos_ordenados.sort()
 
for i in range (N_atletas):
    print (f"{i + 1}º lugar - {nomes[tempos.index(tempos_ordenados[i])]} {tempos_ordenados[i]}")            