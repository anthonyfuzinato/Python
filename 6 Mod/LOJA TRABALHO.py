


# Imports
from pyfiglet import figlet_format 
import pyfiglet 
from datetime import datetime
from random import random
import os


##########################################
            #Listas/Dicionarios/Sets

##########################################

'''      Dicionario      '''
        ########## HOMENS ###########

# Produtos masculinos
BonésH = [
    {"Bone preto": {"Valor": 45.50, "lançamento": "15/05/24", "estoque": 150}},
    {"Bone azul": {"Valor": 35.25, "lançamento": "20/06/24", "estoque": 200}},
    {"Bone vermelho": {"Valor": 40.75, "lançamento": "10/07/24", "estoque": 100}},
    {"Bone verde": {"Valor": 20.20, "lançamento": "05/08/24", "estoque": 250}},
    {"Bone amarelo": {"Valor": 25.30, "lançamento": "15/09/24", "estoque": 180}},
    {"Bone branco": {"Valor": 15.40, "lançamento": "25/10/24", "estoque": 220}},
    {"Bone roxo": {"Valor": 30.60, "lançamento": "10/11/24", "estoque": 130}},
    {"Bone laranja": {"Valor": 18.70, "lançamento": "20/12/24", "estoque": 160}},
    {"Bone rosa": {"Valor": 25.80, "lançamento": "05/01/25", "estoque": 140}},
    {"Bone cinza": {"Valor": 22.90, "lançamento": "15/02/25", "estoque": 170}},
    {"Bone marrom": {"Valor": 28.00, "lançamento": "25/03/25", "estoque": 190}}
]

CasacosH = [
    {"Casaco preto": {"Valor": 100.50, "lançamento": "15/05/24", "estoque": 100}},
    {"Casaco azul": {"Valor": 90.25, "lançamento": "20/06/24", "estoque": 80}},
    {"Casaco vermelho": {"Valor": 105.75, "lançamento": "10/07/24", "estoque": 120}},
    {"Casaco verde": {"Valor": 75.20, "lançamento": "05/08/24", "estoque": 110}},
    {"Casaco amarelo": {"Valor": 85.30, "lançamento": "15/09/24", "estoque": 90}},
    {"Casaco branco": {"Valor": 65.40, "lançamento": "25/10/24", "estoque": 130}},
    {"Casaco roxo": {"Valor": 115.60, "lançamento": "10/11/24", "estoque": 70}},
    {"Casaco laranja": {"Valor": 70.70, "lançamento": "20/12/24", "estoque": 100}},
    {"Casaco rosa": {"Valor": 80.80, "lançamento": "05/01/25", "estoque": 85}},
    {"Casaco cinza": {"Valor": 95.90, "lançamento": "15/02/25", "estoque": 95}},
    {"Casaco marrom": {"Valor": 110.00, "lançamento": "25/03/25", "estoque": 105}}
]

CamisasH = [
    {"Camisa preta": {"Valor": 55.50, "lançamento": "15/05/24", "estoque": 220}},
    {"Camisa azul": {"Valor": 50.25, "lançamento": "20/06/24", "estoque": 180}},
    {"Camisa vermelha": {"Valor": 60.75, "lançamento": "10/07/24", "estoque": 240}},
    {"Camisa verde": {"Valor": 40.20, "lançamento": "05/08/24", "estoque": 200}},
    {"Camisa amarela": {"Valor": 45.30, "lançamento": "15/09/24", "estoque": 210}},
    {"Camisa branca": {"Valor": 35.40, "lançamento": "25/10/24", "estoque": 190}},
    {"Camisa roxa": {"Valor": 50.60, "lançamento": "10/11/24", "estoque": 170}},
    {"Camisa laranja": {"Valor": 30.70, "lançamento": "20/12/24", "estoque": 150}},
    {"Camisa rosa": {"Valor": 40.80, "lançamento": "05/01/25", "estoque": 160}},
    {"Camisa cinza": {"Valor": 38.90, "lançamento": "15/02/25", "estoque": 230}},
    {"Camisa marrom": {"Valor": 44.00, "lançamento": "25/03/25", "estoque": 140}}
]

CalçasH = [
    {"Calça preta": {"Valor": 70.50, "lançamento": "15/05/24", "estoque": 120}},
    {"Calça azul": {"Valor": 60.25, "lançamento": "20/06/24", "estoque": 100}},
    {"Calça vermelha": {"Valor": 75.75, "lançamento": "10/07/24", "estoque": 130}},
    {"Calça verde": {"Valor": 50.20, "lançamento": "05/08/24", "estoque": 110}},
    {"Calça amarela": {"Valor": 55.30, "lançamento": "15/09/24", "estoque": 90}},
    {"Calça branca": {"Valor": 45.40, "lançamento": "25/10/24", "estoque": 140}},
    {"Calça roxa": {"Valor": 65.60, "lançamento": "10/11/24", "estoque": 80}},
    {"Calça laranja": {"Valor": 35.70, "lançamento": "20/12/24", "estoque": 100}},
    {"Calça rosa": {"Valor": 50.80, "lançamento": "05/01/25", "estoque": 120}},
    {"Calça cinza": {"Valor": 52.90, "lançamento": "15/02/25", "estoque": 130}},
    {"Calça marrom": {"Valor": 60.00, "lançamento": "25/03/25", "estoque": 110}}
]

SapatosH = [
    {"Sapato preto": {"Valor": 110.99, "lançamento": "15/05/24", "estoque": 90}},
    {"Sapato azul": {"Valor": 95.99, "lançamento": "20/06/24", "estoque": 80}},
    {"Sapato vermelho": {"Valor": 130.99, "lançamento": "10/07/24", "estoque": 100}},
    {"Sapato verde": {"Valor": 150.99, "lançamento": "05/08/24", "estoque": 70}},
    {"Sapato amarelo": {"Valor": 80.99, "lançamento": "15/09/24", "estoque": 110}},
    {"Sapato branco": {"Valor": 100.99, "lançamento": "25/10/24", "estoque": 120}},
    {"Sapato roxo": {"Valor": 120.99, "lançamento": "10/11/24", "estoque": 90}},
    {"Sapato laranja": {"Valor": 90.99, "lançamento": "20/12/24", "estoque": 100}},
    {"Sapato rosa": {"Valor": 70.99, "lançamento": "05/01/25", "estoque": 110}},
    {"Sapato cinza": {"Valor": 60.99, "lançamento": "15/02/25", "estoque": 130}},
    {"Sapato marrom": {"Valor": 100.99, "lançamento": "25/03/25", "estoque": 120}}
]

