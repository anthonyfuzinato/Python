linguas={"python":"Guido van Rossum",
            "c":"Dennis Ritchie",
            "java":"James Gosling",
            "php":"Rasmus Lerdorf",
            "ruby":"Yukihiro Matz Matsumoto",
            "javascript":"Brendan Eich"}

linguagem=input("Escolha uma linguagem:").lower()
if linguagem in linguas:
    print("Criador:",end=" ")

print(linguas.get(linguagem,"Não conheço o criador da linguagem "+ linguagem))