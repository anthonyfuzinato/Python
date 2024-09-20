def linguas():
    print("^^^^^^^^^^^Linguas disponiveis^^^^^^^^^^")
    print("---------Japonês---------")
    print("---------Chinês---------")
    print("---------Português---------")
    print("---------Inglês---------")
    print("---------Françes---------")
    print("---------Espanhol---------")
    print("---------Italiano---------")
    for idioma in Cumprimento.keys():
        print(idioma, end = " | ")
 
Cumprimento={"Japonês": "こんにちは",
             "Chinês": "你好",
             "Português": "Olá",
             "Inglês": "Hello",
             "Françes":"Salut",
             "Espanhol": "hola",
             "Italiano":"ciao"}
 
linguas()
Nacionalidade=input("\nQual é a sua lingua mãe?").capitalize()
print(f"{Cumprimento.get(Nacionalidade, "Não conheço essa linha")}")