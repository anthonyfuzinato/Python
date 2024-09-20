valor= int(input())
Namigos= int(input())

nomes= []
presentes= []
valores= []
nome= ""
presente= ""
valor= ""
valores_ordenados= []

nomes.append(input("qual o nome dos amigos: ").lower().split())
presentes.append(input("qual sao os presentes?").lower().split())
valores.append(map(int(input("Qual os valores? ").lower().split())))

valores_ordenados= valores.copy()
valores_ordenados.sort()
 
#verificar dinheiro
for i in range (Namigos):
    if sum(valores) > valor:
        valores_ordenados.remove(max(valores_ordenados))

for i in range(Namigos):
    nome= nomes.index(valores_ordenados.index(valores))
    presente= presente.index(nome)
for i in range (Namigos):
     print (f"nome: {nome[i]} presente: {presente} valor: {valores_ordenados}")
  
