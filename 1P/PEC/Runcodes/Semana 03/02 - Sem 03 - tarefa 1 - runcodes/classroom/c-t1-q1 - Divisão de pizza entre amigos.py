qntFatias = int(input("Quantas fatias tem a pizza?: "))
qntAmigos = int(input("Com quantos amigos você vai dividir?: "))

fatiasCada = qntFatias // qntAmigos
fatiasSobra = qntFatias % qntAmigos

print(f"Cada amigo ficará com {fatiasCada} fatias e irá sobrar {fatiasSobra} fatias.")