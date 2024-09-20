numeros= []
import random

for i in range(51):
    numeros.append(i)

numerosorteado= []
for x in range (5):
    numero= (random.choise(numero))
    numerosorteado.append(numero)
    numeros.remove(numero)
    
print(f"O numero sorteado foi: {numerosorteado}")