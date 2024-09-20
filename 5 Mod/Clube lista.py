clubes= input("Lista:\n").split(",")

import random
njogos= 1
while len(clubes) != 0:
    print (f"Njogo: {njogos}")
    clubesorteado= random.choice(clubes)
    print (f"{clubesorteado}-{clubesorteado}")
    clubes.remove(clubesorteado)


    clubesorteado=random.choice(clubes)
    print(clubesorteado, "\n")
    clubes.remove(clubesorteado)

    njogos+= 1
