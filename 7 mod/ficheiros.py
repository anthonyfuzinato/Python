'''
PSI - MODULO 7
Ficheiros
'''

# Criar um ficheiro de texto
f= open("teste.txt","a+")

# Mostrar informaçoes sobre o ficheiro
print(f)

# Mostrar a identificaçao do ficheiro
print(id(f))

# Mostrar o tipo que é o ficheiro 
print(type(f))

# Escrever no ficheiro
f.write("\nModulo 7")

# Escrever no ficheiro o conteudo de uma lista
disciplinas= ["RC","SO","AC"]
f.writelines(disciplinas)

# Ler os dados do ficheiro
print(f.read())

# Ler apenas o caracteres indicados
print(f.read(2))

# Ler uma linha do ficheiro
print(f.redline())

# Ler todos as linhas do ficheiro uma a uma
for linha in f:
    print(linha)

linha= "false"
while linha != "":
    linha= f.readline()
    print(linha)

# Ler todas as linhas do ficheiro e guardar numa lista
lista= f.readlines()
print (lista, end="")


# Mostrar a posiçao do cursos no ficheiro
print(f.tell())

# Deslocar o ponteiro para uma posiçao do ficheiro
f.seek(4)

# Fechar o ficheiro
f.close()