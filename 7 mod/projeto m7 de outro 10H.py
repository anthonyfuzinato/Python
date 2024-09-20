'''
    Projeto Modelo PSI - Módulo 07
    Ficheiros Binários
    Gestão de Atletas
'''
 
def menu_principal():
    print('\n[1] Jogadores')
    print('[2] Clubes')
    print('[3] Login')
    print('[0] Sair\n')
 
def menu_jogadores():
    if login==True: # Opções da área reservada (tem de fazer login)
        print('\n[1.1] Inserir Jogadores')
        print('[1.2] Apagar Jogadores')
    print('[1.3] Consultar Jogadores')
    print("[-] Voltar ao menu anterior\n")
 
def menu_consultar_jogadores():
    print('\n[1.3.1] Consulta por nome')
    print('[1.3.2] Consulta por posicao')
    print("[-] Voltar ao menu anterior\n")
 
def menu_clubes():
    if login==True: # Opções da área reservada (tem de fazer login)\
        print('\n[2.1] Inserir Clubes')
        print('[2.2] Apagar Clubes')
    print('[2.3] Consultar Clubes')
    print("[-] Voltar ao menu anterior\n")
   
def menu_consultar_clubes():
    print('\n[2.3.1] Consulta plantel')
    print('[2.3.2] Consulta orçamento')
    print("[-] Voltar ao menu anterior\n")
 
import os
import pickle
 
#Inserir credenciais de teste no ficheiro
credenciais={'ESEN':'GPSI',
             'Admin':'admin',
             'Boss':'1234'}
 
# codigo para encriptação da password
caracteres='ABCDEFGHIJKLMNOPQRSTUVXYWZ1234567890'
caracteres_codificados='0987654321ZWYXVUTSRQPONMLKJIHGFEDCBA'
encriptacao={}
for i in range(0,len(caracteres)):
    encriptacao.update({caracteres[i]:caracteres_codificados[i]})
 
# encriptação da password
for username in credenciais:
    codigo=''
    for caracter_pass in credenciais[username]:
        codigo+=encriptacao[caracter_pass.upper()]
    credenciais.update({username:codigo})
 
# Gravar contas para login no ficheiro
arquivo=open('credenciais.dat','wb')
pickle.dump(credenciais,arquivo)
 
 
'''
Programa Principal
'''
 
atletas=[]
login=False
 
opc='1'
voltar_atras="menu_principal"
 
