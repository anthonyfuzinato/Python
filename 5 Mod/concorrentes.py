concorrentes= map(int(input().split()))
patinagem= []

#maximo e minimos
concorrentes.append(patinagem)
print (min(patinagem))
print(max(patinagem))

# retirar
patinagem.remove(min(patinagem))
patinagem.remove(max(patinagem))

# Media de todos 
media= sum(patinagem) / len(concorrentes)
print(f"{media:.2f}")