# Produtos femininos
BonésM = [
    {"Bone preto": {"Valor": 45.50, "lançamento": "15/05/24", "estoque": 150}},
    {"Bone azul": {"Valor": 35.25, "lançamento": "20/06/24", "estoque": 200}},
    {"Bone vermelho": {"Valor": 40.75, "lançamento": "10/07/24", "estoque": 100}},
    {"Bone verde": {"Valor": 20.20, "lançamento": "05/08/24", "estoque": 250}},
    {"Bone amarelo": {"Valor": 25.30, "lançamento": "15/09/24", "estoque": 180}},
    {"Bone branco": {"Valor": 15.40, "lançamento": "25/10/24", "estoque": 220}},
    {"Bone roxo": {"Valor": 30.60, "lançamento": "10/11/24", "estoque": 130}},
    {"Bone laranja": {"Valor": 18.70, "lançamento": "20/12/24", "estoque": 160}},
    {"Bone rosa": {"Valor": 25.80, "lançamento": "05/01/25", "estoque": 140}},
    {"Bone cinza": {"Valor": 22.90, "lançamento": "15/02/25", "estoque": 170}},
    {"Bone marrom": {"Valor": 28.00, "lançamento": "25/03/25", "estoque": 190}}
]

CasacosM = [
    {"Casaco preto": {"Valor": 100.50, "lançamento": "15/05/24", "estoque": 100}},
    {"Casaco azul": {"Valor": 90.25, "lançamento": "20/06/24", "estoque": 80}},
    {"Casaco vermelho": {"Valor": 105.75, "lançamento": "10/07/24", "estoque": 120}},
    {"Casaco verde": {"Valor": 75.20, "lançamento": "05/08/24", "estoque": 110}},
    {"Casaco amarelo": {"Valor": 85.30, "lançamento": "15/09/24", "estoque": 90}},
    {"Casaco branco": {"Valor": 65.40, "lançamento": "25/10/24", "estoque": 130}},
    {"Casaco roxo": {"Valor": 115.60, "lançamento": "10/11/24", "estoque": 70}},
    {"Casaco laranja": {"Valor": 70.70, "lançamento": "20/12/24", "estoque": 100}},
    {"Casaco rosa": {"Valor": 80.80, "lançamento": "05/01/25", "estoque": 85}},
    {"Casaco cinza": {"Valor": 95.90, "lançamento": "15/02/25", "estoque": 95}},
    {"Casaco marrom": {"Valor": 110.00, "lançamento": "25/03/25", "estoque": 105}}
]

CamisasM = [
    {"Camisa preta": {"Valor": 55.50, "lançamento": "15/05/24", "estoque": 220}},
    {"Camisa azul": {"Valor": 50.25, "lançamento": "20/06/24", "estoque": 180}},
    {"Camisa vermelha": {"Valor": 60.75, "lançamento": "10/07/24", "estoque": 240}},
    {"Camisa verde": {"Valor": 40.20, "lançamento": "05/08/24", "estoque": 200}},
    {"Camisa amarela": {"Valor": 45.30, "lançamento": "15/09/24", "estoque": 210}},
    {"Camisa branca": {"Valor": 35.40, "lançamento": "25/10/24", "estoque": 190}},
    {"Camisa roxa": {"Valor": 50.60, "lançamento": "10/11/24", "estoque": 170}},
    {"Camisa laranja": {"Valor": 30.70, "lançamento": "20/12/24", "estoque": 150}},
    {"Camisa rosa": {"Valor": 40.80, "lançamento": "05/01/25", "estoque": 160}},
    {"Camisa cinza": {"Valor": 38.90, "lançamento": "15/02/25", "estoque": 230}},
    {"Camisa marrom": {"Valor": 44.00, "lançamento": "25/03/25", "estoque": 140}}
]

TopsCroppedM = [
    {"Top preto": {"Valor": 30.50, "lançamento": "15/05/24", "estoque": 280}},
    {"Top azul": {"Valor": 25.25, "lançamento": "20/06/24", "estoque": 260}},
    {"Top vermelho": {"Valor": 35.75, "lançamento": "10/07/24", "estoque": 300}},
    {"Top verde": {"Valor": 20.20, "lançamento": "05/08/24", "estoque": 250}},
    {"Top amarelo": {"Valor": 22.30, "lançamento": "15/09/24", "estoque": 270}},
    {"Top branco": {"Valor": 18.40, "lançamento": "25/10/24", "estoque": 290}},
    {"Top roxo": {"Valor": 28.60, "lançamento": "10/11/24", "estoque": 220}},
    {"Top laranja": {"Valor": 16.70, "lançamento": "20/12/24", "estoque": 310}},
    {"Top rosa": {"Valor": 24.80, "lançamento": "05/01/25", "estoque": 230}},
    {"Top cinza": {"Valor": 21.90, "lançamento": "15/02/25", "estoque": 240}},
    {"Top marrom": {"Valor": 26.00, "lançamento": "25/03/25", "estoque": 260}}
]

CalçasM = [
    {"Calça preta": {"Valor": 70.50, "lançamento": "15/05/24", "estoque": 120}},
    {"Calça azul": {"Valor": 60.25, "lançamento": "20/06/24", "estoque": 100}},
    {"Calça vermelha": {"Valor": 75.75, "lançamento": "10/07/24", "estoque": 130}},
    {"Calça verde": {"Valor": 50.20, "lançamento": "05/08/24", "estoque": 110}},
    {"Calça amarela": {"Valor": 55.30, "lançamento": "15/09/24", "estoque": 90}},
    {"Calça branca": {"Valor": 45.40, "lançamento": "25/10/24", "estoque": 140}},
    {"Calça roxa": {"Valor": 65.60, "lançamento": "10/11/24", "estoque": 80}},
    {"Calça laranja": {"Valor": 35.70, "lançamento": "20/12/24", "estoque": 100}},
    {"Calça rosa": {"Valor": 50.80, "lançamento": "05/01/25", "estoque": 120}},
    {"Calça cinza": {"Valor": 52.90, "lançamento": "15/02/25", "estoque": 130}},
    {"Calça marrom": {"Valor": 60.00, "lançamento": "25/03/25", "estoque": 110}}
]