while opc!='0':
 
    if voltar_atras=="menu_principal":
        menu_principal()
        opc=input(': ')
   
    #Jogadores
    if opc=='1' or voltar_atras=="menu_jogadores":
        menu_jogadores()
        opc=input(': ')
 
        # Listar o nome dos clubes existentes
        print("\n-- Clubes existentes --")
        if opc=='1.1' and login==True: # testa se está logado
            lista_clubes=os.listdir('Equipas\\')
            for equipa in lista_clubes:
                print(equipa[:-4])
           
            # Ler o nome do clube escolhido
            clube=input('\nNome do clube do jogador: ')
           
            try:
                # Tenta abrir o ficheiro. Se não existir gera uima exceção
                arquivo=open('Equipas\\'+clube+'.dat','r+b')
               
                #Carregar os jogadores do ficheiro para o dicionário    
                ficheiro_vazio=False
                try:
                    # Verifica se tem jogadores
                    jogadores=pickle.load(arquivo)
                except EOFError:
                    #Testa se é o ficheiro está vazio.
                    #Nesse caso será o 1º jogador a ser inserido no ficheiro
                    ficheiro_vazio=True
 
                #Ler os dados do novo jogador
                nome=input('\nNome do jogador: ')
                posicao=input('Posicao do jogador: ')
                valor=input('Valor do jogador: ')
               
                if ficheiro_vazio==False:
                # Se já tiver jogadores guardados no ficheiro
                    arquivo.close()
                    # Reescrever o ficheiro
                    arquivo=open('Equipas\\'+clube+'.dat','wb')
                    # Guardar os dados do ficheiro
                    jogadores.update({nome:[posicao,valor]})
 
                else:
                # Se for o 1º jogador a ser inserido no ficheiro
                    jogadores={}
                    # Cria um novo dicionário com os dados do jogador inserido
                    jogadores.update({nome:[posicao,valor]})
 
                # Guardar os dados no ficheiro
                pickle.dump(jogadores,arquivo)
                arquivo.close()
 
                input('\nJogador adicionado com sucesso\nPrima ENTER para continuar')
 
            except OSError:
                # Mensagem de erro caso o ficheiro não exista
                print('Equipa não encontrada')
 
        elif opc=='1.2' and login==True: # testa se está logado
        # Apagar jogador
            # Lê o clube a que o jogador pertence
            clube=input('Clube do jogador a eliminar: ')
            # Abre o ficheiro do clube escolhido
            arquivo=open('Equipas\\'+clube+'.dat','r+b')
 
            # Carregar os dados do ficheiro para um dicionário
            jogadores=pickle.load(arquivo)
            arquivo.close()
 
            # Apaga o jogador selecionado do dicionário
            jogador=input('Nome do jogador que deseja apagar: ')
            jogadores.pop(jogador)
           
            # Reescrever o ficheiro com o dicionário atualizado
            arquivo=open('Equipas\\'+clube+'.dat','wb')
            pickle.dump(jogadores,arquivo)
            arquivo.close()
 
            input('Jogador apagado com sucesso\nPressione ENTER para continuar')
 
        elif opc=='1.3':
        # Consulta de Jogadores
            menu_consultar_jogadores()
            opc=input(': ')
 
            if opc=='1.3.1':
            # Consulta Plantel
                # listar o nome dos ficheiros(equipas) existentes
                lista_clubes=os.listdir('Equipas\\')
               
                nome_jogador=input('Nome do jogador: ')
               
                jogador_encontrado=False
 
                # Procurar o Jogador em todos os ficheiros
                for equipa in lista_clubes:
                   
                    # abrir o ficheiro correspondente ao clube no modo de leitura
                    arquivo=open('Equipas\\'+equipa,'rb')
                    jogadores=pickle.load(arquivo)
                   
                    # Procurar o nome do jogador escollhido no ficheiro selecionado
                    if nome_jogador in jogadores.keys():
                        # Mostrar o nome do clube a que o joagador pretence (nome do ficheiro sem a extensa)
                        print('\nFoi encontrado\nJoga no clube',equipa[:-4])
                        jogador_encontrado=True
                        break
                   
                # Mensagem caso não encontre o jogador emn nenhum ficheiro
                if jogador_encontrado==False:
                    print('Jogador não encontrado')
 
            elif opc=='1.3.2':
            # Listar por Posição
                # Listar o nome de todos os ficheiros (clubes)
                lista_clubes=os.listdir('Equipas\\')
               
                posicao_jogador=input('Posição do jogador: ')
 
                # Procurar em todos os ficheiros jogadores da posição escolhida
                for equipa in lista_clubes:
                   
                    # Abrir o ficheiro selecionado em modo de leitura
                    arquivo=open('Equipas\\'+equipa,'rb')
                    jogadores=pickle.load(arquivo)
                   
                    # Procurar no ficheiro selecionado os jogadores da posição indicada pelo utilizador
                    for jogador,posicao in jogadores.items():
                        if posicao[0]==posicao_jogador:
                            print('\nNome do jogador:',jogador,'\nClube onde joga:',equipa[:-4])
 
            elif opc=='-':
                menu_jogadores()
                voltar_atras="menu_jogadores";
 
        elif opc=="-":
            menu_principal()
            voltar_atras="menu_principal";
   
    #Clubes
    elif opc=='2' or voltar_atras=="menu_clubes":
        menu_clubes()
        opc=input(': ')
 
        if opc=='2.1' and login==True: # Testar se está logado
        # Inserir novo Clube
            clube=input('Nome do clube: ')
 
            #Criar o ficheiro binário para o clube
            arquivo=open('Equipas\\'+clube+'.dat','wb')
 
            input('\nO clube foi inserido.\nPressione ENTER para continuar')
 
            # Fechar o ficheiro criado
            arquivo.close()
 
        elif opc=='2.2' and login==True: # Testar se está logado
        # Apagar Clube  
            clube=input('Nome do clube: ')
            confirma=input(f'Tem certeza que deseja apagar o clube {clube} e todos os seus atletas\n\t\t(S) (N)\n: ')
 
            # Confirmar que o utilizador quer apagar o ficheiro
            if confirma.upper()=='S':
               
                #Eliminar o ficheiro binário
                try:
                    os.remove('Equipas\\'+clube+'.dat')
                    input('Clube apagado com sucesso\nPrima ENTER para continuar')
                except OSError:
                    # Mostrar Erro caso o ficheiro não exista
                    print('Clube não existe')
 
        elif opc=='2.3':
        # Consultr Clubes
            menu_consultar_clubes()
            opc=input(': ')
 
            if opc=='2.3.1':
 
                # Listar o nome dos clubes existentes
                print("\n-- Clubes existentes --")
                lista_clubes=os.listdir('Equipas\\')
                for equipa in lista_clubes:
                    print(equipa[:-4])
               
                #Consultar o plantel de um clube
                clube=input('\nNome do clube: ')
               
                try:
                   
                    # Tenta abrir o ficheiro relacionado com o clube escolhido
                    arquivo=open('Equipas\\'+clube+'.dat','rb')
                   
                    # Lê os dados do ficheiro (clube escolhido) e guarda os dados (Jogadores) num dicionário
                    lista_jogadores=pickle.load(arquivo)
                    # Fecha o ficheiro aberto
                    arquivo.close()
 
                    # Cabeçalho da consulta
                    print('\nNome\tPosição\t\tValor')
                    print('-----------------------------')
                   
                    # Listagem de todos os jogadores do clube escolhido
                    for jogador in lista_jogadores:
                        print(jogador,lista_jogadores[jogador][0],lista_jogadores[jogador][1],sep='\t')
               
                except OSError:
                    # Caso teve havido um erro com o ficheiro selecionado
                    print('Erro na abertura do ficheiro')
 
            elif opc=='2.3.2':
            # Consulta valor do plantel
 
                # Listar o nome dos clubes existentes
                print("\n-- Clubes existentes --")
                lista_clubes=os.listdir('Equipas\\')
                for equipa in lista_clubes:
                    print(equipa[:-4])
               
                # Ler o clube escolhido
                clube=input('\nNome do clube: ')
               
                #Abrir o ficheiro em modo leitura relacionado com o clube escolhido
                arquivo=open('Equipas\\'+clube+'.dat','rb')
               
                #Ler os dados do ficheiro
                jogadores=pickle.load(arquivo)
               
                # Calcular o somatório dos passes dos jogadores
                soma_valores=0
                for jogador in jogadores.values():
                    soma_valores+=int(jogador[1])
               
                # Mostrar o Total do valor dos passes dos jogadores do clube escolhido
                print('\nOrçamento do',clube,'é',soma_valores,"euros")
 
            elif (opc=='-'):
                menu_clubes()
                voltar_atras="menu_clubes";
 
        elif opc=='-':
                voltar_atras="menu_principal";
 
    #Login
    elif opc=='3':
 
        # ler as credênciais
        utilizador=input('Username: ')
        palavra_chave=input('Password: ')
 
        # Abrir o ficheiro onde estão as contas
        arquivo=open('credenciais.dat','r+b')
 
        # Copiar as credênciais encriptadas
        credenciais=pickle.load(arquivo)
 
        # Testar se os dados do login estão corretos
        for username,password in credenciais.items():
            # Desencriptar a password
            codigo=""
            for caracter in password:
                codigo+=caracteres[caracteres_codificados.find(caracter)]
                login=True
 
        # Testar se encontrou alguma conta com as credenciais usadas no login
        if login==False:
            print('Login incorreto') 