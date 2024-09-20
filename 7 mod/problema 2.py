import datetime
import time
import os
 
def menu():
    os.system("cls")
    print("-"*30)
    print("Diário Digital".center(30))
    print("-"*30)
    print("1 - Ler Diário")
    print("2 - Escrever no Diário")
    print("3 - Apagar o diário")
    print("0 - Sair")
 
def ler_diario():
    try:
        # Tentar abrir o ficheiro de texto
        f=open(".\\diario.txt","r")
        # Ler o todo o conteudo do ficheiro de texto
        print(f.read())
    except FileNotFoundError:
        print("O diário não existe!")
    except FileExistsError:
        print("Erro no ficheiro!")
 
def apagar_diario():
    try:
        os.remove(".\\diario.txt")
        print("O ficheiro do diário foi apagado.")
    except FileNotFoundError:
        print("O ficheiro já foi apagado")
       
def escrever_post():
    try:
       
        # Tentar abrir o ficheiro de texto no modo leitura
        f=open(".\\diario.txt","r")
       
        # Testar se já existe um Post na data atual
        if str(datetime.date.today()) not in f.read():
            nova_data=True
        else:
            nova_data=False
       
        # Abrir o ficheiro no modo append
        f.close()
        f=open(".\\diario.txt","a")
       
        # Escrever a data atual no Post
        if nova_data == True:
            f.write("\n\n" + str(datetime.date.today()) + "\n----------")
       
        # Escrever o Texto do Post
        f.write("\n" + input("Introduza o texto que deseja adicionar ao diário:\n"))
       
    except FileExistsError:
         print("Erro no ficheiro!")
 
while True:
   
    menu()
    opcao = input("\nOpção:")
 
    if opcao=="0":
        break
 
    elif opcao=="1":
        os.system('cls')
        ler_diario()
   
    elif opcao=="2":
        os.system('cls')
        escrever_post()
   
    elif opcao=="3":
        apagar_diario()
   
    input("\n Pressione enter para continuar...")