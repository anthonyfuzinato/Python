#============================= PARTE INFORMATIVA =============================#
# 1 imports
# 2 funçoes (defs)
# 3 Dicionarios
# 4 Listas
# 5 Tuplas
# 6 Sets
# 7 Inicio do progama (Login)
# 8 Progama principal
 
#============================= Import´s =============================#
import os
from datetime import datetime
import time
import pickle
from datetime import datetime, timedelta
import bcrypt
import time
from cryptography.fernet import Fernet
#============================= FUNÇOES =============================#
 
def login():
    print("=" * 25)
    print("Login".center(25))
    print("=" * 25)
    print("1- Criar conta")
    print("2- Entrar conta")
    print("3- Remover conta")
    print("0- Sair")
 
def loginpp():
    print ("1- Continuar")
    print ("0- Sair")
 
def entrar():
    print ("1- Continuar")
    print ("0- Sair")
 
def removerpp():
    print ("1- Continuar")
    print ("0- Sair")
 
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
 
def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()
 
def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password.encode()).decode()
 
# Carregar a chave
with open('key.key', 'rb') as key_file:
    key = key_file.read()
 
fernet = Fernet(key)
credenciais = {}
 
def menu_principal():
    print("=" * 30)
    print("Menu Principal".center(30))
    print("=" * 30)
    print("1- Adicionar")
    print("2- Remover")
    print("3- Editar")
    print("4- Mostrar todos tenis")
    print("5- Pesquisar")
    print("6- Noticias")
    print("7- Carrinho de compra")
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
    print ("3- Pesquisa por cor")
    print ("0- sair")
    print ("-"*30)
 
def novidades():
    os.system("cls")
    print ("=====================================")
    print ("======       Novidades         ======")
    print ("=====================================")
    print ("1- Look's")
    print ("2- Noticias")
    print ("0- sair")
    print ("-"*15)
 
def carrin():
    print ("========================================")
    print ("========== Carrinho de compra ==========")
    print ("========================================")
    print("1. Adicionar Tênis ao Carrinho")
    print("2. Remover Tênis do Carrinho")
    print("3. Mostrar Recibo")
    print("0. Sair")
 
def salvar_tenis():
    with open("tenis.pkl", "wb") as file:
        pickle.dump(tenis, file)
 
def salvar_compras():
    with open("compras.pkl", "wb") as file:
        pickle.dump(carrinho, file)
 
def mostrar_recibo():
    global recibo
    total = 0
    recibo = ""
    for item in carrinho:
        total += item["total"]
        recibo += f'Marca: {item["marca"]}, Modelo: {item["modelo"]}, Quantidade: {item["quantidade"]}, Valor Unitário: R${item["valor_unitario"]:.2f}, Total: R${item["total"]:.2f}\n'
    recibo += f"\nTotal da compra: R${total:.2f}\n"
 
    with open("recibo.txt", "w") as file:
        file.write(recibo)
 
    try:
        with open("recibo.txt", "w") as file:
            file.write(recibo)
        print("Recibo gerado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o recibo: {e}")
 
def ultimos_tenis_lancados():
    os.system("cls")
    print("========================================")
    print("====== Últimos Tênis Lançados ======")
    print("========================================")
 
def noticias():
     os.system("cls")
     print ("====================================")
     print ("======       Noticias         ======")
     print ("====================================")
     print ("Noticias".center(30))
     print ("0- sair")
     print ("="*30)
 
