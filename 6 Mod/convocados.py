convocados={'Diogo Costa':'Porto',
          'José Sá':'Wolves',
          'Rui Patrício':'Roma',
          'António Silva':'Benfica',
          'Danilo Pereira':'PSG',
          'Diogo Leite': 'Union Berlim',
          'Gonçalo Inácio':'Sporting',
          'João Mário':'Benfica',
          'João Cancelo':'Barcelona',
          'Diogo Dalot':'Man United',
          'Pepe':'Porto',
          'Nélson Semedo':'Wolves',
          'Nuno Mendes':'PSG',
          'Raphael Guerreiro':'Dortmund',
          'Rúben Dias':'Man City',
          'Toti Gomes':'Wolves',
          'Bruno Fernandes':'Man United',
          'João Palhinha':'Fulham',
          'João Neves':'Benfica',
          'Matheus Nunes':'Man City',
          'Otávio':'Al Nassr',
          'Rúben Neves':'Al Hilal',
          'Vitinha':'PSG',
          'Bruma':'Braga',
          'Bernardo':'Man City',
          'Ronaldo':'Al Nassr',
          'Trincão':'Sporting',
          'Conceição':'Porto',
          'Gonçalo Ramos':'PSG',
          'Félix':'Barcelona',
          'Jota Silva':'Votótia de Guimarães',
          'Rafael Leão':'Milan'}

clubes=[]
todos_clubes= []
for clube in convocados.values():
    if clube not in clubes:
        clubes.append(clube)
    todos_clubes.append(clube)

print(clubes)

print(f"E foram convocados {len(convocados)}")

print (f"Existem {len(clubes)} times diferentes")

print("--- Numero de Jogadores por clube ---\n")
for clube in clubes:
    print(f"{clube}:{todos_clubes.count(clube)}")
    for nome in convocados:
        if convocados[nome]==clube:
            print(nome)