SapatosM = [
    {"Sapato preto": {"Valor": 110.99, "lançamento": "15/05/24", "estoque": 90}},
    {"Sapato azul": {"Valor": 95.99, "lançamento": "20/06/24", "estoque": 80}},
    {"Sapato vermelho": {"Valor": 130.99, "lançamento": "10/07/24", "estoque": 100}},
    {"Sapato verde": {"Valor": 150.99, "lançamento": "05/08/24", "estoque": 70}},
    {"Sapato amarelo": {"Valor": 80.99, "lançamento": "15/09/24", "estoque": 110}},
    {"Sapato branco": {"Valor": 100.99, "lançamento": "25/10/24", "estoque": 120}},
    {"Sapato roxo": {"Valor": 120.99, "lançamento": "10/11/24", "estoque": 90}},
    {"Sapato laranja": {"Valor": 90.99, "lançamento": "20/12/24", "estoque": 100}},
    {"Sapato rosa": {"Valor": 70.99, "lançamento": "05/01/25", "estoque": 110}},
    {"Sapato cinza": {"Valor": 60.99, "lançamento": "15/02/25", "estoque": 130}},
    {"Sapato marrom": {"Valor": 100.99, "lançamento": "25/03/25", "estoque": 120}}
]


############     CRIANÇAS     ################
BonésCrianças = [
    {"Bone preto": {"Valor": 22.50, "lançamento": "15/05/24", "estoque": 150}},
    {"Bone azul": {"Valor": 18.25, "lançamento": "20/06/24", "estoque": 160}},
    {"Bone vermelho": {"Valor": 20.75, "lançamento": "10/07/24", "estoque": 140}},
    {"Bone verde": {"Valor": 12.20, "lançamento": "05/08/24", "estoque": 130}},
    {"Bone amarelo": {"Valor": 15.30, "lançamento": "15/09/24", "estoque": 145}},
    {"Bone branco": {"Valor": 10.40, "lançamento": "25/10/24", "estoque": 155}},
    {"Bone roxo": {"Valor": 18.60, "lançamento": "10/11/24", "estoque": 125}},
    {"Bone laranja": {"Valor": 13.70, "lançamento": "20/12/24", "estoque": 165}},
    {"Bone rosa": {"Valor": 14.80, "lançamento": "05/01/25", "estoque": 120}},
    {"Bone cinza": {"Valor": 12.90, "lançamento": "15/02/25", "estoque": 135}},
    {"Bone marrom": {"Valor": 16.00, "lançamento": "25/03/25", "estoque": 170}},
]

CasacosCrianças = [
    {"Casaco preto": {"Valor": 70.50, "lançamento": "15/05/24", "estoque": 220}},
    {"Casaco azul": {"Valor": 65.25, "lançamento": "20/06/24", "estoque": 210}},
    {"Casaco vermelho": {"Valor": 75.75, "lançamento": "10/07/24", "estoque": 230}},
    {"Casaco verde": {"Valor": 50.20, "lançamento": "05/08/24", "estoque": 240}},
    {"Casaco amarelo": {"Valor": 60.30, "lançamento": "15/09/24", "estoque": 225}},
    {"Casaco branco": {"Valor": 55.40, "lançamento": "25/10/24", "estoque": 215}},
    {"Casaco roxo": {"Valor": 80.60, "lançamento": "10/11/24", "estoque": 205}},
    {"Casaco laranja": {"Valor": 48.70, "lançamento": "20/12/24", "estoque": 235}},
    {"Casaco rosa": {"Valor": 55.80, "lançamento": "05/01/25", "estoque": 200}},
    {"Casaco cinza": {"Valor": 58.90, "lançamento": "15/02/25", "estoque": 210}},
    {"Casaco marrom": {"Valor": 65.00, "lançamento": "25/03/25", "estoque": 220}},
]

CamisasCrianças = [
    {"Camisa preto": {"Valor": 65.50, "lançamento": "15/05/24", "estoque": 180}},
    {"Camisa azul": {"Valor": 60.25, "lançamento": "20/06/24", "estoque": 190}},
    {"Camisa vermelho": {"Valor": 70.75, "lançamento": "10/07/24", "estoque": 170}},
    {"Camisa verde": {"Valor": 48.20, "lançamento": "05/08/24", "estoque": 200}},
    {"Camisa amarelo": {"Valor": 55.30, "lançamento": "15/09/24", "estoque": 185}},
    {"Camisa branco": {"Valor": 52.40, "lançamento": "25/10/24", "estoque": 175}},
    {"Camisa roxo": {"Valor": 60.60, "lançamento": "10/11/24", "estoque": 195}},
    {"Camisa laranja": {"Valor": 42.70, "lançamento": "20/12/24", "estoque": 165}},
    {"Camisa rosa": {"Valor": 50.80, "lançamento": "05/01/25", "estoque": 155}},
    {"Camisa cinza": {"Valor": 47.90, "lançamento": "15/02/25", "estoque": 160}},
    {"Camisa marrom": {"Valor": 55.00, "lançamento": "25/03/25", "estoque": 170}},
]

TopsCroppedCrianças = [
    {"Top cropped preto": {"Valor": 30.50, "lançamento": "15/05/24", "estoque": 140}},
    {"Top cropped azul": {"Valor": 28.25, "lançamento": "20/06/24", "estoque": 145}},
    {"Top cropped vermelho": {"Valor": 35.75, "lançamento": "10/07/24", "estoque": 130}},
    {"Top cropped verde": {"Valor": 22.20, "lançamento": "05/08/24", "estoque": 155}},
    {"Top cropped amarelo": {"Valor": 30.30, "lançamento": "15/09/24", "estoque": 135}},
    {"Top cropped branco": {"Valor": 18.40, "lançamento": "25/10/24", "estoque": 160}},
    {"Top cropped roxo": {"Valor": 32.60, "lançamento": "10/11/24", "estoque": 125}},
    {"Top cropped laranja": {"Valor": 25.70, "lançamento": "20/12/24", "estoque": 150}},
    {"Top cropped rosa": {"Valor": 24.80, "lançamento": "05/01/25", "estoque": 120}},
    {"Top cropped cinza": {"Valor": 22.90, "lançamento": "15/02/25", "estoque": 130}},
    {"Top cropped marrom": {"Valor": 23.00, "lançamento": "25/03/25", "estoque": 145}},
]

