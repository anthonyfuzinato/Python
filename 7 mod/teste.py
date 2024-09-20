#============================= PARTE INFORMATIVA =============================#
# 1 menu - Login no nosso progama/site

#============================= Import´s =============================#
import os
from datetime import datetime
import time
import pickle

#============================= FUNÇOES =============================#

def login():
    print("=" * 25)
    print("Login".center(25))
    print("=" * 25)
    print("1- Criar conta")
    print("2- Entrar conta")
    print("3- Remover conta")
    print("0- Sair")

def tentar_abrir_ficheiro():
    global credenciais
    try:
        with open("credenciais.bin", "rb") as f:
            credenciais = pickle.load(f)
    except FileNotFoundError:
        credenciais = {}

def salvar_credenciais():
    with open("credenciais.bin", "wb") as f:
        pickle.dump(credenciais, f)

def menu_principal():
    print("=" * 30)
    print("Menu Principal".center(30))
    print("=" * 30)
    print("1- Adicionar")
    print("2- Remover")
    print("3- Editar")
    print("4- Mostrar todos tenis")
    print("5- Pesquisar")
    print("8- Novidades / Tenis Caros")
    print ("0- Sair")

def ficheiros_tenis():
    with open("tenis.txt", "w") as ftenis:
        for key, value in tenis.items():
            ftenis.write(f"{key}: {value}\n")

def salvar_tenis():
    with open("tenis.txt", "w") as ftenis:
        for marca, modelos in tenis.items():
            for modelo, detalhes in modelos.items():
                ftenis.write(f"{marca}: {modelo} - {detalhes['valor']} - {detalhes['data_lancamento']} - {detalhes['estoque']} - {detalhes['cor']}\n")

def pesquisa():
    os.system("cls")
    print ("====================================")
    print ("======       Pesquisa         ======")
    print ("====================================")
    print ("1- Pesquisa Modelo")
    print ("2- Pesquisa quantia")
    print ("0- sair")
    print ("-"*30)

def creditos():
    os.system("cls")
    try:
        with open("Credenciais.txt", "w+") as f:
            print("-" * 30)
            print("Progama elaborado por Anthony Fuzinato".center(30))
            print("(c) Direitos Reservados".center(30))
            print("ESEN - Curso profissional de GPSI".center(30))
            print(f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}".center(30))
            print("-" * 30)
            print(f.read())  
            time.sleep(3)
            print("Saindo do progama, Obrigado")

    except FileExistsError:
        print("Arquivo 'Credenciais.txt' não conseguiu ser criado com sucesso.")

