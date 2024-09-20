primeira= int(input())
segunda= int(input())

if primeira < segunda:
    nota= (primeira- segunda) -1
    if nota == (-2):
        print("intervalo de segunda")
    elif nota == (-3):
        print("intervalo de terceira")
    elif nota == (-4):
        print("intervalo de quarta")
    elif nota == (-5):
        print("intervalo de quinta")
    elif nota == (-6):
        print("intervalo de sexta")
    elif nota == (-7):
        print("intervalo de sétima")

elif primeira > segunda:
    nota= (primeira + segunda)
    if nota == 2:
        print("intervalo de segunda")
    elif nota == 3:
        print("intervalo de terceira")
    elif nota == 4:
        print("intervalo de quarta")
    elif nota == 5:
        print("intervalo de quinta")
    elif nota == 6:
        print("intervalo de sexta")
    elif nota == 7:
        print("intervalo de sétima")
        
elif primeira + segunda > 8 or primeira + segunda > (-8):
    if segunda == 2:
        print("intervalo de segunda")
    elif segunda == 3:
        print("intervalo de terceira")
    elif segunda == 4:
        print("intervalo de quarta")
    elif segunda == 5:
        print("intervalo de quinta")
    elif segunda == 6:
        print("intervalo de sexta")
    elif segunda == 7:
        print("intervalo de sétima")