'''
Sets
'''

# Progama para registrar a morada dos clientes das lojas
lista_moradas= []
while True: 
    morada=(input("Morada do cliente: "))
    if morada == "0":
        break
    lista_moradas.append(morada)

cidades= set(lista_moradas)

# Percorrer 1 a 1 e contar
for cidade in cidades:
    print(cidade,":",lista_moradas.count(cidade))

print(lista_moradas)
print(cidades)

###########################################################################
'''
# Declarar set
cidades= {"Viseu","Porto","Lisboa","Viseu","Porto","Porto","Braga"}

# Adicionar elementos ao set
cidades.add("Viana do castelo")

# Apagar elementos do set
cidades.remove("Porto")

# Mostrar elementos do set
print (cidades)
'''