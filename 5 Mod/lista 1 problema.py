import time
def menu():
    print("----------------M E N U------------------")
    print("1-Admissao de doente")
    print("2-Atendimento de doente")
    print("3-Urgencia")
    print("4-Listagem de doentes")
    print ("5-Anular consulta")
    print ("6-Pesquisar doente")
    print("0- Sair")
lista_doentes=[]

opcao = "-1"
while opcao != 0:
    menu()
    opcao = input("Opçao que desejas: ")

if opcao == "1":
    lista_doentes.append(input("Nome do paciente: "))

elif opcao == "2":
    if len(lista_doentes) == 0:
        print ("nao existem doentes na lista de espera")
    else:
        print(lista_doentes[0])
        lista_doentes.pop(0)
    time.sleep(2)

elif opcao =="3":
    nome=input("\n Nome do doente: ")
    lista_doentes.insert(0,nome)

elif opcao == "4":
    print ("\n------------------------\nLista de Doentes em espera:\n------------------------")
    for nome in lista_doentes:
        print(nome)
    input("Pressione enter para continuar...")

elif opcao == "5":
    nome= input("Nome do doente: ")
    lista_doentes.remove(nome)

elif opcao == "6":
    nome=input("Nome do doente: ")
    if lista_doentes.count(nome)== 0:
        print("Nao existe ninguem com esse nome na lista de espera.")
    else:
        lista_doentes.index(nome)+1