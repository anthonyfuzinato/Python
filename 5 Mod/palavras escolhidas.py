import random 
string= "FUTEBOL".upper()
palavra= []

for i in string:
    palavra.append(i)

while len(palavra) != 0:
    letraescolhida= random.choice(palavra)
    print(letraescolhida, end= "")
    palavra.remove(letraescolhida)