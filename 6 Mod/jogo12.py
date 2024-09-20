perguntas1= ("Qual o plural de chapéu?"
            "Barack Obama foi presidente de que país?"
            "Em que país de localiza o Taj Mahal?"
            "Quem inventou a lâmpada?"
            "Quais as respectivas cores da reciclagem do papel, do vidro, do metal e do plástico?"
            "A que temperatura a água ferve?"
            "Quanto tempo a Terra demora para dar uma volta completa em torno dela mesma?"
            "O que é mais pesado: 1 quilo de algodão ou 1 quilo de ferro?")

perguntas= []
sorteadas= []
perguntas.append(perguntas1)

import random 
for i in perguntas:
    random.choice(perguntas)
    print ()