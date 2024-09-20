'''
Estruturas de Dados Compostas
Dicionários
'''
 
# Declarar o dicionário
capitais={"Portugal":"Lisboa",
          "França": "Paris",
          "Alemanha":"Berlim"}
 
# Aceder a um dos elementos do dicionário
print(capitais["Portugal"])
 
# Aceder ao elemento e verificar se o elemento existe
pais_escolhido=input("Escolhe um pais:")
# Verificar se existe a chave escolhida no dicionário
if pais_escolhido in capitais:
    print("A capital é",end=" ")
print(capitais.get(pais_escolhido,"Não conheço a capital de "+ pais_escolhido))
 
# Mostrar todos os elmentos do dicionário iterando a chave
print("Paises:")
for pais in capitais.keys():
    print("\t",pais)
 
# Mostrar todos os elmentos (chave,valor) do dicionário
print("Paises-Capitais:")
for chave,valor in capitais.items():
    print(chave,"-",valor)
 
# Mostrar todos os valores do dicionário
print("Capitais:")
for capital in capitais.values():
    print(capital)
 
# Nostrar o dicionário com os pares chave-valor
print(capitais)    
 
# Mostrar o tamanho do dicionário (numero de elementos)
print("Número de paises:",len(capitais))
 
# Apagar o ultimo elemento do dicionário
capitais.popitem()
 
# Apagar um elemento especifico
capitais.pop("Portugal")
del capitais["Alemanha"]
 
# Apagar todos os elementos do dicionário
capitais.clear()
 
# Inserir um novo elemento
capitais.update({"Brasil":"Brasilia"})
 
# Eleminar o dicionária
del(capitais)
 
# Atualizar um elemento do dicionário (mudar o valor)
capitais.update({"Portugal":"Lisbon"})

print(capitais)

# Dicionario aninhado (dicionario dentro outro dicionario)
enciclopedia= {"Brasil":{"Moeda":"Real", "Habitantes":200000000,"capital":"Brasilia"},
               "Portugal":{"Moeda":"Euro","Habitantes":11000000,"Capital":"Lisboa"}}

#Aceder a um item do dicionario aninhado
print(enciclopedia["Brasil"])

# Aceder a um valor do item do dicionario aninhado
print(enciclopedia["Brasil", [capital]])

# Mostrar os dados do dicionário através de uma chave escolhida pelo utilizador
pais_escolhido=input("Qual o pais que pretende consultar:")
dado_escolhido=input(f"Escolha um destes dados ({enciclopedia[pais_escolhido].keys()}:")
print(dado_escolhido,":",enciclopedia[pais_escolhido][dado_escolhido])

# Dicionario com valores de varios tipos
aluno= {"nome":"Carlos Navarro",
        "idade":16,
        "notas":{"PSI":14,"Portugues":12,"Matematica":15},
        "codigo postal":{"codigo":3500,"localidade":"Viseu"},
        "nee":True,
        "Media":12.7}

# Construtor (usar um construtor para criar um dicionario)
pessoa= dict(nome="Carlos Navarro", idade=16,morada="Viseu")
print(pessoa)

#copiar os valores do dicionario para outro dicionario
outra_pessoa= pessoa.copy()
