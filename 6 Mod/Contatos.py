Contactos = {
    "Carlos Malta": {"telemovel" : 918780166, "Data de nascimento": "5-11-1973", "Email":"p946@esenviseu.net"},
    "Dinis Marques": {"telemovel": 963899851, "Data de Nascimento": "04-10-2008", "Email": "a22990@esenviseu.net"},
    "Emanuel Nunes": {"telemovel" : 935236658,"Data de nascimento": "4-5-2008", "Email":"a24576@esenviseu.net"},
    "Gabriel Ricardo":{"telemovel":931307257, "Data de nascimento":"17-09-2008", " Email":"a24745@esen.viseu.net"},
    "Gonçalo Rodrigues":{"telemovel": 960159003, "Data de nascimento":"03-01-2008", "Email": "a24586@esenviseu.net"},
    "Eduardo Cartaxo":{"telemovel": 967859453, "Data de nascimento": "20-10-2008", "Email": "a24578@esenviseu.net"},
    "Gabriel Marques":{"telemovel":960128022, "Data de nascimento":"10-12-2008","Email":"a24590@esenviseu.net"},
    "Emily Ribeiro":{"telemovel":960411558, "Data de nascimento": "03-09-2007", "Email": "a22992@esenviseu.net"},
    "Duarte Gonçalves":{"telemovel":932524664, "Data de nascimento":"26-9-2008","Email": "a24575@esenviseu.net"},
    "Gonçalo Matos":{"telemovel": 926515105, "Data de nascimento": "10-07-2007", "Email": "a24591@esenviseu.net"},
    "Anthony Fuzinato":{"telemovel":936395308,"Data de nascimento": "18-07-2008","Email":"a24553@esenviseu.net"},
    "Dinis Ribeiro" : {"telemovel" : 926814526, "Data de nascimento" : "28-7-2007" , "Email" : "a24570@esenviseu.net"},
    "David Silva":{"telemovel":962683451,"Data de Nascimento":"21-06-2008","Email":"a22989@eesenviseu.net"},
    "Gabriel Ribeiro":{"telemovel":938606858,"Data de nascimento":"27-6-2008","Email" :"a24693@esenviseu.net"},
    "Dinis Sobral":{"telemovel":934951279,"Data de nascimento":"18-4-2008","Email" :"a24571@esenviseu.net"}}

def menu():
    print ("-"*22)
    print ("Menu".center(20))
    print ("-"*22)
    print ("1- Listar Contactos")
    print ("2- Inserir Contacto")
    print ("3- Consultar Contacto")
    print ("4- Remover Contacto")
    print ("5- editar Contacto")
    print ("0- Sair")
    print ("-"*20)

while True:
    menu()
    opçao= int(input("Qual a opçao que voce deseja? "))
    
    if opçao == 0:
        break
    elif opçao == 1:
        nomes= []
        for i in Contactos.keys():
            nomes.append(i)
        nomes.sort()
        n_registros = 0
        for k in nomes:
            print(k + ": " + str(Contactos[k]["telemovel"]))
            n_registros+= 1
            if n_registros %5== 0:
                input("Pressione o enter para carregar...")

        input("\nPressione a tecla enter para continuar...")

    elif opçao == 2:
        print("Introduza os dados do contacto..")
        nome= input("Qual o nome que desejas adicionar? ")
        telemovel= input("Qual o telemovel que desejas adicionar? ")
        data_nascimento= input("Qual data de nascimento que desejas adicionar? ")
        email= input("Qual o email que desejas adicionar? ")

        Contactos[nome]={"telemovel":telemovel, "Data de Nascimento": data_nascimento, "Email": Email}
    
    elif opçao == 3:
        tipo_pesquisa= input("Pesquisa por nome | telemovel | email: ".lower())

        if tipo_pesquisa == "nome":
            nome = input("Nome do contato: ")
            print ("telemovel", Contactos[nome]["telemovel"])
            print ("Data de Nascimento", Contactos[nome]["Data de Nascimento"])
            print ("Email", Contactos[nome]["Email"])
        
    elif (tipo_pesquisa=="telemóvel"):
            numero=int(input("Nº de Telemóvel:"))
            for nome in Contactos.keys():
                if(Contactos[nome]["telemóvel"]==numero):
                    print("Nome:",nome)
                    print("Data de Nascimento:",Contactos[nome]["Data Nascimento"])
                    print("Email:",Contactos[nome]["Email"])
       
    elif (tipo_pesquisa=="Email"):
        email=input("Qual o Email do contacto:")
        for nome in Contactos.keys():
            if(Contactos[nome]["Email"]==email):
                print("Nome:",nome)
                print("Data de Nascimento:",Contactos[nome]["Data Nascimento"])
                print("Telefone:",Contactos[nome]["telemóvel"])

    elif opçao == 4:
        while True:
            nome= input("Nome do contato que quer remover: ")
            input()
            if nome not in Contactos:
                print ("O nome nao se encontra nos contatos...")

                if input("Desejas continuar remover algum contacto? (S/N)").lower() == "n":
                    break
            else:
                Contactos.pop(nome)
                print ("O seu contato foi eliminado com sucesso")
                print()

    elif opçao == 5:
        