CalçasCrianças = [
    {"Calça preta": {"Valor": 65.50, "lançamento": "15/05/24", "estoque": 210}},
    {"Calça azul": {"Valor": 60.25, "lançamento": "20/06/24", "estoque": 200}},
    {"Calça vermelha": {"Valor": 70.75, "lançamento": "10/07/24", "estoque": 220}},
    {"Calça verde": {"Valor": 48.20, "lançamento": "05/08/24", "estoque": 230}},
    {"Calça amarela": {"Valor": 55.30, "lançamento": "15/09/24", "estoque": 215}},
    {"Calça branca": {"Valor": 52.40, "lançamento": "25/10/24", "estoque": 225}},
    {"Calça roxa": {"Valor": 60.60, "lançamento": "10/11/24", "estoque": 210}},
    {"Calça laranja": {"Valor": 42.70, "lançamento": "20/12/24", "estoque": 235}},
    {"Calça rosa": {"Valor": 50.80, "lançamento": "05/01/25", "estoque": 205}},
    {"Calça cinza": {"Valor": 47.90, "lançamento": "15/02/25", "estoque": 215}},
    {"Calça marrom": {"Valor": 55.00, "lançamento": "25/03/25", "estoque": 220}},
]

SapatosCrianças = [
    {"Sapato preto": {"Valor": 90.50, "lançamento": "15/05/24", "estoque": 190}},
    {"Sapato azul": {"Valor": 80.25, "lançamento": "20/06/24", "estoque": 180}},
    {"Sapato vermelho": {"Valor": 100.75, "lançamento": "10/07/24", "estoque": 200}},
    {"Sapato verde": {"Valor": 75.20, "lançamento": "05/08/24", "estoque": 210}},
    {"Sapato amarelo": {"Valor": 85.30, "lançamento": "15/09/24", "estoque": 195}},
    {"Sapato branco": {"Valor": 65.40, "lançamento": "25/10/24", "estoque": 205}},
    {"Sapato roxo": {"Valor": 80.60, "lançamento": "10/11/24", "estoque": 215}},
    {"Sapato laranja": {"Valor": 70.70, "lançamento": "20/12/24", "estoque": 190}},
    {"Sapato rosa": {"Valor": 55.80, "lançamento": "05/01/25", "estoque": 220}},
    {"Sapato cinza": {"Valor": 70.90, "lançamento": "15/02/25", "estoque": 175}},
    {"Sapato marrom": {"Valor": 75.00, "lançamento": "25/03/25", "estoque": 200}},
]

'''        LISTA         '''

todos_itens= []
itens_encontrados = []
carrinho= []

funcionarioloja = {
    'joao': {'cargo': 'Analista', 'salario': 3000},
    'maria': {'cargo': 'Gerente', 'salario': 3000},
    'pedro': {'cargo': 'Desenvolvedor', 'salario': 3000},
    'ana': {'cargo': 'Designer', 'salario': 2500},
    'carlos': {'cargo': 'Analista', 'salario': 1500},
    'julia': {'cargo': 'Estagiário', 'salario': 1200}
}


'''     Sets e Tupla   '''
# famosos if 1
famosos = [
    ("Tom Hanks", "Nike Air Force 1"),
    ("Leonardo DiCaprio", "Adidas Yeezy Boost 350"),
    ("Meryl Streep", "Converse Chuck Taylor All Star"),
    ("Brad Pitt", "Puma Suede"),
    ("Jennifer Lawrence", "Reebok Classic Leather"),
    ("Beyoncé", "Adidas Superstar"),
    ("Elton John", "Gucci Ace"),
    ("Taylor Swift", "Reebok Club C"),
    ("Ed Sheeran", "Vans Old Skool"),
    ("Rihanna", "Puma Fenty"),
    ("Travis Scott", "Nike Air Jordan 1"),
    ("Post Malone", "Crocs Post Malone Duet Max Clog"),
    ("Drake", "Adidas Ultra Boost"),
    ("Lil Nas X", "Nike Air Max 97"),
    ("Cardi B", "Reebok Cardi B Club C"),
    ("Serena Williams", "NikeCourt Flare"),
    ("Lionel Messi", "Adidas Nemeziz"),
    ("Cristiano Ronaldo", "Nike Mercurial"),
    ("Usain Bolt", "Puma Bolt"),
    ("LeBron James", "Nike LeBron")
]

# Tenis (Novos lançamentos if 1)
tenis_recentes = {
    "Nike Air Max 2090",
    "Adidas Ultraboost 21",
    "New Balance Fresh Foam 1080v11",
    "Puma RS-X³",
    "Reebok Nano X1",
    "Under Armour HOVR Phantom 2",
    "Asics GEL-Nimbus 23",
    "Saucony Endorphin Speed",
    "Hoka One One Clifton 7",
    "Brooks Ghost 13"
}

# Noticias
noticias_esportivas = {
    "Cristiano Ronaldo Usa Tênis da SportX e Aumenta Visibilidade da Marca",
    "SportX Ajusta Preços Após Endosso de Cristiano Ronaldo",
    "Novo Endosso de Messi Impulsiona Vendas da RunFast",
    "RunFast Ajusta Preços Após Sucesso de Endosso de Lionel Messi",
    "Neymar Eleva Status da JumpMaster com Seu Último Look",
    "JumpMaster Revisa Preços Após Popularidade Crescente com Neymar"
}

# Estrutura de carrinho vazia para cada categoria
carrinho = {}

# Organizando todos os produtos
produtos = {
    'Masculino': {
        'Bonés': BonésH,
        'Casacos': CasacosH,
        'Camisas': CamisasH,
        'Calças': CalçasH,
        'Sapatos': SapatosH
    },
    'Feminino': {
        'Bonés': BonésM,
        'Casacos': CasacosM,
        'Camisas': CamisasM,
        'Tops e Cropped': TopsCroppedM,
        'Calças': CalçasM,
        'Sapatos': SapatosM
    },
    'Infantil': {
        'Bonés': BonésCrianças,
        'Casacos': CasacosCrianças,
        'Camisas': CamisasCrianças,
        'Tops e Cropped': TopsCroppedCrianças,
        'Calças': CalçasCrianças,
        'Sapatos': SapatosCrianças
    }
}