def tenis_novidades():
    print ("====================================")
    print ("======       Novidades         ======")
    print ("====================================")
    print("1- Novidades")
    print("2- Tenis mais Caros")
 
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
'''primeiro dicionario (coraçao do progama) aqui com este dicionario podemos conseguir tudo
que quisermos desde o valor,cor,stoque e lançamento, ele vai ser muito utilizado durante o funcionamento
do progama...'''
tenis = {
    "nike": {
        "air max": {"valor": 150.00, "data_lancamento": "01/01/2022", "estoque": 20, "cor": "Preto"},
        "air force 1": {"valor": 120.00, "data_lancamento": "15/03/2021", "estoque": 15, "cor": "Branco"},
        "jordan": {"valor": 200.00, "data_lancamento": "10/07/2022", "estoque": 10, "cor": "Vermelho"},
        "blazer": {"valor": 110.00, "data_lancamento": "05/09/2021", "estoque": 25, "cor": "Azul"},
        "cortez": {"valor": 85.00, "data_lancamento": "20/12/2020", "estoque": 30, "cor": "Cinza"},
        "react": {"valor": 130.00, "data_lancamento": "03/04/2022", "estoque": 12, "cor": "Verde"}
    },
    "adidas": {
        "ultraboost": {"valor": 180.00, "data_lancamento": "11/02/2022", "estoque": 18, "cor": "Preto"},
        "stan smith": {"valor": 95.00, "data_lancamento": "25/06/2021", "estoque": 22, "cor": "Branco"},
        "superstar": {"valor": 90.00, "data_lancamento": "08/08/2021", "estoque": 20, "cor": "Azul"},
        "nmd": {"valor": 170.00, "data_lancamento": "14/10/2022", "estoque": 8, "cor": "Vermelho"},
        "gazelle": {"valor": 80.00, "data_lancamento": "19/11/2020", "estoque": 16, "cor": "Verde"},
        "yeezy": {"valor": 250.00, "data_lancamento": "07/05/2022", "estoque": 5, "cor": "Cinza"}
    },
    "louis vuitton": {
        "archlight": {"valor": 1090.00, "data_lancamento": "02/03/2021", "estoque": 5, "cor": "Preto"},
        "run Away": {"valor": 870.00, "data_lancamento": "30/09/2021", "estoque": 7, "cor": "Branco"},
        "tattoo": {"valor": 820.00, "data_lancamento": "17/11/2020", "estoque": 6, "cor": "Azul"},
        "fastlane": {"valor": 995.00, "data_lancamento": "22/07/2021", "estoque": 8, "cor": "Vermelho"},
        "luxembourg": {"valor": 750.00, "data_lancamento": "12/12/2022", "estoque": 10, "cor": "Verde"}
    },
    "gucci": {
        "ace": {"valor": 650.00, "data_lancamento": "09/04/2021", "estoque": 12, "cor": "Preto"},
        "rhyton": {"valor": 890.00, "data_lancamento": "28/05/2022", "estoque": 9, "cor": "Branco"},
        "tennis 1977": {"valor": 630.00, "data_lancamento": "06/08/2022", "estoque": 11, "cor": "Azul"},
        "screener": {"valor": 870.00, "data_lancamento": "03/12/2020", "estoque": 8, "cor": "Vermelho"},
        "ultrapace": {"valor": 980.00, "data_lancamento": "18/02/2021", "estoque": 5, "cor": "Verde"}
    },
    "new balance": {
        "574": {"valor": 80.00, "data_lancamento": "23/10/2021", "estoque": 20, "cor": "Preto"},
        "990": {"valor": 185.00, "data_lancamento": "30/11/2020", "estoque": 15, "cor": "Branco"},
        "1080": {"valor": 160.00, "data_lancamento": "04/06/2021", "estoque": 10, "cor": "Azul"}
    }
}
#============================= Listas =============================#
'''Aqui temos as listas que vao ser utilizadas durante algumas opçoes do programa
como a lista dinheiro que vai ser usada para guardar o dinheiro que o utilizador inseriu na quantia
maxima que ele desejava, ou os tenis novos que e uma lista que verifica a data dos tenis e verifica
se foi lançado em menos de uma semana, ou os tenis caros que sao tenis acima de 1000 Euros..'''
dinheiro= []
tenis_novos = []
tenis_caros = []
carrinho = []



#============================= Tuplas =============================#
'''Aqui temos a tupla para uma area destinada ao publico/utilizadores que gostam de saber
oque os famosos estao usando nos pés'''
famosos = [
    ("Tom Hanks", "Nike Air Force 1"),
    ("Leonardo DiCaprio", "Adidas Yeezy Boost 350"),
    ("Meryl Streep", "Converse Chuck Taylor All Star"),
    ("Brad Pitt", "Puma Suede"),
    ("Jennifer Lawrence", "Reebok Classic Leather"),
    ("Beyoncé", "Adidas Superstar"),
    ("Elton John", "Gucci Ace"),
    ("Taylor Swift", "Reebok Club C"),
    ("Ed Sheeran", "Vans Old Skool"),
    ("Rihanna", "Puma Fenty"),
    ("Travis Scott", "Nike Air Jordan 1"),
    ("Post Malone", "Crocs Post Malone Duet Max Clog"),
    ("Drake", "Adidas Ultra Boost"),
    ("Lil Nas X", "Nike Air Max 97"),
    ("Cardi B", "Reebok Cardi B Club C"),
    ("Serena Williams", "NikeCourt Flare"),
    ("Lionel Messi", "Adidas Nemeziz"),
    ("Cristiano Ronaldo", "Nike Mercurial"),
    ("Usain Bolt", "Puma Bolt"),
    ("LeBron James", "Nike LeBron")
]


