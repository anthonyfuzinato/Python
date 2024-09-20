# Criando um carrinho vazio
carrinho = []

# Listas de produtos
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

# Funções para adicionar itens por categoria
def adicionar_bone(carrinho, lista):
    print("Escolha um boné da lista abaixo para adicionar ao carrinho:")
    for index, item in enumerate(lista, 1):
        print(f"{index}. {list(item.keys())[0]} - Valor: R${item[list(item.keys())[0]]['Valor']}")

    escolha = int(input("Digite o número correspondente ao boné desejado: "))
    if 1 <= escolha <= len(lista):
        item_escolhido = lista[escolha - 1]
        carrinho.append(item_escolhido)
        print(f"{list(item_escolhido.keys())[0]} foi adicionado ao carrinho.")
    else:
        print("Escolha inválida.")

def adicionar_casaco(carrinho, lista):
    print("Escolha um casaco da lista abaixo para adicionar ao carrinho:")
    for index, item in enumerate(lista, 1):
        print(f"{index}. {list(item.keys())[0]} - Valor: R${item[list(item.keys())[0]]['Valor']}")

    escolha = int(input("Digite o número correspondente ao casaco desejado: "))
    if 1 <= escolha <= len(lista):
        item_escolhido = lista[escolha - 1]
        carrinho.append(item_escolhido)
        print(f"{list(item_escolhido.keys())[0]} foi adicionado ao carrinho.")
    else:
        print("Escolha inválida.")

# Menu de categorias
def menu_categorias():
    print("\nSelecione a categoria de produto:")
    print("1. Bonés")
    print("2. Casacos")
    print("3. Finalizar")

    escolha = int(input("Digite o número correspondente à categoria desejada: "))
    
    if escolha == 1:
        adicionar_bone(carrinho, BonésH)
        menu_categorias()
    elif escolha == 2:
        adicionar_casaco(carrinho, CasacosH)
        menu_categorias()
    elif escolha == 3:
        print("\nCarrinho atual:", carrinho)
    else:
        print("Opção inválida. Tente novamente.")
        menu_categorias()

# Chamando o menu de categorias
menu_categorias()