################################################
            ########Funçoes########


# Menu bem vindo loja 
def bemvindo():
    print ("-"*30)
    print ("Bem-Vindo".center(30))
    print ("-"*30)

# menu principal
def escolha1():
    os.system("cls")
    print ("================================================")
    print ("===========      MENU PRINCIPAL      ===========")
    print ("================================================")
    print ("1- Novidades e Artigos em destaques")
    print ("2- Homem")
    print ("3- Mulher")
    print ("4- Criança")
    print ("5- Pesquisar")
    print ("6- Carrinhos de compra")
    print ("7- Funcionarios")
    print ("8- Administrador - Estoque / Adicionar / Remover")
    print ("0- Sair")
    print("_"*30)

# Novidades e Looks / Novas edioçoes / Noticias
def novidades():
    os.system("cls")
    print ("=====================================")
    print ("======       Novidades         ======")
    print ("=====================================")
    print("1- Look's")
    print("2- Novas ediçoes")
    print("3- Noticias")
    print ("0- sair")
    print("-"*15)

def lançamentos():
    os.system("cls")
    print ("=======================================")
    print ("======       Lançamentos         ======")
    print ("=======================================")
    print ("1- Mostrar lista Lançamentos")
    print ("2- Adicionar novos itens")
    print ("3- Remover itens")
    print ("0- sair")
    print ("================================")

def Looksdomes():
    os.system("cls")
    print ("-"*15)
    print ("1- Look Atores")
    print ("2- Look Cantores")
    print ("3- Look Atletas")
    print ("0- sair")
    print ("-"*15)

def lookss():
    os.system("cls")
    print ("="*30)
    print ("1- Atores")
    print ("2- Cantores")
    print ("3- Atletas")
    print ("0- sair")
    print ("="*30)

def noticias():
     os.system("cls")
     print ("====================================")
     print ("======       Noticias         ======")
     print ("====================================")
     print ("Noticias".center(30))
     print ("0- sair")
     print ("="*30)

# roupa homem
def roupah():
    os.system("cls")
    print("1- Chápeus/Bonés")
    print("2- Jaquetas/Casacos")
    print("3- Camisas")
    print("4- Calças")
    print("5- Tenis/meias")
    print ("0- sair")

# def mulher 
def roupam():
    os.system("cls")
    print("1- Chápeus/Bonés")
    print("2- Jaquetas/Casacos")
    print("3- Camisas")
    print ("4- TopsCroppedM ")
    print("5- Calças")
    print("6- Tenis/meias")
    print ("0- sair")

# def criança
def criança():
    os.system("cls")
    print("1- Chápeus/Bonés")
    print("2- Casacos")
    print("3- Camisas")
    print ("4- TopsCroppedM ")
    print("5- Calças/calçoes")
    print("6- Tenis/meias")
    print ("0- sair")

# Menu para pesquisa
def pesquisa():
    os.system("cls")
    print ("====================================")
    print ("======       Pesquisa         ======")
    print ("====================================")
    print("1- Pesquisa Homem")
    print("2- Pesquisa Mulher")
    print("3- Pesquisa Criança")
    print("4- Pesquisa por preço")
    print ("0- sair")
    print ("-"*30)

def funcionarios():
    os.system("cls")
    print ("========================================")
    print ("======       Funcionarios         ======")
    print ("========================================")
    print("1. Contratar")
    print("2. Demitir")
    print("3. Ver lista de funcionários")
    print("4. Pesquisar funcionário por nome")
    print("5. Sair")

def administrador():
    os.system("cls")
    print ("===================================")
    print ("======       Estoque         ======")
    print ("===================================")
    print("1- Estoque")
    print("2- Adicionar ao estoque")
    print("3- Remover do estoque")
    print("-"*30)

# Menu principal com direitos autorais
def creditos():
    os.system("cls")
    print ("-"*30) 
    print ("Progama elaborado por Anthony Fuzinato".center(15))
    print ("(c) Direitos Reservados".center(15))
    print ("ESEN - Curso profissional de GPSI".center(15))
    print (f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}")
    print ("-"*30) 

##########################################
            # Codigo
bemvindo()

input("Pressione uma tecla pra continuar..")


