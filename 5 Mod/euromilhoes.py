import random
print("-|PROGRAMA DE EUROMILHÕES|-")

boletins=[[[2,6,9,19,34],[2,8]],[[7,12,18,30,43],[1,7]],[[1,5,19,41,49],[6,7]],[[20,30,35,36,25],[6,8]],[[20,22,26,28,40],[10,12]],[[6,12,17,29,30],[3,10]],[[15,28,39,42,45],[3,7]],[[21,29,32,37,39],[3,9]],[[3,10,39,41,43],[1,5]],[[5,7,12,19,47],[3,10]]]

# Iniciar variáveis
total_bolas = []
bolas_sorteadas = []
total_estrelas = []
estrelas_sorteadas = []
bolas_certas = 0
estrelas_certas = 0
 

#input
bolas=int(input("Escolha as bolas: ".split()))
estrela= int(input("Estrelas: "))
aposta= [bolas,estrela]
boletins.append(aposta)

# Inserir bolas e estrelas
for i in range(1,51):
    total_bolas.append(i)
 
for j in range(1,13):
    total_estrelas.append(j)
 
# Sortear bolas e estrelas
for numeros in range(5):
    bola = random.choice(total_bolas)
    bolas_sorteadas.append(bola)
    total_bolas.remove(bola)
    bolas_certas += bolas_sorteadas.count(chave_bolas[numeros])    
 
for brilho in range(2):
    estrela = random.choice(total_estrelas)
    estrelas_sorteadas.append(estrela)
    total_estrelas.remove(estrela)
    estrelas_certas += estrelas_sorteadas.count(chave_estrelas[brilho])  

# ordenar
    bolas_sorteadas.sort()
    estrelas_sorteadas.sort()
nestrelascertas= 0
# Verificar os prémios
for boletim in boletins:
    n_bolas_certas=0
    n_estrelas_certas=0
    for bola in boletim[0]:
        if(bola in bolas_sorteadas):
            n_bolas_certas+=1
    for estrela in boletim[1]:
        if(estrela in estrelas_sorteadas):
            n_estrelas_certas+=1
    print(f"\nAposta {boletim}\n{n_bolas_certas} bolas certas\n{n_estrelas_certas} estrelas certas")
    if(n_bolas_certas==5 and n_estrelas_certas==2):
        print("JACKPOT")
    elif(n_bolas_certas==5 and n_estrelas_certas==1):
        print("2º Prémio")
    elif(n_bolas_certas==5 and n_estrelas_certas==0):
        print("3º Prémio")
    elif(n_bolas_certas==4 and n_estrelas_certas==2):
        print("4º Prémio")
    elif(n_bolas_certas==4 and n_estrelas_certas==1):
        print("5º Prémio")
    elif(n_bolas_certas==3 and n_estrelas_certas==2):
        print("6º Prémio")
    elif(n_bolas_certas==4 and n_estrelas_certas==0):
        print("7º Prémio")
    elif(n_bolas_certas==2 and n_estrelas_certas==2):
        print("8º Prémio")
    elif(n_bolas_certas==3 and n_estrelas_certas==1):
        print("9º Prémio")
    elif(n_bolas_certas==3 and n_estrelas_certas==0):
        print("10º Prémio")
    elif(n_bolas_certas==1 and n_estrelas_certas==2):
        print("11º Prémio")
    elif(n_bolas_certas==2 and n_estrelas_certas==1):
        print("12º Prémio")
    elif(n_bolas_certas==2 and n_estrelas_certas==0):
        print("13º Prémio")
    else:
        print("Não tem prémio")