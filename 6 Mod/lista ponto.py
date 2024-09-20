lista_pontos=[]
Q1, Q2, Q3, Q4=0,0,0,0
lista_pontosQ1= []
lista_pontosQ2= []
lista_pontosQ3= []
lista_pontosQ4= []
while True:
    ponto = tuple(map(int,input("Coordenadas Ponto(x,y):").split(",")))
    if(ponto==(0,0)):
        break
    lista_pontos.append(ponto)
   
    # Testar Q1
    if(ponto[0]>0 and ponto[1]>0):
        Q1+=1
        lista_pontosQ1.append(ponto)
   
    # Testar Q2
    elif(ponto[0]<0 and ponto[1]>0):
        Q2+=1
        lista_pontosQ2.append(ponto)
 
    # Testar Q3
    elif(ponto[0]<0 and ponto[1]<0):
        Q3+=1
        lista_pontosQ3.append(ponto)
   
    # Testar Q3
    elif(ponto[0]>0 and ponto[1]<0):
        Q4+=1
        lista_pontosQ4.append(ponto)
 
    else:
        print("O ponto está em cima da linha")
 
print("Q1:",len(lista_pontosQ1, "pontos", lista_pontosQ1)
print("Q1:",len(lista_pontosQ2, "pontos", lista_pontosQ2)
print("Q1:",len(lista_pontosQ3, "pontos", lista_pontosQ3)
print("Q1:",len(lista_pontosQ4, "pontos", lista_pontosQ4)
 
print(lista_pontos)