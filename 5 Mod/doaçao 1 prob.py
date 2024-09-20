doacoes= = []

while True:
    doacao=int(input())
    if doacao == 0:
        break
    else:
        doacoes.append(doacao)
    
print("Nº de pessoas que doaram foi de ", len(doacoes))
print("Valor acumulado de doaçoes foi de ", sum(doacoes))