while True:
    escolha1()
    opção= int(input("Qual a opçao que desejas? "))
    # Novidades
    if opção == 1:
        novidades() # Vai chamar a funçao
        print(f'\033[1;40;4mÓtima Escolha, !!!\033[m')
        opcao = int(input("Qual a opçao que desejas? "))
            
        if opcao == 1:
                for i in range(0, len(famosos), 5):
                    for nome, outfit in famosos[i:i+5]:
                        print(f"Nome: {nome}, Outfit: {outfit}")
                    
                    # Pedir ao usuário para pressionar "Enter" para continuar
                    print("==============================================\n")
                    input("Pressione Enter para ver mais 5 famosos...")
                    print("==============================================\n")

        elif opcao == 2:
                lançamentos()
                opção= int(input("Qual a opçao que desejas? "))
                if opção == 1:
                    print("-" * 30)  

                    print("Tenis Lançados Recentemente: \n")
                    for tenis in tenis_recentes: 
                        print(tenis)

                    print("-" * 30)
                    input("Pressione enter...")
        
                elif opção == 2:
                     add= input("New: ").capitalize()
                     tenis_recentes.add(add) # Adicionar a lista Add a variavel Add
                     break
                elif opção == 3:
                     pop= input("Old: ").capitalize()
                     for pop in tenis_recentes:
                          tenis_recentes.pop(pop) # Remover a lista Add a variavel Add
                          input("Pressione enter...")
                          break
        elif opcao == 3:
                noticias()
                for i in noticias_esportivas:
                    print (f"{i}\n".center(30))
                    print ("================================================\n")
                input ("Pressione a tecla enter para continuar...")
        elif(opcao==0):
                 break
           
        else:
                 print("Ainda nao temos esta opçao, Desculpe..")
        
    # Pesquisar Roupas (Nao e muito eficiente mas percorre sua respetiva lista e da o valor e data do lançamento)
    elif opção == 2:
        while True:
            roupah()
            opcao = int(input("Qual opçao? "))
            if opcao == 1:
                # Usuario escolher a cor
                cor = input("Insira (bone (cor)): ").capitalize()
                encontrado = False
                # Percorre a lista 
                for item in BonésH:
                    if cor in item:
                        print("Cor encontrada:")
                        print(item[cor]) # chamar o for item na posiçao cor
                        encontrado = True # Define a variável encontrado como True para indicar que a cor foi encontrada.
                if not encontrado: # se nao for encontrado
                    print("Cor não encontrada.")
                input("Pressione enter...")


            elif opcao == 2:
                cor = input("Insira (Casaco (cor)): ").capitalize()
                encontrado = False
                for item in CasacosH:
                    if cor in item:
                        print("Cor encontrada:")
                        print(item[cor]) # chamar o for item na posiçao cor
                        encontrado = True # Define a variável encontrado como True para indicar que a cor foi encontrada.
                if not encontrado: # se nao for encontrado
                    print("Cor não encontrada.")
                input("Pressione enter...")

            elif opcao == 3:
                cor = input("Insira (Camisa (cor)): ").capitalize()
                encontrado = False
                for item in CamisasH:
                    if cor in item:
                        print("Cor encontrada:")
                        print(item[cor]) # chamar o for item na posiçao cor
                        encontrado = True # Define a variável encontrado como True para indicar que a cor foi encontrada.
                if not encontrado: # se nao for encontrado
                    print("Cor não encontrada.")
                input("Pressione enter...")


            elif opcao == 4:
                cor = input("Insira (Calça (cor)): ").capitalize()
                encontrado = False
                for item in CalçasH:
                    if cor in item:
                        print("Cor encontrada:")
                        print(item[cor]) # chamar o for item na posiçao cor
                        encontrado = True # Define a variável encontrado como True para indicar que a cor foi encontrada.
                if not encontrado: # se nao for encontrado
                    print("Cor não encontrada.")
                input("Pressione enter...")

            elif opcao == 5:
                cor = input("Insira (Sapato (cor)): ").capitalize()
                encontrado = False
                for item in SapatosH:
                    if cor in item:
                        print("Cor encontrada:")
                        print(item[cor]) # chamar o for item na posiçao cor
                        encontrado = True # Define a variável encontrado como True para indicar que a cor foi encontrada.
                if not encontrado: # se nao for encontrado
                    print("Cor não encontrada.")
                input("Pressione enter...")

            elif(opcao==0):
                 break
    # SE OPÇAO IGUAL A 2 = SECÇAO MULHER
    elif opção == 3:
        while True:
            roupam()
            opcao= int(input("Qual a opçao que desejas? "))
            if opcao == 1:
                    cor = input("Insira (Bone (cor)): ").capitalize()
                    encontrado = False
                    for item in BonésM:
                        if cor in item: 
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")

            elif opcao == 2:
                    cor = input("Insira (Casaco (cor)):").capitalize()
                    encontrado = False
                    for item in CasacosM:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")

            elif opcao == 3:
                    cor = input("Insira (Camisa (cor)): ").capitalize()
                    encontrado = False
                    for item in CamisasM:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")

            elif opcao == 4:
                    cor = input("Insira (Top (cor)):").capitalize()
                    encontrado = False
                    for item in TopsCroppedM:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")

            elif opcao == 5:
                    cor = input("Insira (Calça (cor)): ").capitalize()
                    encontrado = False
                    for item in CalçasM:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")
                
            elif opcao == 6:
                    cor = input("Insira (sapato (cor)): ").capitalize()
                    encontrado = False
                    for item in SapatosM:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")
            elif(opcao==0):
                 break
    
    # SE OPÇAO FOR 3 == CRIANÇA
    elif opção == 4:
        while True:
            criança()
            opçao= int(input("Qual a opçao que desejas? "))
            if opçao == 1:
                        cor = input("Insira (bone (cor)): ").capitalize()
                        encontrado = False
                        for item in BonésCrianças:
                            if cor in item:
                                print("Cor encontrada:")
                                print(item[cor]) 
                                encontrado = True
                        if not encontrado:
                            print("Cor não encontrada.")
                        input("Pressione enter...")

            elif opçao == 2:
                    cor = input("Insira (Casacos (cor)): ").capitalize()
                    encontrado = False
                    for item in CasacosCrianças:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")
                
            elif opçao == 3:
                    cor = input("Insira (Camisas (cor)): ").capitalize()
                    encontrado = False
                    for item in CamisasCrianças:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")

            elif opçao == 4:
                    cor = input("Insira (Top cropped (cor)): ").capitalize()
                    encontrado = False
                    for item in TopsCroppedCrianças:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")


            elif opçao == 5:
                    cor = input("Insira (Calças (cor)): ").capitalize()
                    encontrado = False
                    for item in CalçasCrianças:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")

            elif opçao == 6:
                    cor = input("Insira (Sapato (cor)): ").capitalize()
                    encontrado = False
                    for item in SapatosCrianças:
                        if cor in item:
                            print("Cor encontrada:")
                            print(item[cor]) 
                            encontrado = True
                    if not encontrado:
                        print("Cor não encontrada.")
                    input("Pressione enter...")
            elif(opcao==0):
                 break
            
            input("Pressione uma tecla...")

    # Pesquisa
    elif opção == 5:
        while True:
            print( figlet_format("Pesquisa ", font = "isometric3" ) )
            pesquisa()

            opcao= int(input("Qual a opçao que desejas? "))

            if opcao == 1:
                # Lista com todos os itens masculinos
                todos_itens = BonésH + CasacosH + CamisasH + CalçasH + SapatosH
        
                # Input para pesquisar itens por tipo de roupa
                tipo_pesquisado = input("Digite o tipo de roupa que deseja pesquisar (Bone, Casaco, Camisa, Calça ou Sapato): ").lower()

                # Procurar itens pelo tipo de roupa
                for item in todos_itens:
                    tipo = list(item.keys())[0]  # Obtém o tipo de roupa do item
                    if tipo_pesquisado.lower() in tipo.lower():  # Verifica se o tipo de roupa pesquisado está presente
                        itens_encontrados.append(item)

                # Exibir os itens encontrados
                if itens_encontrados:
                    print("Itens encontrados para o tipo de roupa", tipo_pesquisado + ":")
                    for item in itens_encontrados:
                        print(item)
    
                elif(opcao==0):
                    break

                else:
                    print("Nenhum item encontrado para o tipo de roupa", tipo_pesquisado + ".")
                    input("Pressione enter...")

            elif opcao == 2:
                todos_itens = BonésM + CalçasM + CamisasM + CasacosM + SapatosM + CasacosM + TopsCroppedM

                tipo_pesquisado = input("Digite o tipo de roupa que deseja pesquisar (bone, Casaco, Camisa,top, Calça ou Sapato): ").lower()

                for item in todos_itens:
                    tipo = list(item.keys())[0]  # Obtém o tipo de roupa do item
                    if tipo_pesquisado.lower() in tipo.lower():  # Verifica se o tipo de roupa pesquisado está presente
                        itens_encontrados.append(item)

                if itens_encontrados:
                    print("Itens encontrados para o tipo de roupa", tipo_pesquisado + ":")
                    for item in itens_encontrados:
                        print(item)
            

                else:
                    print("Nenhum item encontrado para o tipo de roupa", tipo_pesquisado + ".")
                    input("Pressione enter...")
        
            elif opcao == 3:
                todos_itens = BonésCrianças + SapatosCrianças + TopsCroppedCrianças + CasacosCrianças + CalçasCrianças + CamisasCrianças

                tipo_pesquisado = input("Digite o tipo de roupa que deseja pesquisar (Bone, Casaco, Camisa, Calça ou Sapato): ").lower()

                for item in todos_itens:
                    tipo = list(item.keys())[0]  # Obtém o tipo de roupa do item
                    if tipo_pesquisado.lower() in tipo.lower():  # Verifica se o tipo de roupa pesquisado está presente
                        itens_encontrados.append(item)

                if itens_encontrados:
                    print("Itens encontrados para o tipo de roupa", tipo_pesquisado + ":")
                    for item in itens_encontrados:
                        print(item)
            
                elif(opcao==0):
                    break

                else:
                    print("Nenhum item encontrado para o tipo de roupa", tipo_pesquisado + ".")
                    input("Pressione enter...")
            
            elif opcao == 4:
                todos_itens = BonésH + CasacosH + CamisasH + CalçasH + SapatosH + BonésM + CalçasM + CamisasM + CasacosM + SapatosM + CasacosM + TopsCroppedM + BonésCrianças + SapatosCrianças + TopsCroppedCrianças + CasacosCrianças + CalçasCrianças + CamisasCrianças
                preço= int(input("Qual o preço que tens para gastar? "))

                for lista in todos_itens:
                    for item in lista:
                        # Obter o valor de cada item na lista
                        valor_item = list(item.values())[0]["Valor"]
                if preço <= valor_item:
                    print(valor_item)
                
                input("Pressione enter para continuar...")

            elif(opcao==0):
                 break
            
            input("Pressione qualquer tecla para prosseguir...")

    elif opção == 6:
        while True:
            print("\n=== Loja de Roupas ===")
            print("1. Adicionar item ao carrinho")
            print("2. Exibir carrinho")
            print("3. Remover item do carrinho")
            print("4. Sair")
            
            # Solicita ao usuário que escolha uma opção
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                # Opção para adicionar item ao carrinho
                
                # Exibe as categorias disponíveis
                print("\nCategorias disponíveis:")
                for i, categoria in enumerate(produtos.keys(), 1):
                    print(f"{i}. {categoria}")
                
                # Solicita ao usuário que escolha uma categoria
                escolha_categoria = int(input("\nEscolha uma categoria: "))
                categoria_selecionada = list(produtos.keys())[escolha_categoria - 1]
                
                # Exibe os tipos de produtos disponíveis para a categoria selecionada
                print(f"\nTipos de produtos disponíveis para {categoria_selecionada}:")

                # Obtém a lista de tipos de produtos disponíveis na categoria selecionada
                tipos_disponiveis = list(produtos[categoria_selecionada].keys())

                # Itera sobre a lista de tipos disponíveis, enumerando-os a partir de 1
                for i, tipo in enumerate(tipos_disponiveis, 1):
                    # Exibe o índice e o nome do tipo de produto
                    print(f"{i}. {tipo}")
                
                # Solicita ao usuário que escolha um tipo de produto
                escolha_tipo = int(input("\nEscolha um tipo de produto: "))
                tipo_selecionado = tipos_disponiveis[escolha_tipo - 1]
                
                # Exibe os itens disponíveis para o tipo selecionado
                print(f"\nItens disponíveis para {tipo_selecionado}:")

                # Obtém a lista de itens disponíveis no tipo selecionado dentro da categoria selecionada
                itens_disponiveis = produtos[categoria_selecionada][tipo_selecionado]

                # Itera sobre a lista de itens disponíveis, enumerando-os a partir de 1
                for i, item in enumerate(itens_disponiveis, 1):
                    # Exibe o índice e o nome do item
                    print(f"{i}. {list(item.keys())[0]}")
                
                # Solicita ao usuário que escolha um item e a quantidade desejada
                escolha_item = int(input("\nEscolha um item: "))
                item_selecionado = list(itens_disponiveis[escolha_item - 1].keys())[0]
                quantidade = int(input("Quantidade desejada: "))

                # Adiciona o item selecionado ao carrinho
                if categoria_selecionada not in carrinho:
                    carrinho[categoria_selecionada] = {}
                
                if tipo_selecionado not in carrinho[categoria_selecionada]:
                    carrinho[categoria_selecionada][tipo_selecionado] = []
                
                carrinho[categoria_selecionada][tipo_selecionado].append({"Item": item_selecionado, "Quantidade": quantidade})
                print(f"\n{item_selecionado} adicionado ao carrinho com quantidade de {quantidade}")
            
            elif escolha == "2": # Opção para exibir o conteúdo do carrinho
                # Constrói uma string representando o carrinho
                carrinho_str = "\n=== Carrinho de Compras ==="
                for categoria, tipos in carrinho.items():
                    carrinho_str += f"\n\n{categoria}:"
                    for tipo, itens in tipos.items():
                        for item in itens:
                            carrinho_str += f"\n{item['Item']} - Quantidade: {item['Quantidade']}"
                print(carrinho_str)


            elif escolha == "3":
                # Exibe o conteúdo do carrinho antes de remover um item
                carrinho_str = "\n=== Carrinho de Compras ==="
                for categoria, tipos in carrinho.items():
                    carrinho_str += f"\n\n{categoria}:"
                    for tipo, itens in tipos.items():
                        for item in itens:
                            carrinho_str += f"\n{item['Item']} - Quantidade: {item['Quantidade']}"
                print(carrinho_str)
                
                # Solicita ao usuário as informações do item a ser removido
                item_selecionado = input("Digite o nome do item que deseja remover: ").capitalize()
                quantidade = int(input("Digite a quantidade do item que deseja remover: "))
                
                # Remove o item do carrinho, se existir
                if categoria_selecionada in carrinho and tipo_selecionado in carrinho[categoria_selecionada]:
                    for i, x in enumerate(carrinho[categoria_selecionada][tipo_selecionado]):
                        if x["Item"] == item_selecionado and x["Quantidade"] == quantidade:
                            del carrinho[categoria_selecionada][tipo_selecionado][i]
                            print(f"{item_selecionado} removido do carrinho.")
                            break
                            
                input ("Pressione enter para continuar...")
            elif escolha == "4":
                # Opção para sair do programa
                print("\nObrigado por usar nosso sistema de compras!")
                break
            
            else:
                # Mensagem para escolhas inválidas
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

