import numpy
import random
 
def mostrar_tabuleiro(tabuleiro):
    print(tabuleiro_jogo)
 
# Defenir a matriz do jogo
linhas=int(input("Quantas linhas:"))
colunas=int(input("Quantas colunas:"))
minas=int(input("Quantas minas:"))
tabuleiro = numpy.matrix([['-']*colunas]*linhas)
tabuleiro_jogo= numpy.matrix([["-"]*colunas]*linhas)
# -------- Criar as minas ------------
 
# lista com as posições do tabuleiro
casas=[]
for i in range(linhas*colunas):
    casas.append(i+1)
 
# escolher de forma aleatória a posição das minas
for i in range(minas):
    numero_casa=random.choice(casas)  
    linha_casa= numero_casa // colunas
    coluna_casa=numero_casa % colunas
    if(coluna_casa==0):
        linha_casa-=1
        coluna_casa=colunas-1
    casas.remove(numero_casa)
    tabuleiro[linha_casa,coluna_casa]="X"
 
#----------------------------------------------------------
 
# Jogar
   
mostrar_tabuleiro(tabuleiro_jogo)
 
while True:
   
    # ---- ler a posição da casa escolhida pelo jogador -----
   
    # Ler e verificar a linha escolhida
    linha=linhas+1
    while(linha>linhas):
        linha=int(input("Linha:"))-1
        if(linha>linhas-1):
            print("Linha Errada")
     
    # Ler e verificar a coluna escolhida
    coluna=colunas+1
    while(coluna>colunas):  
        coluna=int(input("Coluna:"))-1
        if(coluna>colunas-1):
            print("Coluna Errada")
   
    # Testar se abriu uma mina
    if(tabuleiro[linha,coluna]=="X"):
        print("Game Over")
        print(tabuleiro)
        break

    # testa se ja esta ocupado
    if(tabuleiro[linha,coluna]=="1" or tabuleiro[linha,coluna]=="2" or tabuleiro[linha,coluna]=="3"):
        print("Ja foi escolhido! ")

    # Testar quantas minas existem nas casas adjacentes
    numero_minas_adjacentes=0
   
    # Testar a casa à esquerda
    if (coluna!=0):
        if(tabuleiro[linha,coluna-1]=="X"):
            numero_minas_adjacentes+=1
 
    # Testar a casa à direita
    if (coluna!=colunas-1):
        if(tabuleiro[linha,coluna+1]=="X"):
            numero_minas_adjacentes+=1
   
    # Testar a casa em cima
    if (linha!=0):
        if(tabuleiro[linha-1,coluna]=="X"):
            numero_minas_adjacentes+=1
   
     # Testar a casa em baixo
    if (linha!=linhas-1):
        if(tabuleiro[linha+1,coluna]=="X"):
            numero_minas_adjacentes+=1
 
    # Testar a casa em cima à esquerda
    if (linha!=0 and coluna!=0):
        if(tabuleiro[linha-1,coluna-1]=="X"):
            numero_minas_adjacentes+=1
   
    # Testar a casa em cima à direita
    if (linha!=0 and coluna!=colunas-1):
        if(tabuleiro[linha-1,coluna+1]=="X"):
            numero_minas_adjacentes+=1
 
    # Testar a casa em baixo à esquerda
    if (linha!=linhas-1 and coluna!=0):
        if(tabuleiro[linha+1,coluna-1]=="X"):
            numero_minas_adjacentes+=1
 
    # Testar a casa em baixo à direita
    if (linha!=linhas-1 and coluna!=colunas-1):
        if(tabuleiro[linha+1,coluna+1]=="X"):
            numero_minas_adjacentes+=1
 
    # Escrever na casa o número de minas adjacente
    tabuleiro_jogo[linha,coluna]=numero_minas_adjacentes
 
    mostrar_tabuleiro(tabuleiro_jogo)

    contar_casas_ocupadas= 0
    for linha in range(tabuleiro_jogo.shape[0]):
        for coluna in range(tabuleiro_jogo.shape[1]):
            if tabuleiro_jogo[linha,coluna]!='-':
                contar_casas_ocupadas+=1
            if contar_casas_ocupadas==linhas*colunas-minas:
                print('Parabens! Descobriu todas as minhas ')
                break