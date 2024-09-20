'''
PSI - Módulo 7
Ficheiros - Módulo 7
'''
 
# Função para criar um menu
def menu():
    print('='*30)
    print('MENU DE FUNÇÕES'.center(30))
    print('='*30)
    print('1 - Administração')
    print('2 - Consulta')
    print('0 - Sair')
    print('='*30)
 
# Função para criar um menu de administração
def menu_admin():
    print('='*30)
    print('MENU DE ADMINISTRAÇÃO'.center(30))
    print('='*30)
    print('1 - Novo Idioma')
    print('2 - Apagar Idioma')
    print('0 - Voltar')
    print('='*30)
 
# Importar o módulo
import os
 
# Criar uma pasta (mkdir = make directory)
try:
    os.mkdir('.\\Lusíadas')
except FileExistsError:
    print('Já existe essa pasta\n')
 
# Listar os ficheiros de uma pasta
print('Em qual destes idiomas quer ler os Lusíadas?')
lista_idiomas = os.listdir('.\\Lusíadas')
for idioma in lista_idiomas:
    print(idioma[:-4])
   
while True:
 
    menu()
    opcao = input('Opção: ')
 
    if opcao == '1':
        menu_admin()
        opcao_admin = input('Opção: ')
 
        if opcao_admin == '1':
            novo_idioma = input('Nome do idioma: ').capitalize()
            if os.path.exists(novo_idioma + '.txt'):
                print('Esse idioma já existe\n')
                input('Pressione ENTER para voltar ao menu')
                break
            else:
                # Criar novo ficheiro com o nome
                ficheiro = open('.\\Lusíadas\\' + novo_idioma + '.txt', 'w')
                texto = input('Texto: ')
                # Gravar o texto no ficheiro
                ficheiro.write(texto)
                ficheiro.close()
                print('O ficheiro foi gravado com sucesso')    
 
        if opcao_admin == '2':
            apagar_idioma = input('Nome do idioma: ').capitalize()
            # Apagar o ficheiro correspondente ao idioma
            try:
                os.remove('.\\Lusíadas\\' + apagar_idioma + '.txt')
                print('O ficheiro foi apagado com sucesso')
            except FileNotFoundError:
                print('Esse idioma não existe\n')
            except FileExistsError:
                print('Erro no ficheiro')
   
    if opcao == '0':
        break 