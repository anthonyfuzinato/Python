carros= []
def menu():
    print ("-----E S T A C I O N A M E N T O----")
    print ("1- Entrada")
    print ("2. Saida")
    print ("3- Verificar se a vagas livres")
    print ("0- Terminar")

carroslivre = 0
opcao= -1
vagaslivres= 0

while vagaslivres != 0 or vagaslivres < 10:
    if opcao == "1":
        matricula= input("Matricula: ")
        carros.append(matricula)
        carroslivre+= 1
        print ("Bem-vindo")

    elif opcao == "2" or opcao == matricula:
        carros.remove(matricula)
        carroslivre -= 1
        print ("Obrigado")

    elif opcao == "3":
        vagaslivres= carroslivre < 5
        print (vagaslivres)
    elif opcao == "0":
        break