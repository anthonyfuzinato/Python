import random 

def menu(): 
    print("-"*30)
    print("Menu")
    print("-"*30)
    print("1- Iniciante")
    print("2- Medio")
    print("3- Dificil")
    print("4- Mostrar pontos")
    print("0- Acabar Jogo")
    print("-"*30)

opcao= int(input())
string= ""
pontostotais= 0

pontos= []
palavrasiniciante= []
palavramedia= []
palavradificil= []

stringfacil= "Bolo", "Ovo", "Rato","Oculos", "Lapis".upper()
stringmedio= "Horario", "Aviao","Caderno","Monitor","Porta".upper()
stringdificil= "Computador","AutoCarro","Janelas","Processador".upper()


while opcao != 0:

    #opçao 1 
    if opcao == "1":
        print("Palavra Facil")
        for i in palavrasiniciante:
            string= random.choice(stringfacil)
            print(string)
            palavrasiniciante [string]
            tentativa=input().upper()
        
        if tentativa == string:
            print("Acertou! 3 pontos")
            string.remove(palavrasiniciante)
            pontostotais += 10

    #opçao 2
    elif opcao == "2":
        print("Palavra Media")
        
        for i in palavramedia:
            string= random.choice(stringmedio)
            print(string)
            palavramedia [string]
            tentativa=input().upper()
        
        if tentativa == string:
            print("Acertou! 3 pontos")
            string.remove(palavramedia)
            pontostotais += 50  

    #opçao 3
    elif opcao == "3":
        print("Palavra Dificil")
        
        for i in palavradificil:
            string= random.choice(stringdificil)
            print(string)
            palavradificil [string]
            tentativa=input().upper()
        
        if tentativa == string:
            print("Acertou! 3 pontos")
            string.remove(palavradificil)
            pontostotais += 100      

    #opçao 4
        if opcao== 4:
            pontos.append(pontostotais)
            