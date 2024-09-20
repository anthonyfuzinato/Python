def menu():
    print("---------- Moedas ----------")
    for moeda in dinheiro.keys():
        print(moeda, end = " | ")

menu()

dinheiro = {"Real":{"taxa":5.46, "moeda":"R$"},
        "Dólar":{"taxa":1.08, "moeda":"$"},
        "Iene":{"taxa":163.20, "moeda":"I$"},
        "Franco Suíço":{"taxa"0.96, "moeda":"FS$"},
        "Yuan":{"taxa":7.70, "moeda":"Y$"},
        "Zloty":{"taxa":4.32, "moeda":"Z$"}}

preço= int(input("Qual o preço do produto(€)? "))
moedas= input("Qual a moeda que vc deseja? ").capitalize()

if moedas in dinheiro:
    print("Nao tenho essa moeda")
else:
    print(f"{moedas} : {dinheiro[moedas]["taxa"]*preço:.2f}")