lista= ["Pera","Cereja","Morango",1000,True]


for i in lista:
    print(i)

print ("Elemento guardado na posiçao 2:", lista[2])

lista.append("Beringela")

lista.insert(2,"Melao")

lista.pop()
lista.pop(1)

lista.remove("Melao")

lista.extend (["Banana","Manga","Lixia"])

print (lista.index("Banana"))

print (lista.count("Banana"))

lista.sort()

lista.reverse()

lista_numerica= [1,2,3,4,5,6,7]

print ("O total dos elementos da liste é: ", sum(lista_numerica))

print ("O maior valor da lista é", max(lista_numerica))
print ("O menor valor da lista é", min(lista_numerica))

print (f"A lista tem {len(lista_numerica)} elementos")

print(lista)
