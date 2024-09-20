def ler(nome):
    while True:
        try:
            ficheiro= open(".\\" + {nome} + ".txt","r")
            return (ficheiro.read())
        except:
            return ("Nao encontramos esse caminho..")

nome= (input("Qual o caminho que desejas abrir? "))
texto= ler(nome)
print (texto)