# Funcionarios
    elif opção == 7:
        funcionarios()
        while True:
            escolha = input("\nEscolha uma opção: ")

            if escolha == '1':
                nome = input("Digite o nome do novo funcionário: ").lower()
                cargo = input("Digite o cargo do novo funcionário: ").capitalize()
                salario = float(input("Digite o salário do novo funcionário: "))
                funcionarioloja[nome] = {'cargo': cargo, 'salario': salario}
                print(f"\n{nome} contratado como {cargo} com salário de R${salario}.")
                input("Pressione enter...")
                break
            elif escolha == '2':
                nome = input("Digite o nome do funcionário a ser demitido (sem acentos): ").lower()
                if nome in funcionarioloja:
                    del funcionarioloja[nome]
                    print(f"\n{nome} demitido com sucesso.")
                else:
                    print(f"\n{nome} não encontrado na lista de funcionários da loja.")
                input("Pressione enter...")
                break
            elif escolha == '3':
                print("\nLista de funcionários da loja:")
                for nome, detalhes in funcionarioloja.items():
                    print(f"Nome: {nome}, Cargo: {detalhes['cargo']}, Salário: R${detalhes['salario']}")
                input("Pressione enter...")
                break
            elif escolha == '4':
                nome = input("Digite o nome do funcionário que deseja pesquisar (Sem acento por favor): ").capitalize()
                if nome in funcionarioloja:
                    print(f"\nDetalhes de {nome}:")
                    print(f"Cargo: {funcionarioloja[nome]['cargo']}, Salário: R${funcionarioloja[nome]['salario']}")
                
                else:
                    print(f"\n{nome} não encontrado na lista de funcionários da loja.")
                input("Pressione enter...")
                break
            elif escolha == '5':
                print("\nSaindo...")
                input("Pressione enter...")
                break

    # Adiministraçao
    elif opção == 8:
        while True:
            administrador()
            opçao= int(input("Qual a opçao que desejas? "))

            if opçao == 1:
                # Produtos masculinos
                produtos_masculinos = [BonésH, CasacosH, CamisasH, CalçasH, SapatosH]

                for categoria in produtos_masculinos:
                    for produto in categoria:
                        nome = list(produto.keys())[0]
                        estoque = produto[nome]["estoque"]
                        print(f"{nome}: {estoque}")
                    break

                # Produtos femininos
                produtos_femininos = [BonésM, CasacosM, CamisasM, TopsCroppedM, CalçasM, SapatosM]

                for categoria in produtos_femininos:
                    for produto in categoria:
                        nome = list(produto.keys())[0]
                        estoque = produto[nome]["estoque"]
                        print(f"{nome}: {estoque}")
                    break

                # Produtos infantis
                produtos_infantis = [BonésCrianças, CasacosCrianças, CamisasCrianças, TopsCroppedCrianças, CalçasCrianças, SapatosCrianças]

                for categoria in produtos_infantis:
                    for produto in categoria:
                        nome = list(produto.keys())[0]
                        estoque = produto[nome]["estoque"]
                        print(f"{nome}: {estoque}")
                break

            elif(opçao==0):
                 break

            elif opçao == 2:
                # Adicionar produto ao estoque
                def adicionar_produto(dicionario, nome, valor, lancamento, estoque):
                    novo_produto = {nome: {"Valor": valor, "lançamento": lancamento, "estoque": estoque}}
                    dicionario.append(novo_produto)

                # Adicionar um novo boné
                novo_nome = input("Digite o nome do boné que deseja adicionar: ").lower()
                novo_valor = float(input("Digite o valor do boné: "))
                novo_lancamento = input("Digite a data de lançamento (DD/MM/AA): ")
                novo_estoque = int(input("Digite a quantidade em estoque: "))

                novo_produto = {novo_nome: {"Valor": novo_valor, "lançamento": novo_lancamento, "estoque": novo_estoque}}
                BonésH.append(novo_produto)

                print("\nAdicionado com sucesso!")
                print("Estoque atualizado:")
                break

            elif opçao == 3:   # opçao == 3    
               # Remover produto do estoque
                def remover_produto(dicionario, nome):
                    for produto in dicionario:
                        if nome in produto:
                            dicionario.remove(produto)
                        break

                nome_remover = input("\nDigite o nome do boné que deseja remover: ").lower()
                for produto in BonésH:
                    if nome_remover in produto:
                        BonésH.remove(produto)
                        print(f"\nBoné {nome_remover} removido com sucesso!")
                    break

                print("\nEstoque atualizado:")


 # Sair
    elif opção == 0:
        break
        
    # Caso o utilizador coloque uma tecla que nao ha na def
    else:
             print ("Ainda nao temos esta opçao, Desculpe..")
             input("Pressione uma tecla...")
 
creditos()