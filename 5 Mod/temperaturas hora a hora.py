temp= map(int(input().split()))

print (max(temp) - min(temp))

print (f"{sum(temp) / len(temp):.2f}")

for i in temp: 
    if i > 40:
        print (f"Alerta Laranja no horario {len(max(temp.index(max(i+1))))}")   
    elif i < 0:
        print (f"Alerta de Neve no horario {len(min(temp.index(min(i+1))))}") 