#============================= Sets =============================#
'''Aqui os sets que sao estruturas de dados nao mutaveis (nao podem se repetir) eu usei
para as noticias tambem em funçao para os utilizadores para pessoas que gostam de estar por dentro
do mundo influencer digital'''
noticias_celebridades = {
    "Brad Pitt foi visto passeando com seus filhos em Los Angeles.",
    "Beyoncé lançou uma nova música que está no topo das paradas.",
    "Tom Hanks será o protagonista do próximo filme de Steven Spielberg.",
    "Jennifer Lopez e Ben Affleck foram vistos juntos em um restaurante.",
    "Lady Gaga ganhou um prêmio por sua atuação em 'A Star is Born'.",
    "Kim Kardashian lançou uma nova linha de produtos de beleza.",
}
#============================= PROGRAMA LOGIN =============================#
'''Aqui e o Login para os utilizadores da loja, voce pode adicionar,entrar e remover utilizadores'''
os.system("cls")
while True:
    tentar_abrir_ficheiro()
    time.sleep(1)
    login()
    opçao1 = int(input("Escolha uma opção: "))
    login_valido = False
    if opçao1 == 1:
        nome, senha = input("Digite o Username e separado por um espaço a Senha: ").split()
        if nome not in credenciais:  # criar um novo login
            encrypted_senha = encrypt_password(senha)
            credenciais.update({nome: encrypted_senha})
            print("==================\nConta criada com sucesso!\n==================")
            login_valido = True
            salvar_credenciais()
            input("Pressione enter para prosseguir...")
        elif nome in credenciais:  # ja existe uma conta com este usuario
            print("==================\nJa existe este username..\n==================")
            input("Pressione enter para prosseguir...")      
        else:
            print("Esta opçao ainda nao existe\n Tente novamente em 3 segundos")
            time.sleep(3)

    elif opçao1 == 2:
        nome, senha = input("Digite o Username e separado por um espaço a Senha: ").split()
        if nome in credenciais and decrypt_password(credenciais[nome]) == senha:
            print("==================\nEntrou na conta com sucesso!\n==================")
            input("Pressione enter para prosseguir...")
            login_valido= True
        else:
            print("Nome de usuário ou senha incorretos.")
            input("Pressione enter para continuar...")
            login_valido= False  
            
    elif opçao1 == 3:
        removerpp()
        opcaologin= int(input("Qual a opçao que desejas: "))
        if opcaologin == 1:
            entrada = input("Digite o Username e separado por um espaço a Senha: ").split()
            if len(entrada) != 2:
                print("Entrada inválida. Por favor, forneça o Username e a Senha separados por um espaço.")
            else:
                nome, senha = entrada
                login_valido = False
                for x in list(credenciais.keys()):  # Iterar sobre uma cópia das chaves
                    if nome in credenciais and decrypt_password(credenciais[nome]) == senha:
                        del credenciais[nome]
                        salvar_credenciais()
                        print("Conta removida com sucesso...")
                        input("Pressione enter para continuar...")
                        login_valido = False
                        break  # Conta encontrada e removida, sair do loop
                    else:
                        print("Usuário e senha não encontrados ou já foram deletados.\nAgora precisas esperar 5 segundos para prosseguir..")
                        time.sleep(5)
                        login_valido= False
        elif opcaologin == 0:
            break
        else:
            print("Esta opçao ainda nao existe\n Tente novamente em 3 segundos")
            time.sleep(3)


    elif opçao1 == 0:
        print("Obrigado por utilizar nosso progama!")
        break

    else:
        print("Nao temos esta opção!\nEspere 3 segundos para tentar novamente..")
        time.sleep(3)

    #============================= PROGRAMA PRINCIPAL =============================#
    ''' Aqui é o progama principal onde tudo vai acontecer, a maioria das opçoes eu tive de fazer for's
    para percorrer as listas, dicionarios,tuplas ou os sets, nao e um programa dificil de entender'''
    os.system("cls")
    while login_valido == True:
        menu_principal()
        opçao = int(input("Qual a opção que voce deseja: "))

        if opçao == 1:
            ficheiros_tenis()
            marca = input("Digite a marca do tênis: ").lower()
            modelo = input("Digite o modelo do tênis: ").lower()
            valor = float(input("Digite o valor do tênis: " ))
            data_lancamento = input("Digite a data de lançamento do tênis (dd/mm/aaaa): ")
            estoque = int(input("Digite a quantidade em estoque do tênis: "))
            cor = input("Digite a cor do tênis: ").capitalize()

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
            marca = input("Digite a marca do tênis que deseja remover: ").lower()
            modelo = input("Digite o modelo do tênis que deseja remover: ").lower()

            if marca in tenis and modelo in tenis[marca]:
                del tenis[marca][modelo]
                salvar_tenis()
                print(f"Tênis {modelo} da marca {marca} removido com sucesso!")
            else:
                print(f"Marca {marca} não encontrado no modelo ou voce ja tem {marca} no carrinho.")

        elif opçao == 3:
            marca = input("Digite a marca do tênis que deseja alterar: ")
            if marca in tenis:
                modelo = input("Digite o modelo do tênis que deseja alterar: ")
                if modelo in tenis[marca]:
                    print(f"Dados atuais do {modelo} da marca {marca}:")
                    print(f"Valor: {tenis[marca][modelo]['valor']}")
                    print(f"Data de Lançamento: {tenis[marca][modelo]['data_lancamento']}")
                    print(f"Estoque: {tenis[marca][modelo]['estoque']}")

                    alterar_opcao = input("O que você deseja alterar? (1-Valor, 2-Data de Lançamento, 3-Stoque): ")

                    if alterar_opcao == "1":
                        novo_valor = float(input("Digite o novo valor: "))
                        tenis[marca][modelo]['valor'] = novo_valor # Atualiza o valor do tênis no dicionário 'tenis' para a marca e modelo especificados
                        print(f"Valor do {modelo} da marca {marca} alterado com sucesso!")

                    elif alterar_opcao == "2":
                        nova_data = input("Digite a nova data de lançamento (dd/mm/aaaa): ")
                        tenis[marca][modelo]['data_lancamento'] = nova_data # Atualiza a data de lançamento do tênis no dicionário 'tenis' para a marca e modelo especificados
                        print(f"Data de lançamento do {modelo} da marca {marca} alterada com sucesso!")

                    elif alterar_opcao == "3":
                        novo_estoque = int(input("Digite o novo estoque: "))
                        tenis[marca][modelo]['estoque'] = novo_estoque  # Atualiza a quantidade em stoque do tênis no dicionário 'tenis' para a marca e modelo especificados
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
            for marca, modelos in tenis.items(): # percorre o dicionario tenis
                print ("="* 15)
                print(f"Marca: {marca}")
                print ("="* 15)
                for modelo, detalhes in modelos.items(): # percorre o dicionario tenis
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
                for marca, modelos in tenis.items(): # percorre o dicionario tenis
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
                valor_maximo = float(input("Digite o valor máximo: "))
                encontrado = False
                for marca, modelos in tenis.items():
                    for modelo, detalhes in modelos.items():
                        if detalhes['valor'] <= valor_maximo:
                            print(f"Marca: {marca}, Modelo: {modelo}, Valor: R${detalhes['valor']}, Data de Lançamento: {detalhes['data_lancamento']}, Estoque: {detalhes['estoque']}, Cor: {detalhes['cor']}")
                            encontrado = True
                if not encontrado:
                    print("Nenhum tenis encontrado com o valor especificado!")


            elif opçaoo == 3:
                cor = input("Digite a cor do tênis que deseja buscar: ").strip().title()
                encontrado = False

                # Percorre o dicionário de tênis
                for marca, modelos in tenis.items():
                    # Percorre cada modelo dentro da marca
                    for nome_modelo, detalhes in modelos.items():
                        # Verifica se a cor digitada pelo usuário está nos detalhes do tênis
                        if cor in detalhes['cor']:
                            encontrado = True
                            print(f"Marca: {marca}, Modelo: {nome_modelo}, Valor: {detalhes['valor']}, Data de Lançamento: {detalhes['data_lancamento']}, Estoque: {detalhes['estoque']}, Cor: {detalhes['cor']}")
                if not encontrado:
                    print("Nenhum tênis encontrado com essa cor.")
            elif opçaoo == 0:
                continue


        elif opçao == 6:
            novidades() # Vai chamar a funçao
            print(f'\033[1;40;4mÓtima Escolha, !!!\033[m')
            opcao = int(input("Qual a opçao que desejas? "))

            if opcao == 1:
                    for i in range(0, len(famosos), 5):
                        for nome, outfit in famosos[i:i+5]:
                            print(f"Nome: {nome}, Outfit: {outfit}")

                        # Pedir ao usuário para pressionar "Enter" para continuar
                        print("==============================================\n")
                        input("Pressione Enter para ver mais 5 famosos...")
                        print("==============================================\n")

            elif opcao== 2:
                noticias()
                for i in noticias_celebridades:
                    print (f"{i}\n".center(30))
                    print ("================================================\n")
                input ("Pressione a tecla enter para continuar...")

                print("=" * 30)


        elif opçao == 7:
            os.system("cls")
            carrin()
            op = int(input("Escolha uma opção: "))

            if op == 1:
                os.system("cls")
                print("Adicionar Tênis ao Carrinho")
                marca = input("Marca do tênis: ").lower()
                modelo = input("Modelo do tênis: ").lower()
                quantidade_venda = int(input("Quantidade: "))
                if marca in tenis and modelo in tenis[marca]:
                    if tenis[marca][modelo]["estoque"] >= quantidade_venda:
                        tenis[marca][modelo]["estoque"] -= quantidade_venda
                        total = tenis[marca][modelo]["valor"] * quantidade_venda
                        item = {
                            "marca": marca,
                            "modelo": modelo,
                            "quantidade": quantidade_venda,
                            "valor_unitario": tenis[marca][modelo]["valor"],
                            "total": total
                        }
                        carrinho.append(item)
                        salvar_tenis()
                        salvar_compras()
                        print(f"{quantidade_venda}x {marca} {modelo} adicionado(s) ao carrinho.")
                    else:
                        print("Quantidade indisponível no estoque.")
                else:
                    print("Marca ou modelo não encontrado.")
                time.sleep(2)

            elif op == 2:
                os.system("cls" if os.name == "nt" else "clear")
                print("Remover Tênis do Carrinho")
                marca = input("Marca do tênis: ").lower()
                modelo = input("Modelo do tênis: ").lower()

                item_removido = False
                for item in carrinho:
                    if item["marca"] == marca and item["modelo"] == modelo:
                        tenis[marca][modelo]["estoque"] += item["quantidade"]
                        carrinho.remove(item)
                        salvar_tenis()
                        salvar_compras()
                        print(f"{item['quantidade']}x {marca} {modelo} removido(s) do carrinho.")
                        item_removido = True
                        break

                if not item_removido:
                    print("Item não encontrado no carrinho.")
                time.sleep(2)

            elif op == 3:
                mostrar_recibo()
                try:
                    with open("recibo.txt", "w") as file:
                        file.write(recibo)

                    # Agora, vamos ler o conteúdo do arquivo recibo.txt
                        os.system("cls")
                    with open("recibo.txt", "r") as file:
                        conteudo_recibo = file.read()
                        print("Conteúdo do recibo:")
                        print(conteudo_recibo)

                except Exception as e:
                    print(f"Ocorreu um erro ao gerar o recibo: {e}")

            elif op == 0:
                break

            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(2)


        elif opçao == 8:
            os.system("cls")
            tenis_novidades()
            opcaooo= int(input("Escolha uma opçao: "))
            for marca, modelos in tenis.items():
                for modelo, detalhes in modelos.items():
                    data_lancamento = datetime.strptime(detalhes["data_lancamento"], "%d/%m/%Y")
                    if (datetime.now() - data_lancamento).days <= 30:
                        tenis_novos.append((marca, modelo, detalhes))
                    if detalhes["valor"] >= 1000:
                        tenis_caros.append((marca, modelo, detalhes))
            if opcaooo == 1:
                print("Novidades:")
                if tenis_novos:
                    for marca, modelo, detalhes in tenis_novos:
                        print(f"Marca: {marca}, Modelo: {modelo}, Valor: R${detalhes['valor']}, Data de Lançamento: {detalhes['data_lancamento']}, Estoque: {detalhes['estoque']}, Cor: {detalhes['cor']}")
                else:
                    print("Nenhum tenis novo encontrado.")

            elif opcaooo == 2:
                print("\nTenis Caros:")
                if tenis_caros:
                    for marca, modelo, detalhes in tenis_caros:
                        print(f"Marca: {marca}, Modelo: {modelo}, Valor: R${detalhes['valor']}, Data de Lançamento: {detalhes['data_lancamento']}, Estoque: {detalhes['estoque']}, Cor: {detalhes['cor']}")
                else:
                    print("Nenhum tenis caro encontrado.")

        elif opçao == 0:
            print("Obrigado por utilizar nosso programa!")
            creditos()
            break

        else:
            print("Opção inválida! Por favor, tente novamente.\nEspere 3 segundos para tentar novamente...")
            time.sleep(3)

        input("Pressione Enter para continuar...")
        os.system("cls")