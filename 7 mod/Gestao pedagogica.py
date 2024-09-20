'''
PSI - Módulo 7
Ficheiros
Gestão Pedagógica
'''
 
import pickle
import os
 
 
def criar_ficha():
  global alunos
  alunos = {'a24571': {'nome':'Dinis Sobral','notas':{'Portugues':[],'PSI':[]},'Data Nascimento':(18,4,2008)}}
 
def gravar_ficheiro_binario():
    global alunos
    # Abrir ficheiro binário no modo de escrita
    f=open(".\\alunos.bin","wb")
    # Gravar os dados dos alunos no ficheiro
    pickle.dump(alunos,f)
    # Fechar o ficheiro
    f.close()
 
def ler_ficheiro_binario():
    global alunos
    # Abrir ficheiro binário no modo de leitura
    f=open(".\\alunos.bin","rb")
    # Carregar os dados do ficheiro para a variável.
    try:
        alunos=pickle.load(f)
    except FileNotFoundError:
        print("Ficheiro não encontrado")
    # Fechar o ficheiro
    f.close()
 
def menu():
    print("-"*25)
    print("Menu".center(25))
    print("-"*25)
    print("1 - Criar Ficha Aluno")
    print("2 - Adicionar Notas ")
    print("3 - Eliminar Aluno")
    print("4 - Mostrar Notas")
    print("5 - Imprimir dados do aluno")
    print("6 - Mostrar lista de alunos")
    print("0 - Sair")
 
# ------------------- Programa ---------------------
 
# Carregar os dados do ficheiro no inicio do programa
criar_ficha()
ler_ficheiro_binario()
 
while True:
   
    global alunos
    menu()
   
    opcao=input("\n Opção:")
    os.system('cls')
 
    if (opcao=='0'):
        break
 
    elif(opcao=='1'):
        print("---- Criar novo aluno ----\n")
        numero_processo=input("Nº_processo:")
        if numero_processo not in alunos:
            print("Nao existe esse aluno")
            break

        nome=input("Nome:")
        dia,mes,ano=map(int,input("Data de Nascimento(dd/mm/yyyy):").split('/'))
        # Adicionar a ficha do aluno à variável
        alunos[numero_processo]={'nome':nome,'notas':{'Português':[],'PSI':[]},'Data Nascimento':(dia,mes,ano)}
        print("\n Aluno gravado com sucesso.")
   
    elif opcao== "2":
        processo=input("Numero de processo")
        if processo not in alunos:
            print("Aluno nao encontrado")
            break


        else:
            materia,nota=input("Escreva o nome da disciplina e a nota: ").split()
            try:
                alunos[processo]["notas"][materia].append(nota)
            except KeyError:
                print("A disciplina nao existe")
                SN = input("Deseja adicionar a disciplina (S/N): ").capitalize()
                if SN =="S":
                    alunos[processo]["notas"][materia]=int(nota)
                    print("Disciplina adicionada com sucesso..")
                
    elif opcao=="3":
        print("-- Eliminar o Aluno --")
        n_processo= input("Nº do processo: ")
        if n_processo in alunos:
            alunos.pop(n_processo)
            print("Aluno eliminado")
        else:
            print("Aluno nao encontrado.")

    elif opcao=="4":
        print ("-- Notas --")
        numero_processo= input("Nº do processo: ")
        disciplina =input("Disciplina desejada: ").capitalize()
        for nota in alunos[numero_processo]["notas"][disciplina]:
            print(nota)

    elif opcao == "5":
        print("-- Imprimir dados --")
        n_processo= input("Nº do processo: ")
        if n_processo in alunos:
            from datetime import datetime 
            dia= datetime.now().day()
            mes= datetime.now().month()
            ano= datetime.now().year()

            ft= open(".\\notas do aluno" + n_processo + "_" + dia + "-" + mes + "-" + ano + ".txt", "w")
            ft.write("Nome:", alunos[n_processo]["nome"])
            ft.write("Data de nascimento:", alunos[n_processo]["Data Nascimento"])
            print("\nNotas:",alunos[n_processo]["notas"])
            n_nota = 1
            for disciplina in alunos[n_processo]["notas"]:
                print(disciplina,": ")
                for nota in alunos[n_processo]["notas"][disciplina]:
                    print(f"Mod {n_nota}:",nota)
                    n_nota += 1
        else:
            print("Aluno ")

    elif(opcao=='6'):
        for nprocesso in alunos:
            print(nprocesso, "-", alunos[nprocesso]['nome'], alunos[nprocesso]['Data Nascimento'] )
 
    input("Pressione a tecla enter para continuar.")
    os.system("cls")



gravar_ficheiro_binario()