#============================= DICIONARIOS =============================# 
# Tenis
tenis = {
    "Nike": {
        "Air Max": {"valor": 150.00, "data_lancamento": "01/01/2022", "estoque": 20, "cor": "Preto"},
        "Air Force 1": {"valor": 120.00, "data_lancamento": "15/03/2021", "estoque": 15, "cor": "Branco"},
        "Jordan": {"valor": 200.00, "data_lancamento": "10/07/2022", "estoque": 10, "cor": "Vermelho"},
        "Blazer": {"valor": 110.00, "data_lancamento": "05/09/2021", "estoque": 25, "cor": "Azul"},
        "Cortez": {"valor": 85.00, "data_lancamento": "20/12/2020", "estoque": 30, "cor": "Cinza"},
        "React": {"valor": 130.00, "data_lancamento": "03/04/2022", "estoque": 12, "cor": "Verde"}
    },
    "Adidas": {
        "Ultraboost": {"valor": 180.00, "data_lancamento": "11/02/2022", "estoque": 18, "cor": "Preto"},
        "Stan Smith": {"valor": 95.00, "data_lancamento": "25/06/2021", "estoque": 22, "cor": "Branco"},
        "Superstar": {"valor": 90.00, "data_lancamento": "08/08/2021", "estoque": 20, "cor": "Azul"},
        "NMD": {"valor": 170.00, "data_lancamento": "14/10/2022", "estoque": 8, "cor": "Vermelho"},
        "Gazelle": {"valor": 80.00, "data_lancamento": "19/11/2020", "estoque": 16, "cor": "Verde"},
        "Yeezy": {"valor": 250.00, "data_lancamento": "07/05/2022", "estoque": 5, "cor": "Cinza"}
    },
    "Louis Vuitton": {
        "Archlight": {"valor": 1090.00, "data_lancamento": "02/03/2021", "estoque": 5, "cor": "Preto"},
        "Run Away": {"valor": 870.00, "data_lancamento": "30/09/2021", "estoque": 7, "cor": "Branco"},
        "Tattoo": {"valor": 820.00, "data_lancamento": "17/11/2020", "estoque": 6, "cor": "Azul"},
        "Fastlane": {"valor": 995.00, "data_lancamento": "22/07/2021", "estoque": 8, "cor": "Vermelho"},
        "Luxembourg": {"valor": 750.00, "data_lancamento": "12/12/2022", "estoque": 10, "cor": "Verde"}
    },
    "Gucci": {
        "Ace": {"valor": 650.00, "data_lancamento": "09/04/2021", "estoque": 12, "cor": "Preto"},
        "Rhyton": {"valor": 890.00, "data_lancamento": "28/05/2022", "estoque": 9, "cor": "Branco"},
        "Tennis 1977": {"valor": 630.00, "data_lancamento": "06/08/2022", "estoque": 11, "cor": "Azul"},
        "Screener": {"valor": 870.00, "data_lancamento": "03/12/2020", "estoque": 8, "cor": "Vermelho"},
        "Ultrapace": {"valor": 980.00, "data_lancamento": "18/02/2021", "estoque": 5, "cor": "Verde"}
    },
    "New Balance": {
        "574": {"valor": 80.00, "data_lancamento": "23/10/2021", "estoque": 20, "cor": "Preto"},
        "990": {"valor": 185.00, "data_lancamento": "30/11/2020", "estoque": 15, "cor": "Branco"},
        "1080": {"valor": 160.00, "data_lancamento": "04/06/2021", "estoque": 10, "cor": "Azul"}
    }
}
#============================= Listas =============================# 
dinheiro= []
#============================= PROGRAMA LOGIN =============================#
os.system("cls")
while True:
    tentar_abrir_ficheiro()
    time.sleep(1)
    login()
    opçao1 = int(input("Escolha uma opção: "))
    login_valido = False
    if opçao1 == 1:
        nome, senha = input("Digite o Username e em seguida a Senha: ").split()
        if nome not in credenciais:  # criar um novo login
            credenciais.update({nome: senha})
            print("==================\nConta criada com sucesso!\n==================")
            login_valido = True
            salvar_credenciais()
            input("Pressione enter para prosseguir...")
        elif nome in credenciais:  # ja existe uma conta com este usuario
            print("==================\nJa existe este username..\n==================")
            input("Pressione enter para prosseguir...")
        else:
            print("Aconteceu algum erro inesperado, Tente novamente!")
    elif opçao1 == 2:
        nome, senha = input("Digite o Username e em seguida a Senha: ").split()
        for x in credenciais:  # for para percorrer o dicinario/ficheiro para entrar na conta e verificar se esta errada
            if credenciais[x] == senha and x == nome:  # entrar na conta
                print("==================\nEntrou na conta com sucesso!\n==================")
                login_valido = True
                salvar_credenciais()
                break
            elif credenciais[x] != senha and x == nome:  # erro caso senha esteja errada
                print("Voce digitou a senha errada...")
                input("Pressione enter para continuar...")
            elif nome and senha not in credenciais[x]:  # else para caso nao leia o usuario no dicionario
                print("Essa conta nao existe!")
                break
    elif opçao1 == 3:
        entrada = input("Digite o Username e em seguida a Senha: ").split()
        if len(entrada) != 2:
            print("Entrada inválida. Por favor, forneça o Username e a Senha separados por um espaço.")
        else:
            nome, senha = entrada
            login_valido = False
            for x in list(credenciais.keys()):  # Iterar sobre uma cópia das chaves
                if credenciais[x] == senha and x == nome:
                    credenciais.pop(x)
                    salvar_credenciais()
                    print("Conta removida com sucesso...")
                    input("Pressione enter para continuar...")
                    login_valido = True
                    break  # Conta encontrada e removida, sair do loop

            if not login_valido:
                print("Usuário e senha não encontrados ou já foram deletados.\nAgora precisas esperar 5 segundos para prosseguir..")
                time.sleep(5)

    elif opçao1 == 4:
        print(credenciais)

    elif opçao1 == 0:
        print("Obrigado por utilizar nosso progama!")
        break

    else:
        print("Nao temos esta opção!\nEspere 3 segundos para tentar novamente..")
        time.sleep(3)

    #============================= PROGRAMA PRINCIPAL =============================#
    os.system("cls")
    while login_valido == True:
        menu_principal()
        opçao = int(input("Qual a opção que voce deseja: "))

        if opçao == 1:
            ficheiros_tenis()
            marca = input("Digite a marca do tênis: ")
            modelo = input("Digite o modelo do tênis: ")
            valor = float(input("Digite o valor do tênis: "))
            data_lancamento = input("Digite a data de lançamento do tênis (dd/mm/aaaa): ")
            estoque = int(input("Digite a quantidade em estoque do tênis: "))
            cor = input("Digite a cor do tênis: ")

            if marca in tenis:
                tenis[marca][modelo] = {
                    "valor": valor,
                    "data_lancamento": data_lancamento,
                    "estoque": estoque,
                    "cor": cor
                }
            else:
                tenis[marca] = {
                    modelo: {
                        "valor": valor,
                        "data_lancamento": data_lancamento,
                        "estoque": estoque,
                        "cor": cor
                    }
                }
            salvar_tenis()
            print(f"Tênis {modelo} da marca {marca} adicionado com sucesso!")




        elif opçao == 2:
            # Função para remover um modelo de tênis do dicionário e do arquivo
            marca = input("Digite a marca do tênis que deseja remover: ")
            modelo = input("Digite o modelo do tênis que deseja remover: ")

            if marca in tenis and modelo in tenis[marca]:
                del tenis[marca][modelo]
                salvar_tenis()
                print(f"Tênis {modelo} da marca {marca} removido com sucesso!")
            else:
                print(f"Modelo {modelo} não encontrado na marca {marca}.")





        elif opçao == 3:
            marca = input("Digite a marca do tênis que deseja alterar: ")
            if marca in tenis:
                modelo = input("Digite o modelo do tênis que deseja alterar: ")
                if modelo in tenis[marca]:
                    print(f"Dados atuais do {modelo} da marca {marca}:")
                    print(f"Valor: {tenis[marca][modelo]['valor']}")
                    print(f"Data de Lançamento: {tenis[marca][modelo]['data_lancamento']}")
                    print(f"Estoque: {tenis[marca][modelo]['estoque']}")
                    
                    alterar_opcao = input("O que você deseja alterar? (1-Valor, 2-Data de Lançamento, 3-Estoque): ")
                    
                    if alterar_opcao == "1":
                        novo_valor = float(input("Digite o novo valor: "))
                        tenis[marca][modelo]['valor'] = novo_valor
                        print(f"Valor do {modelo} da marca {marca} alterado com sucesso!")
                    
                    elif alterar_opcao == "2":
                        nova_data = input("Digite a nova data de lançamento (dd/mm/aaaa): ")
                        tenis[marca][modelo]['data_lancamento'] = nova_data
                        print(f"Data de lançamento do {modelo} da marca {marca} alterada com sucesso!")
                    
                    elif alterar_opcao == "3":
                        novo_estoque = int(input("Digite o novo estoque: "))
                        tenis[marca][modelo]['estoque'] = novo_estoque
                        print(f"Estoque do {modelo} da marca {marca} alterado com sucesso!")
                    
                    else:
                        print("Opção inválida!")
                    
                    salvar_tenis()
                else:
                    print(f"Modelo {modelo} não encontrado na marca {marca}.")
            else:
                print(f"Marca {marca} não encontrada.")



        elif opçao == 4:
            print ("\nBela Escolha!\n")
            for marca, modelos in tenis.items():
                print ("="* 15)
                print(f"Marca: {marca}")
                print ("="* 15)
                for modelo, detalhes in modelos.items():
                    print(f" \nModelo: {modelo}")
                    print(f"        Valor: {detalhes['valor']}")
                    print(f"            Data de Lançamento: {detalhes['data_lancamento']}")
                    print(f"                Estoque: {detalhes['estoque']}")
                    print(f"                    Cor: {detalhes['cor']}\n")
                    print ("="* 15)
                    input("Pressione enter para o proximo tenis..")
                    print ("="* 15)
                    print("\n")

        

        elif opçao == 5:
            pesquisa()
            opçaoo= int(input("Digite oque desejas? "))
            if opçaoo == 1:
                pesquisa = input("Digite o modelo do tênis que deseja pesquisar: ")
                encontrado = False
                for marca, modelos in tenis.items():
                    for modelo, detalhes in modelos.items():
                        if pesquisa.lower() in modelo:
                            print(f"Marca: {marca}")
                            print(f"  Modelo: {modelo}")
                            print(f"    Valor: {detalhes['valor']}")
                            print(f"    Data de Lançamento: {detalhes['data_lancamento']}")
                            print(f"    Estoque: {detalhes['estoque']}")
                            print(f"    Cor: {detalhes['cor']}\n")
                            encontrado = True
                if not encontrado:
                    print("Nenhum tênis encontrado com esse termo de pesquisa.")
            elif opçaoo == 2:
                pesquisa = int(input("Digite o modelo do tênis que deseja pesquisar: "))
                for x in tenis.values():
                    if pesquisa >= tenis[x]:
                        dinheiro.append(x)
                        print(dinheiro)


        elif opçao == 8:
            print(f'\033[1;40;4mÓtima Escolha, !!!\033[m')




        elif opçao == 0:
            print("Obrigado por utilizar nosso programa!")
            login_valido = False
            creditos()
            break

        else:
            print("Opção inválida! Por favor, tente novamente.")
        input("Pressione Enter para continuar...")
        os.system("cls")
