# declarar tupla
meses= ("janeiro","feveireiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")

# aceder a um elemento da tupla
print(meses[1])

# dicionario aniversario
aniversarios={
                'Anthony': (18,7),
                'David':(21,6),
                'Marques': (4,10),
                'Ribeiro':(28,7),
                'Sobral': (18,4),
                'Gonçalves': (26,9),
                'Cartaxo': (20,10),
                'Emanuel': (4,5),
                'Emily': (3,9),
                'Gabriel': (10,12),
                'Gonçalo': (3,1),
                'Ricardo':(17,9),
                'Matos':(10,7)
             }

# Mostrar o dia de aniversario de um aluno
nome_aluno= input("Qual o aluno: ").capitalize()
print(aniversarios[nome_aluno][0], "de", meses[aniversarios[nome_aluno][1]-1])

# Mostrar todos os alunos que fazem anos num determinado mes 
from datetime import datetime 
mes= datetime.now().month

'''
posiçao= 0
for nome_meses in meses:
    posiçao+= 1  
    if mes==nome_meses:3
        break  
'''

for i in aniversarios.keys():
    if mes == aniversarios[i][1]:
        print (i,":",aniversarios[i][0], "de",meses[aniversarios[i][1]-1])
