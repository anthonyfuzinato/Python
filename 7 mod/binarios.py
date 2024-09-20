'''
Ficheiro binario
'''

import pickle

# Criar ficheiro
f = open(".\\dados.bin", "bw")

# Estrutura de dados
lista= [10,11,16,19]

# Escrever
pickle.dump(lista,f)

# Fechar o ficheiro
f.close()

# Abrir ficheiro no modo leitura
f = open(".\dados.bin", "b")

# Ler o ficheiro e copiar a estrutura de dados
lista= pickle.load(f)
for nota in lista:
    print(nota)